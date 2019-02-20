#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # start a counter
    num_batches = -1 #My loop will add one during a fail condition
    enough_ingredients = True
    # while amount of ingredients is greater than ingredients necessary for the recipe
    while (enough_ingredients):
        for key, value in recipe.items():
            # Subtract the recipe amounts from the on hand amounts
            if ingredients.get(key):
                if ingredients[key] - value >= 0:
                    ingredients[key] = ingredients[key] - value
                else:
                    enough_ingredients = False
        # if any of those ends up being less than 0 -> BREAK
            else:
                enough_ingredients = False
        # otherwise add one to the counter
        num_batches += 1

    for key, value in ingredients.items():
        print(key, value)
    # return the counter number
    return num_batches




# recipe = { 'milk': 2 }
# ingredients = { 'milk': 200 }
# print(recipe_batches(recipe, ingredients))

# if __name__ == '__main__':
#     # Change the entries of these dictionaries to test
#     # your implementation with different inputs
#     recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#     ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#     print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))