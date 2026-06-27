"""Loading the Adult / Census Income data.

Reads the vendored CSV and returns (df, y): the raw feature frame and the binary target
(`above_50k`, ~24% positive). Column names are normalized to snake_case so the rest of
the package can reference them consistently. No transform is applied here — loading only.
"""

import pandas as pd

TARGET = "above_50k"

NUMERIC = ["age", "education_num", "hours_per_week", "capital_gain", "capital_loss"]
CATEGORICAL = ["workclass", "marital_status", "occupation", "relationship", "sex"]


def load_census(path: str = "data/adult_census.csv") -> tuple[pd.DataFrame, pd.Series]:
    """Load the Adult / Census Income data; return (feature_frame, target)."""
    df = pd.read_csv(path)
    df.columns = [c.replace("-", "_") for c in df.columns]
    y = df[TARGET].astype(int)
    x = df.drop(columns=[TARGET])
    return x, y
