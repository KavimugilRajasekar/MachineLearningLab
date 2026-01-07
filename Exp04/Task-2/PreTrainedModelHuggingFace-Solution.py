from transformers import pipeline

# Load pretrained sentiment analysis model
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Test message
text = "Free offer available"

result = classifier(text)

print("Text:", text)
print("Prediction:", result)
