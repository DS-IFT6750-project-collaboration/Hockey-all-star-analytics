def play_json_to_play_dict(play_json):
    # returns nothing if the event is not of type SHOT or GOAL
    if play_json["result"]["eventTypeId"] not in ["SHOT", "GOAL"]:
        return None
    
    
    shooter_id = None
    shooter_name = None
    goalie_id = None
    goalie_name = None
    # logic for attributing shooter and goalie name (if exists)
    if play_json.get("players"):
        for player in play_json["players"]:
            if player["playerType"] in ["Shooter", "Scorer"]:
                shooter_id = str(player["player"]["id"])
                shooter_name = player["player"]["fullName"]
            if player["playerType"] == "Goalie":
                goalie_id = str(player["player"]["id"])
                goalie_name = player["player"]["fullName"]
                
    strength = None
    if play_json["result"].get("strength"):
        strength = play_json["result"]["strength"]["code"]
    
    play_dict = {
        "event_idx": play_json["about"]["eventId"],
        "event_type_id": play_json["result"]["eventTypeId"],
        "period_idx": play_json["about"]["period"],
        "period_type": play_json["about"]["periodType"],
        "game_time": play_json["about"]["dateTime"],
        "shot_type": play_json["result"].get("secondaryType"),
        "team_initiative_id": play_json["team"].get("triCode"),
        "team_initiative_name": play_json["team"].get("name"),
        "x_coord": play_json["coordinates"].get("x"),
        "y_coord": play_json["coordinates"].get("y"),
        "shooter_id": shooter_id,
        "shooter_name": shooter_name,
        "goalie_id": goalie_id,
        "goalie_name": goalie_name,
        "strength": strength,
        "empty_net_bool": play_json["result"].get("emptyNet")
    }
    
    return play_dict


def game_json_to_plays_list(game_json):
    all_plays_list = game_json["liveData"]["plays"]["allPlays"]
    
    game_metadata = {
        "gamePk": game_json["gameData"]["game"]["pk"],
        "game_season": game_json["gameData"]["game"]["season"],
        "game_type": game_json["gameData"]["game"]["type"],
        "game_start_time": game_json["gameData"]["datetime"].get("dateTime")
    }
    
    plays_dict_list = list(filter(None, [play_json_to_play_dict(play) for play in all_plays_list]))
    plays_with_metadata = []
    for play_dict in plays_dict_list:
        play_dict.update(game_metadata)
        plays_with_metadata.append(play_dict)
        
    return plays_with_metadata