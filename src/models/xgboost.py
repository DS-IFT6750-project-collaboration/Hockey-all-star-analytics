from os import environ

import numpy as np
import pandas as pd

from comet_ml import Experiment
from xgboost import XGBClassifier

COMET_API_KEY = environ.get("COMET_API_KEY")
experiment = Experiment(project_name="hockey-all-star-analytics", api_key=COMET_API_KEY)

def train_xgb(df):
    experiment.log_dataframe_profile(df)
    return 0