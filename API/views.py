from API import *
from flask import jsonify, request, json, make_response
from .modules import User


@app.route('/api/login', methods=["POST"])
def login():
    try:
        json_data = json.loads(request.data)
        username = json_data["USERNAME"]
        verdict = User.validate_username(username)
        if verdict:
            return make_response(verdict), 400
        password = json_data["PASSWORD"]
        return jsonify(STATUS='This is only a test', PASSWORD=password, USERNAME=username), 200

    except KeyError as error:
            return jsonify(CAUSE="Variable " + str(error.args[0]) + " does not exists in the submitted data"), 400


@app.route('/api/logout', methods=["POST"])
def logout():
    try:
        json_data = json.loads(request.data)
        session_id = json_data["SESSION-ID"]
        return jsonify(STATUS='User ' + session_id + ' Successfully logout '), 200
    except KeyError as error:
            return jsonify(CAUSE="Can't find variable " + str(error.args[0]) + " in the submitted data"), 400
