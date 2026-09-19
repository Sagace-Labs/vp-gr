# gr v1

_Generated from `manifest.toml` and `metrics.json`. Do not edit._

Released 2026-09-06 · signature 1

**Why this version.** first release: binary XGBoost on Morgan, MACCS and RDKit descriptors over the Tox21 glucocorticoid-receptor screens

## Outputs

| column | dtype | range | meaning |
|---|---|---|---|
| `gr_agonist` | float32 | 0.0–1.0 | P(activates the glucocorticoid receptor reporter in the Tox21 qHTS agonist screen) |
| `gr_antagonist` | float32 | 0.0–1.0 | P(suppresses the hormone-driven glucocorticoid receptor reporter in the Tox21 qHTS antagonist screen) |
| `gr_cytotox` | float32 | 0.0–1.0 | P(reduces viability in the counter-screen over the same library). A compound that kills the cell suppresses the reporter and reads as an antagonist, so a high score here qualifies the antagonist column |

Missing values: NaN when RDKit cannot parse the input SMILES

## Performance — `scaffold-shuffle-5seed@1`

Protocol `scaffold-shuffle-5seed@1` — Bemis-Murcko scaffold split with scaffold groups permuted by seed, so distinct seeds give distinct test sets. Five seeds; report mean and standard deviation over the held-out test folds.

Evaluated 2026-09-06 on n_train=5201, n_val=394, n_test=1340.

### `gr_agonist`

| metric | mean | std | per seed |
|---|---|---|---|
| auc_roc | 0.799 | 0.047 | 0.877, 0.829, 0.748, 0.775, 0.765 |
| auprc | 0.157 | 0.176 | 0.019, 0.418, 0.017, 0.011, 0.321 |
| mcc | 0.108 | 0.133 | 0.000, 0.279, 0.000, -0.001, 0.262 |
| brier | 0.108 | 0.083 | 0.004, 0.184, 0.013, 0.147, 0.193 |

### `gr_antagonist`

Measured on n_train=3871, n_val=285, n_test=1068.

| metric | mean | std | per seed |
|---|---|---|---|
| auc_roc | 0.728 | 0.164 | 0.894, 0.859, 0.536, 0.522, 0.829 |
| auprc | 0.218 | 0.167 | 0.353, 0.440, 0.033, 0.025, 0.237 |
| mcc | 0.206 | 0.153 | 0.266, 0.413, 0.063, -0.004, 0.289 |
| brier | 0.135 | 0.074 | 0.025, 0.069, 0.216, 0.182, 0.185 |

### `gr_cytotox`

Measured on n_train=4920, n_val=370, n_test=1276.

| metric | mean | std | per seed |
|---|---|---|---|
| auc_roc | 0.769 | 0.082 | 0.692, 0.875, 0.773, 0.664, 0.841 |
| auprc | 0.129 | 0.150 | 0.016, 0.214, 0.022, 0.007, 0.387 |
| mcc | 0.139 | 0.182 | -0.010, 0.210, 0.037, -0.007, 0.465 |
| brier | 0.113 | 0.095 | 0.054, 0.032, 0.229, 0.227, 0.021 |

## Performance — `scaffold-balanced-5seed@1`

Protocol `scaffold-balanced-5seed@1` — Bemis-Murcko scaffold split with scaffold groups permuted by seed and each group placed in the fold it overfills least, so a group larger than a fold's capacity settles in train instead of starving that fold. Same fold fractions, seeds and metrics as scaffold-shuffle-5seed@1; only the packing differs. Five seeds; report mean and standard deviation over the held-out test folds.

Evaluated 2026-09-19 on n_train=5585, n_val=533, n_test=817.

### `gr_agonist`

| metric | mean | std | per seed |
|---|---|---|---|
| auc_roc | 0.800 | 0.022 | 0.822, 0.800, 0.800, 0.760, 0.820 |
| auprc | 0.416 | 0.134 | 0.534, 0.281, 0.540, 0.226, 0.499 |
| mcc | 0.354 | 0.127 | 0.456, 0.217, 0.540, 0.227, 0.332 |
| brier | 0.107 | 0.065 | 0.157, 0.163, 0.028, 0.025, 0.159 |

### `gr_antagonist`

Measured on n_train=4264, n_val=379, n_test=581.

| metric | mean | std | per seed |
|---|---|---|---|
| auc_roc | 0.860 | 0.028 | 0.885, 0.841, 0.845, 0.828, 0.901 |
| auprc | 0.497 | 0.115 | 0.652, 0.464, 0.404, 0.356, 0.607 |
| mcc | 0.407 | 0.110 | 0.504, 0.413, 0.244, 0.331, 0.543 |
| brier | 0.071 | 0.025 | 0.069, 0.069, 0.118, 0.050, 0.048 |

### `gr_cytotox`

Measured on n_train=5314, n_val=499, n_test=753.

| metric | mean | std | per seed |
|---|---|---|---|
| auc_roc | 0.769 | 0.071 | 0.728, 0.779, 0.897, 0.686, 0.757 |
| auprc | 0.171 | 0.054 | 0.136, 0.243, 0.227, 0.101, 0.150 |
| mcc | 0.119 | 0.055 | 0.136, 0.168, 0.128, 0.012, 0.151 |
| brier | 0.091 | 0.076 | 0.231, 0.029, 0.033, 0.109, 0.051 |

> Comparable only with metrics carrying the same protocol id.

## Data

Tox21 glucocorticoid receptor qHTS — PubChem BioAssay AID 720691 (qHTS assay to identify small molecule agonists of the glucocorticoid receptor (GR) signaling pathway), AID 720692 (qHTS assay to identify small molecule antagonists of the glucocorticoid receptor (GR) signaling pathway), AID 720693 (qHTS assay to identify small molecule antagonists of the glucocorticoid receptor (GR) signaling pathway - cell viability counter screen), rows called Active or Inactive, one row per compound labelled by majority call across its assay records. Retrieved 2026-09-06, licensed public-domain, redistributed here.

`6935` compounds, positive rate `0.022`, table SHA-256 `fe5cb4b40fe6b9e8…`

Regenerate and check for upstream drift with `python -m vp_gr.data fetch --verify`.

## Model

xgboost-binary on `combo3` features. Shipped weights: one model per output, each on every compound its endpoint labels minus a 10% scaffold carve used for early stopping

`weights.joblib` SHA-256 `9f7617a32b1473d3…`

## Provenance

Environment: python 3.11.11, rdkit 2026.03.5, xgboost 3.2.0.

Reproducibility is to this dataset hash and this environment, not bit-exact: the sources are live endpoints and RDKit descriptor values move between releases.
