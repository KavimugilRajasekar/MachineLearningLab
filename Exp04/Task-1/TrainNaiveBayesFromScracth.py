from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Dataset
messages = [
    "Win a free mobile now",
    "Meeting scheduled at 10 AM",
    "Claim your lottery prize",
    "Project deadline is tomorrow",
    "Limited offer buy now",
    "Team lunch today",
    "Congratulations you won",
    "Please review the document",
    "Free coupons available",
    "Call me when free"
]

labels = [
    "Spam", "Not Spam", "Spam", "Not Spam", "Spam",
    "Not Spam", "Spam", "Not Spam", "Spam", "Not Spam"
]

# Convert text to Bag-of-Words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# Train Naïve Bayes model
model = MultinomialNB()
model.fit(X, labels)

# Test message
test_message = ["Free offer available"]
test_vector = vectorizer.transform(test_message)

prediction = model.predict(test_vector)

print("Test Message:", test_message[0])
print("Predicted Class:", prediction[0])

# Accuracy on training data
train_predictions = model.predict(X)
accuracy = accuracy_score(labels, train_predictions)

print("Model Accuracy:", accuracy)
