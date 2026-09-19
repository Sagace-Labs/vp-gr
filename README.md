# vp-gr

Predicts glucocorticoid receptor (NR3C1) agonism and antagonism from a SMILES
string — a molecular initiating event for drug-induced liver injury, where a
xenobiotic that drives or blocks the receptor perturbs hepatic gluconeogenesis,
lipid handling and the inflammatory response.

## Install

    pip install vp-gr

## Use

    from vp_gr import predict
    predict(["CC(=O)Oc1ccccc1C(=O)O"])
    # -> DataFrame[gr_agonist, gr_antagonist, gr_cytotox]

Returns one row per input and one column per declared output. `gr_agonist` is
the probability of activating the receptor reporter, `gr_antagonist` the
probability of suppressing the hormone-driven reporter, and `gr_cytotox` the
probability of reducing viability in the counter-screen over the same library.
Each output is fit and scored on the compounds its own screen called.
Unparseable SMILES come back as NaN. Pin a version with
`predict(smiles, version="v1")`; list what is available with `versions()`.

## Current version

**v1**, signature 1, measured under protocols `scaffold-shuffle-5seed@1`
and `scaffold-balanced-5seed@1`. The full record — metrics per output,
protocol and seed, dataset hash, environment — is in
[`src/vp_gr/versions/v1/CARD.md`](src/vp_gr/versions/v1/CARD.md).

## Data

PubChem BioAssay AID 720691 and AID 720692, the Tox21 qHTS screens for agonists
and antagonists of the glucocorticoid receptor signalling pathway, and AID
720693, the antagonist assay's cell-viability counter-screen over the same
library. All three are reduced to one row per compound labelled by the majority
call across its assay records, retrieved 2026-09-06 and redistributed here as a
United States government work in the public domain. Rebuild and check for
upstream drift with `python -m vp_gr.data fetch --verify`; see
[`data/README.md`](data/README.md) for the expected layout.

## Retrain

    python -m vp_gr.train --version v2 --reason "why this version exists"
    python -m vp_gr.evaluate --version v2

`train` fits one deployment model per output on the whole dataset and writes a
new version directory; `evaluate` refits per seed under the protocol and
records what those held-out models scored. Reproducibility is to the recorded
dataset hash and environment, which can change.

## Licence

Code is Apache-2.0 ([`LICENSE`](LICENSE)). The bundled dataset is in the public
domain ([`LICENSE-DATA`](LICENSE-DATA)).

## Cite

See [`CITATION.cff`](CITATION.cff).
