from transformers import pipeline

# Load the zero-shot classification model
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

def classify_command(message_text):
    """Classify the command using zero-shot classification."""
    # Define potential command labels
    labels = ['turn on the light', 'turn off the light', 'other']

    # Use the zero-shot classifier to match the command
    result = classifier(message_text, candidate_labels=labels)

    # Get the highest scored label
    predicted_label = result['labels'][0]
    return predicted_label

