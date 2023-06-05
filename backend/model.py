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
    name = Required(str, unique = True)
    level = Required(int)
    school = Required(str)
    casting_time_value = Required(int)
    casting_time_unit = Required(str)
    range_value = Optional(int)
    range_unit = Required(str)
    component_v = Required(bool)
    component_s = Required(bool)
    component_m = Required(bool)
    material_description = Optional(str)
    description = Required(str)
    upcast = Optional(str)
    classes = Required(str) # Zbog restrikcije na samo jednu klasu u databaseu, ne mogu zadrzati atomarnost podataka te ce lista klasa biti string poput: "Sorcerer, Warlock, Wizard" pa cu rasclanjivati string za search
    source_book = Required(str)

    def set_level(self, value):
        if value < 0 or value > 9:
            raise ValueError("Mystra banned all spells over lvl 9 after the spell plague, and negative levels don't make sense")
        self.level = value

    def set_school(self, value):
        if not isinstance(value, School):
            raise TypeError("Invalid school of magic")
        self.school = value

    def set_casting_time_value(self, value):
        if value < 0:
            raise ValueError("Can not cast in negative time!")
        self.casting_time_value = value 

    def set_casting_time_unit(self, value):
        if not isinstance(value, CastingTimeUnit):
            raise ValueError("Casting time unit must be: Action, Bonus Action, Reaction, Special, Minute or Hour!")
        self.casting_time_unit = value 

    def set_range_value(self, value):
        if value < 0:
            raise ValueError("Range can not be!")
        self.range_value = value 

    def set_range_unit(self, value):
        if not isinstance(value, RangeUnit):
            TypeError("Invalid range unit!")
        self.range_unit = value 

    def set_material_description(self, value):
        if self.component_m is False and value is not None:
            raise ValueError("Material description should not exist if there is no material component")
        self.material_description = value
        
    def set_material_component(self, value):
        if self.material_description is None and value is True:
            raise ValueError("Must provide material component")
        self.component_m = value


def connect():
    db.bind(provider='sqlite', filename='spells.db', create_db=True)
    db.generate_mapping(create_tables=True)