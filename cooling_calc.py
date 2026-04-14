# Simple cooling load estimation (very basic)

def cooling_load(power_kw):
    # 1 kW IT load ≈ 3412 BTU/h
    return power_kw * 3412

if __name__ == "__main__":
    it_load = float(input("Enter IT load (kW): "))
    print(f"Estimated cooling load: {cooling_load(it_load)} BTU/h")
