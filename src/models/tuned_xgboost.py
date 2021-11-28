from os import environ

import numpy as np
import pandas as pd

from comet_ml import Experiment
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

np.random.seed(0)

def preprocess_data():
    season_plays_df = pd.read_csv("./data/processed/plays_2015-2020.csv", index_col=False)
    train_df, test_df = split_dataset(season_plays_df)

def load_data(train=True):
    if train:
        X = np.load("./data/processed/x_train_2021-11-20.npy") 
        y = np.load("./data/processed/y_train_2021-11-20.npy")
    if not train:
        X = np.load("./data/processed/x_test_2021-11-20.npy") 
        y = np.load("./data/processed/y_test_2021-11-20.npy")
    return X, y


def load_params():
    params={
        "n_estimators": 100,
        "max_depth": 4,
        "learning_rate": 0.1,
    }
    
    return params


def base_xgb(X, y, params):      
    model = XGBClassifier(objective="binary:logistic", **params)
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    model.fit(x_train, y_train,
              eval_set=[(x_test, y_test)],
              eval_metric=["logloss", "error", "auc"]
    )

    return model


if __name__ == "__main__":
    experiment = Experiment(project_name="hockey-all-star-analytics")
    X, y = load_data()
    params = load_params()
    model = base_xgb(X, y, params)
    experiment.end()