from .api_client import send_reply_message
from .command_processor import classify_command
from ...iot_test.iot import turn_on_light, turn_off_light

def handle_text_message(event):
    user_id = event['source']['userId']
    message_text = event['message']['text']
    print(f"Received text message from {user_id}: {message_text}")

    # Use command_processor to classify the command
    task = classify_command(message_text)
    if task == 'turn on the light':
        turn_on_light()
        reply_text = "Turning on the light!!!"
    elif task == 'turn off the light':
        turn_off_light()
        reply_text = "Turning off the light~~"
    else:
        reply_text = "Sry! I can't understand this command!!! :("

    send_reply_message(event['replyToken'], reply_text)