from pony.orm import db_session
from model import Spell, connect

connect()

def delete_spell(spell_name):
    with db_session:
        spell = Spell.get(name=spell_name)
        if spell:
            spell.delete()
        else:
            print(f"No spell found with the name: {spell_name}")


if __name__ == '__main__':
    spell_name = "Magic Missile" 
    delete_spell(spell_name)
