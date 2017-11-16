from flask import jsonify
from configuration import Username_Policies
import re


class User(object):

    username = None
    password = None
    session_id = None

    def __init__(self,username):
        self.username = username

    @staticmethod
    def validate_username(username):
        reason = ""
        if len(username) <= 4 or len(username) > 15:
            reason = jsonify(Username=username, Reason=Username_Policies[0])
            return reason
        elif re.search('^[0-9].*', username):
                reason = jsonify(Username=username, Reason=Username_Policies[3])
                return reason
        elif re.search('[!@#$%^&*\(\)\[\]\{\}\"\,]', username):
                reason = jsonify(Username=username, Reason=[Username_Policies[1],Username_Policies[2]])
                return reason
        return None

    @staticmethod
    def generate_session_id(self):
        self.session_id = "DUMMY_SESSION_ID"

    def get_session_id(self):
        return self.session_id
