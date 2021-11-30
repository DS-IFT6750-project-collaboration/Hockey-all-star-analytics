# Q2. Data acquisition

>Write a brief tutorial on how your team downloaded the dataset. Imagine that you were searching for a guide on how to download the play-by-play data; your guide should make you go “Perfect - this is exactly what I was looking for!”. This can be as simple as copying in your function and an example usage, and writing one or two sentences describing it.

The NHL play-by-play data is available through a RESTful API. To interact efficiently with it, a custom `ApiEngine` class was created to query, download, and store the raw data in JSON format. Then, the `StorageEngine` class is used to interact and load stored JSON files. This will prove useful to tidy the raw data.

The `ApiEngine` can be used in the following ways:
1. Instanciate the engine with the directory to store API responses:
 `api_engine = ApiEngine(storage_directory_path)`
2. Query an API `endpoint` for https://statsapi.web.nhl.com/api/v1/ :
 `api_engine.query_api(endpoint)`
3. Query a season schedule by specifying the `start_year`:
 `api_engine.get_season_schedule(start_year)`
4. Query a game by its `gamePk` unique id:
 `api_engine.get_game(gamePk)`
5. Query all season games based on `gamePk` listed in the season schedule specified by `start_year`:
 `api_engine.get_all_season_games(start_year)`

The `StorageEngine` can be used in the following ways:
1. Instanciate the engine with the directory of the store files:
 `storage_engine = StorageEngine(storage_directory_path)`
2. Get a stored season schedule by specifying its `start_year`:
 `storage_engine = storage_engine.get_season_schedule(start_year)`
3. Get a stored game by its `gamePk` unique id:
 `storage_engine.get_game(gamePk)`
4. Get the list of `gamePk` found in a stored season schedule specified by `start_year` (which can be used to iteratively load individual games):
 `storage_engine.get_all_season_gamePk(start_year)`