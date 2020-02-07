#!/usr/bin/python

'''
Input:
   recipe { 'milk': 100, 'butter': 50, 'flour': 5 }, 
    ingredients { 'milk': 138, 'butter': 48, 'flour': 51 }

for each key of recipe:
    find the corresponding ingredients key
    divide ingredients value // recipe value

    Add result of division to new list
    New list will be like this:
        [ 1, 0, 10 ] 

Find first lowest value in new list: 0

This value represents the batches to be returned

'''

import math

def recipe_batches(recipe, ingredients):
    # all possible batches given the ingredients we have
    possible_batches = []

    # ingredients[key] will throw an error if the key doesn't exist, so 
    # I am using ingredients.get(key, default value) which returns
    # the default if key is not there

    for key in recipe:
        if ingredients.get(key, None): 
            possible_batches.append(ingredients[key] // recipe[key])
        else:
            return 0

    return min(possible_batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
