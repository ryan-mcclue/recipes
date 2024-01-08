#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

import sys

from dataclasses import dataclass
from enum import Enum, auto
from typing import List

class INGREDIENT_CAT(Enum):
  DAIRY = 0
  FRUIT_VEG = auto(),
  FROZEN = auto(),
  TOILETRIES = auto(),
  MEDICINAL = auto(),
  CONDIMENT = auto(),
  MEAT = auto(),
  CANNED = auto(),
  ALCOHOL = auto(),
  OTHER = auto()

@dataclass
class Ingredient:
  name: str
  amount: float
  category: INGREDIENT_CAT

global_ingredients = [
  Ingredient("butter", 1, INGREDIENT_CAT.DAIRY), 
  Ingredient("olive-oil", 1, INGREDIENT_CAT.OTHER),
  Ingredient("salt", 1, INGREDIENT_CAT.OTHER),
  Ingredient("pepper", 1, INGREDIENT_CAT.OTHER),
  Ingredient("hummus", 1, INGREDIENT_CAT.OTHER),
  Ingredient("peanut-butter", 1, INGREDIENT_CAT.OTHER),
  Ingredient("cheese-sticks", 1, INGREDIENT_CAT.DAIRY),
  Ingredient("fava-beans", 1, INGREDIENT_CAT.OTHER),
  Ingredient("dates", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("apples", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("bananas", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("carrots", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("dark-chocolate", 1, INGREDIENT_CAT.OTHER),
  Ingredient("vita-wheats", 1, INGREDIENT_CAT.OTHER),
  Ingredient("corn-chips", 1, INGREDIENT_CAT.OTHER),
  Ingredient("rolled-oats", 1, INGREDIENT_CAT.OTHER),
  Ingredient("yogurt", 1, INGREDIENT_CAT.DAIRY),
  Ingredient("frozen-berries", 1, INGREDIENT_CAT.FROZEN),
  Ingredient("ice-cream", 1, INGREDIENT_CAT.FROZEN),
  Ingredient("mixed-nuts", 1, INGREDIENT_CAT.OTHER),
  Ingredient("cinnamon", 1, INGREDIENT_CAT.CONDIMENT),
  Ingredient("coconut-flakes", 1, INGREDIENT_CAT.OTHER),
  Ingredient("seeds", 1, INGREDIENT_CAT.OTHER),
  Ingredient("honey", 1, INGREDIENT_CAT.OTHER),
  Ingredient("juice", 1, INGREDIENT_CAT.DAIRY),
  Ingredient("kale", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("milk", 1, INGREDIENT_CAT.DAIRY),
  Ingredient("paper-towels", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("tissues", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("toilet-paper", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("deoderant", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("toothpaste", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("dental-floss", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("sunscreen", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("panadol", 1, INGREDIENT_CAT.MEDICINAL),
  Ingredient("nurofen", 1, INGREDIENT_CAT.MEDICINAL),
  Ingredient("demazin", 1, INGREDIENT_CAT.MEDICINAL),
  Ingredient("sponge", 1, INGREDIENT_CAT.OTHER),
  Ingredient("bar-soap", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("soap", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("stove-cleaner", 1, INGREDIENT_CAT.OTHER),
  Ingredient("bin-bags", 1, INGREDIENT_CAT.OTHER),
  Ingredient("compost-bags", 1, INGREDIENT_CAT.OTHER),
  Ingredient("dishwasher-tablets", 1, INGREDIENT_CAT.OTHER),
  Ingredient("detergent", 1, INGREDIENT_CAT.OTHER),
  Ingredient("glen-20", 1, INGREDIENT_CAT.OTHER),
  Ingredient("betadine", 1, INGREDIENT_CAT.MEDICINAL),
  Ingredient("band-aids", 1, INGREDIENT_CAT.MEDICINAL),
  Ingredient("cotton-balls", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("shampoo/conditioner", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("cleanser", 1, INGREDIENT_CAT.TOILETRIES),
  Ingredient("sudafed", 1, INGREDIENT_CAT.MEDICINAL),
  Ingredient("strepsils", 1, INGREDIENT_CAT.MEDICINAL),
  Ingredient("eucalyptus", 1, INGREDIENT_CAT.MEDICINAL),
  Ingredient("pino-clean", 1, INGREDIENT_CAT.OTHER),
  Ingredient("scourer", 1, INGREDIENT_CAT.OTHER),
  Ingredient("aa-batteries", 1, INGREDIENT_CAT.OTHER),
  Ingredient("aaa-batteries", 1, INGREDIENT_CAT.OTHER),
  Ingredient("lime", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("orange", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("lemon", 1, INGREDIENT_CAT.FRUIT_VEG),
]

tuscan_chicken = [
  Ingredient("chicken-breast", 700, INGREDIENT_CAT.MEAT),
  Ingredient("egg", 1, INGREDIENT_CAT.DAIRY),
  Ingredient("oregano", 1, INGREDIENT_CAT.CONDIMENT),
  Ingredient("thyme", 0.5, INGREDIENT_CAT.CONDIMENT),
  Ingredient("paprika", 1.5, INGREDIENT_CAT.CONDIMENT),
  Ingredient("garlic-salt", 0.25, INGREDIENT_CAT.CONDIMENT),
  Ingredient("plain-flour", 3, INGREDIENT_CAT.OTHER),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("garlic", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("tin-tomatoes", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("red-capsicum", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("tomato-paste", 1, INGREDIENT_CAT.OTHER),
  Ingredient("white-wine", 90, INGREDIENT_CAT.ALCOHOL),
  Ingredient("chicken-stock", 1, INGREDIENT_CAT.OTHER),
  Ingredient("double-cream", 90, INGREDIENT_CAT.DAIRY),
  Ingredient("parmesan-cheese", 0.5, INGREDIENT_CAT.DAIRY),
  Ingredient("baby-spinach", 120, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("fresh-parsley", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("fussili-pasta", 500, INGREDIENT_CAT.OTHER),
]

fettucine_bolognese = [
  Ingredient("beef-mince", 500, INGREDIENT_CAT.MEAT),
  Ingredient("fettucine-pasta", 500, INGREDIENT_CAT.OTHER),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("celery", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("carrot", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("pancetta", 150, INGREDIENT_CAT.MEAT),
  Ingredient("red-wine", 200, INGREDIENT_CAT.ALCOHOL),
  Ingredient("tomato-paste", 2, INGREDIENT_CAT.OTHER),
  Ingredient("passata", 200, INGREDIENT_CAT.OTHER),
  Ingredient("chicken-stock", 1, INGREDIENT_CAT.OTHER),
]

beef_chow_fun = [
  Ingredient("light-soy-sauce", 2, INGREDIENT_CAT.OTHER),
  Ingredient("dark-soy-sauce", 2, INGREDIENT_CAT.OTHER),
  Ingredient("oyster-sauce", 2, INGREDIENT_CAT.OTHER),
  Ingredient("sesame-oil", 2, INGREDIENT_CAT.OTHER),
  Ingredient("brown-sugar", 1, INGREDIENT_CAT.OTHER),
  Ingredient("rice-vinegar", 1, INGREDIENT_CAT.OTHER),
  Ingredient("ginger", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("garlic", 3, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("white-pepper", 0.25, INGREDIENT_CAT.CONDIMENT),
  Ingredient("flank-steak", 500, INGREDIENT_CAT.MEAT),
  Ingredient("thin-rice-noodles", 200, INGREDIENT_CAT.OTHER),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("yellow-capsicum", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("bean-sprouts", 200, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("spring-onions", 4, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("baby-spinach", 60, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("red-chilli", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("sesame-seeds", 1, INGREDIENT_CAT.OTHER),
]

butter_chicken = [
  Ingredient("chicken-breast", 700, INGREDIENT_CAT.MEAT),
  Ingredient("natural-yogurt", 80, INGREDIENT_CAT.DAIRY),
  Ingredient("lemon-juice", 1, INGREDIENT_CAT.OTHER),
  Ingredient("garlic", 5, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("garam-masala", 2.5, INGREDIENT_CAT.CONDIMENT),
  Ingredient("coriander", 1, INGREDIENT_CAT.CONDIMENT),
  Ingredient("paprika", 2, INGREDIENT_CAT.CONDIMENT),
  Ingredient("chilli-powder", 1, INGREDIENT_CAT.CONDIMENT),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("ginger", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("curry-powder", 1, INGREDIENT_CAT.CONDIMENT),
  Ingredient("cinnamon", 0.5, INGREDIENT_CAT.CONDIMENT),
  Ingredient("chicken-stock", 0.5, INGREDIENT_CAT.OTHER),
  Ingredient("passata", 400, INGREDIENT_CAT.OTHER),
  Ingredient("tomato-paste", 2, INGREDIENT_CAT.OTHER),
  Ingredient("cardamom-pods", 6, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("double-cream", 175, "diary"),
  Ingredient("fresh-coriander", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("white-rice", 500, INGREDIENT_CAT.OTHER),
]

chicken_pie = [
  Ingredient("puff-pastry", 2, "frozen"),
  Ingredient("chicken-breast", 500, INGREDIENT_CAT.MEAT),
  Ingredient("carrot", 3, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("potato", 3, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("fresh-thyme", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("plain-flour", 6, INGREDIENT_CAT.OTHER),
  Ingredient("milk", 300, INGREDIENT_CAT.DAIRY),
  Ingredient("egg", 1, INGREDIENT_CAT.DAIRY),
  Ingredient("lemon-juice", 1, INGREDIENT_CAT.OTHER),
  Ingredient("brocolli", 1, INGREDIENT_CAT.FRUIT_VEG),
]

beef_stroganoff = [
  Ingredient("fillet-steak", 600, INGREDIENT_CAT.MEAT),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("mushroom", 300, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("plain-flour", 2, INGREDIENT_CAT.OTHER),
  Ingredient("beef-stock", 2, INGREDIENT_CAT.OTHER),
  Ingredient("dijon-mustard", 1, INGREDIENT_CAT.OTHER),
  Ingredient("sour-cream", 150, INGREDIENT_CAT.DAIRY),
  Ingredient("penne-pasta", 500, INGREDIENT_CAT.OTHER),
  Ingredient("fresh-chives", 1, INGREDIENT_CAT.FRUIT_VEG),
]  

kung_pao_chicken = [
  Ingredient("rice-wine", 2, INGREDIENT_CAT.OTHER),
  Ingredient("white-pepper", 0.25, INGREDIENT_CAT.OTHER),
  Ingredient("dark-soy-sauce", 5, INGREDIENT_CAT.OTHER),
  Ingredient("hoisin-sauce", 4, INGREDIENT_CAT.OTHER),
  Ingredient("sesame-oil", 1, INGREDIENT_CAT.OTHER),
  Ingredient("garlic", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("ginger", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("chicken-breast", 500, INGREDIENT_CAT.MEAT),
  Ingredient("corn-flour", 1, INGREDIENT_CAT.OTHER),
  Ingredient("red-chilli", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("red-capsicum", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("zucchini", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("spring-onion", 12, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("cashew", 1, INGREDIENT_CAT.OTHER),
  Ingredient("white-rice", 500, INGREDIENT_CAT.OTHER),
]  

cottage_pie = [
  Ingredient("brown-onion", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("celery", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("carrot", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("green-beans", 200, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("beef-mince", 900, INGREDIENT_CAT.MEAT),
  Ingredient("worcestershire-sauce", 2, INGREDIENT_CAT.OTHER),
  Ingredient("beef-stock", 2, INGREDIENT_CAT.OTHER),
  Ingredient("potato", 1800, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("heavy-cream", 120, INGREDIENT_CAT.DAIRY),
  Ingredient("corn-flour", 2, INGREDIENT_CAT.OTHER),
]

chicken_paprikash = [
  Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("garlic", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("tin-tomatoes", 400, INGREDIENT_CAT.OTHER),
  Ingredient("celery", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("chicken-breast", 500, INGREDIENT_CAT.MEAT),
  Ingredient("plain-flour", 2, INGREDIENT_CAT.OTHER),
  Ingredient("sweet-paprika", 2, INGREDIENT_CAT.OTHER),
  Ingredient("chicken-stock", 2, INGREDIENT_CAT.OTHER),
  Ingredient("sour-cream", 225, INGREDIENT_CAT.DAIRY),
  Ingredient("fussili-pasta", 500, INGREDIENT_CAT.OTHER),
]

mee_goreng = [
  Ingredient("shallot", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("mushroom", 5, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("garlic", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("white-cabbage", 0.5, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("chicken-breast", 500, INGREDIENT_CAT.MEAT),
  Ingredient("thick-egg-noodles", 2, INGREDIENT_CAT.OTHER),
  Ingredient("bean-sprouts", 150, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("spring-onion", 6, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("red-chilli", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("sweet-soy-sauce", 4, INGREDIENT_CAT.OTHER),
  Ingredient("dark-soy-sauce", 3, INGREDIENT_CAT.OTHER),
  Ingredient("oyster-sauce", 2, INGREDIENT_CAT.OTHER),
  Ingredient("sweet-chilli-sauce", 2, INGREDIENT_CAT.OTHER),
  Ingredient("white-pepper", 0.25, INGREDIENT_CAT.OTHER),
]  

black_pepper_beef = [
  Ingredient("black-peppercorns", 10, INGREDIENT_CAT.OTHER),
  Ingredient("sirloin", 450, INGREDIENT_CAT.MEAT),
  Ingredient("sesame-oil", 1, INGREDIENT_CAT.OTHER),
  Ingredient("brown-onion", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("red-capsicum", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("green-capsicum", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("cornflour", 2, INGREDIENT_CAT.OTHER),
  Ingredient("dark-soy-sauce", 2, INGREDIENT_CAT.OTHER),
  Ingredient("oyster-sauce", 2, INGREDIENT_CAT.OTHER),
  Ingredient("red-chilli", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("chinese-cooking-wine", 1, INGREDIENT_CAT.OTHER),
  Ingredient("beef-stock", 0.5, INGREDIENT_CAT.OTHER),
  Ingredient("garlic", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("ginger", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("white-rice", 500, INGREDIENT_CAT.OTHER),
]

meatball_pasta_bake = [
  Ingredient("beef-mince", 500, INGREDIENT_CAT.MEAT),
  Ingredient("shallot", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("garlic", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("breadcrumbs", 60, INGREDIENT_CAT.OTHER),
  Ingredient("egg", 1, INGREDIENT_CAT.DAIRY),
  Ingredient("italian-herbs", 1, INGREDIENT_CAT.OTHER),
  Ingredient("tin-tomatoes", 400, INGREDIENT_CAT.OTHER),
  Ingredient("beef-stock", 1, INGREDIENT_CAT.OTHER),
  Ingredient("worcestershire-sauce", 1, INGREDIENT_CAT.OTHER),
  Ingredient("smoked-paprika", 1, INGREDIENT_CAT.OTHER),
  Ingredient("cheddar-cheese", 40, INGREDIENT_CAT.DAIRY),
  Ingredient("mozarella-cheese", 30, INGREDIENT_CAT.DAIRY),
  Ingredient("rigatoni-pasta", 500, INGREDIENT_CAT.OTHER),
]

kofta = [
  Ingredient("lamb-mince", 500, INGREDIENT_CAT.MEAT),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("garlic", 3, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("fresh-mint", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("cumin", 3, INGREDIENT_CAT.OTHER),
  Ingredient("coriander", 2, INGREDIENT_CAT.OTHER),
  Ingredient("chilli-flakes", 1, INGREDIENT_CAT.OTHER),
  Ingredient("cinnamon", 1, INGREDIENT_CAT.OTHER),
  Ingredient("flatbread", 4, INGREDIENT_CAT.OTHER),
  Ingredient("cherry-tomatoes", 10, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("salad-mix", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("white-wine-vinegar", 1, INGREDIENT_CAT.OTHER),
  Ingredient("tzatiki", 1, INGREDIENT_CAT.DAIRY),
  Ingredient("skewers", 6, INGREDIENT_CAT.OTHER),
]  

honey_garlic_chicken = [
  Ingredient("chicken-tenderloins", 500, INGREDIENT_CAT.MEAT),
  Ingredient("cornflour", 2, INGREDIENT_CAT.OTHER),
  Ingredient("garlic", 4, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("honey", 110, INGREDIENT_CAT.OTHER),
  Ingredient("chicken-stock", 0.5, INGREDIENT_CAT.OTHER),
  Ingredient("rice-vinegar", 1, INGREDIENT_CAT.OTHER),
  Ingredient("light-soy-sauce", 1, INGREDIENT_CAT.OTHER),
  Ingredient("white-rice", 500, INGREDIENT_CAT.OTHER),
  Ingredient("brocolli", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("carrot", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("green-beans", 200, INGREDIENT_CAT.FRUIT_VEG),
]

hot_breakfast = [
  Ingredient("cannellini-beans", 2, INGREDIENT_CAT.OTHER),
  Ingredient("tin-tomatoes", 2, INGREDIENT_CAT.OTHER),
  Ingredient("dark-brown-sugar", 2, INGREDIENT_CAT.OTHER),
  Ingredient("egg", 12, INGREDIENT_CAT.DAIRY),
  Ingredient("avocado", 2, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("mushrooms", 500, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("red-wine-vinegar", 100, INGREDIENT_CAT.OTHER),
  Ingredient("tomato-paste", 2, INGREDIENT_CAT.OTHER),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
  Ingredient("thyme", 0.5, INGREDIENT_CAT.CONDIMENT),
  Ingredient("smoked-paprika", 0.5, INGREDIENT_CAT.CONDIMENT),
  Ingredient("chilli-flakes", 0.5, INGREDIENT_CAT.CONDIMENT),
  Ingredient("bread", 1, INGREDIENT_CAT.OTHER),
]

chicken_schnitzel = []
sausages_and_mash = []
burrito = []
burger = []
pizza = []
chilli_con_carne = []
beef_and_ale_casserole = []
chicken_tikka_masala = []
black_pepper_tofu = []

global_recipes = [
  # stir fry
  black_pepper_beef, mee_goreng, beef_chow_fun, black_pepper_tofu, kung_pao_chicken,
  # curry
  chicken_tikka_masala, butter_chicken,
  # stew
  meatball_pasta_bake, chicken_paprikash, cottage_pie, beef_stroganoff, fettucine_bolognese, tuscan_chicken, beef_and_ale_casserole, chilli_con_carne, chicken_pie, honey_garlic_chicken,
  # sandwich
  kofta, burrito, burger, pizza,
  # other
  chicken_schnitzel, sausages_and_mash,
]

def recipes():
  global global_ingredients
  global global_recipes

  ingredients = {}

  recipes_list = [hot_breakfast, kung_pao_chicken]
  for recipe in recipes_list:
    for ingredient in recipe:
      if ingredients.get(ingredient.name, None) is not None:
        ingredients[ingredient.name].amount += ingredient.amount
      else:
        ingredients[ingredient.name] = ingredient

  for ingredient in global_ingredients:
    ingredients[ingredient.name] = ingredient 

  sorted_ingredients = dict(sorted(ingredients.items(), key=lambda i: i[1].category.name))

  want_to_print = True
  if want_to_print:
    print_output = open("recipes.md", "w")
  else:
    print_output = sys.stdout


  cur_category = ""
  for ingredient_name, ingredient in sorted_ingredients.items():
    category = ingredient.category
    if cur_category != category:
      cur_category = category
      print(f"\n**{cur_category.name.replace('', '').upper()}**:", file=print_output)
    print(f"{ingredient_name} ({ingredient.amount}), ", file=print_output)


  # NOTE(Ryan): To inform bash script to create pdf and open it
  if want_to_print:
    print("to-print")

if __name__ == "__main__":
  recipes()
