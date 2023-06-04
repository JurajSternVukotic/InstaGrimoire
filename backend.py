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


@property 
def level(self):
    return self._level

@level.setter 
def level(self, value):
    if value < 0 or value > 9:
        raise ValueError("Mystra banned all spells over lvl 9 after the spell plague, and negative levels don't make sense")
    self._level = value 

@property
def school_enum(self):
    return School(self.school)

@school_enum.setter
def school_enum(self, value):
    if not isinstance(value, School):
        raise TypeError("Invalid magic school")
    self.school = value.value

@property
def casting_time_value(self):
    return self._casting_time_value

@casting_time_value.setter
def casting_time_value(self, value):
    if value < 0:
        raise ValueError("Can not cast in negative time!")
    self._casting_time_value = value 

@property
def casting_time_enum(self):
    return CastingTimeUnit(self.casting_time)

@casting_time_enum.setter
def casting_time_enum(self, value):
    if not isinstance(value, CastingTimeUnit):
        raise TypeError("Invalid casting time unit")
    self.casting_time = value.value

@property
def range_value(self):
    return self._range_value

@range_value.setter
def range_value(self, value):
    if value is not None and value < 0:
        raise ValueError("Range can not be negative")
    self._range_value = value

@property
def range_unit(self):
    return RangeUnit(self.range_unit)

@range_unit.setter
def school_enum(self, value):
    if not isinstance(value, RangeUnit):
        raise TypeError("Invalid range unit")
    self.range_unit = value.value


@property
def material_description(self):
    return self._material_description

@material_description.setter
def material_description(self, value):
    if self.component_m is False and value is not None:
        raise ValueError("Material description should be none when there is no material component")
    
db.bind(provider='sqlite', filename='spells.db', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    new_spell = Spell(
        name="Magic Missile",
        level=1,
        school="Evocation",
        casting_time_value=1,
        casting_time_unit="Action",
        range_value=120,
        range_unit="Feet",
        component_v=True,
        component_s=True,
        component_m=False,
        #material_description=,
        description="You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several.",
        upcast="When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart for each slot above 1st.",
        classes="Wizard",
    )

with db_session:
    spell = Spell.get(name="Magic Missile")
    print(spell.name, spell.level, spell.school, spell.description, spell.upcast)