from os import environ

import numpy as np
import pandas as pd

from comet_ml import Experiment
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

np.random.seed(0)


def load_data(train=True):
    if train:
        X = np.load("./data/processed/x_train_2021-11-20.npy") 
        y = np.load("./data/processed/y_train_2021-11-20.npy")
    if not train:
        X = np.load("./data/processed/x_test_2021-11-20.npy") 
        y = np.load("./data/processed/y_test_2021-11-20.npy")
    return X, y


def base_xgb(X, y, params={}):      
    model = XGBClassifier(objective="binary:logistic", use_label_encoder=False, **params)
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    model.fit(x_train, y_train,
              eval_set=[(x_test, y_test)],
              eval_metric=["logloss", "error", "auc"]
    )

    return model


if __name__ == "__main__":
    experiment = Experiment(project_name="hockey-all-star-analytics")
    X, y = load_data()
    model = base_xgb(X, y)
    experiment.end()