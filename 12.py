import pickle 
import random

with open('/workspaces/codespaces-blank/data/food_Info.pkl', 'rb') as f:
    food_tables = pickle.load(f)
    

def recommend_food(calorie_limit):
    selected_foods_breakfast = []
    selected_foods_lunch = []
    selected_foods_dinner = []

    remaining_calories_breakfast = int(calorie_limit * 0.4)
    remaining_calories_lunch = int(calorie_limit * 0.3)
    remaining_calories_dinner = int(calorie_limit * 0.3)

    while remaining_calories_breakfast > 0:
        # Choose a random food table
        table_name = random.choice(list(food_tables.keys()))
        table = food_tables[table_name]
        
        if list(table.values())[0][0][5] == 1:
            # Choose a random food item from the selected table
            food_name = random.choice(list(table.keys()))
            
            food_calories = table[food_name][0][4]

            # Check if adding the food exceeds the remaining calories
            # if abs(remaining_calories_breakfast - food_calories) in range(50):
            selected_foods_breakfast.append((food_name, food_calories))
            remaining_calories_breakfast -= food_calories
            
    while remaining_calories_lunch > 0:
        # Choose a random food table
        table_name = random.choice(list(food_tables.keys()))
        table = food_tables[table_name]
        
        if list(table.values())[0][0][6] == 1:
            # Choose a random food item from the selected table
            food_name = random.choice(list(table.keys()))
            
            food_calories = table[food_name][0][4]

            # Check if adding the food exceeds the remaining calories
            # if abs(remaining_calories_breakfast - food_calories) in range(50):
            selected_foods_lunch.append((food_name, food_calories))
            remaining_calories_lunch -= food_calories
            
    while remaining_calories_dinner > 0:
        # Choose a random food table
        table_name = random.choice(list(food_tables.keys()))
        table = food_tables[table_name]
        
        if list(table.values())[0][0][7] == 1:
            # Choose a random food item from the selected table
            food_name = random.choice(list(table.keys()))
            
            food_calories = table[food_name][0][4]

            # Check if adding the food exceeds the remaining calories
            # if abs(remaining_calories_breakfast - food_calories) in range(50):
            selected_foods_dinner.append((food_name, food_calories))
            remaining_calories_dinner -= food_calories

    return selected_foods_breakfast, selected_foods_lunch, selected_foods_dinner


daily_calorie_limit = 1500
recommended_foods_breakfast, recommended_foods_lunch, recommended_foods_dinner = recommend_food(daily_calorie_limit)

print("Recommended foods for Breakfast:")
for food, calories in recommended_foods_breakfast:
    print(f"{food}: {calories} calories")

print("\nRecommended foods for Lunch:")
for food, calories in recommended_foods_lunch:
    print(f"{food}: {calories} calories")

print("\nRecommended foods for Dinner:")
for food, calories in recommended_foods_dinner:
    print(f"{food}: {calories} calories")
