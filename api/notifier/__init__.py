from flask import Blueprint
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


notifier_blueprint = Blueprint(
    'notifier_blueprint',
    __name__,
    url_prefix='/api',
)
