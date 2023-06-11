from pony.orm import db_session
from model import Spell, connect
#connect()

def get_spell(spell_name):
    with db_session:
        spell = Spell.get(name=spell_name)
        if spell is not None:
            return {
                "name": spell.name,
                "level": spell.level,
                "school": spell.school,
                "casting_time_value": spell.casting_time_value,
                "casting_time_unit": spell.casting_time_unit,
                "range_value": spell.range_value,
                "range_unit": spell.range_unit,
                "component_v": spell.component_v,
                "component_s": spell.component_s,
                "component_m": spell.component_m,
                "description": spell.description,
                "upcast": spell.upcast,
                "classes": spell.classes,
                "source_book": spell.source_book
            }
        else:
            return None  


if __name__ == "__main__":
    spell_name = "Magic Missile"
    get_spell(spell_name)
