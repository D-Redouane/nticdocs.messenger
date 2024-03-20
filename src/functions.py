from pymessenger import Bot
import json
from flask import Flask, request
import requests
from variables import *




# --------------------------------------------------------
# --------------------------------------------------------
# ----------------------- Commands -----------------------
# --------------------------------------------------------
# --------------------------------------------------------



# Define a function to handle start/help commands
def handle_start_help(bot, sender_id):
  print("Received start/help command")
  bot.send_text_message(sender_id,
                        "Welcome! Use /list to browse the directory.")

# Define a function to handle start/help commands
def handle_other_messages(bot, sender_id):
  print("Received other messages command")
  bot.send_text_message(sender_id,
                        "I cant help with this command. Use /list to browse the directory. or Read the How to use section in the page or in the README file on github account of the bot ")

# Define a function to handle list commands
def handle_list(bot, sender_id):
  print("Received list command")

  # Replace this line with your logic to read the local directory structure
  tree_object = read_directory_structure(JSON_FILE_PATH)

  # print(tree_object)

  if tree_object:
    user_directory_map[sender_id] = [tree_object]
    print(user_directory_map[sender_id])
    inline_keyboard = create_inline_keyboard(tree_object, True)
    send_message(bot, sender_id, "Select an item:", inline_keyboard)
    send_message(bot, sender_id, "We recived your /list message we will replay as soon as possible")
  else:
    send_message(bot, sender_id,
                 "Error: Unable to read local directory structure")



API = "https://graph.facebook.com/v19.0/me/messages?access_token="+TOKEN

def handle_template(bot, sender_id):
    request_body = {
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                        "template_type": "generic",
                        "elements": [
                            {
                                "title": "Welcome!",
                                "image_url": "https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg",
                                "subtitle": "We have the right hat for everyone.",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://www.originalcoastclothing.com/",
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://www.originalcoastclothing.com/",
                                        "title": "View Website"
                                    }, {
                                        "type": "postback",
                                        "title": "Start Chatting",
                                        "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                    }
                                ]
                            },
                            {
                                "title": "Welcome!",
                                "image_url": "https://raw.githubusercontent.com/fbsamples/original-coast-clothing/main/public/styles/male-work.jpg",
                                "subtitle": "We have the right hat for everyone.",
                                "default_action": {
                                    "type": "web_url",
                                    "url": "https://www.originalcoastclothing.com/",
                                    "webview_height_ratio": "tall",
                                },
                                "buttons": [
                                    {
                                        "type": "web_url",
                                        "url": "https://www.originalcoastclothing.com/",
                                        "title": "View Website"
                                    }, {
                                        "type": "postback",
                                        "title": "Start Chatting",
                                        "payload": "DEVELOPER_DEFINED_PAYLOAD"
                                    }
                                ]
                            }
                        ]
                }
            }
        }
    }
    response = requests.post(API, json=request_body).json()
    return response

def handle_buttons(bot, sender_id):
    request_body = {
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "What do you want to do next?",
                    "buttons": [
                        {
                            "type": "web_url",
                            "url": "https://www.messenger.com",
                            "title": "Visit Messenger"
                        },
                        {
                            "type": "web_url",
                            "url": "https://www.youtube.com",
                            "title": "Visit Youtube"
                        },
                    ]
                }
            }
        }
    }
    response = requests.post(API, json=request_body).json()
    return response

def handle_quickr(bot, sender_id):
    request_body = {
        "recipient": {
            "id": sender_id
        },
        "messaging_type": "RESPONSE",
        "message": {
            "text": "Pick a color:",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Red",
                    "payload": "<POSTBACK_PAYLOAD>",
                    "image_url": "http://example.com/img/red.png"
                }, {
                    "content_type": "text",
                    "title": "Green",
                    "payload": "<POSTBACK_PAYLOAD>",
                    "image_url": "http://example.com/img/green.png"
                }
            ]
        }
    }
    response = requests.post(API, json=request_body).json()
    return response

