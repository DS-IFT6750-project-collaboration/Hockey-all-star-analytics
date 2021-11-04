from ipywidgets import interact

from data.data_query import StorageEngine

@interact(start_year=[2016, 2017, 2018, 2019, 2020])
def view_season(start_year=2016):
    # load engine
    storage_engine = StorageEngine("./data/raw")
    # load list of all gamePk for selected season
    gamePk_list = storage_engine.get_all_season_gamePk(start_year)
            
    @interact(game_idx=(0, len(gamePk_list)-1, 1))
    def view_games(game_idx=0):
        # load the game for the (season, gamePk) selected
        game_json = storage_engine.get_game(start_year, gamePk_list[game_idx])
        
        # function to specify the data to display
        def _print_metadata(game_json):
            season = game_json["gameData"]["game"]["season"]
            gamePk = game_json["gamePk"]
            game_type = game_json["gameData"]["game"]["type"]
            start_time = game_json["gameData"]["datetime"]["dateTime"]
            venue = game_json["gameData"]["venue"]["name"]
            
            home_tri = game_json["gameData"]["teams"]["home"]["triCode"]
            away_tri = game_json["gameData"]["teams"]["away"]["triCode"]
            
            print("season:\t", season)
            print("gamePk:\t", gamePk)
            print("game_type:\t", game_type)
            print("start_time:\t", start_time)
            print("venue:\t", venue)
            print(f"{home_tri} (home) vs. {away_tri} (away)")
        
        _print_metadata(game_json)    
            
    view_games()