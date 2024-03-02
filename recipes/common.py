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
