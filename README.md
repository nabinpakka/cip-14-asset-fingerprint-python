# cip-14-asset-fingerprint-python

This project is an implementation of modified bech32 python library for asset fingerprint according to CIP-14.
You can learn more about CIP-14 [here](https://cips.cardano.org/cips/cip14/).

## Requirements

- python version >= 3.6
- libraries (bech32, blake2d from hashlib)

## Work flow

- Modify encode function of bech32. You can copy and paste contents from "modifiedBechInit.py"
- Run Fingerprint.py to test.