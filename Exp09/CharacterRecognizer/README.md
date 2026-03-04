# Character Recognition System (MNIST) - ML Lab

This project implements a handwritten digit recognition application using a Convolutional Neural Network (CNN) trained on the MNIST dataset. It features a GUI built with Tkinter that allows users to draw digits with a mouse and get real-time predictions.

## Features
- **CNN Model**: Achieves ~99% accuracy on digit recognition.
- **Minimalist GUI**: White and Grey theme with Black Outlines.
- **Real-time Prediction**: Preprocesses the drawing to match MNIST standards (28x28 grayscale).

---

## Code Level Explanation

### 1. Model Training (`train_model.py`)

The core of the system is a CNN built using TensorFlow/Keras.

```python
model = models.Sequential([
    # Layer 1: Convolutional layer with 32 filters, 3x3 kernel
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)), # Downsampling
    
    # Layer 2: Convolutional layer with 64 filters
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Layer 3: Final Convolutional layer
    layers.Conv2D(64, (3, 3), activation='relu'),
    
    # Flattening and Dense Layers
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax') # 10 output classes (0-9)
])
```
- **Preprocessing**: The 28x28 images are normalized to values between 0 and 1.
- **Optimizer**: `adam` optimizer is used for efficient training.
- **Loss Function**: `sparse_categorical_crossentropy` as our labels are integers.

### 2. GUI Application (`app.py`)

The GUI is built with Python's built-in `tkinter` library.

#### Drawing Mechanism
- A `tk.Canvas` captures mouse motion events.
- Simultaneously, a `PIL.Image` (binary mask) is updated in the background. This ensures the model receives a clean image, independent of the UI's scaling or colors.

#### Image Processing (In Code)
When the user clicks "PREDICT":
1. The `PIL.Image` (300x300 canvas) is resized to **28x28 pixels**.
2. It is converted to a NumPy array and normalized (`/ 255.0`).
3. It is reshaped to `(1, 28, 28, 1)` to match the model's input expectations.

---

## How to Run

1. **Activate Virtual Environment**:
   ```powershell
   .\charlab\Scripts\activate
   ```
2. **Train the Model** (optional if `model.h5` already exists):
   ```bash
   python train_model.py
   ```
3. **Run the App**:
   ```bash
   python app.py
   ```

## UI Themes
- **Background**: Light Grey (`#F5F5F5`)
- **Outlines**: Solid Black (`#000000`)
- **Interaction**: White/Grey components for a premium minimalist look.
