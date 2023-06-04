from enum import Enum
from typing import Required
from pony.orm import *

db = Database()

class School(Enum):
    ABJURATION = "Abjuration"
    CONJURATION = "Conjuration"
    DIVINATION = "Divination"
    ENCHANTMENT = "Enchantment"
    EVOCATION = "Evocation"
    ILLUSION = "Illusion"
    NECROMANCY = "Necromancy"
    TRANSMUTATION = "Transmutation"

class CastingTimeUnit(Enum):
    ACTION = "Action"
    BONUS_ACTION = "Bonus Action"
    REACTION = "Reaction"
    SPECIAL = "Special"
    MINUTE = "Minute"
    HOUR = "Hour"

class RangeUnit(Enum):
    FEET = "Feet"
    MILES = "Miles"
    SELF = "Self"
    TOUCH = "Touch"
    UNLIMITED = "Unlimited"
    SPECIAL = "Special"



class Spell(db.Entity):
    id = PrimaryKey(int, auto = True)
    name = Required(str)
    level = Required(int)
    school = Required(School)
    casting_time_value = Required(int)
    casting_time_unit = Required(CastingTimeUnit)
    range_value = Optional(int)
    range_unit = Required(RangeUnit)
    component_v = Required(bool)
    component_s = Required(bool)
    component_m = Required(bool)
    material_description = Optional(str)
    description = Required(str)
    classes = Required(str) # Zbog restrikcije na samo jednu klasu u databaseu, ne mogu zadrzati atomarnost podataka te ce lista klasa biti string poput: "Sorcerer, Warlock, Wizard" pa cu rasclanjivati string za search


@property 
def level(self):
    return self._level

@level.setter 
def level(self, value):
    if value < 0 or value > 9:
        raise ValueError("Mystra banned all spells over lvl 9 after the spell plague, and negative levels don't make sense")
    self._level = value 

@property
def casting_time_value(self):
    return self._casting_time_value

@casting_time_value.setter
def casting_time_value(self, value):
    if value < 0:
        raise ValueError("Can not cast in negative time!")
    self._casting_time_value = value 

@property
def range_value(self):
    return self._range_value

@range_value.setter
def range_value(self, value):
    if value is not None and value < 0:
        raise ValueError("Range can not be negative")
    self._range_value = value

@property
def material_description(self):
    return self._material_description

@material_description.setter
def material_description(self, value):
    if self.component_m is False and value is not None:
        raise ValueError("Material description should be none when there is no material component")