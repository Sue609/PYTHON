weight = input("Weight: ")
measurement = input("(L)bs or (K)g: ")
weight_l = int(weight) * 0.45
weight_k = int(weight) / 0.45

if measurement.upper() == "L":
    print(f"You are {weight_l} kilos")
    
else:
    print(f"You are {weight_k} pounds")