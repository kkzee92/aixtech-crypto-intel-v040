# Architecture v0.40

```mermaid
flowchart LR
    FX["Synthetic fixtures or injected public data"] --> AT["Source attestation + lineage"]
    AT --> RG["Regime + multi-factor filters"]
    RG --> ST["Asset-class strategies (adaptive)"]
    ST --> RK["Risk gates: caps, vol scale, correlation, kill switch"]
    RK --> EN["Paper engine only"]
    EN --> AU["Hash-chained audit + timestamps + digests"]
    SEC["Zero-trust controls + redaction"] --> AU
    CLI["CLI: scan / brief / posture"] --> EN
```

## Design principles
- Paper-only by construction. Mode guards refuse live execution.
- Injectable I/O so tests never touch the network.
- Data lineage: every payload carries a digest and source label (SYNTHETIC / PUBLIC_READ).
- Zero-trust: least privilege, assume credentials may leak, redact aggressively.
- Inspired by zeekiankok92 harness: agent rules, CI gates, disclosure trail, human sign-off.

See security-architecture.md for controls.
