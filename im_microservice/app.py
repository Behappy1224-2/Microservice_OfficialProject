from flask import Flask, request, abort
from handlers.message_handler import handle_text_message
from config import LINE_CHANNEL_ACCESS_TOKEN 
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_data = request.get_json()

    if json_data is None:
        abort(400)

    events = json_data.get('events', [])
    for event in events:
        event_type = event['type']
        if event_type == 'message':
            message_type = event['message']['type']
            if message_type == 'text':
                handle_text_message(event)

    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
