# v0.40 enhancements

## Strategy
- Adaptive multi-factor filters per asset class (volatility scaling, relative strength, volume confirmation, regime overlay).
- Refined size caps and cost assumptions.
- Proxy indicators for multi-timeframe, open interest, liquidity, yield differentials.

## Cyber / data security
- Expanded zero-trust model with stronger isolation between research and any future execution planes.
- Advanced secret redaction patterns (including seed phrases, cloud keys, PATs).
- Explicit data lineage digests on all research payloads.
- Updated threat model and RBAC.
- Harness integration: agent rules, recommended CI gates, disclosure trail style from zeekiankok92/aixtech-agent-harness-demo.

## Process
- Paper-only invariants preserved.
- Synthetic fixtures only.
- Human review and auditability emphasized.

This version consolidates and advances prior AIxTech crypto-intel iterations while adopting the agent-harness safety patterns.
