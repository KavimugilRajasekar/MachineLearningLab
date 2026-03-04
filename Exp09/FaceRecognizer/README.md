# Face Intelligence - Minimalist Web Application

A premium, real-time face recognition system built with **Flask** and **face_recognition (dlib)**. This application provides a modern, high-performance web interface that resolves common camera hardware issues by leveraging native browser camera access.

## 🚀 Key Features
- **Browser-Based Vision**: Uses JavaScript's `getUserMedia` API to reliably capture camera feeds without desktop driver conflicts.
- **Minimalist Design**: A sleek White, Grey, and Black UI with curved corners, bold black outlines, and smooth typography.
- **Intelligent Recognition**: Powered by the state-of-the-art `dlib` library, matching faces against your `known_faces` directory with optimized tolerance.
- **Real-Time Performance**: Processes every second frame on the backend to maintain a smooth 60fps video feed in the browser.

## 📁 Directory Structure
```text
FaceRecognizer/
├── app.py              # Flask Backend & Recognition Logic
├── known_faces/        # Folder containing your .jpg/jpeg face samples
├── templates/
│   └── index.html      # Minimalist Web Interface (HTML/CSS/JS)
├── facelab/            # Python Virtual Environment
└── README.md           # This documentation
```

## 🛠️ Technical Implementation (Code Level)

### Backend (`app.py`)
- **Face Loading**: On startup, the script scans `known_faces/`, generates 128-dimension embeddings for each person, and stores them in memory for instant matching.
- **Frame Processing**: Receives Base64 images from the browser, decodes them using `PIL`, and resizes them by 50% using `OpenCV` to quadruple processing speed.
- **Recognition Logic**: 
  - Uses `face_recognition.face_encodings` to detect faces.
  - Compares them using `face_recognition.compare_faces` with a **0.6 tolerance** (relaxed for better reliability).
  - Returns coordinates and names as a JSON response.

### Frontend (`index.html`)
- **Canvas Mirroring**: To ensure the UI feels natural (like a mirror), the video is flipped via CSS (`scaleX(-1)`), while the JavaScript manually mirrors the face coordinates so that name tags are **not** flipped and remain readable.
- **Dynamic Overlays**: Uses HTML5 Canvas to draw high-contrast black/white boxes and labels that track faces with sub-pixel precision.

## 🚦 How to Run

1.  **Activate Environment**:
    Make sure you are in the project folder with your `facelab` environment ready.
2.  **Start the Server**:
    ```powershell
    python app.py
    ```
3.  **Access the Web App**:
    Open [**http://127.0.0.1:5000**](http://127.0.0.1:5000) in your browser (Chrome or Edge recommended).
4.  **Allow Camera**:
    Click "Allow" when the browser asks for camera permission.

## ⚖️ Customization
- **Strictness**: Change `tolerance=0.6` in `app.py` (Lower = Stricter, Higher = More Flexible).
- **Design**: Modify the CSS variables in `index.html` to change the colors or border radius.

---
*Developed for Machine Learning Lab - Face Detection Project.*
