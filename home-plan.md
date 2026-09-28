# Home: backup and solar plan

For the loads in [home-usage.md](home-usage.md): **~29 kW rated, ~13 kW typical (~16.5 kW while cooking), three‑phase**,
at a 7 marla house in a private housing society in the Islamabad/Rawalpindi area. Researched September 2026; prices are indicative, so get quotes.

## 1. Roof space (bylaws)

The society's official building bylaws could not be opened from here. The numbers below use the
plot size and typical setbacks. **Confirm them with the society's building control office before finalising.**

| Item | Value | Basis |
|---|---:|---|
| Plot | 30 × 55 ft = 1,650 sq ft | Typical 7 marla plot |
| Setbacks (assumed) | front ~10 ft, rear ~5 ft, sides 0 | Typical for this plot size (to confirm) |
| First‑floor roof | ~30 × 40 ft ≈ 1,200 sq ft | Double storey, same footprint as ground |
| Minus mumty (~120 sq ft), water tank (~40), 1.5 ft edge walkway | ≈ 850 sq ft usable | |

Panels: modern 585–620 W N‑type bifacial, about 2.3 × 1.13 m (~28–29 sq ft each).

| Mounting | Panels | Capacity | Status |
|---|---:|---:|---|
| **A. Low tilted rows on the roof slab** (10–15° tilt, spaced to avoid self‑shading) | 16–20 | **~10–12 kWp** | Normally allowed; still needs a society‑registered installer |
| **B. Elevated structure over the whole roof** (panels above mumty and tank) | 30–34 | **~18–20 kWp** | Only if the society approves. Some societies ban rooftop structures, so check first |

The Islamabad/Rawalpindi area gets about 4.5–5.5 peak sun hours a day. In summer heat, panels deliver ~75 % of their rating at noon.

| | Option A (~11 kWp) | Option B (~19 kWp) |
|---|---:|---:|
| Noon output in summer | ~8 kW | ~14 kW |
| Daily energy | ~45–55 kWh | ~80–95 kWh |
| Runs **all** daytime load (~13 kW) on solar? | **No.** Covers ~7–8 ACs; the rest comes from grid or battery | **Yes, at midday.** Morning and evening top‑up from grid |

**Conclusion:** "all load on panels during the day" is only realistic with the **elevated structure (option B)**.
With low rows (option A), solar carries about 60 % of the daytime load, and the hybrid inverter automatically takes the rest from the grid.

## 2. Battery

All loads for 2 hours: ~13–16.5 kW × 2 h ≈ 26–33 kWh at the sockets. After inverter losses (92 %) and 90 % depth of discharge,
that is **~32–40 kWh nominal**.

**Choice: 8 × Pylontech US5000 = 38.4 kWh** (~36 kWh usable).
- That runs everything for ~2 h, including cooking, and ~2.5 h when not cooking.
- Price: ~Rs 255–275k each → **~Rs 2.05–2.2M**.
- 8 × 100 A continuous comfortably covers the ~500 A the two inverters can draw.

Refill between outages comes from solar in the day, or from the grid at up to ~12 kW (limited by the sanctioned load).

## 3. Inverter

**2 × Inverex Nitrox 12 kW three‑phase 48 V (Deye SUN‑12K‑SG04LP3), in parallel = 24 kW.**
- Deye‑made and sold through Inverex, so the warranty works in Pakistan.
- IP65, so it can be wall‑mounted outdoors in shade.
- Each unit handles 100 % unbalanced load, **up to 50 % of rating per phase**. Two units give **~12 kW per phase**.
- 240 A battery charging per unit.
- Each unit has 2 solar inputs, so there's room for the full option B array.
- Up to 10 units can be paralleled, so a third can be added later.
- Open API: RS485 / Modbus → Home Assistant (e.g. the open‑source ha‑solarman integration).
- Price: **~Rs 550–745k each** (listings, June–Sept 2026).

**Strong alternative: 2 × Solis S6‑EH3P15K02‑NV‑YD‑L (three‑phase, 48 V, 15 kW each) = ~30 kW.**
- Backup port rated at the full 15 kW, with 2× surge for 10 s and <10 ms switchover.
- Up to 290 A battery charge/discharge per unit; supports unbalanced three‑phase loads.
- About **Rs 625k each** in Pakistan.
- API: documented Modbus RS485, with open‑source Home Assistant integrations (solis_modbus, solax_modbus) and Predbat support.
- Use your own RS485‑to‑Ethernet/MQTT bridge. Solis Wi‑Fi dataloggers have stopped serving local Modbus after firmware updates.
- Confirm with the dealer: the maximum number of parallel units, and the per‑phase output limit (about 22.8 A ≈ 5.2 kW per phase per unit).

The ~29 kW all‑on rating exceeds 24 kW on paper. In practice, all ACs don't run their compressors flat‑out together,
and the priority controller below keeps the total under ~22 kW.

**Phase balancing** (the installer should plan this; each phase ≤ ~10 kW rated):

