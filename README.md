# Home Power Backup: Inverter & Battery Recommendation

Goal: a hybrid system that runs from **mains and solar (solar optional / can be switched off)**,
gives **4 hours of backup per day**, and has an **open, local API** so it can be automated
(Home Assistant / AI‑driven energy management). Priority: **quality first, price second**.

---

## 1. Load analysis

| Load | Rated (W) | Realistic running (W) | Notes |
|---|---:|---:|---|
| 1.5 ton inverter AC (Kenwood) | 1800 | ~1000 | Drops to ~1000 W once room temp is reached |
| 2 ton inverter AC | 2400 | ~1300–1400 | Same inverter‑compressor behaviour |
| Desktop PC | 1500 | 300–600 | 1500 W is usually the PSU rating, not the actual draw |
| Lights + fans | 500 | 300–500 | |
| **Total** | **6200** | **~3000–3500** | |

Key points:

- **Peak (everything at full power): 6.2 kW.** The inverter must be able to carry this, with
  headroom for heat derating (inverters are rated at 25 °C; at 40 °C+ they lose 10–20 %).
- **Inverter ACs have soft‑start**, so there is no large motor surge — good for battery inverters.
- **Low mains voltage** only matters while on grid. When the voltage sags, the ACs pull more
  current for the same power. A hybrid inverter will switch to battery below a set threshold
  (e.g. 185–190 V). On battery the output is a clean regulated 230 V, so the sag no longer matters —
  but it *does* mean you use battery more often, which is why the battery must not be undersized.

## 2. Battery sizing

Losses to account for: inverter efficiency (~92 %) and usable depth of discharge (~90 % for LiFePO4).

| Scenario | Avg load | Energy at AC (4 h) | Battery **nominal** needed |
|---|---:|---:|---:|
| A. No load management | 5.0 kW | 20 kWh | **~24 kWh** |
| B. Managed to 4 kW (shed/limit one AC) | 4.0 kW | 16 kWh | **~19–20 kWh** |
| C. Realistic after ACs settle | ~3.2 kW | ~13 kWh | ~15–16 kWh |

**Recommendation: ~20 kWh nominal LiFePO4 at 48 V, with automatic load management (scenario B),
in a modular battery that can be expanded to 25 kWh later.** Your 16 kWh figure is the *usable*
energy; the battery you buy has to be ~20 kWh nominal to deliver that.

Recharge speed also matters: if power returns for only a few hours between outages, the system
must refill 16–20 kWh quickly from mains. Aim for **≥150 A (~7–8 kW) of charging**.

(`sizing.py` in this repo lets you re-run these numbers with your own loads.)

## 3. Inverter size

**8 kW class, 48 V, single‑phase hybrid** (grid + solar + battery). This carries the 6.2 kW
peak with headroom in a hot room, while load management keeps battery draw at ~4 kW during outages.
A 5 kW inverter would be at its limit and would derate in summer.

## 4. Recommended systems

### Option 1 — Best quality & most open (recommended given "quality first"): **Victron**

| Part | Model | Why |
|---|---|---|
| Inverter/charger | **2 × MultiPlus‑II 48/5000/70‑50** in parallel (~8 kW continuous, 140 A charging) — or 1 × Quattro 48/10000 | Industrial‑grade, low‑frequency transformer design, excellent with motor/AC loads, 50 A transfer relay, PowerAssist |
| Solar charger | SmartSolar MPPT RS 450/200 (or 2 × MPPT 250/100) | Solar is a separate unit — switch it off with a DC isolator and the system keeps running on mains + battery |
| Controller | **Cerbo GX** running **Venus OS** | Venus OS is **open source**; exposes **MQTT, Modbus‑TCP, Node‑RED**, full local control |
| Battery | 5 × Pylontech US5000 (24 kWh) or BYD Battery‑Box Premium LVS 20/24 | Tier‑1 LiFePO4, CAN‑bus communication with Victron |

