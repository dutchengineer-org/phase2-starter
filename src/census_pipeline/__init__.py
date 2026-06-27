"""census_pipeline — the frozen v2.1.0 serving package for Adult / Census Income.

This is the Phase 2 starter package: it is COMPLETE and does not change across M5–M9. You
build the serving, container, deployment, and infrastructure layers AROUND it; you do not
edit the package itself.

    from census_pipeline import FeatureTransform, leakage_free_split, train_artifact
"""

from census_pipeline.artifact import ModelCard, TrainedModel, train_artifact
from census_pipeline.data import CATEGORICAL, NUMERIC, TARGET, load_census
from census_pipeline.features import FeatureTransform
from census_pipeline.model import train_and_score
from census_pipeline.split import leakage_free_split

__version__ = "2.1.0"
__all__ = [
    "CATEGORICAL",
    "NUMERIC",
    "TARGET",
    "FeatureTransform",
    "ModelCard",
    "TrainedModel",
    "leakage_free_split",
    "load_census",
    "train_and_score",
    "train_artifact",
]
