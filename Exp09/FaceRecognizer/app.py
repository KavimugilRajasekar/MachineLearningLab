from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import face_recognition
import cv2
import numpy as np
import os
import base64
import io
from PIL import Image

app = Flask(__name__)
CORS(app)

# ---------------------------
# Load Known Faces
# ---------------------------
known_face_encodings = []
known_face_names = []

def load_known_faces():
    path = "known_faces"
    if not os.path.exists(path):
        os.makedirs(path)
        
    for file in os.listdir(path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(path, file)
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)
            
            if len(encodings) > 0:
                known_face_encodings.append(encodings[0])
                known_face_names.append(os.path.splitext(file)[0])
    print(f"Loaded {len(known_face_names)} known faces.")

load_known_faces()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    data = request.json
    if not data or 'image' not in data:
        return jsonify({"error": "No image data"}), 400

    # Decode base64 image
    img_data = base64.b64decode(data['image'].split(',')[1])
    image = Image.open(io.BytesIO(img_data)).convert('RGB')
    frame = np.array(image)
    
    # Convert RGB to BGR for OpenCV processing (if needed) but face_recognition uses RGB
    # We'll stick to RGB
    
    # Resize for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    
    # Find all face locations and encodings
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    results = []
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Increased tolerance from 0.5 to 0.6 to be less strict
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
        name = "Unknown"
        confidence = 0

        if len(known_face_encodings) > 0:
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                confidence = round((1 - face_distances[best_match_index]) * 100, 2)

        results.append({
            "name": name,
            "confidence": f"{confidence}%" if name != "Unknown" else "",
            "location": [top * 2, right * 2, bottom * 2, left * 2] # Scale back up
        })

    return jsonify({"faces": results})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
