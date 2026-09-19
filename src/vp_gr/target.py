"""The endpoints this pathway predicts.

Frozen so the data sources are auditable.

All three assays were verified live against PubChem on 2026-09-06, and screen
the same library:

    AID 720691   qHTS assay to identify small molecule agonists of the
                 glucocorticoid receptor (GR) signaling pathway
                                                          10486 substances
    AID 720692   the same, antagonists                    10486 substances
    AID 720693   the antagonist assay's cell viability
                 counter screen                           10486 substances
"""

from __future__ import annotations

from dataclasses import dataclass

__all__ = ["ANTAGONIST", "CYTOTOX", "TARGET", "TARGETS", "Endpoint", "all_names", "get"]


@dataclass(frozen=True)
class Endpoint:
    """One molecular initiating event, identified by the assay that reads it out."""

    name: str
    pathway: str
    mie: str
    pubchem_aid: int
    assay_name: str


TARGET = Endpoint(
    name="AGONIST",
    pathway="glucocorticoid receptor / NR3C1",
    mie=(
        "binding of the glucocorticoid receptor ligand-binding domain by a steroid-like "
        "ligand, which drives the receptor to its response element"
    ),
    pubchem_aid=720691,
    assay_name=(
        "qHTS assay to identify small molecule agonists of the glucocorticoid "
        "receptor (GR) signaling pathway"
    ),
)

ANTAGONIST = Endpoint(
    name="ANTAGONIST",
    pathway="glucocorticoid receptor / NR3C1",
    mie=(
        "occupancy of the glucocorticoid receptor ligand-binding domain that blocks "
        "the receptor's response to its hormone"
    ),
    pubchem_aid=720692,
    assay_name=(
        "qHTS assay to identify small molecule antagonists of the glucocorticoid "
        "receptor (GR) signaling pathway"
    ),
)

CYTOTOX = Endpoint(
    name="VIABILITY",
    pathway="glucocorticoid receptor / NR3C1",
    mie="loss of cell viability, which registers on the reporter readout as a consequence",
    pubchem_aid=720693,
    assay_name=(
        "qHTS assay to identify small molecule antagonists of the glucocorticoid "
        "receptor (GR) signaling pathway - cell viability counter screen"
    ),
)

TARGETS: dict[str, Endpoint] = {
    "AGONIST": TARGET,
    "ANTAGONIST": ANTAGONIST,
    "VIABILITY": CYTOTOX,
}


def get(name: str) -> Endpoint:
    try:
        return TARGETS[name.upper()]
    except KeyError:
        raise KeyError(f"unknown target {name!r}; known: {sorted(TARGETS)}") from None


def all_names() -> list[str]:
    return sorted(TARGETS)
