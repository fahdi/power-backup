# Home: usage and requirements (draft)

A second site, separate from the office in [usage.md](usage.md). All ACs are Kenwood inverter ACs.
This is a draft; the open questions below decide the system size.

## Loads

| Load | Qty | Rated each (W) | Realistic running each (W) | Rated total (W) | Running total (W) |
|---|---:|---:|---:|---:|---:|
| Kenwood eSmart Onyx 1.5 ton (KES‑1866S) | 8 | ~1800 | ~1000 | 14,400 | 8,000 |
| Kenwood 1 ton inverter | 1 | ~1200 | ~700 | 1,200 | 700 |
| Kenwood 2 ton floor‑standing inverter (bought, not yet installed) | 2 (to confirm) | ~2400 | ~1350 | 4,800 | 2,700 |
| LED lights (6–8 per room, ~11 rooms → up to ~88) | ~88 | ~12 | ~12, about half on | ~1,050 | ~500 |
| Ceiling fans | 13 | ~75 | ~60 at normal speed | ~975 | ~750 |
| **Total** | | | | **~22,400** | **~12,650** |

Notes:
- The KES‑1866S is a T3 full‑DC inverter AC, with EER 4.0 and a 120–270 V operating range. It keeps running through deep
  voltage sags on its own, but it draws more current as the voltage drops.
- Wattages are estimates carried over from the office figures (1.5 ton: 1800 W peak, ~1000 W once at temperature).
  Check the rating plates for exact input power.
- Lights assume 6–8 LED lights *per room* across ~11 rooms (one per AC). If it is 6–8 in total, lights drop to ~100 W, which barely changes the totals.
- Fans: 13 × ~75 W standard AC ceiling fans. Energy‑saver (inverter/DC) fans use ~30–40 W each and would halve this.
- Not yet listed: fridge(s), water pump / motor, geyser, kitchen appliances, etc.

## What the numbers imply (before answers)

| Scenario | Avg load | 4 h energy | Battery (nominal) | Inverter |
|---|---:|---:|---:|---|
| Everything on | ~12.7 kW | ~51 kWh | ~61 kWh | ~25 kW (three‑phase) |
| Night backup: 3 bedrooms (3 × 1.5 ton) + fridge, all fans, some lights | ~4.2 kW | ~17 kWh | ~20–21 kWh | 8–12 kW |
| No ACs: all 13 fans + lights + fridge | ~1.5 kW | ~6 kWh | ~7–8 kWh | 5 kW |

## Open questions

1. Number of 2 ton floor‑standing ACs, and their model.
2. Which ACs must run during an outage, and for how many hours per day?
3. Supply: single‑ or three‑phase, and sanctioned load.
4. Roof available for solar? At home it is usually worth it (see net billing notes in [countries/pakistan.md](countries/pakistan.md)).
5. Other loads: water pump/motor, fridge(s), geyser.
6. Are the 6–8 LED lights per room, or in total? And how many rooms?
