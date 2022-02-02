# telegram-notifier

Tool to send notification via Telegram to a list of contact (telegram ids) based on Flask

## Install requirements

    pip install -r requirements.txt

## .env file

The file have to contain this information :

    FLASK_ENV=development/production

    FLASK_KEY="random_string"
    JWT_KEY="random_string"

    TOKEN="telegram_token"


## Methods

### Login

Method : `POST`

Endpoint : `/api/login`

JSON : `{"username":"<user>","password":"<password>"}`

### Create user

Method : `POST`

Endpoint : `/api/create_user`

JSON : `{"username":"<user>","password":"<password>"}`

### Add contact 

Method : `POST`

Endpoint : `/api/add_contact`

JSON : `{"telegram_id": "<telegram_id_conversation>"}`

### Get the list of all the contacts

Method : `GET`

Endpoint : `/api/contacts`

### Delete a contact

Method : `POST`

Endpoint : `/api/delete_contact`

JSON : `{"id": "<db_id_contact>"}`

The ID to put is not the Telegram id of the conversation, but the internal ID in the DB

### Send notification to all the contacts

Method : `POST`

Endpoint : `/api/send_notification`

JSON : `{"message" : "Message to send to the contacts"}`

