year_of_interest_count = 0
year_of_interest_life_expectancy_sum = 0
year_of_interest_max_life_expectancy = 0
year_of_interest_min_life_expectancy = 1_000_000_000
year_of_interest_min_life_expectancy_country = ""
year_of_interest_max_life_expectancy_country = ""

min_life_expectancy = 1_000_000_000
min_life_expectancy_country = ""
min_life_expectancy_year = ""

max_life_expectancy = 0
max_life_expectancy_country = ""
max_life_expectancy_year = ""

average_life_expectancy = 0

print()
print("Welcome to data analysis console 📈")

lines = "--------------------------------------------------------------------------"

print(lines)
print()

year_of_interest = input("Enter the year of interest: ")

try:
    with open("./week06/life-expectancy.csv") as life_expectancy:
        for line in enumerate(life_expectancy):
            (index, data) = line
            if index > 0:
                current_life_expectancy = float(data.strip().split(',')[3])
                # Get minimum life expectancy
                if current_life_expectancy < min_life_expectancy: 
                    min_life_expectancy = current_life_expectancy
                    min_life_expectancy_country = data.strip().split(',')[0]
                    min_life_expectancy_year = data.strip().split(',')[2]
                # Get maximum life expectancy
                if current_life_expectancy > max_life_expectancy: 
                    max_life_expectancy = current_life_expectancy
                    max_life_expectancy_country = data.strip().split(',')[0]
                    max_life_expectancy_year = data.strip().split(',')[2]
        
                if data.strip().split(',')[2] == year_of_interest:
                    year_of_interest_life_expectancy_sum += float(data.strip().split(',')[3])
                    year_of_interest_count += 1
                    # Get minimum life expectancy in year of interest
                    if current_life_expectancy < year_of_interest_min_life_expectancy:
                        year_of_interest_min_life_expectancy = current_life_expectancy
                        year_of_interest_min_life_expectancy_country = data.strip().split(',')[0]
                    # Get maximum life expectancy in year of interest
                    if current_life_expectancy > year_of_interest_max_life_expectancy:
                        year_of_interest_max_life_expectancy = current_life_expectancy
                        year_of_interest_max_life_expectancy_country = data.strip().split(',')[0]
    
    average_life_expectancy = year_of_interest_life_expectancy_sum / year_of_interest_count

    print(f"The overall max life expectancy is: {max_life_expectancy} from {max_life_expectancy_country} in {max_life_expectancy_year}")
    print(f"The overall min life expectancy is: {min_life_expectancy} from {min_life_expectancy_country} in {min_life_expectancy_year}")
    print()
    print(f"For the year {year_of_interest}: ")
    print(f"The average life expectancy across all countries was {round(average_life_expectancy, 2)}")
    print(f"The max life expectancy was in {year_of_interest_max_life_expectancy_country} with {year_of_interest_max_life_expectancy}")
    print(f"The min life expectancy was in {year_of_interest_min_life_expectancy_country} with {year_of_interest_min_life_expectancy}")
    print()
    print(lines)
except:
    print("❌ Error: Invalid year.")