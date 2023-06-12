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
from pony.orm import raw_sql





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


def apply_filters(query, filters):
    if 'id' in filters:
        query = query.filter(lambda s: s.id == int(filters['id']))
    if 'sourcebook' in filters and filters['sourcebook'].lower() != 'any':
        query = query.filter(lambda s: s.source_book.lower() == filters['sourcebook'].lower())  # change here
    if 'name' in filters:
        lower_case_name = filters['name'].lower()
        query = query.filter(lambda s: raw_sql(f"LOWER(s.name) LIKE '%{lower_case_name}%'"))
    if 'school' in filters and filters['school'].lower() != 'any':
        query = query.filter(lambda s: s.school.lower() == filters['school'].lower())  # change here
    if 'level' in filters and filters['level'].lower() != 'any':
        query = query.filter(lambda s: s.level == int(filters['level']))  # Assuming level is a number
    if 'casting_time_unit' in filters and filters['casting_time_unit'].lower() != 'any':
        query = query.filter(lambda s: s.casting_time_unit.lower() == filters['casting_time_unit'].lower())  # change here
    if 'range_unit' in filters and filters['range_unit'].lower() != 'any':
        query = query.filter(lambda s: s.range_unit.lower() == filters['range_unit'].lower())  # change here


    return query




@app.route('/spells', methods=['GET'])
@db_session
def get_all_spells():
    filters = request.args
    query = select(s for s in Spell)
    query = apply_filters(query, filters)
    spells = query[:]
    spell_dicts = [s.to_dict() for s in spells]
    return jsonify(spell_dicts), 200

@app.route('/sourcebooks', methods=['GET'])
@db_session
def get_all_sourcebooks():
    sourcebooks = list(select(s.source_book for s in Spell).distinct())
    return jsonify(sourcebooks), 200


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
