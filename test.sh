# EXAMPLES

## Login - get token
resp=`curl -X POST http://localhost:5000/api/login -H 'Content-Type: application/json'   -d '{"username":"admin","password":"admin"}'`

token=`echo $resp | jq -r .access_token`

echo $token

## Test that your token is valid
curl http://localhost:5000/api/test -H "Authorization: Bearer $token"

## Add a contact
curl -X POST http://localhost:5000/api/add_contact -H 'Content-Type: application/json' -H "Authorization: Bearer $token"   -d '{"telegram_id":"1523881017"}'

## Send a notification
curl -X POST http://localhost:5000/api/send_notification -H 'Content-Type: application/json' -H "Authorization: Bearer $token"   -d '{"message":"<h1>📨 IT WORKS 📨</h1>"}'

# TELEGRAM EXAMPLE
. .env
curl -X POST \
     -H 'Content-Type: application/json' \
     -d '{"chat_id": "@mk_dev", "text": "This is a test from curl", "disable_notification": true}' \
     https://api.telegram.org/bot$TOKEN/sendMessage

