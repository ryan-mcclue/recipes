#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

import sys

from dataclasses import dataclass
from typing import List

# NOTE(Ryan): Recipe
@dataclass
class R:
  name: str
  protein: str
  grain: str
  duration: float
  ingredients: List

# NOTE(Ryan): Ingredient
@dataclass
class I:
  name: str
  amount: float
  category: str

# alcohol
# canned
# condiments

# TODO(Ryan): Max-flow to ensure constraints, e.g. 2 beef, 2 pasta etc.
global_recipes = [
  R("tuscan-chicken", "chicken", "pasta", 1,
    [I("chicken-breast", 700, "meat"),
     I("egg", 1, "dairy"),
     I("oregano", 1, "condiment"),
     I("thyme", 0.5, "condiment"),
     I("paprika", 1.5, "condiment"),
     I("garlic-salt", 0.25, "condiment"),
     I("plain-flour", 3, "other"),
     I("brown-onion", 1, "fruit-veg"),
     I("garlic", 2, "fruit-veg"),
     I("sun-dried-tomatoes", 150, "fruit-veg"),
     I("red-capsicum", 1, "fruit-veg"),
     I("tomato-paste", 1, "other"),
     I("white-wine", 90, "alcohol"),
     I("chicken-stock", 1, "other"),
     I("double-cream", 90, "dairy"),
     I("parmesan-cheese", 0.5, "dairy"),
     I("baby-spinach", 120, "fruit-veg"),
     I("fresh-parsley", 1, "fruit-veg"),
     I("fussili-pasta", 500, "other"),
    ],
    ),
  R("fettucine-bolognese", "beef", "pasta", 1,
    [I("beef-mince", 500, "meat"),
     I("fettucine-pasta", 500, "other"),
     I("brown-onion", 1, "fruit-veg"),
     I("celery", 1, "fruit-veg"),
     I("carrot", 1, "fruit-veg"),
     I("pancetta", 150, "meat"),
     I("red-wine", 200, "alcohol"),
     I("tomato-paste", 2, "other"),
     I("chicken-stock", 1, "other"),
    ],
    ),
  R("beef-chow-fun", "beef", "noodles", 45,
    [I("light-soy-sauce", 2, "other"),
     I("dark-soy-sauce", 2, "other"),
     I("oyster-sauce", 2, "other"),
     I("sesame-oil", 2, "other"),
     I("brown-sugar", 1, "other"),
     I("rice-vinegar", 1, "other"),
     I("ginger", 1, "fruit-veg"),
     I("garlic", 3, "fruit-veg"),
     I("white-pepper", 0.25, "condiment"),
     I("flank-steak", 500, "meat"),
     I("flat-rice-noodles", 200, "other"),
     I("brown-onion", 1, "fruit-veg"),
     I("yellow-capsicum", 1, "fruit-veg"),
     I("bean-sprouts", 200, "fruit-veg"),
     I("spring-onions", 4, "fruit-veg"),
     I("baby-spinach", 60, "fruit-veg"),
     I("red-chilli", 1, "fruit-veg"),
     I("sesame-seeds", 1, "other"),
    ],
    ),
  R("beef-massaman", "beef", "rice", 3,
    [I("red-onion", 1, "fruit-veg"),
     I("red-chilli", 2, "fruit-veg"),
     I("coriander", 2, "condiment"),
     I("cumin", 2, "condiment"),
     I("cinnamon", 0.5, "condiment"),
     I("white-pepper", 0.5, "condiment"),
     I("garlic", 3, "fruit-veg"),
     I("lemongrass", 2, "fruit-veg"),
     I("ginger", 1, "fruit-veg"),
     I("fish-sauce", 3, "other"),
     I("brown-sugar", 1, "other"),
     I("fresh-coriander", 1, "fruit-veg"),
     I("corn-flour", 1.5, "other"),
     I("beef-chuck", 1000, "meat"),
     I("beef-stock", 2, "other"),
     I("coconut-milk", 400, "other"),
     I("potato", 3, "fruit-veg"),
     I("lime-juice", 1, "other"),
     I("white-rice", 500, "other"),
    ],
    ),
  R("butter-chicken", "chicken", "rice", 2,
    [I("chicken-breast", 700, "meat"),
     I("natural-yogurt", 80, "dairy"),
     I("lemon-juice", 1, "other"),
     I("garlic", 5, "fruit-veg"),
     I("garam-masala", 2.5, "condiment"),
     I("coriander", 1, "condiment"),
     I("paprika", 2, "condiment"),
     I("chilli-powder", 1, "condiment"),
     I("brown-onion", 1, "fruit-veg"),
     I("ginger", 2, "fruit-veg"),
     I("curry-powder", 1, "condiment"),
     I("cinnamon", 0.5, "condiment"),
     I("chicken-stock", 0.5, "other"),
     I("passata", 400, "other"),
     I("tomato-paste", 2, "other"),
     I("cardamom-pods", 6, "fruit-veg"),
     I("double-cream", 175, "diary"),
     I("fresh-coriander", 1, "fruit-veg"),
     I("white-rice", 500, "other"),
    ],
    ),
  R("chicken-pie", "chicken", "pastry", 1.5,
    [I("puff-pastry", 2, "frozen"),
     I("chicken-breast", 500, "meat"),
     I("carrot", 3, "fruit-veg"),
     I("potato", 3, "fruit-veg"),
     I("fresh-thyme", 2, "fruit-veg"),
     I("brown-onion", 1, "fruit-veg"),
     I("plain-flour", 6, "other"),
     I("milk", 300, "dairy"),
     I("egg", 1, "dairy"),
     I("lemon-juice", 1, "other"),
     I("brocolli", 1, "fruit-veg"),
    ],
    ),
  R("beef-stroganoff", "beef", "pasta", 45,
    [I("fillet-steak", 600, "meat"),
     I("brown-onion", 1, "fruit-veg"),
     I("mushroom", 300, "fruit-veg"),
     I("plain-flour", 2, "other"),
     I("beef-stock", 2, "other"),
     I("dijon-mustard", 1, "other"),
     I("sour-cream", 150, "dairy"),
     I("penne-pasta", 500, "other"),
     I("fresh-chives", 1, "fruit-veg"),
    ],
    ),
  R("kung-pao-chicken", "chicken", "rice", 1,
    [I("rice-wine", 2, "other"),
     I("white-pepper", 0.25, "other"),
     I("dark-soy-sauce", 5, "other"),
     I("hoisin-sauce", 4, "other"),
     I("sesame-oil", 1, "other"),
     I("garlic", 2, "fruit-veg"),
     I("ginger", 1, "fruit-veg"),
     I("chicken-breast", 500, "meat"),
     I("corn-flour", 1, "other"),
     I("red-chilli", 2, "fruit-veg"),
     I("red-capsicum", 2, "fruit-veg"),
     I("zucchini", 1, "fruit-veg"),
     I("spring-onion", 12, "fruit-veg"),
     I("cashew", 1, "other"),
     I("white-rice", 500, "other"),
    ],
    ),

]

