#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

import sys

from dataclasses import dataclass
from enum import Enum, auto
from typing import List

class INGREDIENT_CAT(Enum):
  INGREDIENT_CAT_DAIRY = 0
  INGREDIENT_CAT_FRUIT_VEG = auto(),
  INGREDIENT_CAT_FROZEN = auto(),
  INGREDIENT_CAT_TOILETRIES = auto(),
  INGREDIENT_CAT_MEDICINAL = auto(),
  INGREDIENT_CAT_CONDIMENT = auto(),
  INGREDIENT_CAT_MEAT = auto(),
  INGREDIENT_CAT_CANNED = auto(),
  INGREDIENT_CAT_ALCOHOL = auto(),
  INGREDIENT_CAT_OTHER = auto()

@dataclass
class Ingredient:
  name: str
  amount: float
  category: INGREDIENT_CAT

global_ingredients = [
  Ingredient("butter", 1, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY), 
  Ingredient("olive-oil", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("salt", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("pepper", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("hummus", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("peanut-butter", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("cheese-sticks", 1, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("fava-beans", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("dates", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("apples", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("bananas", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("carrots", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("dark-chocolate", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("vita-wheats", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("corn-chips", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("rolled-oats", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("yogurt", 1, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("frozen-berries", 1, INGREDIENT_CAT.INGREDIENT_CAT_FROZEN),
  Ingredient("ice-cream", 1, INGREDIENT_CAT.INGREDIENT_CAT_FROZEN),
  Ingredient("mixed-nuts", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("cinnamon", 1, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("coconut-flakes", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("seeds", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("honey", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("juice", 1, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("kale", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("milk", 1, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("paper-towels", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("tissues", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("toilet-paper", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("deoderant", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("toothpaste", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("dental-floss", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("sunscreen", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("panadol", 1, INGREDIENT_CAT.INGREDIENT_CAT_MEDICINAL),
  Ingredient("nurofen", 1, INGREDIENT_CAT.INGREDIENT_CAT_MEDICINAL),
  Ingredient("demazin", 1, INGREDIENT_CAT.INGREDIENT_CAT_MEDICINAL),
  Ingredient("sponge", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("bar-soap", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("soap", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("stove-cleaner", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("bin-bags", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("compost-bags", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("dishwasher-tablets", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("detergent", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("glen-20", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("betadine", 1, INGREDIENT_CAT.INGREDIENT_CAT_MEDICINAL),
  Ingredient("band-aids", 1, INGREDIENT_CAT.INGREDIENT_CAT_MEDICINAL),
  Ingredient("cotton-balls", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("shampoo/conditioner", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("cleanser", 1, INGREDIENT_CAT.INGREDIENT_CAT_TOILETRIES),
  Ingredient("sudafed", 1, INGREDIENT_CAT.INGREDIENT_CAT_MEDICINAL),
  Ingredient("strepsils", 1, INGREDIENT_CAT.INGREDIENT_CAT_MEDICINAL),
  Ingredient("eucalyptus", 1, INGREDIENT_CAT.INGREDIENT_CAT_MEDICINAL),
  Ingredient("pino-clean", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("scourer", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("cannellini-beans", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("tin-tomatoes", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("dark-brown-sugar", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("egg", 12, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("avocado", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("mushrooms", 500, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("red-wine-vinegar", 100, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("tomato-paste", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("thyme/smoked-paprika/chilli-flakes", 1, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("bread", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]

tuscan_chicken = [
  Ingredient("chicken-breast", 700, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("egg", 1, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("oregano", 1, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("thyme", 0.5, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("paprika", 1.5, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("garlic-salt", 0.25, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("plain-flour", 3, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("garlic", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("sun-dried-tomatoes", 150, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("red-capsicum", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("tomato-paste", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("white-wine", 90, INGREDIENT_CAT.INGREDIENT_CAT_ALCOHOL),
  Ingredient("chicken-stock", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("double-cream", 90, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("parmesan-cheese", 0.5, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("baby-spinach", 120, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("fresh-parsley", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("fussili-pasta", 500, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]

fettucine_bolognese = [
  Ingredient("beef-mince", 500, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("fettucine-pasta", 500, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("celery", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("carrot", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("pancetta", 150, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("red-wine", 200, INGREDIENT_CAT.INGREDIENT_CAT_ALCOHOL),
  Ingredient("tomato-paste", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("passata", 200, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("chicken-stock", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]

beef_chow_fun = [
  Ingredient("light-soy-sauce", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("dark-soy-sauce", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("oyster-sauce", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("sesame-oil", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("brown-sugar", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("rice-vinegar", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("ginger", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("garlic", 3, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("white-pepper", 0.25, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("flank-steak", 500, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("thin-rice-noodles", 200, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("yellow-capsicum", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("bean-sprouts", 200, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("spring-onions", 4, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("baby-spinach", 60, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("red-chilli", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("sesame-seeds", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]

butter_chicken = [
  Ingredient("chicken-breast", 700, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("natural-yogurt", 80, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("lemon-juice", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("garlic", 5, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("garam-masala", 2.5, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("coriander", 1, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("paprika", 2, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("chilli-powder", 1, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("ginger", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("curry-powder", 1, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("cinnamon", 0.5, INGREDIENT_CAT.INGREDIENT_CAT_CONDIMENT),
  Ingredient("chicken-stock", 0.5, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("passata", 400, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("tomato-paste", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("cardamom-pods", 6, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("double-cream", 175, "diary"),
  Ingredient("fresh-coriander", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("white-rice", 500, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]

chicken_pie = [
  Ingredient("puff-pastry", 2, "frozen"),
  Ingredient("chicken-breast", 500, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("carrot", 3, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("potato", 3, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("fresh-thyme", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("plain-flour", 6, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("milk", 300, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("egg", 1, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("lemon-juice", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("brocolli", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
]

beef_stroganoff = [
  Ingredient("fillet-steak", 600, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("mushroom", 300, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("plain-flour", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("beef-stock", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("dijon-mustard", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("sour-cream", 150, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("penne-pasta", 500, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("fresh-chives", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
]  

kung_pao_chicken = [
  Ingredient("rice-wine", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("white-pepper", 0.25, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("dark-soy-sauce", 5, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("hoisin-sauce", 4, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("sesame-oil", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("garlic", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("ginger", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("chicken-breast", 500, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("corn-flour", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("red-chilli", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("red-capsicum", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("zucchini", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("spring-onion", 12, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("cashew", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("white-rice", 500, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]  

cottage_pie = [
  Ingredient("brown-onion", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("celery", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("carrot", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("green-beans", 200, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("beef-mince", 900, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("worcestershire-sauce", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("beef-stock", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("potato", 1800, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("heavy-cream", 120, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("corn-flour", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]

chicken_paprikash = [
  Ingredient("brown-onion", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("garlic", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("tin-tomatoes", 400, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("celery", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("chicken-breast", 500, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("plain-flour", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("sweet-paprika", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("chicken-stock", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("sour-cream", 225, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("fussili-pasta", 500, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]

mee_goreng = [
  Ingredient("shallot", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("mushroom", 5, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("garlic", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("white-cabbage", 0.5, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("chicken-breast", 500, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("thick-egg-noodles", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("bean-sprouts", 150, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("spring-onion", 6, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("red-chilli", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("sweet-soy-sauce", 4, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("dark-soy-sauce", 3, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("oyster-sauce", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("sweet-chilli-sauce", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("white-pepper", 0.25, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]  

black_pepper_beef = [
  Ingredient("black-peppercorns", 10, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("sirloin", 450, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("sesame-oil", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("brown-onion", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("red-capsicum", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("green-capsicum", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("cornflour", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("dark-soy-sauce", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("oyster-sauce", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("red-chilli", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("chinese-cooking-wine", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("beef-stock", 0.5, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("garlic", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("ginger", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("white-rice", 500, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]

meatball_pasta_bake = [
  Ingredient("beef-mince", 500, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("shallot", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("garlic", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("breadcrumbs", 60, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("egg", 1, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("italian-herbs", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("tin-tomatoes", 400, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("beef-stock", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("worcestershire-sauce", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("smoked-paprika", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("cheddar-cheese", 40, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("mozarella-cheese", 30, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("rigatoni-pasta", 500, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]

kofta = [
  Ingredient("lamb-mince", 500, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("brown-onion", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("garlic", 3, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("fresh-mint", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("cumin", 3, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("coriander", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("chilli-flakes", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("cinnamon", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("flatbread", 4, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("cherry-tomatoes", 10, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("salad-mix", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("white-wine-vinegar", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("tzatiki", 1, INGREDIENT_CAT.INGREDIENT_CAT_DAIRY),
  Ingredient("skewers", 6, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
]  

honey_garlic_chicken = [
  Ingredient("chicken-tenderloins", 500, INGREDIENT_CAT.INGREDIENT_CAT_MEAT),
  Ingredient("cornflour", 2, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("garlic", 4, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("honey", 110, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("chicken-stock", 0.5, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("rice-vinegar", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("light-soy-sauce", 1, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("white-rice", 500, INGREDIENT_CAT.INGREDIENT_CAT_OTHER),
  Ingredient("brocolli", 1, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("carrot", 2, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
  Ingredient("green-beans", 200, INGREDIENT_CAT.INGREDIENT_CAT_FRUIT_VEG),
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

  recipes_list = [tuscan_chicken, kung_pao_chicken, fettucine_bolognese]
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
      print(f"\n**{cur_category.name.replace('INGREDIENT_CAT_', '').upper()}**:", file=print_output)
    print(f"{ingredient_name} ({ingredient.amount}), ", file=print_output)


  # NOTE(Ryan): To inform bash script to create pdf and open it
  if want_to_print:
    print("to-print")

if __name__ == "__main__":
  recipes()
