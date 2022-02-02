import requests, logging
from app import TELEGRAM_KEY

def send_telegram_message(id_conversation, message):
    
    telegram_endpoint = 'https://api.telegram.org/bot' + TELEGRAM_KEY + '/sendMessage'
    logging.info(telegram_endpoint)
    data = {"chat_id": id_conversation, "text": message}

    result = requests.post(telegram_endpoint, data = data)

    result_json = result.json()
    if (result_json['ok']):
        logging.debug('📨 Message sent successfully')
    else:
        logging.error('Error when sending the message')
        logging.error(result.text)

