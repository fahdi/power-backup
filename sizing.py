#!/usr/bin/env python3
"""Battery/inverter sizing calculator for the home backup system.

Edit LOADS or the constants below and run: python3 sizing.py
"""

# name: (rated watts, realistic running watts)
LOADS = {
    "1.5 ton AC": (1800, 1000),
    "2 ton AC": (2400, 1350),
    "Desktop PC": (1500, 450),
    "Lights + fans": (500, 400),
}

BACKUP_HOURS = 4
INVERTER_EFFICIENCY = 0.92
DEPTH_OF_DISCHARGE = 0.90
HEAT_DERATING = 0.85  # inverter output at ~40 C vs rated at 25 C


def battery_nominal_kwh(avg_load_kw: float) -> float:
    return avg_load_kw * BACKUP_HOURS / INVERTER_EFFICIENCY / DEPTH_OF_DISCHARGE


def main() -> None:
    peak_kw = sum(rated for rated, _ in LOADS.values()) / 1000
    realistic_kw = sum(running for _, running in LOADS.values()) / 1000

    print(f"Peak load:        {peak_kw:.1f} kW")
    print(f"Realistic load:   {realistic_kw:.1f} kW")
    print(f"Min inverter:     {peak_kw / HEAT_DERATING:.1f} kW rated (peak incl. heat derating)")
    print()
    print(f"Battery for {BACKUP_HOURS} h backup (nominal LiFePO4 capacity):")
    for label, kw in [
        ("A. Unmanaged, 5 kW avg", 5.0),
        ("B. Managed to 4 kW", 4.0),
        (f"C. Realistic {realistic_kw:.1f} kW", realistic_kw),
    ]:
        print(f"  {label:<28} {kw * BACKUP_HOURS:5.1f} kWh at AC -> {battery_nominal_kwh(kw):5.1f} kWh nominal")


if __name__ == "__main__":
    main()
