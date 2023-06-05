from pony.orm import db_session
from model import Spell, School, CastingTimeUnit, RangeUnit, connect

#connect()

def add_spell(spell_data):
    with db_session:
        new_spell = Spell(
            name = spell_data["name"],
            level = spell_data["level"],
            school = School[spell_data["school"].upper()].value,
            casting_time_value = spell_data["casting_time_value"],
            casting_time_unit = CastingTimeUnit[spell_data["casting_time_unit"].upper()].value,
            range_value = spell_data["range_value"],
            range_unit = RangeUnit[spell_data["range_unit"].upper()].value,
            component_v = spell_data["component_v"],
            component_s = spell_data["component_s"],
            component_m = spell_data["component_m"],
            description = spell_data["description"],
            upcast = spell_data["upcast"],
            classes = spell_data["classes"]
        )
        return new_spell.to_dict() # This will convert the created spell into a dictionary

if __name__ == '__main__':
    spell_data = {
        "name": "Magic Missile",
        "level": 1,
        "school": "Evocation",
        "casting_time_value": 1,
        "casting_time_unit": "Action",
        "range_value": 120,
        "range_unit": "Feet",
        "component_v": True,
        "component_s": True,
        "component_m": False,
        "description": "You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target. The darts all strike simultaneously, and you can direct them to hit one creature or several.",
        "upcast": "When you cast this spell using a spell slot of 2nd level or higher, the spell creates one more dart for each slot above 1st.",
        "classes": "Wizard"
    }
    print(add_spell(spell_data))
