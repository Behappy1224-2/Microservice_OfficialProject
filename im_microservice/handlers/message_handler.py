import requests
import os
from .api_client import send_reply_message
from .command_processor import classify_command

pi_url = os.getenv('pi_url', 'default_token_if_not_set')

def handle_text_message(event):
    user_id = event['source']['userId']
    message_text = event['message']['text']
    print(f"Received text message from {user_id}: {message_text}")
    control_url = f"{pi_url}/control_light"
    # Use command_processor to classify the command
    task = classify_command(message_text)
    if task == 'turn on the light':
        requests.post(control_url, json={'action': 'turn on the light'})
        reply_text = "Turning on the light!!!"
    elif task == 'turn off the light':
        requests.post(control_url, json={'action': 'turn off the light'})
        reply_text = "Turning off the light~~"
    else:
        reply_text = "Sry! I can't understand this command!!! :("

    send_reply_message(event['replyToken'], reply_text)