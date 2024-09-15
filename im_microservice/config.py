# config.py
import os

# Read the LINE_CHANNEL_ACCESS_TOKEN from environment variables
# If it's not set, you can set a default value or handle the error
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', 'default_token_if_not_set')

print(f"Using Access Token: {LINE_CHANNEL_ACCESS_TOKEN}")
# You can add additional configuration settings here if needed