| Phase | Loads | Rated |
|---|---|---:|
| L1 | 2 ton standing AC + 3 × 1.5 ton | ~7.8 kW |
| L2 | 2 ton standing AC + 3 × 1.5 ton | ~7.8 kW |
| L3 | 2 × 1.5 ton + 1 ton + kitchen (cooktops, air fryer) + pump | ~10–11 kW, with cooking shedding an AC (below) |

Lights, fans and exhaust fans are spread across all three phases.

## 4. Priority load shedding ("which turns off first")

The inverter's built‑in Smart Load port only gives one or two steps. For a full, user‑defined order, use **Home Assistant**:
- It reads live battery SOC and per‑phase load from the inverters over Modbus.
- It switches ACs **off via an IR blaster in each AC room**, e.g. a Broadlink RM4 mini, controlled locally. This needs no rewiring.
  If the Kenwood Wi‑Fi app turns out to be Tuya‑ or Gree‑based, that works too.
- It switches the pump through a smart relay and contactor, e.g. Shelly Pro with a local API.

**Default order.** Change it any time in Home Assistant:

| Order | Load | Turns off when (grid is down) |
|---:|---|---|
| 1 | Water pump | Immediately; runs only on grid or solar surplus |
| 2 | 2 ton standing AC #1 (drawing room) | SOC < 70 % or total load > 20 kW |
| 3 | 2 ton standing AC #2 (lounge) | SOC < 60 % or any phase > 11 kW |
| 4 | 1.5 ton ACs in non‑bedrooms (one by one) | SOC < 50 % |
| 5 | 1 ton AC | SOC < 40 % |
| 6 | Bedroom 1.5 ton ACs (one by one) | SOC < 30 % |
| never | Lights, fans, exhaust fans, fridge, router/PC, cooktops, air fryer | Keep on. When cooking starts, the next AC in the list is paused instead |

Restore when grid or solar returns: one load every ~2 minutes, in reverse order, to avoid a current surge.
Inverter ACs also have their own restart delay.

## 5. Housing‑society specific

- **Registered installer only:** the society allows solar work only by installers registered with it. The system must stay
  within the capacity approved in its **feasibility report**, and Tier‑1 equipment is required.
- **Don't count on export income.** Societies that distribute their own power have disputed net‑metering credits
  (e.g. announced deductions on exported units, contested at NEPRA). With new‑user buyback now only ~Rs 8–11/unit, **set the inverters to self‑consumption / zero export**
  and use the battery instead of exporting.
- **Confirm the sanctioned load** of the three‑phase connection. Set the inverters' grid charge limit so charging plus house load stays under it.

## 6. Shopping list and budget

| Item | Qty | Indicative price |
|---|---:|---:|
| Inverex Nitrox 12 kW 3‑phase 48 V | 2 | Rs 1.1–1.5M |
| Pylontech US5000 (4.8 kWh) + rack | 8 | Rs 2.05–2.2M |
| N‑type 585–620 W panels (option A ~11 kWp; option B ~19 kWp) | 18 / 32 | Rs 0.42–0.47M / Rs 0.72–0.8M (at Rs 37–42 per watt) |
| Mounting (low rows / elevated), DC & AC cabling, protection, earthing | 1 | Rs 0.3–0.5M / Rs 0.6–0.9M (own estimate) |
| Home Assistant box + 11 IR blasters + pump relay/contactor | 1 | Rs 0.12–0.2M (own estimate) |
| Installation and paralleling / commissioning | 1 | Rs 0.2–0.35M (own estimate) |
| **Total** | | **~Rs 4.2–5.2M (option A)**, **~Rs 4.8–5.9M (option B)** |

## 7. Next steps

1. Ask the society's building control office for the exact setbacks, and whether an **elevated solar structure** is allowed. This decides option A or B.
2. Get the sanctioned load from the electricity bill.
3. Get 2–3 quotes from **society‑registered installers** for this exact list (Nitrox 12K 3P × 2 in parallel, 8 × US5000).
4. Install the two 2 ton standing ACs on their own circuits, placed per the phase plan above.

Sources:
- [Deye SUN‑12K‑SG04LP3 datasheet](https://www.deyeinverter.com/deyeinverter/2024/10/21/datasheet_sun-5-12k-sg04lp3_241021_en.pdf)
- [Inverex Nitrox 12 kW 3‑phase price (W11stop)](https://w11stop.com/inverex-nitrox-12kw-hybrid-solar-inverter)
- [Inverex Nitrox 12 kW 3‑phase (solarpanelprices.pk)](https://solarpanelprices.pk/product/inverex-nitrox-12-kw-48v-3-phase-dual-output-ip-65-hybrid-inverter-price-in-pakistan/)
- [Panel prices Sept 2026](https://pakistansolarmarket.com/)
- [KES‑1866S specs](https://electrociti.pk/kenwood-kes-1866s-esmart-onyx-1-5-ton-inverter-ac-advanced-features-for-optimal-cooling-performance/)
- [Home Assistant Gree integration](https://www.home-assistant.io/integrations/gree/)
- [Home Assistant Tuya integration](https://www.home-assistant.io/integrations/tuya/)
