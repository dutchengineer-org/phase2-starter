# Phase 2 Starter — Ship

This is the starting point for the **Phase 2 (ship)** projects of the DutchEngineer
*Ship an End-to-End ML Product* path. You fork it at **Module 5 (Packaging &
Reproducibility)** and carry the same repository through Modules 6–9.

You fork a fresh starter here rather than continuing your Phase 1 repo so a rough start in
the build phase never blocks you in the ship phase: you begin with a model that already
works and spend your effort on packaging, serving, and deployment.

## What this repo gives you

- A **trained model artifact** for the **Adult / Census Income** data — a serialized,
  calibrated model that loads and predicts, the same shape Module 4 produced.
- The **working package** that produced it. The package matches the reference shape frozen
  at [`v2.1.0`](https://github.com/adutchengineer/ml-pipeline-starter/releases/tag/v2.1.0)
  — the final version of the `ml-pipeline-starter` reference. **The package does not change
  again from here**; every Phase 2 module builds *around* this artifact rather than growing
  the package.

## What you build on it

| Module | What you add |
|---|---|
| M5 — Packaging & Reproducibility | A reproducible, slim Docker image that builds from scratch and scores a record. |
| M6 — APIs & Model Serving | A schema-validated `/predict` endpoint plus a batch path. |
| M7 — Frontend & ML Product Thinking | A minimal frontend that consumes the API and presents predictions honestly. |
| M8 — Cloud Deployment | The product deployed publicly with dev→prod promotion and a working rollback. |
| M9 — Infrastructure as Code | The service's infrastructure declared in version-controlled code. |

By the end of Module 8 the product is live on the internet; by Module 9 its infrastructure
is reproducible. This deployed service is what the **Phase 3 (operate)** starter is built
from.

## How to use it

1. **Fork** this repo to your own account.
2. Clone your fork locally and build to each module's spec and rubric.
3. Work on a **branch** per module (`git checkout -b m5-docker`), open a pull request, and
   merge to `main` once it meets the rubric.

## The reference

The package shape to read is
[`adutchengineer/ml-pipeline-starter@v2.1.0`](https://github.com/adutchengineer/ml-pipeline-starter/releases/tag/v2.1.0).
Read it to understand the artifact you are shipping — do not fork it as your project.
