print("input cargo_weight")

def calculate_fuel(cargo_weight):
    if cargo_weight == "satellite": 
        cargo_weight = 1000
    elif cargo_weight == "rover":
        cargo_weight = 2500
    elif cargo_weight == "supplies":
        cargo_weight = 500
    else:
        cargo_weight="launch"
        print("error")

cargo_weight= base_ship + cargo_weight
    return 

        
