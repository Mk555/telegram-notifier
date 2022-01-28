
import logging

from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

from api import db_api
from api.auth import blueprint
from api.auth.login_utils import verify_pass
from api.auth.models import User

## Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

@blueprint.route("/login", methods=["POST"])
def login():
    logging.debug('🔐 Login')
    
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = User.query.filter_by(username=username).first()

    if verify_pass(password, user.password):
        logging.debug('🔓 Login successful for : ' + username)
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        logging.error('🚨 Login error for : ' + username)
        return jsonify({"msg": "Error during the login"}), 401



##########################
# INIT
@blueprint.route('/init')
def init():
    logging.info('🌟 INITIALIZATION DATA')
    user = User(username='admin', password='admin')
    db_api.session.add(user)
    db_api.session.commit()

    return jsonify({"msg": "Init data successful"}), 200
