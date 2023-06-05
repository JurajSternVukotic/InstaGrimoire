from pony.orm import db_session
from model import Spell, School, CastingTimeUnit, RangeUnit, connect

#connect()

def add_spell():
    new_spell = Spell(
        name = "Magic Missile",
        level = 1,
        school = School.EVOCATION.value,
        casting_time_value = 1,
        casting_time_unit = CastingTimeUnit.ACTION.value,
        range_value = 120,
        range_unit = RangeUnit.FEET.value,
        component_v = True,
        component_s = True,
        component_m = False,
        description = "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several.",
        upcast = "When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart for each slot above 1st.",
        classes = "Wizard"

    )

if __name__ == '__main__':
    with db_session:
        add_spell()