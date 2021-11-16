import pandas as pd
import numpy as np

### Milestone 1 ###

def normalize_plays_coords(plays_df):
    def normalize_period_coords(plays_df):
        #mask for even periods
        #plays_df[["x_coord_norm", "y_coord_norm"]] = plays_df[["x_coord", "y_coord"]].copy()
        mask = (plays_df["period_idx"]%2==0)
        plays_df.loc[mask, "x_coord_norm"] = -plays_df["x_coord"]
        plays_df.loc[mask, "y_coord_norm"] = -plays_df["y_coord"]
        return plays_df

    def normalize_side_coords(plays_df):
        negative_side_df = plays_df.groupby(["gamePk", "team_initiative_id"]).filter(lambda x: x["x_coord_norm"].mean() < 0)
        plays_df.loc[negative_side_df.index, "x_coord_norm"] = -negative_side_df["x_coord_norm"]
        plays_df.loc[negative_side_df.index, "y_coord_norm"] = -negative_side_df["y_coord_norm"]
        return plays_df
    
    plays_df[["x_coord_norm", "y_coord_norm"]] = plays_df[["x_coord", "y_coord"]].copy()
    plays_df = normalize_period_coords(plays_df)
    plays_df = normalize_side_coords(plays_df)
    return plays_df


### Basic features ###

def basic_features(plays_df):
    dist_from_net = _dist_from_net(plays_df)
    angle_from_net = _angle_from_net(plays_df)
    is_goal = _is_goal(plays_df)
    empty_net = _empty_net(plays_df)
           
    features_df = pd.concat([dist_from_net, angle_from_net, is_goal, empty_net], axis=1)
    return features_df

def _dist_from_net(plays_df):
    net_pos = np.array([100-11, 0])
    shot_vector = net_pos - plays_df[["x_coord_norm", "y_coord_norm"]]
    dist_from_net = np.linalg.norm(shot_vector, ord=2, axis=1)
    return pd.Series(dist_from_net, name="dist_from_net", index=plays_df.index)

def _angle_from_net(plays_df):
    net_pos = np.array([100-11, 0])
    shot_vector = net_pos - plays_df[["x_coord_norm", "y_coord_norm"]]
    cos_angle = shot_vector @ net_pos / (np.linalg.norm(net_pos, ord=2) * np.linalg.norm(shot_vector, ord=2, axis=1))
    angle = np.arccos(cos_angle)
    return pd.Series(np.degrees(angle), name="angle_from_net", index=plays_df.index)
    
def _is_goal(plays_df):
    str_to_int = {"SHOT": 0, "GOAL": 1}
    is_goal = plays_df.event_type_id.replace(str_to_int)
    return pd.Series(is_goal, name="is_goal", index=plays_df.index)
    
def _empty_net(plays_df):
    return pd.Series(plays_df.empty_net_bool, name="empty_net", index=plays_df.index)


### Advanced features ###

def advanced_features(plays_df):
    seconds_elapsed = _game_seconds(plays_df)
    game_period = _game_period(plays_df)
    x_coord = _og_x_coords(plays_df)
    y_coord = _og_y_coords(plays_df)
    dist_from_net = _dist_from_net(plays_df)
    angle_from_net = _angle_from_net(plays_df)
    shot_type = _shot_type(plays_df)
    empty_net = _empty_net(plays_df)
    
    features_df = pd.concat(
        [seconds_elapsed, game_period, x_coord, y_coord,
         dist_from_net, angle_from_net, shot_type, empty_net],
        axis=1
    )
    
    return features_df


def _game_seconds(plays_df):
    plays_df["game_time"] = pd.to_datetime(plays_df["game_time"])
    plays_df["game_start_time"] = pd.to_datetime(plays_df["game_start_time"])
    seconds_elapsed = (plays_df.game_time - plays_df.game_start_time).dt.total_seconds()
    return pd.Series(seconds_elapsed, name="seconds_elapsed", index=plays_df.index)

def _game_period(plays_df):
    return pd.Series(plays_df.period_idx, name="game_period", index=plays_df.index)

def _og_x_coords(plays_df):
    return pd.Series(plays_df.x_coord, name="x_coord", index=plays_df.index)

def _og_y_coords(plays_df):
    return pd.Series(plays_df.y_coord, name="y_coord", index=plays_df.index)

def _shot_type(plays_df):
    return pd.Series(plays_df.event_type_id, name="shot_type", index=plays_df.index)