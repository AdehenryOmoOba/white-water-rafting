max_life_expectancy = 0
min_life_expectancy = 1_000_000_000

print()
print("Welcome to data analysis console 📈")

lines = "--------------------------------------------------------------------------"

print(lines)
print()

with open("./week06/life-expectancy.csv") as life_expectancy:
    for line in enumerate(life_expectancy):
        (index, data) = line
        if index > 0:
            current_life_expectancy = float(data.strip().split(',')[3])
            # Get minimum life expectancy
            if current_life_expectancy < min_life_expectancy: 
                min_life_expectancy = current_life_expectancy
            # Get maximum life expectancy
            if current_life_expectancy > max_life_expectancy: 
                max_life_expectancy = current_life_expectancy
print(f"The overall max life expectancy is: {max_life_expectancy}")
print(f"The overall min life expectancy is: {min_life_expectancy}")

print()
print(lines)