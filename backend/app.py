from flask import Flask, request, jsonify
from flask_cors import CORS
from model import Spell, School, CastingTimeUnit, RangeUnit, connect
from add_spell import add_spell
from get_spell import get_spell
from delete_spell import delete_spell
from update_spell import update_spell
from pony.orm import db_session, select
from werkzeug.utils import secure_filename
import os
import json




app = Flask(__name__)
CORS(app)
connect()

@app.route('/spell', methods=['POST'])
def add_spell_route():
    data = request.get_json()
    spell = add_spell(data)
    return jsonify(spell), 201

@app.route('/spell/<name>', methods=['GET'])
def get_spell_route(name):
    spell = get_spell(name)
    if spell is not None:
        return jsonify(spell), 200
    else:
        return jsonify({"error": "No spell found with the provided name"}), 404


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

@app.route('/spell/<name>', methods=['PATCH'])
def update_spell_route(name):
    data = request.get_json()
    update_spell(name, data)
    return '', 200


@app.route('/upload-json', methods=['POST'])
def upload_json():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(os.getcwd(), filename)  
        file.save(filepath)

        with open(filepath, 'r') as f:
            spells = json.load(f)

        errors = []
        for spell_data in spells:
            with db_session:
                try:
                    add_spell(spell_data)
                except Exception as e:
                    errors.append({"spell": spell_data["name"], "error": str(e)})
        os.remove(filepath)

        if errors:
            return jsonify({"errors": errors}), 500

        return jsonify({"message": "Spells imported successfully"}), 201




if __name__ == '__main__':
    app.run(debug=True)
