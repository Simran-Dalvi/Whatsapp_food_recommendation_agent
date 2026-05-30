from recommendation import recommend_food

preferences = {
    'type' : 'veg',
    'category' : 'Indian',
    'budget' : 250,
    'style' : 'spicy'
}

preferences2 = {
    'type' : 'veg',
    'category' : 'japanese',
    'budget' : 500,
    # 'style' : 'spicy'
}


dishes = recommend_food(preferences2)

print("Recommended dishes: \n", dishes)