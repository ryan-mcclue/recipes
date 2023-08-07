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
  instructions: str

# NOTE(Ryan): Ingredient
@dataclass
class I:
  name: str
  amount: float


# TODO(Ryan): Max-flow to ensure constraints, e.g. 2 beef, 2 pasta etc.
global_recipes = [
  R("tuscan-chicken", "chicken", "pasta", 1,
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
    """
    1. Heat the extra virgin olive oil and butter in a pan. Add the onion, celery, carrot and pancetta and sweat on a gentle heat for about 10 minutes until the onion has softened.
    2. Add the meat and brown all over.
    3. Increase the heat, add the wine and allow to evaporate.
    4. Dilute the tomato puree in a little of the stock and stir into the meat.
    5. Reduce the heat to low, cover with a lid and cook on a gentle heat for 2 hours, checking and adding a little extra stock from time to time to avoid the sauce from drying out.
    6. Remove from the heat and serve with freshly cooked tagliatelle.
    """
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
    """
    1. Mix light/dark/oyster soy sauce, sesame oil, brown sugar, rice vinegar, minced ginger, garlic cloves, Sriracha, white pepper in a bowl.
    2. Place the sliced beef in a second bowl and add one third of the marinade. Stir together and, cover and leave to marinate for 15-30 minutes. Cover the remaining sauce and put to one side.
    3. Meanwhile, cook the noodles according to pack instructions (usually boil for 5 mins), then drain in a colander and rinse in cold water until completely cold. Toss together with the 1 tsp of sesame oil and leave in the colander until needed.
    4. Heat 1 tbsp vegetable oil in a wok until smoking. Scoop out half of the beef from the bowl and fry on high for 2-3 minutes until just cooked. Remove from the wok and place in clean bowl, then repeat with the remaining beef.
    5. Add the remaining ½ tbsp oil to the wok and fry the onions for 2 minutes.
    6. Add in the yellow pepper and cook for 1 minute, then add in the reserved marinade/sauce and bring to the boil.
    7. Add in the noodles and beansprouts and cook for 3-4 minutes- tossing the noodles every so often (carefully so as not to break them) - until completely heated through.
    8. Add in the beef and cook for a further minute.
    9. At the last minute, stir in the spring onions (scallions) and spinach.
    10. Divide between four plates and serve topped with chilli slices and sesame seeds.
    """
    ),
  R("beef-massaman", "beef", "rice", 3,
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
    """
    1. Mix light/dark/oyster soy sauce, sesame oil, brown sugar, rice vinegar, minced ginger, garlic cloves, Sriracha, white pepper in a bowl.
    2. Place the sliced beef in a second bowl and add one third of the marinade. Stir together and, cover and leave to marinate for 15-30 minutes. Cover the remaining sauce and put to one side.
    3. Meanwhile, cook the noodles according to pack instructions (usually boil for 5 mins), then drain in a colander and rinse in cold water until completely cold. Toss together with the 1 tsp of sesame oil and leave in the colander until needed.
    4. Heat 1 tbsp vegetable oil in a wok until smoking. Scoop out half of the beef from the bowl and fry on high for 2-3 minutes until just cooked. Remove from the wok and place in clean bowl, then repeat with the remaining beef.
    5. Add the remaining ½ tbsp oil to the wok and fry the onions for 2 minutes.
    6. Add in the yellow pepper and cook for 1 minute, then add in the reserved marinade/sauce and bring to the boil.
    7. Add in the noodles and beansprouts and cook for 3-4 minutes- tossing the noodles every so often (carefully so as not to break them) - until completely heated through.
    8. Add in the beef and cook for a further minute.
    9. At the last minute, stir in the spring onions (scallions) and spinach.
    10. Divide between four plates and serve topped with chilli slices and sesame seeds.
    """
    ),

]

## 
# massaman
# chicken pie, butter chicken

# stroganoff, cottage pie, rendang
# paprikash, mee goreng (thin), kung pao


# black pepper beef, beef goulash, beef ragu, beef and guiness stew, lasagne, steak pie, chilli con-carne, spicy ginger beef stir fry
# chicken parmesan, chicken korma, chicken tikka masala, chicken madras, chicken marsala, honey garlic, honey lemon, szechuan chicken 

def recipes():
  global global_recipes

  names = ""
  ingredients = {}
  for recipe in global_recipes:
    names += (recipe.name + f"({recipe.duration}), ")
    for ingredient in recipe.ingredients:
      if ingredients.get(ingredient.name, None) is not None:
        ingredients[ingredient.name] += ingredient.amount
      else:
        ingredients[ingredient.name] = ingredient.amount

  # TODO(Ryan): Print assumptions: olive oil, butter, salt, pepper
  # TODO(Ryan): Print misc. like paper towels, toilet paper etc. 
  # TODO(Ryan): print snacks
  print(names[:-2])
  for name, amount in ingredients.items():
    print(f"* {name}: {amount}")

if __name__ == "__main__":
  recipes()
