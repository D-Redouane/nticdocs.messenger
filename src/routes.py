from flask import Blueprint, jsonify, request
from .functions import *

webhook_routes = Blueprint('webhook', __name__)

# bot = initialize_bot(TOKEN)

# Handle incoming messages
@webhook_routes.route('/webhook', methods=['POST'])
def handle_incoming_messages():
  data = request.get_json()
  if data["object"] == "page":
    for entry in data["entry"]:
      for messaging_event in entry["messaging"]:
        if messaging_event.get("message"):
          sender_id = messaging_event["sender"]["id"]
          message_text = messaging_event["message"]["text"]
          if message_text == "/start" or message_text == "/help":
            handle_start_help(bot, sender_id)
          elif message_text == "/list":
            # handle_list(bot, sender_id)
            handle_start_help(bot, sender_id)
          elif message_text == "/template":
            handle_template(bot, sender_id)
          elif message_text == "/button":
            handle_buttons(bot, sender_id)
          elif message_text == "/quickr":
            handle_quickr(bot, sender_id)
          elif message_text == "/list2":
            handle_list2(bot, sender_id)
          elif message_text == "/hi":
            handle_hi(bot, sender_id)
          elif message_text == "/image":
            handle_image(bot, sender_id)
          elif message_text == "/receipt":
            handle_receipt(bot, sender_id)
          else:
            handle_other_messages(bot, sender_id)
        elif messaging_event.get("postback"):
          sender_id = messaging_event["sender"]["id"]
          payload = messaging_event["postback"]["payload"]
          handle_item_click(bot, sender_id, payload)
  else:
    return "OK"
  return jsonify({'message': 'Message received successfully'})


@webhook_routes.route("/webhook", methods=['GET'])
def webhook():
  return handle_webhook_verification_with_ngrok("Webhook", 200)

  
@webhook_routes.route('/alive', methods=['GET'])
def index():
    return "Alive"

@webhook_routes.route("/", methods=['GET'])
def root_program():
  return handle_webhook_verification_with_ngrok("Root --", 200)


@webhook_routes.route("/privacy_policy", methods=['GET'])
def privacy_policy():
  return handle_webhook_verification_with_ngrok("privacy policy", 200)


# define catch all other routes and all other methods and return a "not allowed message"
@webhook_routes.route("/<path:path>", methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'OPTIONS'])
def catch_all(path):
  return "Not Allowed", 405
