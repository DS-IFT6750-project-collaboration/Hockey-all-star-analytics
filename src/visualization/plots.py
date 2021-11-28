import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.calibration import calibration_curve, CalibrationDisplay
import pandas as pd
import numpy as np

def plots (clf, X_test, y_test):
    valid = pd.DataFrame()
    valid['pred_prob'] = clf.predict_proba(X_test)[::,1]
    valid['true_labels'] = np.array(y_test)
    percentile = [[np.percentile(valid['pred_prob'], i), np.percentile(valid['pred_prob'], i+5)] for i in range(0,100,5)]

    goal_rate = []
    cum=0
    for i in range(0, len(percentile)):
        goals = valid[ (valid['pred_prob']<=percentile[i][1])&(valid['pred_prob']>percentile[i][0]) & (valid['true_labels']==1)].shape[0]

        no_goals = valid[(valid['pred_prob']<=percentile[i][1])&(valid['pred_prob']>percentile[i][0]) & (valid['true_labels']==0)].shape[0]

        if goals==0:
            goal_rate.append(0)
        else:
            goal_rate.append((goals*100)/(goals+no_goals))
    total_goal = valid[valid['true_labels']==1].shape[0]
    
    cumulative = []
    for i in range(0, len(percentile)):
        goals = valid[(valid['pred_prob']>=percentile[i][0]) & (valid['true_labels']==1)].shape[0]
        cumulative.append(goals*100/total_goal)
    #cumulative.append(0)
        
    Shot_prob_percentile = [i for i in range(0,100, 5)]
    
    sns.set(rc={'figure.figsize':(10,5)})
    #ROC_AUC
    fpr, tpr, _ = metrics.roc_curve(y_test,  valid['pred_prob'])
    auc = metrics.roc_auc_score(y_test, valid['pred_prob'])
    plt.plot(fpr,tpr,label="logistic(1-Goals) , auc="+str(auc))
    fpr, tpr, _ = metrics.roc_curve(y_test,  random_baseline)
    plt.legend(loc=4)
    plt.xticks(rotation=50)
    plt.xlabel('False Positive Rate', fontsize=18)
    plt.ylabel('True Positive rate', fontsize=16)
    #plt.show()
    plt.savefig("/Users/henaghonia/Desktop/udem/Sem-1/Data-science/ift6758-Milestone2_blog/images/ROC_AUC1.png")
    plt.show()
    
    ##Plot of goal rate vs Shot probability percentile
    plt.plot(Shot_prob_percentile, goal_rate)
    plt.xlim(max(Shot_prob_percentile), min(Shot_prob_percentile))
    plt.ylim(0, 100)
    plt.xlabel('Shot probability model percentile', fontsize=14)
    plt.ylabel('Goal rate', fontsize=14)
    #plt.show()
    plt.savefig("/Users/henaghonia/Desktop/udem/Sem-1/Data-science/ift6758-Milestone2_blog/images/Goal_rate_Shot_prob.png")
    plt.show()
    
    ##Plot of cumulative goal rate vs Shot probability percentile
    plt.plot(Shot_prob_percentile, cumulative)
    plt.xlim(max(Shot_prob_percentile), min(Shot_prob_percentile))
    #plt.ylim(0, 100)
    plt.xlabel('Shot probability model percentile', fontsize=14)
    plt.ylabel('Goal rate', fontsize=14)
    #plt.show()
    plt.savefig("/Users/henaghonia/Desktop/udem/Sem-1/Data-science/ift6758-Milestone2_blog/images/cum_Shot_prob.png")
    plt.show()
    
    fig = plt.figure(figsize=(10, 10))
    gs = GridSpec(4, 2)
    colors = plt.cm.get_cmap("Dark2")

    ax_calibration_curve = fig.add_subplot(gs[:2, :2])
    display = CalibrationDisplay.from_predictions(
            
            valid['true_labels'],
            valid['pred_prob'],
            name='logistic',
            n_bins=40,
            ax=ax_calibration_curve,
            
        )
    

    
    ax_calibration_curve.grid()
    ax_calibration_curve.set_title("Calibration plots")
    plt.savefig("/Users/henaghonia/Desktop/udem/Sem-1/Data-science/ift6758-Milestone2_blog/images/Calibration_logistic.png")


    
plots (clf_dist, X_test[['dist_from_net']], y_test)

