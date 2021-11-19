import pandas as pd
import numpy as np

### Milestone 1 ###

def normalize_plays_coords(plays_df):
    def normalize_period_coords(plays_df):
        #mask for even periods
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
    plays_df = normalize_plays_coords(plays_df)
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
    plays_df = normalize_plays_coords(plays_df)
    
    seconds_elapsed = _game_seconds(plays_df)
    game_period = _game_period(plays_df)
    x_coord = _og_x_coords(plays_df)
    y_coord = _og_y_coords(plays_df)
    dist_from_net = _dist_from_net(plays_df)
    angle_from_net = _angle_from_net(plays_df)
    shot_type = _shot_type(plays_df)
    empty_net = _empty_net(plays_df)
    previous_event_type = _previous_event_type(plays_df)
    previous_x = _previous_x_coords(plays_df)
    previous_y = _previous_y_coords(plays_df)
    seconds_from_previous = _seconds_from_previous(plays_df)
    dist_from_previous = _dist_from_previous(plays_df)
    rebound = _is_rebound(plays_df)
    angle_change = None
    speed = pd.Series(dist_from_previous / seconds_from_previous, name="speed", index=plays_df.index)
    
    features_df = pd.concat([
        seconds_elapsed,
        game_period,
        x_coord, y_coord,
        dist_from_net,
        angle_from_net,
        shot_type,
        empty_net,
        previous_event_type, 
        previous_x, previous_y,
        seconds_from_previous,
        dist_from_previous,
        rebound,
        angle_change,
        speed,
        ],
        axis=1
    )
    
    return features_df


def _game_seconds(plays_df):
    plays_df["period_time"] = pd.to_datetime(plays_df["period_time"], format="%M:%S")
    period_seconds = (plays_df["period_time"] - pd.to_datetime("1900-01-01")).dt.total_seconds()
    previous_periods_seconds = (plays_df["period_idx"] - 1) * 1200
    seconds_elapsed = period_seconds + previous_periods_seconds
    return pd.Series(seconds_elapsed, name="seconds_elapsed", index=plays_df.index)

def _game_period(plays_df):
    return pd.Series(plays_df.period_idx, name="game_period", index=plays_df.index)

def _og_x_coords(plays_df):
    return pd.Series(plays_df.x_coord, name="x_coord", index=plays_df.index)

def _og_y_coords(plays_df):
    return pd.Series(plays_df.y_coord, name="y_coord", index=plays_df.index)

def _shot_type(plays_df):
    return pd.Series(plays_df.shot_type, name="shot_type", index=plays_df.index)

def _previous_event_type(plays_df):
    period_mask = (plays_df.period_idx == plays_df.previous_event_period)
    return pd.Series(plays_df.loc[period_mask, "previous_event_type"], name="previous_event_type", index=plays_df.index)

def _previous_x_coords(plays_df):
    period_mask = (plays_df.period_idx == plays_df.previous_event_period)
    return pd.Series(plays_df.loc[period_mask, "previous_event_x_coord"], name="previous_x_coord", index=plays_df.index)

def _previous_y_coords(plays_df):
    period_mask = (plays_df.period_idx == plays_df.previous_event_period)
    return pd.Series(plays_df.loc[period_mask, "previous_event_y_coord"], name="previous_y_coord", index=plays_df.index)

def _seconds_from_previous(plays_df):
    plays_df["period_time"] = pd.to_datetime(plays_df["period_time"], format="%M:%S")
    plays_df["previous_event_period_time"] = pd.to_datetime(plays_df["previous_event_period_time"], format="%M:%S")
    period_mask = (plays_df.period_idx == plays_df.previous_event_period)
    time_diff = (plays_df.loc[period_mask,"period_time"] - plays_df.loc[period_mask,"previous_event_period_time"]).dt.total_seconds()
    return pd.Series(time_diff, name="seconds_from_previous", index=plays_df.index)

def _dist_from_previous(plays_df):
    period_mask = (plays_df.period_idx == plays_df.previous_event_period)
    movement_vector = plays_df.loc[period_mask, ["x_coord", "y_coord"]] - plays_df.loc[period_mask, ["previous_event_x_coord", "previous_event_y_coord"]].values
    dists = np.linalg.norm(movement_vector, ord=2, axis=1)
    return pd.Series(dists, name="dist_from_previous", index=movement_vector.index)

def _is_rebound(plays_df):
    period_mask = (plays_df.period_idx == plays_df.previous_event_period)
    rebound_mask = (plays_df.previous_event_type.isin(["SHOT", "GOAL"]))
    plays_df["rebound"] = np.where(period_mask & rebound_mask, True, False)
    return pd.Series(plays_df.rebound, name="rebound", index=plays_df.index)