import requests
import os
from config import LINE_CHANNEL_ACCESS_TOKEN 

def send_reply_message(reply_token, message_text):
    """Send a reply message back to the user via Line Messaging API."""
    url = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {LINE_CHANNEL_ACCESS_TOKEN}',
    }
    data = {
        'replyToken': reply_token,
        'messages': [{'type': 'text', 'text': message_text}],
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print(f"Failed to send message: {response.text}")
    else:
        print("Reply sent successfully.")
