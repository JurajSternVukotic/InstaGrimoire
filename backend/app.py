from flask import Flask, request, jsonify
from model import Spell, School, CastingTimeUnit, RangeUnit, connect
from add_spell import add_spell
from get_spell import get_spell
from delete_spell import delete_spell
from update_spell import update_spell
from pony.orm import db_session, select


app = Flask(__name__)
connect()

@app.route('/spell', methods=['POST'])
def add_spell_route():
    data = request.get_json()
    spell = add_spell(data)
    return jsonify(spell), 201

@app.route('/spell/<name>', methods=['GET'])
def get_spell_route(name):
    spell = get_spell(name)
    return jsonify(spell), 200

@app.route('/spells', methods=['GET'])
@db_session
def get_all_spells():
    spells = select(s for s in Spell)[:]
    spell_dicts = [s.to_dict() for s in spells]
    return jsonify(spell_dicts), 200

@app.route('/spell/<name>', methods=['DELETE'])
def delete_spell_route(name):
    delete_spell(name)
    return '', 204

@app.route('/spell/<name>', methods=['PUT'])
def update_spell_route(name):
    data = request.get_json()
    update_spell(name, data)
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
