# Home: usage and requirements

A second site, separate from the office in [usage.md](usage.md). The system design is in [home-plan.md](home-plan.md).

## Site

- **7 marla house in a private housing society, Islamabad/Rawalpindi area.** Plot is about 30 × 55 ft (1,650 sq ft).
- Double storey; solar goes on the first‑floor roof.
- **Three‑phase** supply. Electricity is distributed by the society (bought from IESCO).

## Loads

| Load | Qty | Rated each (W) | Realistic running each (W) | Rated total (W) | Running total (W) |
|---|---:|---:|---:|---:|---:|
| Kenwood eSmart Onyx 1.5 ton (KES‑1866S) | 8 | ~1800 | ~1000 | 14,400 | 8,000 |
| Kenwood 1 ton inverter | 1 | ~1200 | ~700 | 1,200 | 700 |
| Kenwood 2 ton floor‑standing inverter (bought, not yet installed) | 2 | ~2400 | ~1350 | 4,800 | 2,700 |
| LED lights (6–8 per room, ~11 rooms) | ~88 | ~12 | ~12, about half on | ~1,050 | ~500 |
| Ceiling fans | 13 | ~75 | ~60 | ~975 | ~750 |
| Exhaust fans | 5 | ~40 | ~30 | 200 | 150 |
| Water pump (assumed 1 HP) | 1 | ~750 (starting surge ~3×) | ~250 avg (runs in bursts) | 750 | 250 |
| Electric cooktops (assumed 2 × 2 kW induction) | 2 | ~2000 | ~1000 while cooking | 4,000 | 0 / ~2,000 when cooking |
| Philips air fryer | 1 | ~2000 (models 1400–2200 W) | ~1200 while cooking | 2,000 | 0 / ~1,200 when cooking |
| **Total** | | | | **~29,400** | **~13,000**, or **~16,500 while cooking** |

Notes:
- The KES‑1866S is a T3 full‑DC inverter AC with EER 4.0 and a 120–270 V operating range. AC wattages are estimates;
  check the rating plates for exact input power.
- Lights assume 6–8 LED lights per room. If it is 6–8 in total, lights drop to ~100 W.
- Fans: 13 × ~75 W standard ceiling fans. Energy‑saver (DC) fans use ~30–40 W each.

## Requirements

- **Outages:** run **all loads for 2 hours at a time**.
- **Priority:** you define which loads turn off first when the battery or inverter limit is reached.
- **Daytime:** run all loads **on solar** during the day.
- **Priorities:** quality first, price second; open, local API for automation.

## Still to confirm

- Exact bylaw setbacks for the plot (from the society's building control office), and whether an **elevated solar structure** is allowed.
- Sanctioned load (kW) on the three‑phase connection.
- Cooktop count and wattage, pump HP, air fryer model.
- Whether the Kenwood ACs' Wi‑Fi app can be controlled locally (otherwise an IR blaster per room is used).
