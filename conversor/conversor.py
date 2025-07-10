units = {
    'mass' : ['miligram', 'gram', 'kilogram'],
    'distance' : ['milimeter', 'meter', 'kilometer'],
    'temperature' : ['celsius', 'kelvin', 'fahrehnheit']
}

conversion_mass = {
    'miligram' : 0.001,
    'gram' : 1,
    'kilogram' : 1000.0
}    
    
conversion_distance = {
    'milimeter' : 0.001,
    'meter' : 1,
    'kilometer' : 1000.0
}
    
conversion_to_celsius = {
    'celsius' : lambda x : x,
    'kelvin' : lambda x : x - 273.15,
    'fahrehnheit' : lambda x : (x - 32) * 5/9
}
    
conversion_from_celsius = {
    'celsius' : lambda x : x,
    'kelvin' : lambda x : x + 273.15,
    'fahrehnheit' : lambda x : (x * 9/5) + 32
}
    

def select_unit():
    
    unit = input("").lower()
    
    while unit != "mass" and unit != "distance" and unit != "temperature":
        print("Please, select a valid unit: ")
        unit = input("").lower()
    return unit    


def select_cant():                                                                        
    while True:
        user_num = input("")
        try:
            user_num = float(user_num)
        except ValueError:
            print("|ERROR| select a valid quantity")
        else:
            break
    return user_num;


def check_unit(unit):
    valid_units = units[unit]
    error = f"Error, select a valid option ({".".join(valid_units)}):"
    user_input_unit = input("").lower()
    
    while user_input_unit not in valid_units:
        print(error)
        user_input_unit = input("").lower()

    return user_input_unit


def convert_mass(quantity, mass, new_mass):
    
    #mass unit to gram
    amount_in_base_unit = quantity * conversion_mass[mass]
    #gram to new mass unit
    #example: if new_mass is 'kilogram', the factor from 'kilogram' to 'gram' is 1000
    #to go from 'gram' to 'kilogram', we divide by 1000, which is multiplying by 1/1000 
    gram_to = 1 / conversion_mass[new_mass]
    quant_converted = amount_in_base_unit * gram_to
    
    return quant_converted, new_mass


def convert_distance(quantity, distance, new_distance):
    
    #the same process here
    amount_in_base_unit = quantity * conversion_distance[distance]
    meter_to = 1 / conversion_distance[new_distance]
    quant_converted = amount_in_base_unit * meter_to
    
    return quant_converted, new_distance

def convert_temp(quantity, temp, new_temp):
    
    #convert de temp a celsius and we apply it to the quantity
    amount_in_celsius = conversion_to_celsius[temp](quantity)
    #convert celsius to new_temp and we apply it to the amount in celsius
    quant_converted = conversion_from_celsius[new_temp](amount_in_celsius)
    
    return quant_converted, new_temp


convert_options = {
    'mass' : convert_mass,
    'distance' : convert_distance,
    'temperature' : convert_temp
}

        
def convert_to (unit):
    
    options = ",".join(units[unit])
    print(f"What unit do you want to convert ({options})?")
    convert = check_unit(unit)
    print("How much?")
    quant = select_cant()
    print("Convert to: ")
    new_unit = check_unit(unit)
    
    conversion_funcs = convert_options[unit]
    final_convert, final_unit = conversion_funcs(quant, convert, new_unit)

        
    print(f"{quant} {convert} is equal to {final_convert} {final_unit}")    
                        
                    
def menu():
    print("-"*35)
    print("Unit converter")
    print("-"*35)
    print("Please enter the unit to convert (Mass/Distance/Temperature)")
    unit = select_unit()
    convert_to(unit)