# cottage pie, rendang
# paprikash, mee goreng (thin), kung pao

# black pepper beef, beef goulash, beef ragu, beef and guiness stew, lasagne, steak pie, chilli con-carne, spicy ginger beef stir fry
# chicken parmesan, chicken korma, chicken tikka masala, chicken madras, chicken marsala, honey garlic, honey lemon, szechuan chicken 

def recipes():
  global global_recipes

  names = ""
  ingredients = {}
  # TODO(Ryan): More intelligent recipe culling
  for recipe in global_recipes[:6]:
    names += (recipe.name + f"({recipe.duration}-{recipe.grain}), ")
    for ingredient in recipe.ingredients:
      if ingredients.get(ingredient.name, None) is not None:
        ingredients[ingredient.name].amount += ingredient.amount
      else:
        ingredients[ingredient.name] = ingredient

  regular_ingredients=[I("BUTTER", 0, "dairy"), 
            I("OLIVE-OIL", 0, "other"),
            I("SALT", 0, "other"),
            I("PEPPER", 0, "other"),
            I("HUMMUS", 0, "other"),
            I("BABA-GANOUSH", 0, "other"),
            I("PEANUT-BUTTER", 0, "other"),
            I("CHEESE-STICKS", 0, "dairy"),
            I("FAVA-BEANS", 0, "other"),
            I("DATES", 0, "fruit-veg"),
            I("GRAPES", 0, "fruit-veg"),
            I("DARK-CHOCOLATE", 0, "other"),
            I("TEA", 0, "other"),
            I("VITA-WHEATS", 0, "other"),
            I("CORN-CHIPS", 0, "other"),
            I("ROLLED-OATS", 0, "other"),
            I("YOGURT", 0, "dairy"),
            I("FROZEN-BERRIES", 0, "frozen"),
            I("ICE-CREAM", 0, "frozen"),
            I("MIXED-NUTS", 0, "other"),
            I("CINNAMON", 0, "other"),
            I("COCONUT-FLAKES", 0, "other"),
            I("SEEDS", 0, "other"),
            I("JUICE", 0, "dairy"),
            I("KALE", 0, "fruit-veg"),
            I("MILK", 0, "dairy"),
           ]

  for regular_ingredient in regular_ingredients:
    ingredients[regular_ingredient.name] = regular_ingredient 

  sorted_ingredients = dict(sorted(ingredients.items(), key=lambda i: i[1].category))

  print_output = sys.stdout

  want_to_print = True
  if want_to_print:
    print_output = open("recipes.md", "w")

  print(f"\n##### RECIPES:\n{names[:-2]}\n", file=print_output)
  cur_category = ""

  for ingredient_name, ingredient in sorted_ingredients.items():
    category = ingredient.category
    if cur_category != category:
      cur_category = category
      print(f"\n**{cur_category.upper()}**:", file=print_output)
    print(f"{ingredient_name} ({ingredient.amount}), ", file=print_output)


  # NOTE(Ryan): To inform bash script to create pdf and open it
  if want_to_print:
    print("to-print")

if __name__ == "__main__":
  recipes()
