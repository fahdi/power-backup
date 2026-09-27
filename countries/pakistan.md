# Pakistan: country-specific advice

Researched September 2026. Read this alongside the [main recommendation](../README.md): the load analysis, sizing and inverter choice there apply unchanged; this page covers what is different when buying and installing in Pakistan.

## Authorised distributors and warranty

**Buy Deye only through the official channel.** Deye's authorised Pakistan distribution goes through
**Inverex**, whose **Nitrox** hybrid range is Deye‑made. Deye has been reported to region‑lock
grey‑import units sold outside its approved channels, and grey units carry no local warranty.
In practice, "Deye in Pakistan" means an **Inverex Nitrox** or a Deye unit from an authorised Inverex dealer,
with a written warranty (typically 5 years). Before buying, confirm with the dealer which Deye
model it is and whether the 12 kW is single‑phase (Deye SUN‑12K‑SG02LP1) or three‑phase.
The Nitrox 12 kW listings found were mostly three‑phase.

**Victron** is sold in Pakistan mainly by importers and online retailers. No clear official
distributor turned up, so after‑sales support depends on the installer. Budget roughly
international price (~US$ 1,450 per MultiPlus‑II 48/5000) plus import duty and margin.

## Local prices

**Batteries:** Pylontech US5000 (4.8 kWh) is about **Rs 255,000–275,000** each, roughly Rs 40–45k per kWh.
- 5 units (24 kWh) ≈ **Rs 1.3–1.4 million**.
- The battery is the biggest cost item, which is why upsizing the inverter to 12 kW is comparatively cheap.

## Grid rules

**Net billing changed the maths.** Since 9 Feb 2026, NEPRA moved new solar users from net metering
to **net billing**. The buyback rate for new users is about **Rs 8–11/unit**, versus ~Rs 25 previously, and far below the import tariff.
Exported solar is now worth little, so **storing solar in the battery and using it yourself
is the better deal**. This favours the battery‑heavy design here, and solar remains optional as you wanted.
Existing net‑metering agreements keep their old rate until they expire.

## Climate and installation

**Local conditions:**
- **Heat (45–50 °C summers):** inverters derate, which is another argument for 12 kW. Install in shade with airflow. LiFePO4 batteries prefer below 35 °C, so keep them indoors.
- **Dust:** Deye/Inverex are IP65 (fine for a semi‑outdoor wall). Victron MultiPlus‑II is IP21 and needs a clean indoor room.
- **Voltage sags (160–180 V on summer evenings):** set the inverter's grid low‑voltage cut‑off to ~190 V so the ACs run from the battery rather than the weak grid.
- **Your connection:** check whether it is single‑ or three‑phase, and its sanctioned load. Set the inverter's grid input current limit so charging plus house load doesn't trip the main breaker.

## Final recommendation (what to buy)

Based on the stated load: 6.2 kW peak, ~4 kW managed, 4 h backup per day, quality first, open API.

**Buy the Victron system:**

| # | Item | Qty | Why |
|---|---|---:|---|
| 1 | Victron MultiPlus‑II 48/5000/70‑50 230V | 3 (parallel) | ~12 kW total (~11 kW at 40 °C) runs everything at once; 210 A (~10 kW) mains charging |
| 2 | Victron Cerbo GX (+ GX Touch 50 screen, optional) | 1 | Open‑source Venus OS: MQTT, Modbus‑TCP, Node‑RED, Home Assistant, VRM |
| 3 | Pylontech US5000 (4.8 kWh) | 5 | 24 kWh ≈ 21 kWh delivered: 4 h at 5 kW unmanaged, ~5 h at 4 kW |
| 4 | Victron Lynx Distributor + class‑T/MEGA fuses, 95 mm² DC cables | 1 set | Safe 250 A DC path |
| 5 | 2‑pole contactor on the 2 ton AC circuit, driven by Cerbo relay 1 | 1 | Automatic load shedding |
| 6 | Raspberry Pi 5 / mini PC running Home Assistant | 1 | Automation ("AI") layer |
| 7 | Solar: later, a SmartSolar MPPT RS 450/200 | optional | Separate unit, so solar can be switched off or left out |

**Rough budget (own estimate — get quotes):**
- 3 × MultiPlus‑II: Rs 1.4–1.8M
- Cerbo GX: ~Rs 150k
- 5 × US5000: ~Rs 1.3M
- DC gear, breakers and installation: Rs 250–400k
- **Total: ~Rs 3.1–3.7M** without solar.

**Settings:**
- ESS mode "Keep batteries charged", because outages are the main use.
- AC input current limit matched to your sanctioned load / main breaker.
- The MultiPlus‑II disconnects from mains below ~187 V by itself, so sagging mains is handled.
- Node‑RED rule: grid lost AND SOC < 40 % → open the 2 ton AC contactor; grid back → close it.
- Home Assistant: pre‑charge to 100 % before scheduled load‑shedding; alerts; history.

**Conditions for choosing Victron:**
- A Victron‑experienced installer is within reach. Three units in parallel must be configured with VEConfigure.
- There is a clean, ventilated indoor room. The inverters are IP21 and not dust‑proof.

**If either condition fails, buy this instead:** a Deye single‑phase 12 kW (SUN‑12K‑SG02LP1) from an
authorised Inverex dealer, with the same 5 × Pylontech US5000. Set up load shedding on the Smart Load port,
and use Home Assistant via RS485 Modbus.

Sources: [Profit / Pakistan Today – net billing](https://profit.pakistantoday.com.pk/2026/02/10/pakistans-power-regulator-ends-net-metering-for-solar-consumers-shifts-to-net-billing-model/),
[Solar Citizen – NEPRA 2026 rules](https://www.solarcitizen.com.pk/nepra-prosumer-regulations-2026/),
[BatteryMax – Pylontech US5000](https://www.batterymax.pk/pylontech-us5000-48v-100ah-4-8kwh-lithium-iron-phosphate-lifepo4-lfp-ups-and-solar-lithium-battery.html),
[DIY Solar Forum – Deye region lock](https://diysolarforum.com/threads/new-deye-inverters-blocked-for-eu-usa-pakistan-alternatives-new-solis-growatt.95341/),
[Inverex Global – Nitrox (Deye) 12 kW](https://inverexglobal.com/product/inverex-global-nitrox-hybrid-deye-mppt-inverter-12kw/),
[Deye SUN‑12K‑SG02LP1 (single phase)](https://www.wattuneed.com/en/hybrid-inverters/27065-deye-single-phase-hybrid-inverter-12-kw-48v-sun-12k-sg02lp1-eu-8436531216917.html).
Prices change often — get 2–3 written quotes.
