# Changelog

Released versions are immutable. A correction to a released version is a new
patch version. This file records *why* each version exists.

## v1

Initial release.

Three endpoints. A compound that kills the cell suppresses the reporter and
reads as an antagonist, so the viability counter-screen ships as its own output.
The agonist screen decides which compounds the table holds; the other two carry
a null where they made no call, and each output is fit on the compounds it
labels.

Signature 1: `gr_agonist`, `gr_antagonist` and `gr_cytotox`.
