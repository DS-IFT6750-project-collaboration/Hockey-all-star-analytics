import os
import requests
import json
import time

# class to interact with the API
class ApiEngine():
    def __init__(self, storage_path):
        self.storage_path = storage_path
    
    # pass start_year, return a string to select a season (i.e., 2017 -> 20172018)
    def _start_year_to_season_string(self, start_year):
        return str(start_year) + str(start_year+1)
    
    # save the API JSON response to file
    def save_response(self, response, path, overwrite=False):
        if overwrite:
            with open(path, "w") as file:
                # if overwrite is true, return to beginning of file and overwrite
                file.seek(0)
                file.truncate()
                json.dump(response, file)
            return
        
        with open(path, "w") as file:
            json.dump(response, file)
    
    # query API endpoint
    def query_api(self, endpoint, params=None):
        # base url of the API
        url = f"https://statsapi.web.nhl.com/api/v1/{endpoint}"
        r = requests.get(url, params=params, timeout=3)
        # check if the HTTP request is valid
        try:
            r.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Could not reach API endpoint:\n'{url}'")
        return r.json()
    
    # query API for the schedule of the year (to get valid gamePk)
    def get_season_schedule(self, start_year):
        season_string = self._start_year_to_season_string(start_year)
        season_response = self.query_api("schedule", params={"season": season_string})
        save_path = f"{self.storage_path}/schedule/schedule_{season_string}.json"
        self.save_response(season_response, save_path, overwrite=False)
        
    # query API for a specific game
    def get_game(self, gamePk):
        game_response = self.query_api(f"game/{gamePk}/feed/live")
        season = game_response["gameData"]["game"]["season"]
        save_path = f"{self.storage_path}/games/{season}/game_{season}_{gamePk}.json"
        self.save_response(game_response, save_path, overwrite=False)
    
    # loop to query all games of a season
    def get_all_season_games(self, start_year):
        season_schedule = self.get_season_schedule(start_year)
        
        for date in season_schedule["dates"]:
            for game in date["games"]:
                self.get_game(game["gamePk"])
                time.sleep(3) # delay to avoid spamming requests
                

# class to interact with the stored JSON files
class StorageEngine():
    def __init__(self, storage_path):
        self.storage_path = storage_path
        
    def _start_year_to_season_string(self, start_year):
        return str(start_year) + str(start_year+1)
    
    # load season schedule JSON
    def get_season_schedule(self, start_year):
        season_string = self._start_year_to_season_string(start_year)
        save_path = f"{self.storage_path}/schedule/schedule_{season_string}.json"
        with open(save_path, "r") as file:
            return json.load(file)
    
    # load game JSON
    def get_game(self, start_year, gamePk):
        season_string = self._start_year_to_season_string(start_year)
        save_path = f"{self.storage_path}/games/{season_string}/game_{season_string}_{gamePk}.json"
        with open(save_path, "r") as file:
            return json.load(file)
    
    # get list of valid gamePk from season schedule
    def get_all_season_gamePk(self, start_year):
        season_schedule = self.get_season_schedule(start_year)

        gamePk_list = []
        for date in season_schedule["dates"]:
            for game in date["games"]:
                gamePk_list.append(game["gamePk"])
        return gamePk_list