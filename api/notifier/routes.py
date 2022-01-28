import logging
from flask import jsonify, request
from flask_jwt_extended import jwt_required
#from telegram import Contact
from api.notifier.models import Contact

from api import db_api
from api.notifier import notifier_blueprint

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

    