def handle_list2(bot, sender_id):
    request_body = {
        "recipient": {
            "id": "RECIPIENT_ID"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "list",
                    "top_element_style": "compact",
                    "elements": [
                        {
                            "title": "Classic T-Shirt Collection",
                            "subtitle": "See all our colors",
                            "image_url": "https://originalcoastclothing.com/img/collection.png",
                            "buttons": [
                                {
                                    "title": "View",
                                    "type": "web_url",
                                    "url": "https://originalcoastclothing.com/collection",
                                    "messenger_extensions": True,
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://originalcoastclothing.com/"
                                }
                            ]
                        },
                        {
                            "title": "Classic White T-Shirt",
                            "subtitle": "See all our colors",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://originalcoastclothing.com/view?item=100",
                                "messenger_extensions": False,
                                "webview_height_ratio": "tall"
                            }
                        },
                        {
                            "title": "Classic Blue T-Shirt",
                            "image_url": "https://originalcoastclothing.com/img/blue-t-shirt.png",
                            "subtitle": "100% Cotton, 200% Comfortable",
                            "default_action": {
                                "type": "web_url",
                                "url": "https://originalcoastclothing.com/view?item=101",
                                "messenger_extensions": True,
                                "webview_height_ratio": "tall",
                                "fallback_url": "https://originalcoastclothing.com/"
                            },
                            "buttons": [
                                {
                                    "title": "Shop Now",
                                    "type": "web_url",
                                    "url": "https://originalcoastclothing.com/shop?item=101",
                                    "messenger_extensions": True,
                                    "webview_height_ratio": "tall",
                                    "fallback_url": "https://originalcoastclothing.com/"
                                }
                            ]
                        }
                    ],
                    "buttons": [
                        {
                            "title": "View More",
                            "type": "postback",
                            "payload": "payload"
                        }
                    ]
                }
            }
        }

    }
    response = requests.post(API, json=request_body).json()
    return response

def handle_hi(bot, sender_id):
    request_body = {
        "recipient": {
            "id": sender_id
        },
        "message": {
            "text": "hello, world!"
        }
    }
    response = requests.post(API, json=request_body).json()
    return response

def handle_image(bot, sender_id):
    request_body = {
        "recipient": {
            "id": sender_id
        },
        "message": {
            "attachment": {
                "type": "image",
                "payload": {
                    "url": "http://www.messenger-rocks.com/image.jpg",
                    "is_reusable": True
                }
            }
        }
    }
    response = requests.post(API, json=request_body).json()
    return response

def handle_receipt(bot, sender_id):
    request_body = {
        "recipient": {
            "id": "<PSID>"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "receipt",
                    "recipient_name": "Stephane Crozatier",
                    "order_number": "12345678902",
                    "currency": "USD",
                    "payment_method": "Visa 2345",
                    "order_url": "http://originalcoastclothing.com/order?order_id=123456",
                    "timestamp": "1428444852",
                    "address": {
                        "street_1": "1 Hacker Way",
                        "street_2": "",
                        "city": "Menlo Park",
                        "postal_code": "94025",
                        "state": "CA",
                        "country": "US"
                    },
                    "summary": {
                        "subtotal": 75.00,
                        "shipping_cost": 4.95,
                        "total_tax": 6.19,
                        "total_cost": 56.14
                    },
                    "adjustments": [
                        {
                            "name": "New Customer Discount",
                            "amount": 20
                        },
                        {
                            "name": "$10 Off Coupon",
                            "amount": 10
                        }
                    ],
                    "elements": [
                        {
                            "title": "Classic White T-Shirt",
                            "subtitle": "100% Soft and Luxurious Cotton",
                            "quantity": 2,
                            "price": 50,
                            "currency": "USD",
                            "image_url": "http://originalcoastclothing.com/img/whiteshirt.png"
                        },
                        {
                            "title": "Classic Gray T-Shirt",
                            "subtitle": "100% Soft and Luxurious Cotton",
                            "quantity": 1,
                            "price": 25,
                            "currency": "USD",
                            "image_url": "http://originalcoastclothing.com/img/grayshirt.png"
                        }
                    ]
                }
            }
        }
    }
    response = requests.post(API, json=request_body).json()
    return response



# --------------------------------------------------------
# --------------------------------------------------------
# ----------------------- Commands -----------------------
# --------------------------------------------------------
# --------------------------------------------------------




















