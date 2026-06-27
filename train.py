"""Produce the trained model artifact: run this to get `model/model.joblib`.

This is GIVEN code — the Phase 1 work, frozen. You do not edit it; you run it once to
materialize the artifact your serving layer loads:

    python train.py

It loads the Adult / Census data, builds a leakage-free split, fits and calibrates the
model, and saves a single reloadable `TrainedModel` to `model/model.joblib`. The serving
code you write in M6 loads that file — it does not retrain.
"""

from pathlib import Path

from sklearn.metrics import roc_auc_score

from census_pipeline import (
    CATEGORICAL,
    NUMERIC,
    FeatureTransform,
    leakage_free_split,
    train_artifact,
)
from census_pipeline.data import load_census

OUT = Path("model/model.joblib")


def main() -> None:
    x, y = load_census()
    transform = FeatureTransform(numeric=NUMERIC, categorical=CATEGORICAL)
    x_train, x_test, y_train, y_test = leakage_free_split(x, y, transform)

    # Score the held-out test set so the card records a real metric.
    from sklearn.linear_model import LogisticRegression

    probe = LogisticRegression(max_iter=1000).fit(x_train, y_train)
    auc = float(roc_auc_score(y_test, probe.predict_proba(x_test)[:, 1]))

    model = train_artifact(
        x_train, y_train, transform, metric_name="roc_auc", metric_value=auc
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    model.save(str(OUT))
    print(f"saved {OUT}  (held-out ROC-AUC={auc:.4f})")


if __name__ == "__main__":
    main()
