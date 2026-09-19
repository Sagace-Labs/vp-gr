# GR data

    data/
      gr_tox21.parquet             standardised table (producing the hash)
      example/
        gr_example.parquet         small stratified fixture, used by the tests

`gr_tox21.parquet` holds one row per compound with the two identity columns —
`inchikey` and `smiles` (standardised) — and three label columns. `label` is the
agonist call, `antagonist` is the antagonist call and `cytotox` is the viability
call. Alongside them are associated `potency_um`, `n_calls`, `active_frac` and,
for each of the other two screens, `<label>_n_calls` and `<label>_active_frac`
as provenance. Only the identity and label columns are hashed, so a provenance
column may be added without moving the dataset hash.

## Origin and processing

PubChem BioAssay AID 720691 and AID 720692, the Tox21 qHTS screens for agonists
and antagonists of the glucocorticoid receptor signalling pathway, and AID
720693, the antagonist assay's cell-viability counter-screen over the same
library, retrieved through the public PUG-REST concise assay endpoint. Rows each
assay called Active or Inactive are kept and rows it called Inconclusive are
dropped. Compound identifiers are resolved to isomeric SMILES through the
compound property endpoint; structures are standardised (normalise, largest
fragment, neutralise); records are collapsed to one row per InChIKey by majority
call, and a tie is dropped.

A standardised structure that RDKit will not read back is dropped too, in order
to avoid featurization outputting all-zeros.

The agonist screen decides which compounds the table holds. Where either other
screen made no call the row carries a null, which records the absence of a
call.

`potency_um` is the median of the potencies reported across a compound's agonist
records and is NaN when none reported one. `n_calls` is how many assay records
collapsed into the row and `active_frac` is the share of them that were Active,
so the majority vote stays auditable. The `antagonist_` and `cytotox_` columns
say the same of the other two screens.

## Rebuilding it

    python -m vp_gr.data fetch --verify

This downloads, re-parses and re-hashes, then compares against the hash the
current version recorded. A mismatch in the hash can indicate upstream changes
to the source data or the processing pipeline.

## Licence

The bundled table is a United States government work in the public domain; see
`../LICENSE-DATA`. That file covers these files only, not the package code or
the trained weights.