# --------------------------------------------------------
# --------------------------------------------------------
# -------------------- other functions -------------------
# --------------------------------------------------------
# --------------------------------------------------------



# Define a function to initialize the bot
def initialize_bot(token):
  return Bot(token)

bot = initialize_bot(TOKEN)

# Define a function to read the local directory structure from a JSON file
def read_directory_structure(file_path):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      return json.load(file)
  except json.JSONDecodeError as e:
    print("Error decoding JSON file:", e)
    return None

def handle_webhook_verification_with_ngrok(message,status):
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return "Verification token mismatch", 403
        return request.args['hub.challenge'], 200
    return message, status

# --------------------------------------------------------
# --------------------------------------------------------
# -------------------- other functions -------------------
# --------------------------------------------------------
# --------------------------------------------------------




















# --------------------------------------------------------
# --------------------------------------------------------
# -------------------- bot related to --------------------
# --------------------------------------------------------
# --------------------------------------------------------



# Define a function to create an inline keyboard for listing items
def create_inline_keyboard(items, include_back_button=True):
  keyboard = []
  for item_name, item_info in items.items():
    # Generate a short id for the item
    item_id = str(len(item_id_map))
    item_id_map[item_id] = item_name
    callback_data = f"item_{item_id}"
    button = {"type": "postback", "title": item_name, "payload": callback_data}
    keyboard.append(button)

  if include_back_button:
    back_button = {"type": "postback", "title": "Back 🔙", "payload": "back"}
    keyboard.append(back_button)

  return keyboard

# Define a function to handle callback queries when an item is clicked
def handle_item_click(bot, sender_id, payload):
  print("Received callback query:", payload)

  if payload == 'back':
    handle_back(bot,sender_id)
  else:
    item_id = payload[len('item_'):]
    item_name = item_id_map.get(item_id)
    print("Item name:", item_name)

    current_directory = user_directory_map.get(sender_id, [])
    current_directory = current_directory[-1]

    if current_directory.get(item_name):
      if 'type' in current_directory[item_name] and current_directory[
          item_name]["type"] == "file":
        # Store the current keyboard markup
        last_keyboard_markup = {
            "keyboard": create_inline_keyboard(current_directory, True),
            "one_time_keyboard": True
        }

        # Download the file directly
        print("Sending document to user:", sender_id)
        print("Document URL:", current_directory[item_name]["download_url"])
        bot.send_file(sender_id, current_directory[item_name]["download_url"])

        # Send the last keyboard markup after sending the document
        if last_keyboard_markup:
          send_message(bot, sender_id, "Select an item:", last_keyboard_markup)
      else:
        # Navigate into the subfolder
        user_directory_map[sender_id].append(current_directory[item_name])
        inline_keyboard = create_inline_keyboard(current_directory[item_name],
                                                 include_back_button=True)
        send_message(bot, sender_id, "Select an item:", inline_keyboard)
    else:
      send_message(bot, sender_id, f"Error: Item not found - {item_name}")

# Define a function to handle back navigation
def handle_back(bot,sender_id):
  print("Received back command")
  current_directory_stack = user_directory_map.get(sender_id, [])
  if len(current_directory_stack) > 1:
    current_directory_stack.pop()  # Remove the current directory from stack
    parent_directory = current_directory_stack[-1]  # Get the parent directory
    inline_keyboard = create_inline_keyboard(parent_directory,
                                             include_back_button=True)
    send_message(bot, sender_id, "Select an item:", inline_keyboard)
  else:
    send_message(bot, sender_id, "You are at the root directory.")

# Define a function to send messages
# def send_message(bot, sender_id, message, reply_markup=None):
#   if reply_markup:
#       bot.send_message(sender_id, message, quick_replies=reply_markup)
#   else:
#       bot.send_text_message(sender_id, message)

def send_message(bot, sender_id, message, quick_replies=None):
    params = {
        "recipient": {"id": sender_id},
        "message": {"text": message}
    }
    if quick_replies:
        params["message"]["quick_replies"] = quick_replies

    bot.send_raw("messages", params)



# --------------------------------------------------------
# --------------------------------------------------------
# -------------------- bot related to --------------------
# --------------------------------------------------------
# --------------------------------------------------------