# Phase 2 Starter — Ship

This is the starting point for the **Phase 2 (ship)** projects of the DutchEngineer
*Ship an End-to-End ML Product* path. You fork it at **Module 5 (Packaging &
Reproducibility)** and carry the same repository through Modules 6–9.

You fork a fresh starter here rather than continuing your Phase 1 repo so a rough start in
the build phase never blocks you in the ship phase: you begin with a model that already
works and spend your effort on packaging, serving, and deployment.

## What this repo gives you

- A **working package and a `train.py`** for **Adult / Census Income** — the frozen Phase 1
  build. **To get your model, run `python train.py`** (after `pip install -e .`); it writes
  `model/model.joblib`, the artifact your serving layer loads. The package does not change
  from here; you build *around* it.
- The **empty serving, container, deployment, and infrastructure files** for you to write
  (`serve.py`, `Dockerfile`, `compose.yaml`, the frontend, the infra).
- The reference shape to read is
  [`v2.1.0`](https://github.com/adutchengineer/ml-pipeline-starter/releases/tag/v2.1.0) of the
  `ml-pipeline-starter` reference — read it, do not fork it.

## What you build on it

| Module | What you add | Lesson |
|---|---|---|
| M5 — Packaging & Reproducibility | A reproducible, slim Docker image that builds from scratch and scores a record. | https://learn.dutchengineer.org/courses/packaging-reproducibility/ |
| M6 — APIs & Model Serving | A schema-validated `/predict` endpoint plus a batch path. | https://learn.dutchengineer.org/courses/apis-model-serving/ |
| M7 — Frontend & ML Product Thinking | A minimal frontend that consumes the API and presents predictions honestly. | https://learn.dutchengineer.org/courses/frontend-ml-product/ |
| M8 — Cloud Deployment | The product deployed publicly with dev→prod promotion and a working rollback. | https://learn.dutchengineer.org/courses/cloud-deployment/ |
| M9 — Infrastructure as Code | The service's infrastructure declared in version-controlled code. | https://learn.dutchengineer.org/courses/infrastructure-as-code/ |

By the end of Module 8 the product is live on the internet; by Module 9 its infrastructure
is reproducible. This deployed service is what the **Phase 3 (operate)** starter is built
from.

## Approximate structure to build out

The **package, `train.py`, the data, and `pyproject.toml` are given** — that is the model.
The serving and deployment files are empty; you write them. Names are a guide, not a rule.

```
phase2-starter/
├── pyproject.toml           # installable package metadata + deps    (given)
├── README.md
├── .gitignore
├── train.py                 # run it to produce model/model.joblib   (given)
├── data/
│   └── adult_census.csv     # the Adult / Census Income data          (given)
├── model/                   # `python train.py` writes model.joblib here
├── src/
│   └── census_pipeline/     # the frozen serving package              (given)
│       ├── __init__.py
│       ├── data.py
│       ├── features.py
│       ├── split.py
│       ├── model.py
│       ├── artifact.py
│       ├── serve.py         # FastAPI app: /predict + batch (M6)      (you write)
│       └── schema.py        # request/response schemas (M6)           (you write)
├── .dockerignore            # deterministic build context (M5)        (you write)
├── Dockerfile               # reproducible, slim image (M5)           (you write)
├── compose.yaml             # the stack: service + a dependency (M5)  (you write)
├── frontend/index.html      # minimal UI consuming the API (M7)       (you write)
└── infra/main.tf            # infrastructure as code (M9)             (you write)
```

## Fill in

First produce your model from the given code:

```bash
pip install -e .
python train.py        # writes model/model.joblib
```

Then build these empty files, each on its own branch:

**Module 5 — Packaging & Reproducibility**
- `Dockerfile` — a reproducible, slim image that loads the artifact and scores a record.
- `.dockerignore` — keep the build context deterministic.
- `compose.yaml` — bring up the service plus a real dependency (e.g. Postgres) on one command.

**Module 6 — APIs & Model Serving**
- `src/census_pipeline/schema.py` — request/response schemas; exclude any leakage feature.
- `src/census_pipeline/serve.py` — a FastAPI app exposing `/predict` and a batch path, loading `model/model.joblib`.

**Module 7 — Frontend & ML Product Thinking**
- `frontend/index.html` — a minimal UI that calls the API and presents probabilities honestly.

**Module 9 — Infrastructure as Code**
- `infra/main.tf` — the deployed service's infrastructure declared as code.

## How to use it


1. **Fork** this repo to your own account.
2. Clone your fork locally and build to each module's spec and rubric.
3. Work on a **branch** per module (`git checkout -b m5-docker-image`), open a pull request, and
   merge to `main` once it meets the rubric.

## The reference

The package shape to read is
[`adutchengineer/ml-pipeline-starter@v2.1.0`](https://github.com/adutchengineer/ml-pipeline-starter/releases/tag/v2.1.0).
Read it to understand the artifact you are shipping — do not fork it as your project.
