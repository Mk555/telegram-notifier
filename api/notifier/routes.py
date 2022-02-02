import logging

from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required

from api import db_api
from api.notifier import notifier_blueprint
from api.notifier.models import Contact, User
from api.notifier.login_utils import verify_pass
from api.notifier.telegram_utils import send_telegram_message

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

## Create user
@notifier_blueprint.route('/create_user', methods=["POST"])
@jwt_required()
def create_user():
    logging.info('👤 Create user')

    user = request.json.get("username", None)
    passwd = request.json.get("password", None)

    user = User(username=user, password=passwd)
    db_api.session.add(user)
    db_api.session.commit()

    return jsonify({"msg": "👤 User created"}), 200


##########################
# INIT
@notifier_blueprint.route('/init')
def init():
    logging.info('🌟 INITIALIZATION DATA')
    user = User(username='admin', password='admin')
    db_api.session.add(user)
    db_api.session.commit()

    return jsonify({"msg": "🌟 Init data successful"}), 200

##############
# CONTACT MGMT

## Add contact
@notifier_blueprint.route('/add_contact', methods=["POST"])
@jwt_required()
def add_contact():
    logging.debug('📇 Creating new contact')

    id_telegram = request.json.get("telegram_id", None)
    contact = Contact(telegram_id=id_telegram)

    db_api.session.add(contact)
    db_api.session.commit()

    return jsonify({"msg": "📇 Contact created successfully"}), 200

## Get all contacts
@notifier_blueprint.route('/contacts', methods=["GET"])
@jwt_required()
def get_contacts():
    logging.debug('📇 Get list contacts')

    contacts = Contact.query.all()

    list_contacts = []
    for contact in contacts:
        list_contacts.append({
            'id': contact.id, 
            'telegram_id': contact.telegram_id})

    return jsonify({"msg": "Success", "list_contacts": list_contacts}), 200

## Delete contact
@notifier_blueprint.route('/delete_contact', methods=["POST"])
@jwt_required()
def delete_contact():
    logging.debug('📇 Delete contact')

    id_contact = request.json.get("id", None)

    Contact.query.filter_by(id=id_contact).delete()
    db_api.session.commit()

    return jsonify({"msg": "Success"}), 200


##########
# NOTIFIER

## Send notification to all contacts
@notifier_blueprint.route('/send_notification', methods=["POST"])
@jwt_required()
def sent_notification():
    logging.debug('📨 Sending notification')

    message = request.json.get("message", None)

    contacts = Contact.query.all()
    for contact in contacts:
        send_telegram_message(contact, message)

    return jsonify({"msg": '📨 Message sent !'}), 200
