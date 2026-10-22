"""Core models."""

from __future__ import annotations

from enum import Enum
from dataclasses import dataclass


class AssetClass(str, Enum):
    MAJOR = "major"
    LARGE_CAP_ALT = "large_cap_alt"
    STABLECOIN = "stablecoin"
    DEFI = "defi"
    MEME = "meme"
    L2 = "l2"
    RWA = "rwa"
    PERPETUAL = "perpetual"


class Regime(str, Enum):
    TREND = "trend"
    RANGE = "range"
    STRESS = "stress"


@dataclass
class Signal:
    symbol: str
    asset_class: AssetClass
    side: str  # long / short / none
    size: float
    confidence: float
    reason: str
    regime: Regime
