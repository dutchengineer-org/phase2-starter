"""Training and scoring on a pre-split, leakage-free feature matrix."""

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score


def train_and_score(
    x_train: pd.DataFrame,
    x_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series,
) -> float:
    """Fit a logistic regression on the training matrix; return the held-out ROC-AUC."""
    model = LogisticRegression(max_iter=1000).fit(x_train, y_train)
    proba = model.predict_proba(x_test)[:, 1]
    return float(roc_auc_score(y_test, proba))
