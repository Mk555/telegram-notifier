
import logging

from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

from api import db_api
from api.auth import blueprint
#from api.auth.models import User

## Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

@blueprint.route("/login", methods=["POST"])
def login():
    logging.info('Login')
    logging.info(request.json)
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if(username == 'test') and (password == 'test'):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Error during the login"}), 401



@blueprint.route('/test')
@jwt_required()
def test():
    logging.info('Message received captain !')
    return 'Message received captain !'



###########################
## TEST
#@blueprint.route('/init')
#def init():
#    logging.info('🌟 INITIALIZATION')
#    user = User(username='admin', password='admin')
#    db_api.session.add(user)
#    db_api.session.commit()
#
#
