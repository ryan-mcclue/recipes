#!/usr/bin/python3
# SPDX-License-Identifier: zlib-acknowledgement

from recipes import *

global_ingredients = [
  common.Ingredient("butter", 1, common.INGREDIENT_CAT.DAIRY), 
  common.Ingredient("olive-oil", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("wool-wash", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("peanut-oil", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("cracked-salt", 1, common.INGREDIENT_CAT.CONDIMENT),
  common.Ingredient("cracked-black-pepper", 1, common.INGREDIENT_CAT.CONDIMENT),
  common.Ingredient("white-pepper", 1, common.INGREDIENT_CAT.CONDIMENT),
  common.Ingredient("ground-salt", 1, common.INGREDIENT_CAT.CONDIMENT),
  common.Ingredient("ground-pepper", 1, common.INGREDIENT_CAT.CONDIMENT),
  common.Ingredient("hummus", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("peanut-butter", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("cheese-sticks", 1, common.INGREDIENT_CAT.DAIRY),
  common.Ingredient("fava-beans", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("dates", 1, common.INGREDIENT_CAT.FRUIT_VEG),
  common.Ingredient("apples", 1, common.INGREDIENT_CAT.FRUIT_VEG),
  common.Ingredient("bananas", 1, common.INGREDIENT_CAT.FRUIT_VEG),
  common.Ingredient("carrots", 1, common.INGREDIENT_CAT.FRUIT_VEG),
  common.Ingredient("dark-chocolate", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("cling-wrap", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("alfoil", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("vita-wheats", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("corn-chips", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("rolled-oats", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("yogurt", 1, common.INGREDIENT_CAT.DAIRY),
  common.Ingredient("frozen-berries", 1, common.INGREDIENT_CAT.FROZEN),
  common.Ingredient("ice-cream", 1, common.INGREDIENT_CAT.FROZEN),
  common.Ingredient("mixed-nuts", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("cinnamon", 1, common.INGREDIENT_CAT.CONDIMENT),
  common.Ingredient("coconut-flakes", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("seeds", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("honey", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("juice", 1, common.INGREDIENT_CAT.DAIRY),
  common.Ingredient("kale", 1, common.INGREDIENT_CAT.FRUIT_VEG),
  common.Ingredient("milk", 1, common.INGREDIENT_CAT.DAIRY),
  common.Ingredient("paper-towels", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("tissues", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("toilet-paper", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("toilet-cleaner", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("deoderant", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("toothpaste", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("dental-floss", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("sunscreen", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("panadol", 1, common.INGREDIENT_CAT.MEDICINAL),
  common.Ingredient("nurofen", 1, common.INGREDIENT_CAT.MEDICINAL),
  common.Ingredient("demazin", 1, common.INGREDIENT_CAT.MEDICINAL),
  common.Ingredient("sponge", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("bar-soap", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("soap", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("stove-cleaner", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("bin-bags", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("compost-bags", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("dishwasher-tablets", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("detergent", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("glen-20", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("betadine", 1, common.INGREDIENT_CAT.MEDICINAL),
  common.Ingredient("band-aids", 1, common.INGREDIENT_CAT.MEDICINAL),
  common.Ingredient("cotton-balls", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("shampoo/conditioner", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("cleanser", 1, common.INGREDIENT_CAT.TOILETRIES),
  common.Ingredient("sudafed", 1, common.INGREDIENT_CAT.MEDICINAL),
  common.Ingredient("strepsils", 1, common.INGREDIENT_CAT.MEDICINAL),
  common.Ingredient("eucalyptus", 1, common.INGREDIENT_CAT.MEDICINAL),
  common.Ingredient("pino-clean", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("scourer", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("aa-batteries", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("aaa-batteries", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("lime", 1, common.INGREDIENT_CAT.FRUIT_VEG),
  common.Ingredient("orange", 1, common.INGREDIENT_CAT.FRUIT_VEG),
  common.Ingredient("lemon", 1, common.INGREDIENT_CAT.FRUIT_VEG),
  common.Ingredient("lemon-juice", 1, common.INGREDIENT_CAT.OTHER),
  common.Ingredient("lime-juice", 1, common.INGREDIENT_CAT.OTHER),
]

# stir fry
  # CHICKEN
    # kung pao
    # teriyaki
  # BEEF
    # honey vinegar beef
    # korean beef
  # PORK
    # mapo tofu
    # krad ka pow
# curry
  # CHICKEN
    # thai green
    # butter chicken
  # BEEF
    # rogan josh 
    # rendang 
# pasta
  # CHICKEN
    # pesto
    # stroganoff 
  # BEEF
    # bolognese
    # tomato meatballs
# meat and veg
  # CHICKEN
    # apricot
    # schnitzel
  # BEEF
    # beef nachos (jalapenos)
    # cottage pie
    # crying tiger steak
# wraps/sandwiches 
  # CHICKEN
    # fajita
    # tandoori
  # BEEF
    # kofta
    # burger
# soup/pastry
  # CHICKEN
    # ramen
    # laksa
    # tortellini
  # BEEF
    # beef udon: https://www.youtube.com/watch?v=wS0FDrkKY2I&list=PLvF-uMjWdYl0kcFqrGYtIUTHpyVAEsaLi 
    # taiwanese beef noodle
# stew
  # CHICKEN
    # https://twosleevers.com/jamaican-chicken-curry/
    # https://twosleevers.com/instant-pot-japanese-chicken-curry/ (use breast meat)
  # BEEF
    # https://twosleevers.com/hungarian-goulash/ (needs sour cream mixed in)
    # lamb tagine: https://www.youtube.com/watch?v=jkWbi4-aH8w
# pizza
# 
# barbeque
  # BEEF
    # skewer 
    # sirloin 
  # CHICKEN
    # skewer
    # chicken



def r():
  global global_ingredients

  ingredients = {}

  # IMPORTANT(Ryan): curry (chapati, naan), pasta (garlic bread)
  # for max. juiciness, seems to sear whole breast then bake. then slice lengthways and tear

  # chicken-soup: https://www.youtube.com/watch?v=MxAqHuPPjUs
  # dumpling soup?

  recipes_list = [rendang.recipe, pesto_chicken.recipe]

  for recipe in recipes_list:
    for ingredient in recipe:
      if ingredients.get(ingredient.name, None) is not None:
        ingredients[ingredient.name].amount += ingredient.amount
      else:
        ingredients[ingredient.name] = ingredient

  #for ingredient in global_ingredients:
  #  ingredients[ingredient.name] = ingredient 

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
  r()
