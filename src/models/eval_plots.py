import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import RocCurveDisplay
from sklearn.calibration import CalibrationDisplay


def random_baseline(y_test):
    baseline = np.zeros(y_test.shape)
    baseline[:int(len(baseline)/2)] = 1
    np.random.shuffle(baseline)
    return baseline

def plot_roc_auc(y_true, y_pred):
    fig, axs = plt.subplots(1, 1)

    RocCurveDisplay.from_predictions(y_true, y_pred, ax=axs, name="XGBoost baseline")
    
    baseline = random_baseline(y_true)
    baseline_kwargs = {
        "dashes": (1, 2, 1)
    }
    RocCurveDisplay.from_predictions(y_true, baseline, ax=axs, name="Random baseline", **baseline_kwargs)
    
    plt.title("Responder-Operator Curve (ROC)")
    plt.show()


def plot_goal_rate(y_true, y_proba):
    valid = pd.DataFrame()
    valid['true_labels'] = np.array(y_true)
    percentile = [[np.percentile(y_proba, i), np.percentile(y_proba, i+5)] for i in range(0,100,5)]
    total_goal = np.sum(y_true)

    goal_rate = []
    cum=0
    for i in range(0, len(percentile)):
        goals = valid[ (y_proba<=percentile[i][1])&(y_proba>percentile[i][0]) & (valid['true_labels']==1)].shape[0]
        no_goals = valid[(y_proba<=percentile[i][1])&(y_proba>percentile[i][0]) & (valid['true_labels']==0)].shape[0]
        if goals==0:
            goal_rate.append(0)
        else:
            goal_rate.append((goals*100)/(goals+no_goals))
     
    shot_prob_percentile = np.arange(0, 100, 5)
       
    ##Plot of goal rate vs Shot probability percentile
    plt.plot(shot_prob_percentile, goal_rate)
    plt.xlim(100, 0)
    plt.ylim(0, 100)
    plt.title("Goal Rate")
    plt.xlabel('Shot probability model percentile', fontsize=14)
    plt.ylabel('Goals / (Shots + Goals)', fontsize=14)
    plt.show()


def plot_cumulative_proportion(y_true, y_proba):
    valid = pd.DataFrame()
    valid['true_labels'] = np.array(y_true)
    percentile = [[np.percentile(y_proba, i), np.percentile(y_proba, i+5)] for i in range(0,100,5)]
    #percent = np.percentile(proba[:, 1], np.linspace(0, 100))
    total_goal = np.sum(y_true)
    
    cumulative = []
    for i in range(0, len(percentile)-1):
        goals = valid[(y_proba>=percentile[i][0]) & (y_true==1)].shape[0]
        cumulative.append(goals*100/total_goal)
    cumulative.append(0)
    
    shot_prob_percentile = np.arange(0, 100, 5)
    
    plt.plot(shot_prob_percentile, cumulative)
    plt.xlim(100, 0)
    plt.ylim(0, 100)
    plt.title("Cumulative % of goals")
    plt.xlabel('Shot probability model percentile', fontsize=14)
    plt.ylabel('Proportion', fontsize=14)
    plt.show()
  
    
def plot_calibration_curve(y_true, y_proba):
    fig, axs = plt.subplots(1, 1)

    CalibrationDisplay.from_predictions(y_true, y_proba, ax=axs, name="XGBoost baseline")
    
    plt.title("Calibration Curve")
    plt.show()