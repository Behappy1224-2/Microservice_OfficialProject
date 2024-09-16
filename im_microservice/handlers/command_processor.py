import re
from nltk.stem import PorterStemmer

# Initialize a stemmer to reduce words to their base form
stemmer = PorterStemmer()

# Define keywords for actions
KEYWORDS = {
    'on': ['on', 'activate', 'enable'],
    'off': ['off', 'deactivate', 'disable'],
    'turn': ['turn', 'switch'],
    'light': ['light', 'lights', 'lamp']
}

def classify_command(message_text):
    """Classify the command based on keywords and context."""
    # Preprocess the message: lowercasing, stemming, and tokenization
    message_text = message_text.lower()
    tokens = re.findall(r'\w+', message_text)  # Extract words
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    # Check for keywords in the stemmed tokens
    has_turn = any(stem in KEYWORDS['turn'] for stem in stemmed_tokens)
    has_on = any(stem in KEYWORDS['on'] for stem in stemmed_tokens)
    has_off = any(stem in KEYWORDS['off'] for stem in stemmed_tokens)
    has_light = any(stem in KEYWORDS['light'] for stem in stemmed_tokens)

    # Determine the action based on the detected keywords
    if has_turn and has_light:
        if has_on:
            return "turn on the light"
        elif has_off:
            return "turn off the light"
    
    # If the intent isn't clear, return a default or "other" response
    return "other"

