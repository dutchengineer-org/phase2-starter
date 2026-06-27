# Phase 2 Starter — Ship

This is the starting point for the **Phase 2 (ship)** projects of the DutchEngineer
*Ship an End-to-End ML Product* path. You fork it at **Module 5 (Packaging &
Reproducibility)** and carry the same repository through Modules 6–9.

You fork a fresh starter here rather than continuing your Phase 1 repo so a rough start in
the build phase never blocks you in the ship phase: you begin with a model that already
works and spend your effort on packaging, serving, and deployment.

## What this repo gives you

- The **file layout** for a Phase 2 (ship) project. Every file is empty — you write all of it,
  including `pyproject.toml` and adding the **Adult / Census Income** data yourself.
- A target to build toward: the serving package and the `train.py` that produces your model
  artifact (`model/model.joblib`). Carry these forward from your Phase 1 project, then build
  the serving, container, deployment, and infrastructure layers around the artifact.
- The reference shape to read is
  [`v2.1.0`](https://github.com/adutchengineer/ml-pipeline-starter/releases/tag/v2.1.0) of the
  `ml-pipeline-starter` reference — read it to see the package shape, do not fork it.

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

This is the shape your repo grows into across M5–M9. Every `.py` file is empty — you write
all of it — including `pyproject.toml` and the data loading. The repo gives you the file
layout and nothing else; the code is yours. Names are a guide, not a rule — match the layout, not the
spelling.

```
phase2-starter/
├── pyproject.toml           # package metadata + deps              (you write)
├── README.md
├── .gitignore
├── data/                    # add the Adult / Census CSV here       (you add)
│   └── adult_census.csv     # the Adult / Census Income data        (you add)
├── model/                   # your produced artifact lands here
├── train.py                 # produce model/model.joblib            (you write)
├── src/
│   └── census_pipeline/     # the package — you write all of it     (you write)
│       ├── __init__.py
│       ├── data.py
│       ├── features.py
│       ├── split.py
│       ├── model.py
│       ├── artifact.py
│       ├── serve.py         # FastAPI app: /predict + batch (M6)
│       └── schema.py        # request/response schemas (M6)
├── .dockerignore            # deterministic build context (M5)
├── Dockerfile               # reproducible, slim image (M5)
├── compose.yaml             # the stack: service + a dependency (M5)
├── frontend/index.html      # minimal UI consuming the API (M7)
└── infra/main.tf            # infrastructure as code (M9)
```

## Fill in

Every file in this repo is empty except this README. You write all of it — `pyproject.toml`,
the package code, and adding the Adult / Census data yourself. The list below is what each empty file becomes, in the module that
fills it.

**Carried in from Phase 1 (your build modules)**
- `train.py` and `src/census_pipeline/{__init__,data,features,split,model,artifact}.py` — the
  package and the script that produces `model/model.joblib`. Bring these forward from your
  Phase 1 project, or rebuild them here; the serving work loads the artifact they produce.

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
3. Work on a **branch** per module (`git checkout -b m5-docker`), open a pull request, and
   merge to `main` once it meets the rubric.

## The reference

The package shape to read is
[`adutchengineer/ml-pipeline-starter@v2.1.0`](https://github.com/adutchengineer/ml-pipeline-starter/releases/tag/v2.1.0).
Read it to understand the artifact you are shipping — do not fork it as your project.
