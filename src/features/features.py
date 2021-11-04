import pandas as pd
import numpy as np

def basic_features(plays_df):
    dist_from_net = _dist_from_net(plays_df)
    angle_from_net = _angle_from_net(plays_df)
    is_goal = _is_goal(plays_df)
    empty_net = _empty_net(plays_df)
    
    features_df = pd.concact([dist_from_net, angle_from_net, is_goal, empty_net], axis=1)
    return feature_df



def _dist_from_net(plays_df):
    net_pos = np.array([100-11, 0])
    dist_from_net = np.sqrt(np.sum((net_pos - plays_df[["x_coord_norm", "y_coord_norm"]]) ** 2, axis=1))
    return dist_from_net

def _angle_from_net(plays_df):
    return
    
def _is_goal(plays_df):
    str_to_int = {"SHOT": 0, "GOAL": 1}
    is_goal = plays_df.event_type_id.replace(str_to_int)
    return is_goal
    