def classify_command(message_text):
    """Classify the command based on the input text."""
    message_text = message_text.lower()
    if "turn on" in message_text and "light" in message_text:
        return 'turn on the light'
    elif "turn off" in message_text and "light" in message_text:
        return 'turn off the light'
    else:
        return 'other'
