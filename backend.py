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
    components = Required(str)
    description = Required(str)
    classes = Required(str)


@property 
def level(self):
    return self._level

@level.setter 
def level(self, value):
    if value < 0 or value > 9:
        raise ValueError("Mystra banned all spells over lvl 9 after the spell plague, and negative levels don't make sense")
    self._levle = value 

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