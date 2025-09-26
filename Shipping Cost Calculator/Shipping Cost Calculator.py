# Shipping Cost Calculator (SoloLearn-friendly)
# Works with simple console input/output. No external libraries used.

def ceil2(x):
    return float(f"{x:.2f}")

def get_positive_float(prompt):
    while True:
        try:
            v = float(input(prompt).strip())
            if v < 0:
                print("Please enter a non-negative number.")
                continue
            return v
        except ValueError:
            print("Invalid number. Try again.")

def choose(prompt, options):
    # options is dict: key -> value
    while True:
        val = input(prompt).strip().lower()
        if val in options:
            return options[val]
        print(f"Choose one of: {', '.join(options.keys())}")

def calc_chargeable_weight(actual_w, use_volumetric):
    if not use_volumetric:
        return actual_w
    L = get_positive_float("Length (cm): ")
    W = get_positive_float("Width  (cm): ")
    H = get_positive_float("Height (cm): ")
    volumetric = (L * W * H) / 5000.0  # common divisor
    print(f"Volumetric weight: {ceil2(volumetric)} kg")
    return max(actual_w, volumetric)

def shipping_rates(zone, method):
    """
    Returns a dict of rate components based on zone & method.
    You can tweak these numbers to match your courier.
    """
    # Base by zone
    if zone == "domestic":
        base = 150.0 if method == "standard" else 250.0
        per_kg = 80.0 if method == "standard" else 120.0
        per_km = 0.0   # often ignored domestically
        fuel_pct = 8.0
    else:  # international
        base = 1200.0 if method == "standard" else 1800.0
        per_kg = 500.0 if method == "standard" else 750.0
        per_km = 0.5   # optional (acts like zone-distance)
        fuel_pct = 12.0
    return {
        "base": base,
        "per_kg": per_kg,
        "per_km": per_km,
        "fuel_pct": fuel_pct
    }

def apply_promo(total, code):
    code = code.strip().upper()
    promos = {
        "SAVE10": (10, 200),   # 10% off, max 200
        "FREESHIP": (100, 150) # 100% off base up to 150 (we'll treat as flat 150 max)
    }
    if code in promos:
        pct, cap = promos[code]
        discount = min(total * (pct/100.0), cap)
        return max(total - discount, 0.0), discount
    return total, 0.0

def main():
    print("=== Shipping Cost Calculator ===")

    # Inputs
    zone = choose("Zone [domestic/international]: ",
                  {"domestic": "domestic", "international": "international"})
    method = choose("Method [standard/express]: ",
                    {"standard": "standard", "express": "express"})
    actual_w = get_positive_float("Actual weight (kg): ")
    use_vol = choose("Use volumetric weight? [y/n]: ", {"y": True, "n": False})
    chargeable_w = calc_chargeable_weight(actual_w, use_vol)
    distance = get_positive_float("Approx distance (km, 0 if unknown): ")

    # Optional add-ons
    insurance = choose("Add insurance? [y/n]: ", {"y": True, "n": False})
    insured_value = 0.0
    if insurance:
        insured_value = get_positive_float("Declared item value for insurance: ")

    cod = choose("Cash on Delivery (COD)? [y/n]: ", {"y": True, "n": False})
    promo = input("Promo code (press Enter to skip): ")

    # Rates
    r = shipping_rates(zone, method)

    # Core cost
    cost = r["base"] + (r["per_kg"] * chargeable_w) + (r["per_km"] * distance)

    # Surcharges
    fuel = cost * (r["fuel_pct"] / 100.0)
    cost += fuel

    # Insurance fee (e.g., 1% of declared value, min 50)
    ins_fee = 0.0
    if insurance and insured_value > 0:
        ins_fee = max(insured_value * 0.01, 50.0)
        cost += ins_fee

    # COD fee (fixed + % of COD amount; assume COD amount equals insured value if provided)
    cod_fee = 0.0
    if cod:
        cod_amount = insured_value if insured_value > 0 else 0.0
        cod_fee = 40.0 + (cod_amount * 0.01)
        cost += cod_fee

    # Taxes (e.g., 5% GST/VAT)
    tax = cost * 0.05
    cost += tax

    # Promo
    final_total, discount = apply_promo(cost, promo)

    # Output
    print("\n--- Cost Breakdown ---")
    print(f"Zone: {zone} | Method: {method}")
    print(f"Chargeable weight: {ceil2(chargeable_w)} kg")
    print(f"Base: {ceil2(r['base'])}")
    print(f"Weight charge: {ceil2(r['per_kg'] * chargeable_w)}")
    if r["per_km"] > 0:
        print(f"Distance charge: {ceil2(r['per_km'] * distance)}")
    print(f"Fuel surcharge ({r['fuel_pct']}%): {ceil2(fuel)}")
    if ins_fee > 0:
        print(f"Insurance fee: {ceil2(ins_fee)}")
    if cod_fee > 0:
        print(f"COD fee: {ceil2(cod_fee)}")
    print(f"Tax (5%): {ceil2(tax)}")
    if discount > 0:
        print(f"Promo discount: -{ceil2(discount)}")
    print(f"\nTOTAL: {ceil2(final_total)}")

if __name__ == "__main__":
    main()
