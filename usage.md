# My usage and requirements

The single source of truth for this household's loads and goals. Everything else in this repo
(`README.md`, `countries/pakistan.md`, `sizing.py`) is sized from this page. Update it here first when something changes.

## Location

Pakistan. Mains voltage regularly sags (160–180 V on summer evenings), and there are daily outages / load‑shedding.
Summer peaks are 45–50 °C.

## Loads

| Load | Rated (W) | Realistic running (W) | Notes |
|---|---:|---:|---|
| 1.5 ton inverter AC (Kenwood) | 1800 | ~1000 | Drops from 1800 to ~1000 W once room temperature is reached |
| 2 ton inverter AC | 2400 | ~1350 | Same inverter‑compressor behaviour |
| Desktop PC | 1500 | ~450 | 1500 W is the PSU rating; actual draw is usually 300–600 W |
| Lights + fans | 500 | ~400 | |
| Gree water dispenser (hot + cold, e.g. GW‑JL500FS/FC) | ~700 | ~150 avg | 580 W heater + 110 W compressor cooler, both cycle on and off (JL500F: 550 + 100 W; JL400FS: 420 + 100 W) |
| **Total** | **~6900** | **~3350** | |

## Requirements

- **Backup:** 4 hours per day.
- **Sources:** mains + solar, where solar is optional and can be switched off or added later.
- **Everything running during a mains voltage drop:** ~5 kW average → ~20 kWh delivered → ~24 kWh battery.
- **With load management during outages (~4 kW):** 16 kWh delivered → ~20 kWh battery.
- **Headroom:** 12 kW inverter class, so future loads aren't limited.
- **Open, local API:** for Home Assistant / AI‑driven automation.
- **Priorities:** quality first, price second.

## Chosen system

See [countries/pakistan.md → Final recommendation](countries/pakistan.md#final-recommendation-what-to-buy):
3 × Victron MultiPlus‑II 48/5000 + Cerbo GX + 5 × Pylontech US5000 (24 kWh). The water dispenser
fits within this with no change: ~21 kWh usable covers ~4 h at 5 kW, or ~6 h at the realistic ~3.35 kW.

## Still to confirm

- Supply type (single / three phase) and sanctioned load (kW) from the electricity bill.
- Monthly units (kWh) from recent bills, needed later for sizing solar.
- The exact Gree dispenser model. ~700 W assumes the JL500FS/FC, the highest of the common models.
- Actual PC draw (a plug‑in watt meter will tell you).
