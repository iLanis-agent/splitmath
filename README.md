# Split Math

The log splitter honesty tool. The tonnage on the box was never told
about the knot, the cycle time on the sticker was measured with an
empty ram, and the horsepower was never asked where the amps come
from. Split Math sizes the ram against the round's honest tons, turns
the sticker cycle into a loaded pace, and deflates the horsepower to
what the wall can feed.

- Live app: https://ilanis-agent.github.io/splitmath/app.html
- Landing: https://ilanis-agent.github.io/splitmath/

## What it does

1. **The tonnage truth** - diameter x tons-per-inch (labeled norms:
   0.5 seasoned pine, 1 oak, 1.5 green knotty) held against the box
   tonnage, with verdicts at 80 and 100 percent.
2. **The cycle truth** - the sticker cycle is the empty ram; under
   load the honest cycle is about 1.4x (labeled norm), into
   rounds-per-hour.
3. **The circuit truth** - honest horsepower = 120 V x amps x 0.8
   continuous-load derate (labeled norm) / 746, with verdicts on the
   sticker's ratio to it.

## Files

- `engine.js` - pure functions (`tonnagePlan`, `cyclePlan`, `circuitPlan`) plus renderers
- `app.html` - the app; `index.html` - the landing page
- `oracle.py` - independent Python mirror of the engine
- `test.js` + `expected.json` - 26 oracle cases, `node test.js` runs green

The norms are labeled; the maul keeps the honest ledger.
