from flask import Flask, request, abort, jsonify
from handlers.message_handler import handle_text_message
from handlers.command_processor import classify_command
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


# Endpoint to process commands
@app.route('/api/command', methods=['POST'])
def process_command():
    data = request.get_json()
    message_text = data.get('message', '')
    action = classify_command(message_text)
    return jsonify({"action": action}), 200

# Endpoint to control devices
@app.route('/api/device-control', methods=['POST'])
def control_device():
    data = request.get_json()
    action = data.get('action', '')
    if not action:
        return jsonify({"message": "Invalid action"}), 400
    # Implement your device control logic here
    # For example: if action == "turn on the light":
    return jsonify({"message": "Device controlled successfully"}), 200

# Endpoint to get device status
@app.route('/api/status', methods=['GET'])
def get_status():
    # Implement logic to fetch status
    return jsonify({"status": "Device status here"}), 200



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
