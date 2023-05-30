# I added value error exception handler to prevent the program from crashing in case of an invalid input.

def celcius_to_fahrenheit(temp_in_celcius):
    return temp_in_celcius * (9/5) + 32

def wind_chill_calculator(temp_in_fahrenheit, wind_speed):
    return 35.74 + (0.6215 * temp_in_fahrenheit) - (35.75 * (wind_speed**0.16)) + ((0.4275 * temp_in_fahrenheit) * (wind_speed**0.16))

print()
print("Welcome to wind chill forecast ☁️")

lines = "--------------------------------------------------------------------------"

print(lines)

try:
    temp = float(input("What is the temperature? "))
    print()
    
    while True:
        temp_unit = input("Fahrenheit or Celsius (F/C)? ")
        print()
        if temp_unit.upper() in ("F", "C"):
            break
        else:
            print("❌ Error: Please provide temperature unit in either 'C' for Celcius or 'F' for Fahrenheit")
            print()

    if temp_unit.upper() == "C":
        temp = celcius_to_fahrenheit(temp)
    

    formatted_temp = "{:.1f}".format(temp)

    for i in range(5, 65, 5):
        wind_chill = wind_chill_calculator(temp, i)
        wind_chill = "{:.2f}".format(wind_chill)
        print(f"At temperature {formatted_temp}F, and wind speed {i} mph, the windchill is: {wind_chill}F")
except ValueError:
    print("❌ Error: Temperature value should be a number" )
    
print(lines)