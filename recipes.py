#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

from dataclasses import dataclass
from typing import List

# NOTE(Ryan): Recipe
@dataclass
class R:
  name: str
  protein: str
  grain: str
  ingredients: List
  instructions: str

# NOTE(Ryan): Ingredient
@dataclass
class I:
  name: str
  amount: float

# IMPORTANT(Ryan): Assume olive oil, salt, pepper

# TODO(Ryan): Max-flow to ensure constraints, e.g. 2 beef, 2 pasta etc.
global_recipes = [
  R("tuscan-chicken", "chicken", "pasta", 
    [I("chicken-breast", 800),
     I("egg", 1),
     I("oregano", 1),
     I("thyme", 0.5),
     I("paprika", 1.5),
     I("garlic-salt", 0.25),
     I("plain-flour", 3),
     I("brown-onion", 1),
     I("garlic", 2),
     I("sun-dried-tomatoes", 150),
     I("red-capsicum", 1),
     I("tomato-paste", 1),
     I("white-wine", 90),
     I("chicken-stock", 1),
     I("double-cream", 90),
     I("parmesan-cheese", 0.5),
     I("baby-spinach", 3),
     I("fresh-parsley", 1),
     I("fussili-pasta", 500),
    ],
    """
    1. Preheat the oven to 160C/320F. Trim the chicken breasts to remove any fatty parts.
    2. Whisk the egg lightly in a shallow bowl.
    3. In a separate shallow bowl, mix together the flour, salt, pepper, oregano, thyme, paprika and garlic salt.
    4. Heat 2 tbsp of the olive oil in a large frying pan (skillet) on a medium-to-high heat.
    5. Dip the chicken breasts in the egg, then dredge in the flour mixture.
    6. Place the chicken in the pan and fry on both sides until golden.
    7. Take the chicken out of the pan and place on a tray in the oven for 10 minutes to finish cooking whilst you make the sauce.
    8. Add the oil to the pan and heat on a medium heat.  Add the onion and cook for 3-4 minutes until they start to soften.
    9. Add the garlic, oregano, paprika, sun dried tomatoes, red pepper and tomato puree. Cook for 2 minutes, moving around the pan with a spatula.
    10. Next pour in the wine and allow to bubble for 2 minutes,
    11. Now add the chicken stock, salt and pepper. Bring the boil, then simmer for 5 minutes.
    12. Add the cream, parmesan and the spinach to the sauce and stir and cook for a couple of minutes until the spinach wilts.
    13. Remove the chicken from the oven. Check it's done (insert a knife into the fattest piece of one of the chicken breasts - it should no longer be pink) and place in the pan with the sauce and cook for another couple of minutes.
    14. Serve topped with a sprinkling of fresh parsley. Tastes great with pasta, courgetti (zoodles), rice or saute potatoes.
    """
    ),
  R("chicken-paprikash", "chicken", "pasta", 
    [I("chicken-breast", 800),
     I("egg", 1),
     I("oregano", 1),
     I("thyme", 0.5),
     I("paprika", 1.5),
     I("garlic-salt", 0.25),
     I("plain-flour", 3),
     I("brown-onion", 1),
     I("garlic", 2),
     I("sun-dried-tomatoes", 150),
     I("red-capsicum", 1),
     I("tomato-paste", 1),
     I("white-wine", 90),
     I("chicken-stock", 1),
     I("double-cream", 90),
     I("parmesan-cheese", 0.5),
     I("baby-spinach", 3),
     I("fresh-parsley", 1),
     I("fussili-pasta", 500),
    ],
    """
    1. Preheat the oven to 160C/320F. Trim the chicken breasts to remove any fatty parts.
    2. Whisk the egg lightly in a shallow bowl.
    3. In a separate shallow bowl, mix together the flour, salt, pepper, oregano, thyme, paprika and garlic salt.
    4. Heat 2 tbsp of the olive oil in a large frying pan (skillet) on a medium-to-high heat.
    5. Dip the chicken breasts in the egg, then dredge in the flour mixture.
    6. Place the chicken in the pan and fry on both sides until golden.
    7. Take the chicken out of the pan and place on a tray in the oven for 10 minutes to finish cooking whilst you make the sauce.
    8. Add the oil to the pan and heat on a medium heat.  Add the onion and cook for 3-4 minutes until they start to soften.
    9. Add the garlic, oregano, paprika, sun dried tomatoes, red pepper and tomato puree. Cook for 2 minutes, moving around the pan with a spatula.
    10. Next pour in the wine and allow to bubble for 2 minutes,
    11. Now add the chicken stock, salt and pepper. Bring the boil, then simmer for 5 minutes.
    12. Add the cream, parmesan and the spinach to the sauce and stir and cook for a couple of minutes until the spinach wilts.
    13. Remove the chicken from the oven. Check it's done (insert a knife into the fattest piece of one of the chicken breasts - it should no longer be pink) and place in the pan with the sauce and cook for another couple of minutes.
    14. Serve topped with a sprinkling of fresh parsley. Tastes great with pasta, courgetti (zoodles), rice or saute potatoes.
    """
    ),
]

# stroganoff, black pepper beef, beef goulash, beef ragu, beef and guiness stew, spag. bol, lasagne, massaman, rendang, steak pie, cottage pie, chilli con-carne, spicy ginger beef stir fry

# chicken parmesan, chicken korma, chicken tikka masala, chicken pie, chicken madras, chicken marsala, kung pao chicken, honey garlic, honey lemon, szechuan chicken, butter chicken

def recipes():
  global global_recipes

  names = ""
  ingredients = {}
  for recipe in global_recipes:
    names += (recipe.name + ", ")
    for ingredient in recipe.ingredients:
      if ingredients.get(ingredient.name, None) is not None:
        ingredients[ingredient.name] += ingredient.amount
      else:
        ingredients[ingredient.name] = ingredient.amount

  # TODO(Ryan): print snacks
  print(names[:-2])
  for name, amount in ingredients.items():
    print(f"* {name}: {amount}")

if __name__ == "__main__":
  recipes()
