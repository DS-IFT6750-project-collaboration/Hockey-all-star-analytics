from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def train_validation_split(X, y, test_size=0.2):
    x_train, y_train, x_val, y_val = train_test_split(X, y, test_size=test_size)
    
def train_logistic_regression(x_train, y_train, x_val, y_val):
    clf = LogisticRegression()
    clf.fit(x_train, y_train)
    return clf