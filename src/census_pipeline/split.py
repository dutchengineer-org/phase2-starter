"""Leakage-free splitting — fit the transform on the training rows only.

Split the RAW frame first, fit the transform on the training split only, then apply the
fitted transform to both splits — so no test-row statistics leak into the training matrix.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

from census_pipeline.features import FeatureTransform

SEED = 42


def leakage_free_split(
    df: pd.DataFrame,
    y: pd.Series,
    transform: FeatureTransform,
    test_size: float = 0.2,
    random_state: int = SEED,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Split first, fit the transform on TRAIN only, apply to both. Returns
    (X_train, X_test, y_train, y_test) with no test statistics in the training matrix."""
    raw_train, raw_test, y_train, y_test = train_test_split(
        df, y, test_size=test_size, random_state=random_state, stratify=y
    )
    transform.fit(raw_train)
    x_train = transform.transform(raw_train)
    x_test = transform.transform(raw_test)
    return x_train, x_test, y_train, y_test
