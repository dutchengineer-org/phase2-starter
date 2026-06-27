"""Feature building — a deterministic transform identical at train and serve.

`FeatureTransform.fit` learns the categorical levels and numeric fill values from the
TRAINING frame only; `transform` applies exactly those, so any later input — the full
frame or one incoming request row — produces the same columns in the same order. The same
fitted object is used at train time and at serve time, which is what makes the two
identical and removes train/serve skew.

Dataset-agnostic: the column lists are passed in, so this works on any tabular set.
"""

import pandas as pd


class FeatureTransform:
    """A fit-once, apply-anywhere feature transform: identical at train and serve.

    Usage::

        ft = FeatureTransform(numeric=[...], categorical=[...]).fit(train_df)
        X_train = ft.transform(train_df)
        X_row = ft.transform(one_request_row)   # same columns, same order
    """

    def __init__(self, numeric: list[str], categorical: list[str]) -> None:
        self.numeric = numeric
        self.categorical = categorical
        self._fill: dict[str, float] = {}
        self._levels: dict[str, list[str]] = {}
        self._columns: list[str] = []

    def fit(self, df: pd.DataFrame) -> "FeatureTransform":
        """Learn fill values and category levels from the TRAINING frame only."""
        self._fill = {c: float(df[c].mean()) for c in self.numeric}
        self._levels = {
            c: sorted(df[c].dropna().astype(str).unique().tolist())
            for c in self.categorical
        }
        # Freeze the output column order so transform always reproduces it.
        self._columns = list(self.numeric) + [
            f"{c}_{level}" for c in self.categorical for level in self._levels[c]
        ]
        return self

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Apply the fitted transform — same columns, same order, for any input."""
        if not self._columns:
            raise RuntimeError("FeatureTransform.transform called before fit")
        out = pd.DataFrame(index=df.index)
        for c in self.numeric:
            out[c] = df[c].fillna(self._fill[c])
        for c in self.categorical:
            col = df[c].astype(str)
            for level in self._levels[c]:
                out[f"{c}_{level}"] = (col == level).astype(int)
        return out[self._columns]
