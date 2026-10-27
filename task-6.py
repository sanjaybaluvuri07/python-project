
n = int(input("Enter number of vehicles: "))
distance = float(input("Enter journey distance in km: "))
reserve = float(input("Enter reserve fuel percentage: "))

lowest_cost = float("inf")
best_vehicle = ""

if n <= 0 or distance <= 0 or reserve < 0:
    print("Invalid input!")
else:
    for i in range(n):
        print("\nVehicle", i + 1)

        name = input("Enter vehicle name: ")
        mileage = float(input("Enter mileage (km/litre): "))
        fuel_price = float(input("Enter fuel price per litre: "))
        available_fuel = float(input("Enter available fuel in litres: "))

        if mileage <= 0 or fuel_price <= 0 or available_fuel < 0:
            print("Invalid vehicle details!")
            continue

        # Calculate fuel requirement
        fuel = distance / mileage
        reserve_fuel = fuel * reserve / 100
        total_fuel = fuel + reserve_fuel
        cost = total_fuel * fuel_price

        print("Fuel required:", round(fuel, 2), "litres")
        print("Reserve fuel:", round(reserve_fuel, 2), "litres")
        print("Total fuel needed:", round(total_fuel, 2), "litres")
        print("Journey cost: Rs.", round(cost, 2))

        # Check feasibility
        if available_fuel >= total_fuel:
            print("Status: Feasible")

            if cost < lowest_cost:
                lowest_cost = cost
                best_vehicle = name
        else:
            print("Status: Not feasible")

    print("\n--- JOURNEY COMPARISON ---")

    if best_vehicle != "":
        print("Lowest-cost vehicle:", best_vehicle)
        print("Minimum journey cost: Rs.", round(lowest_cost, 2))
    else:
        print("No feasible vehicle found.")
