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
  duration: float
  ingredients: List

# NOTE(Ryan): Ingredient
@dataclass
class I:
  name: str
  amount: float


# TODO(Ryan): Max-flow to ensure constraints, e.g. 2 beef, 2 pasta etc.
global_recipes = [
  R("tuscan-chicken", "chicken", "pasta", 1,
    [I("chicken-breast", 700),
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
    ),
  R("fettucine-bolognese", "beef", "pasta", 1,
    [I("beef-mince", 500),
     I("fettucine-pasta", 500),
     I("brown-onion", 1),
     I("celery", 1),
     I("carrot", 1),
     I("pancetta", 150),
     I("red-wine", 200),
     I("tomato-paste", 2),
     I("chicken-stock", 1),
    ],
    ),
  R("beef-chow-fun", "beef", "noodles", 45,
    [I("light-soy-sauce", 2),
     I("dark-soy-sauce", 2),
     I("oyster-sauce", 2),
     I("sesame-oil", 2),
     I("brown-sugar", 1),
     I("rice-vinegar", 1),
     I("ginger", 1),
     I("garlic", 3),
     I("white-pepper", 0.25),
     I("flank-steak", 500),
     I("flat-rice-noodles", 200),
     I("brown-onion", 1),
     I("yellow-capsicum", 1),
     I("bean-sprouts", 200),
     I("spring-onions", 4),
     I("baby-spinach", 60),
     I("red-chilli", 1),
     I("sesame-seeds", 1),
    ],
    ),
  R("beef-massaman", "beef", "rice", 3,
    [I("red-onion", 1),
     I("red-chilli", 2),
     I("coriander", 2),
     I("cumin", 2),
     I("cinnamon", 0.5),
     I("white-pepper", 0.5),
     I("garlic", 3),
     I("lemongrass", 2),
     I("ginger", 1),
     I("fish-sauce", 3),
     I("brown-sugar", 1),
     I("fresh-coriander", 1),
     I("corn-flour", 1.5),
     I("beef-chuck", 1),
     I("beef-stock", 2),
     I("coconut-milk", 400),
     I("potatoes", 500),
     I("lime-juice", 1),
     I("white-rice", 500),
    ],
    ),
  R("butter-chicken", "chicken", "rice", 2,
    [I("chicken-breast", 700),
     I("natural-yogurt", 80),
     I("lemon-juice", 1),
     I("garlic", 5),
     I("garam-masala", 2.5),
     I("coriander", 1),
     I("paprika", 2),
     I("chilli-powder", 1),
     I("brown-onion", 1),
     I("ginger", 2),
     I("curry-powder", 1),
     I("cinnamon", 0.5),
     I("chicken-stock", 0.5),
     I("passata", 400),
     I("tomato-paste", 2),
     I("cardamom-pods", 6),
     I("double-cream", 175),
     I("fresh-coriander", 1),
     I("white-rice", 500),
    ],
    ),
  R("chicken-pie", "chicken", "pastry", 1.5,
    [I("puff-pastry", 2),
     I("chicken-breast", 500),
     I("carrot", 3),
     I("potato", 3),
     I("fresh-thyme", 2),
     I("brown-onion", 1),
     I("plain-flour", 6),
     I("milk", 300),
     I("egg", 1),
     I("lemon-juice", 1),
     I("brocolli", 1),
    ],
    ),
  R("beef-stroganoff", "beef", "pasta", 45,
    [I("fillet-steak", 600),
     I("brown-onion", 1),
     I("mushroom", 300),
     I("plain-flour", 2),
     I("beef-stock", 2),
     I("dijon-mustard", 1),
     I("sour-cream", 150),
     I("penne-pasta", 500),
     I("fresh-chives", 1),
    ],
    ),
  R("kung-pao-chicken", "chicken", "rice", 1,
    [I("rice-wine", 2),
     I("white-pepper", 0.25),
     I("dark-soy-sauce", 5),
     I("hoisin-sauce", 4),
     I("sesame-oil", 1),
     I("garlic", 2),
     I("ginger", 1),
     I("chicken-breast", 500),
     I("corn-flour", 1),
     I("red-chilli", 2),
     I("red-capsicum", 2),
     I("zucchini", 1),
     I("spring-onion", 12),
     I("cashew", 1),
     I("white-rice", 500),
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
  for recipe in global_recipes:
    names += (recipe.name + f"({recipe.duration}-{recipe.grain}), ")
    for ingredient in recipe.ingredients:
      if ingredients.get(ingredient.name, None) is not None:
        ingredients[ingredient.name] += ingredient.amount
      else:
        ingredients[ingredient.name] = ingredient.amount

  print("CHECK:")
  to_check=["butter", "olive oil", "salt", "pepper", 
            "hummus", "baba-ganoush", "peanut-butter", "cheese-sticks",
            "dates", "dark-chocolate", "grapes", "tea",
            "vita-wheats", "corn-chips",
            "rolled-oats", "yogurt", "frozen-berries", "mixed-nuts", "cinnamon", "coconut-flakes", "seeds", "juice", "kale",
            "ice-cream"
           ]
  for check in to_check:
    print(f"* {check}")

  print("\nADD:\n")

  print(f"\nRECIPES:\n{names[:-2]}")
  for name, amount in ingredients.items():
    print(f"* {name}: {amount}")

if __name__ == "__main__":
  recipes()
