"""Research parameter catalog for v0.40."""

from __future__ import annotations

import hashlib
import json
from crypto_intel.models import AssetClass

CATALOG_VERSION = "0.40.0"

SPECS = {
    AssetClass.MAJOR: {"size_cap": 0.07, "cost_bps": 8.0, "horizon": 16},
    AssetClass.LARGE_CAP_ALT: {"size_cap": 0.035, "cost_bps": 14.0, "horizon": 12},
    AssetClass.STABLECOIN: {"size_cap": 0.0, "cost_bps": 2.0, "depeg": 0.0045},
    AssetClass.DEFI: {"size_cap": 0.018, "cost_bps": 22.0, "horizon": 10},
    AssetClass.MEME: {"size_cap": 0.004, "cost_bps": 45.0, "horizon": 3},
    AssetClass.L2: {"size_cap": 0.025, "cost_bps": 16.0, "horizon": 12},
    AssetClass.RWA: {"size_cap": 0.018, "cost_bps": 12.0, "horizon": 24},
    AssetClass.PERPETUAL: {"size_cap": 0.015, "cost_bps": 10.0, "horizon": 8},
}


def parameter_digest() -> str:
    material = json.dumps({"version": CATALOG_VERSION, "specs": {k.value: v for k, v in SPECS.items()}}, sort_keys=True)
    return hashlib.sha256(material.encode()).hexdigest()
