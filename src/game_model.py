def game_json_to_metadata_dict(game_json):
    metadata_dict = {
        # game metadata
        "gamePk": str(game_json["gamePk"]),
        "season": game_json["gameData"]["game"]["season"],
        "game_type": game_json["gameData"]["game"]["type"],
        "start_time": game_json["gameData"]["datetime"]["dateTime"],
        "end_time": game_json["gameData"]["datetime"]["endDateTime"],
        
        # team id and venue
        #away team
        "away_id": game_json["gameData"]["teams"]["away"]["id"],
        "away_name": game_json["gameData"]["teams"]["away"]["name"],
        "away_tri": game_json["gameData"]["teams"]["away"]["triCode"],
        "away_franchise": str(game_json["gameData"]["teams"]["away"]["franchise"]["franchiseId"]),
        # home team
        "home_id": game_json["gameData"]["teams"]["home"]["id"],
        "home_name": game_json["gameData"]["teams"]["home"]["name"],
        "home_tri": game_json["gameData"]["teams"]["home"]["triCode"],
        "home_franchise": str(game_json["gameData"]["teams"]["away"]["franchise"]["franchiseId"]),
        # venue
        "venue_id": str(game_json["gameData"]["venue"]["id"]),
        "venue_name": game_json["gameData"]["venue"]["name"],  
        
        # team game stats
        # away team
        "away_goals": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["goals"],
        "away_pim": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["pim"],
        "away_shots": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["shots"],
        "away_powerplay_percent": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["powerPlayPercentage"],
        "away_powerplay_goals": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["powerPlayGoals"],
        "away_powerplay_opportunities": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["powerPlayOpportunities"],
        "away_faceoff_win_percent": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["faceOffWinPercentage"],
        "away_blocked": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["blocked"],
        "away_takeaways": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["takeaways"],
        "away_giveaways": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["giveaways"],
        "away_hit": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["hits"],
        # home team
        "home_goals": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["goals"],
        "home_pim": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["pim"],
        "home_shots": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["shots"],
        "home_powerplay_percent": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["powerPlayPercentage"],
        "home_powerplay_goals": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["powerPlayGoals"],
        "home_powerplay_opportunities": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["powerPlayOpportunities"],
        "home_faceoff_win_percent": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["faceOffWinPercentage"],
        "home_blocked": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["blocked"],
        "home_takeaways": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["takeaways"],
        "home_giveaways": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["giveaways"],
        "home_hit": game_json["liveData"]["boxscore"]["teams"]["away"]["teamStats"]["teamSkaterStats"]["hits"],
        # general play stats
        "n_plays": len(game_json["liveData"]["plays"]["allPlays"]),
        "n_plays_period1": len(game_json["liveData"]["plays"]["playsByPeriod"][0]["plays"]),
        "n_plays_period2": len(game_json["liveData"]["plays"]["playsByPeriod"][1]["plays"]),
        "n_plays_period3": len(game_json["liveData"]["plays"]["playsByPeriod"][2]["plays"]),
        "n_scoring_plays": len(game_json["liveData"]["plays"]["scoringPlays"]),
        "n_penalty_plays": len(game_json["liveData"]["plays"]["penaltyPlays"]),
        "has_shoutout": game_json["liveData"]["linescore"]["hasShootout"],
        
        # coach / officials info
        # coaches
        "away_coach": game_json["liveData"]["boxscore"]["teams"]["away"]["coaches"][0]["person"]["fullName"],
        "home_coach": game_json["liveData"]["boxscore"]["teams"]["away"]["coaches"][0]["person"]["fullName"],
        # referees
        "referee1_id": str(game_json["liveData"]["boxscore"]["officials"][0]["official"]["id"]),
        "referee1_name": game_json["liveData"]["boxscore"]["officials"][0]["official"]["fullName"],
        "referee2_id": str(game_json["liveData"]["boxscore"]["officials"][1]["official"]["id"]),
        "referee2_name": game_json["liveData"]["boxscore"]["officials"][1]["official"]["fullName"],
        # linesman
        "linesman1_id": str(game_json["liveData"]["boxscore"]["officials"][2]["official"]["id"]),
        "linesman1_name": game_json["liveData"]["boxscore"]["officials"][2]["official"]["fullName"],
        "linesman2_id": str(game_json["liveData"]["boxscore"]["officials"][3]["official"]["id"]),
        "linesman2_name": game_json["liveData"]["boxscore"]["officials"][3]["official"]["fullName"], 
        
        # stars of the game
        "first_star_id": str(game_json["liveData"]["decisions"]["firstStar"]["id"]),
        "first_star_name": game_json["liveData"]["decisions"]["firstStar"]["fullName"],
        "second_star_id": str(game_json["liveData"]["decisions"]["secondStar"]["id"]),
        "second_star_name": game_json["liveData"]["decisions"]["secondStar"]["fullName"],
        "third_star_id": str(game_json["liveData"]["decisions"]["thirdStar"]["id"]),
        "third_star_name": game_json["liveData"]["decisions"]["thirdStar"]["fullName"],
    }
    
    return metadata_dict