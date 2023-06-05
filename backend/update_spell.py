from pony.orm import db_session
from model import Spell, connect

#connect()

def update_spell(spell_name, updates):
    with db_session:
        spell = Spell.get(name=spell_name)
        if spell:
            for attribute, new_value in updates.items():
                if hasattr(spell, attribute):
                    setattr(spell, attribute, new_value)
                else:
                    print(f"Spell does not have the attribute: {attribute}")
        else:
            print(f"No spell found with the name: {spell_name}")

if __name__ == '__main__':
    spell_name = "Magic Missile" 
    updates = {"level": 2, "classes": "Wizard,Sorcerer"}  
    update_spell(spell_name, updates)
