import pandas as pd

from src.data.data_query import StorageEngine
from src.data.plays_model import game_json_to_plays_list

def tidy_plays_df(years, augment=False):
    def _tidy_plays_one_year(start_year, storage_engine, augment=False):
        gamePk_list = storage_engine.get_all_season_gamePk(start_year)

        game_plays_df_list = []
        for gamePk in gamePk_list:
            game_json = storage_engine.get_game(start_year, gamePk)
            game_plays_list = game_json_to_plays_list(game_json, augment=augment)
            game_plays_df = pd.DataFrame.from_records(game_plays_list)
            game_plays_df_list.append(game_plays_df)
        
        return pd.concat(game_plays_df_list)
    
    storage_engine = StorageEngine("./data/raw")
    
    season_plays_df_list = []
    for start_year in years:
        season_plays_df = _tidy_plays_one_year(start_year, storage_engine, augment)
        season_plays_df_list.append(season_plays_df)
        
    return pd.concat(season_plays_df_list)    
    

def split_dataset(season_plays_df):
    train_seasons = [20152016, 20162017, 20172018, 20182019]
    test_seasons = [20192020]
    
    train_selection = (season_plays_df.game_type=="R") & (season_plays_df.game_season.isin(train_seasons))
    train_df = season_plays_df.loc[train_selection].copy()
    
    test_selection = (season_plays_df.game_season.isin(test_seasons))
    test_df = season_plays_df.loc[test_selection].copy()
    
    return train_df, test_df