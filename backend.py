from enum import Enum
from typing import Required
from pony.orn import *

db = Database()

class Spell(db.Entity):
    id = PrimaryKey(int, auto = True)
    name = Required(str)
    level = Required(int)
    school = Required(Enum)
    casting_time = Requierd(Enum)
    range = Required(str)
    range = Required(int)
    components = Required(str)
    description = Required(str)
    classes = Required(str)

