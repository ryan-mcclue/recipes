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

# 
# 
# beef_chow_fun = [
#   Ingredient("light-soy-sauce", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("dark-soy-sauce", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("oyster-sauce", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("sesame-oil", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("brown-sugar", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("rice-vinegar", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("ginger", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("garlic", 3, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("white-pepper", 0.25, INGREDIENT_CAT.CONDIMENT),
#   Ingredient("flank-steak", 500, INGREDIENT_CAT.MEAT),
#   Ingredient("thin-rice-noodles", 200, INGREDIENT_CAT.OTHER),
#   Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("yellow-capsicum", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("bean-sprouts", 200, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("spring-onions", 4, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("baby-spinach", 60, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("red-chilli", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("sesame-seeds", 1, INGREDIENT_CAT.OTHER),
# ]
# 
# 
# chicken_pie = [
#   Ingredient("puff-pastry", 2, "frozen"),
#   Ingredient("chicken-breast", 500, INGREDIENT_CAT.MEAT),
#   Ingredient("carrot", 3, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("potato", 3, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("fresh-thyme", 2, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("plain-flour", 6, INGREDIENT_CAT.OTHER),
#   Ingredient("milk", 300, INGREDIENT_CAT.DAIRY),
#   Ingredient("egg", 1, INGREDIENT_CAT.DAIRY),
#   Ingredient("lemon-juice", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("brocolli", 1, INGREDIENT_CAT.FRUIT_VEG),
# ]
# 
# beef_stroganoff = [
#   Ingredient("fillet-steak", 600, INGREDIENT_CAT.MEAT),
#   Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("mushroom", 300, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("plain-flour", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("beef-stock", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("dijon-mustard", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("sour-cream", 150, INGREDIENT_CAT.DAIRY),
#   Ingredient("penne-pasta", 500, INGREDIENT_CAT.OTHER),
#   Ingredient("fresh-chives", 1, INGREDIENT_CAT.FRUIT_VEG),
# ]  
# 
# 
# chicken_paprikash = [
#   Ingredient("brown-onion", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("garlic", 2, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("tin-tomatoes", 400, INGREDIENT_CAT.OTHER),
#   Ingredient("celery", 2, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("chicken-breast", 500, INGREDIENT_CAT.MEAT),
#   Ingredient("plain-flour", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("sweet-paprika", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("chicken-stock", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("sour-cream", 225, INGREDIENT_CAT.DAIRY),
#   Ingredient("fussili-pasta", 500, INGREDIENT_CAT.OTHER),
# ]
# 
# mee_goreng = [
#   Ingredient("shallot", 2, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("mushroom", 5, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("garlic", 2, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("white-cabbage", 0.5, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("chicken-breast", 500, INGREDIENT_CAT.MEAT),
#   Ingredient("thick-egg-noodles", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("bean-sprouts", 150, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("spring-onion", 6, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("red-chilli", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("sweet-soy-sauce", 4, INGREDIENT_CAT.OTHER),
#   Ingredient("dark-soy-sauce", 3, INGREDIENT_CAT.OTHER),
#   Ingredient("oyster-sauce", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("sweet-chilli-sauce", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("white-pepper", 0.25, INGREDIENT_CAT.OTHER),
# ]  
# 
# black_pepper_beef = [
#   Ingredient("black-peppercorns", 10, INGREDIENT_CAT.OTHER),
#   Ingredient("sirloin", 450, INGREDIENT_CAT.MEAT),
#   Ingredient("sesame-oil", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("brown-onion", 2, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("red-capsicum", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("green-capsicum", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("cornflour", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("dark-soy-sauce", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("oyster-sauce", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("red-chilli", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("chinese-cooking-wine", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("beef-stock", 0.5, INGREDIENT_CAT.OTHER),
#   Ingredient("garlic", 2, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("ginger", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("white-rice", 500, INGREDIENT_CAT.OTHER),
# ]
# 
# meatball_pasta_bake = [
#   Ingredient("beef-mince", 500, INGREDIENT_CAT.MEAT),
#   Ingredient("shallot", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("garlic", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("breadcrumbs", 60, INGREDIENT_CAT.OTHER),
#   Ingredient("egg", 1, INGREDIENT_CAT.DAIRY),
#   Ingredient("italian-herbs", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("tin-tomatoes", 400, INGREDIENT_CAT.OTHER),
#   Ingredient("beef-stock", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("worcestershire-sauce", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("smoked-paprika", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("cheddar-cheese", 40, INGREDIENT_CAT.DAIRY),
#   Ingredient("mozarella-cheese", 30, INGREDIENT_CAT.DAIRY),
#   Ingredient("rigatoni-pasta", 500, INGREDIENT_CAT.OTHER),
# ]
# 
# 
# honey_garlic_chicken = [
#   Ingredient("chicken-tenderloins", 500, INGREDIENT_CAT.MEAT),
#   Ingredient("cornflour", 2, INGREDIENT_CAT.OTHER),
#   Ingredient("garlic", 4, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("honey", 110, INGREDIENT_CAT.OTHER),
#   Ingredient("chicken-stock", 0.5, INGREDIENT_CAT.OTHER),
#   Ingredient("rice-vinegar", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("light-soy-sauce", 1, INGREDIENT_CAT.OTHER),
#   Ingredient("white-rice", 500, INGREDIENT_CAT.OTHER),
#   Ingredient("brocolli", 1, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("carrot", 2, INGREDIENT_CAT.FRUIT_VEG),
#   Ingredient("green-beans", 200, INGREDIENT_CAT.FRUIT_VEG),
# ]
# 

# stir fry
  # CHICKEN
    # kung pao
    # teriyaki
  # BEEF
    # honey vinegar beef
    # korean beef
# curry
  # CHICKEN
    # thai green
    # butter chicken
    # https://twosleevers.com/instant-pot-japanese-chicken-curry/
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
    # adobo https://twosleevers.com/instant-pot-chicken-adobo/
  # BEEF
    # beef nachos (jalapenos)
    # cottage pie
    # https://twosleevers.com/ethiopian-beef-stew/
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
    # beef noodle
    # spanish chorizo
    # beef udon: https://www.youtube.com/watch?v=wS0FDrkKY2I&list=PLvF-uMjWdYl0kcFqrGYtIUTHpyVAEsaLi 
    # https://twosleevers.com/russian-borscht/
# stew
  # CHICKEN
    # https://twosleevers.com/jamaican-chicken-curry/
    # https://twosleevers.com/ethiopian-chicken-stew/
  # BEEF
    # https://twosleevers.com/easy-beef-daube/
    #   https://twosleevers.com/hungarian-goulash/
    # lamb tagine: https://www.youtube.com/watch?v=jkWbi4-aH8w
# pizza


def r():
  global global_ingredients

  ingredients = {}

  # IMPORTANT(Ryan): curry (chapati, naan), pasta (garlic bread)
  # for max. juiciness, seems to sear whole breast then bake. then slice lengthways and tear

  # chicken-soup: https://www.youtube.com/watch?v=MxAqHuPPjUs
  # dumpling soup?

  recipes_list = [laksa.recipe, pesto_chicken.recipe, honey_vinegar_beef.recipe]

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
  r()
