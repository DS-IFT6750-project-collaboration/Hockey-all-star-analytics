import pandas as pd

def split_dataset(season_plays_df):
    train_seasons = [20152016, 20162017, 20172018, 20182019]
    test_seasons = [20192020]
    
    train_selection = (season_plays_df.game_type=="R") & (season_plays_df.game_season.isin(train_seasons))
    train_df = season_plays_df.loc[train_selection].copy()
    
    test_selection = (season_plays_df.game_season.isin(test_seasons))
    test_df = season_plays_df.loc[test_selection].copy()
    
    return train_df, test_df