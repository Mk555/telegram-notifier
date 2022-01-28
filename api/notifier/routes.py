import logging

from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

from api import db_api
from api.notifier import notifier_blueprint
from api.notifier.models import Contact, User
from api.notifier.login_utils import verify_pass

##########
# LOGIN

@notifier_blueprint.route("/login", methods=["POST"])
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
@notifier_blueprint.route('/init')
def init():
    logging.info('🌟 INITIALIZATION DATA')
    user = User(username='admin', password='admin')
    db_api.session.add(user)
    db_api.session.commit()

    return jsonify({"msg": "Init data successful"}), 200

##########
# NOTIFIER
@notifier_blueprint.route('/test')
@jwt_required()
def test():
    logging.debug('🚀 Message received captain !')
    return jsonify({"msg": '🚀 Message received captain !'}), 200

@notifier_blueprint.route('/add_contact', methods=["POST"])
@jwt_required()
def add_contact():
    logging.debug('Creating new contact')

    id_telegram = request.json.get("telegram_id", None)
    contact = Contact(telegram_id=id_telegram)

    db_api.sesion.add(contact)
    db_api.session.commit()

    return jsonify({"msg": "Contact created successfully"}), 200

@notifier_blueprint.route('/send_notification', methods=["POST"])
@jwt_required()
def sent_notification():
    logging.debug('Sending notification')

    message = request.json.get("message", None)
    logging.debug(message)

    return jsonify({"msg": 'Message sent !'}), 200
    

@notifier_blueprint.route('/create_poll')
def create_poll():
    logging.debug('🗳️ Creating poll')
    return jsonify({"msg": '🗳️ Creating poll'}), 200

    