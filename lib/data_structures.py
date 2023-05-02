spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food.get('name') for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(food["name"] + ' (' + food['cuisine'] + ') | Heat Level: ' + food["heat_level"] * "🌶")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(food["name"] + ' (' + food['cuisine'] + ') | Heat Level: ' + food["heat_level"] * "🌶")

def get_average_heat_level(spicy_foods):
    total = 0
    for food in spicy_foods:
        total+=food['heat_level']
    return total/len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
