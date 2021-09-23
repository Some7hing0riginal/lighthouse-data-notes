"""
Alberto is making spaghetti tonight and he needs to make sure that if he doesn't have enough of the ingredients in his pantry, he adds them to his shopping list.

    For each item in the recipe, check if the ingredient is in Alberto's pantry.

    If the recipe ingredient is in the pantry, check if the recipe requires more of the ingredient than what Alberto has in storage. If so, add the name and the quantity he needs to purchase as key-value pairs in the dictionary shopping_list.

    If the recipe item is not in the pantry, add the ingredient and the quantity as key-value pairs in the dictionary shopping_list.


"""

pantry = {'pasta': 3, 'garlic': 4,'sauce': 2,
          'basil': 2, 'salt': 3, 'olive oil': 3,
          'rice': 3, 'bread': 3, 'peanut butter': 1,
          'flour': 1, 'eggs': 1, 'onions': 1, 'mushrooms': 3,
          'broccoli': 2, 'butter': 2,'pickles': 6, 'milk': 2,
          'chia seeds': 5}

meal_recipe = {'pasta': 2, 'garlic': 2, 'sauce': 3,
          'basil': 4, 'salt': 1, 'pepper': 2,
          'olive oil': 2, 'onions': 2, 'mushrooms': 6}


shopping_list = dict()

for (ingredient, quantity) in meal_recipe.items():
    if ingredient in pantry:
        if pantry[ingredient] < quantity:
            shopping_list[ingredient] = quantity - pantry[ingredient]
    else:
        shopping_list[ingredient] = quantity
print(shopping_list)
    
    
