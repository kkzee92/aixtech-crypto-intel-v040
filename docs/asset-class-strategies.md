# Asset-class strategies (v0.40 enhanced)

Research heuristics only. Each class has edge hypothesis, entry filters, invalidation, horizon, and size cap. Adaptive filters respond to volatility and regime. Not a promise of returns.

## Regime overlay
- **Trend**: sustained directional move with contained range.
- **Range**: mean-reverting conditions.
- **Stress**: elevated bar range / volatility — directional ideas stand aside or size reduced.

## Major (BTC, ETH)
Hypothesis: liquid majors support EMA trend following with multi-timeframe confirmation proxy and volume filter. Adaptive EMA lengths based on recent ATR. Mean reversion only in range + RSI extremes. Cap 6-8%. Horizon 12-24 bars. Cost 6-10 bps.
Enhancement: volatility-scaled size; relative strength vs broad market proxy.

## Large-cap alt
Hypothesis: volume-confirmed breakouts work outside stress. Relative strength vs major required. Cap 3-4%. Cost 12-16 bps.
Enhancement: lag veto if major is diverging; volume profile proxy.

## Stablecoin
Hypothesis: peg integrity is the signal. Multi-stable dispersion watch. 15-20 bp watch, 40-50 bp depeg alert. Size forced to 0. Contagion count across stables can tighten risk.
Enhancement: correlation matrix of major stables; alert on sudden basis.

## DeFi
Hypothesis: trend only in calm regimes; high vol or stress = gap risk. Liquidity proxy (volume / price impact). Cap 1.5-2%. Cost 20-25 bps.
Enhancement: TVL change proxy (simulated), funding or yield filter.

## Meme
Hypothesis: most bursts are untradeable. Require extreme short-term burst + rising volume + not over-extended. Short horizon (2-4 bars). Cap 0.3-0.5%. Cost 40-50 bps.
Enhancement: decay rate filter; social-volume proxy (synthetic).

## L2
Hypothesis: relative strength vs L1 or sector benchmark. No trade if benchmark stressed. Cap 2-3%. Cost 14-18 bps.
Enhancement: cross-chain flow or bridge volume proxy; lag vs major.

## RWA
Hypothesis: slow, yield-oriented. Halt on large gaps or stress. Cap 1.5-2%. Horizon longer. Cost 10-14 bps.
Enhancement: compliance / lock-up filter proxy; yield differential vs stables.

## Perpetual
Hypothesis: funding-rate carry when spot drift contained; crowded funding as alert not signal. Cap 1-2%. Cost 8-12 bps.
Enhancement: open-interest change proxy; basis vs spot; liquidation cascade risk filter.

## Still out of scope
Live order routing, withdrawal keys, real exchange adapters, claims of future returns.