**API / AI:** Venus OS is open source (github.com/victronenergy/venus); local MQTT + Modbus‑TCP;
Home Assistant integration; Node‑RED runs on the Cerbo itself. VRM's **Dynamic ESS** does
forecast‑based (weather + consumption) charge/discharge scheduling.

**Load management:** Cerbo GX relay → contactor on the 2 ton AC circuit. Node‑RED rule:
"grid lost AND SOC < 60 % → shed 2 ton AC" (or also when battery power > 4 kW).

### Option 2 — Best quality per rupee: **Deye (also sold as Sunsynk)**

| Part | Model | Why |
|---|---|---|
| Hybrid inverter | **Deye SUN‑8K‑SG05LP1** (8 kW, 48 V, single phase) | Built‑in 2 MPPT solar, **190 A battery charging** (fast refill), UPS‑grade switchover, very common locally = easy service |
| Battery | 4 × Deye SE‑G5.1 Pro‑B (20.5 kWh) or 4–5 × Pylontech US5000 | Native CAN/RS485 comms with the inverter |

**API / AI:** RS485 / Modbus‑RTU, documented register map; open‑source Home Assistant
integrations (**ha‑solarman** local via the Wi‑Fi logger, or an ESPHome RS485 adapter).
Works with open‑source optimisers **EMHASS** and **Predbat**.

**Load management:** built‑in **Smart Load (GEN port)** — wire the 2 ton AC to it and set it to
switch off when grid is lost or SOC drops below a threshold. No extra hardware needed.

Solar is optional: the Deye runs fine as grid + battery only; add a DC isolator to switch PV off.

### Avoid for this job

Low‑cost high‑frequency "Axpert / Voltronic" clones: they work, but reliability with two ACs
running for hours in summer heat is noticeably worse, parallel setups are finicky, and fan/
capacitor failures are common. Not a match for "quality first".

## 5. Comparison

| | Victron (Opt. 1) | Deye (Opt. 2) |
|---|---|---|
| Build quality / longevity | ★★★★★ | ★★★★ |
| Open API | ★★★★★ (open‑source OS, MQTT, Modbus‑TCP) | ★★★★ (Modbus RS485, community integrations) |
| Built‑in load shedding | Via GX relay + Node‑RED | Native Smart Load port |
| Mains recharge speed | 140 A (2 units) | 190 A |
| Local service availability | Fewer dealers | Very widely available |
| Indicative total cost (inverter + ~20–24 kWh battery, no panels)* | ~US$ 8,000–10,000 | ~US$ 5,000–6,500 |

\*Rough 2026 ballpark only — get local quotes; prices vary a lot by market and import duties.

## 6. "AI" / automation layer (open source)

Run **Home Assistant** on a small PC/Raspberry Pi connected to the inverter and add:

1. **EMHASS** or **Predbat** — open-source optimisers that forecast consumption and solar and plan
   when to charge the battery from grid/solar.
2. **Outage‑schedule automation** — if outages follow a schedule, force the battery to 100 % before
   each scheduled outage.
3. **Load‑shedding rules** — during outage: keep the 1.5 ton AC, PC and lights; shed the 2 ton AC
   (or raise its setpoint via an IR blaster such as Broadlink) when battery power > 4 kW or SOC is low.
4. **Low‑voltage protection** — set the grid low‑voltage cut‑off to ~190 V so the ACs run from
   the battery during deep sags instead of the weak grid.

## 7. Bottom line

- **Quality first:** Victron 2 × MultiPlus‑II 48/5000 + Cerbo GX + MPPT + ~24 kWh Pylontech/BYD.
- **Best value while still good quality:** Deye SUN‑8K‑SG05LP1 + ~20 kWh Deye/Pylontech battery.
- Either way: **8 kW inverter, ~20 kWh LiFePO4 at 48 V, automatic load management to ~4 kW**,
  expandable to 25 kWh if you want to run everything unmanaged.

Installation checklist: proper DC breakers/fuses between battery and inverter, separate AC breakers
for each AC, a PV DC isolator, correct cable sizing (48 V at 8 kW ≈ 170 A DC → 50–70 mm² cable),
earthing, and installation in a ventilated, shaded spot.
