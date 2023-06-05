from pony.orm import db_session
from model import Spell, connect
#connect()

def get_spell(spell_name):
    with db_session:
        spell = Spell.get(name=spell_name)
        if spell is not None:
            print(f"Name: {spell.name}")
            print(f"Level: {spell.level}")
            print(f"School: {spell.school}")
            print(f"Casting Time Value: {spell.casting_time_value}")
            print(f"Casting Time Unit: {spell.casting_time_unit}")
            print(f"Range Value: {spell.range_value}")
            print(f"Range Unit: {spell.range_unit}")
            print(f"Component V: {spell.component_v}")
            print(f"Component S: {spell.component_s}")
            print(f"Component M: {spell.component_m}")
            print(f"Description: {spell.description}")
            print(f"Upcast: {spell.upcast}")
            print(f"Classes: {spell.classes}")
            print(f"Sourcebook: {spell.source_book}")
        else:
            print(f"No spell found with name {spell_name}")


if __name__ == "__main__":
    spell_name = "Magic Missile"
    get_spell(spell_name)
