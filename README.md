# AIxTech Crypto Intel v0.40

Paper-only automated cryptocurrency **trading information system**. Research, signals, and risk evaluation only. No live order placement, no exchange secret storage, not financial advice.

Inspired by the AI-agent harness practices from [zeekiankok92/aixtech-agent-harness-demo](https://github.com/zeekiankok92/aixtech-agent-harness-demo) (CI gates, PDPA-style guards, disclosure trail, human review).

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![version](https://img.shields.io/badge/version-0.40-blue)
![mode](https://img.shields.io/badge/execution-paper%20only-orange)
![Licence](https://img.shields.io/badge/licence-MIT-green)

## Features
- Asset-class-specific strategies with adaptive multi-factor filters (regime, volume, volatility, relative strength).
- Strengthened cyber and data security architecture: zero-trust, advanced redaction, data lineage, isolation.
- Hash-chained audit logs, source attestation, kill switches, class-based risk caps.
- Synthetic fixtures only; injectable I/O for tests.
- CI-style gates recommended (ruff, pytest, gitleaks, personal-data tripwire).

## Asset Classes
See [docs/asset-class-strategies.md](docs/asset-class-strategies.md) for per-class research rules, enhancements, and risk parameters.

## Security
See [docs/security-architecture.md](docs/security-architecture.md) and [docs/v040-enhancements.md](docs/v040-enhancements.md).

## Run (research mode)
```bash
python3 -m venv .venv && source .venv/bin/activate
# pip install -r requirements-dev.txt  # if present
# python -m crypto_intel scan fixtures/candles_synthetic.json
```

**Honesty notes:** Scores describe synthetic data only. No live connectors. Promote signals only in a separate, human-approved system.

## Licence
MIT. Builds on prior AIxTech crypto-intel versions.
