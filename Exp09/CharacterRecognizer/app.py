import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageDraw, ImageOps
import tensorflow as tf
import numpy as np
import os

class CharacterRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digit Recognizer")
        self.root.geometry("450x600")
        self.root.configure(bg="#F5F5F5")  # Light Grey background
        
        self.model = None
        self.model_path = 'model.h5'
        
        # Colors & Styles
        self.BG_COLOR = "#F5F5F5"
        self.ACCENT_COLOR = "#FFFFFF"
        self.OUTLINE_COLOR = "#000000"
        self.TEXT_COLOR = "#333333"

        # Load the model
        if os.path.exists(self.model_path):
            try:
                self.model = tf.keras.models.load_model(self.model_path)
            except Exception as e:
                messagebox.showerror("Model Error", f"Failed to load model: {e}")
        else:
            messagebox.showwarning("Model Not Found", "Model file 'model.h5' not found. Please train the model first.")

        # Title
        tk.Label(root, text="CHARACTER RECOGNIZER", font=('Segoe UI', 18, 'bold'), bg=self.BG_COLOR, fg=self.TEXT_COLOR).pack(pady=20)

        # Drawing Area with Black Outline and padding
        self.canvas_frame = tk.Frame(root, bg=self.OUTLINE_COLOR, padx=2, pady=2)
        self.canvas_frame.pack(pady=10)
        
        self.canvas_width = 280
        self.canvas_height = 280
        self.canvas = tk.Canvas(self.canvas_frame, width=self.canvas_width, height=self.canvas_height, bg="black", cursor="cross", highlightthickness=0)
        self.canvas.pack()
        
        # PIL Image and Draw object
        self.image1 = Image.new("L", (self.canvas_width, self.canvas_height), 0)
        self.draw = ImageDraw.Draw(self.image1)

        self.canvas.bind("<B1-Motion>", self.paint)

        # Labels for output
        self.label_result = tk.Label(root, text="Draw a digit (0-9)", font=('Segoe UI', 14), bg=self.BG_COLOR, fg=self.TEXT_COLOR)
        self.label_result.pack(pady=10)

        self.label_confidence = tk.Label(root, text="", font=('Segoe UI', 10), bg=self.BG_COLOR, fg="#666666")
        self.label_confidence.pack()

        # Custom Styled Buttons (Simulating Curved Edges with Canvas if needed, but standard buttons with border)
        self.button_frame = tk.Frame(root, bg=self.BG_COLOR)
        self.button_frame.pack(pady=30)

        # Use ttk for better look or standard with specific relief
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", font=('Segoe UI', 11), padding=10)

        self.btn_predict = tk.Button(self.button_frame, text="PREDICT", command=self.predict, 
                                     bg=self.ACCENT_COLOR, fg=self.OUTLINE_COLOR, 
                                     font=('Segoe UI', 11, 'bold'), 
                                     relief="flat", bd=1, highlightbackground=self.OUTLINE_COLOR, highlightthickness=1)
        self.btn_predict.grid(row=0, column=0, padx=15, ipadx=10)

        self.btn_clear = tk.Button(self.button_frame, text="CLEAR", command=self.clear_canvas, 
                                   bg=self.BG_COLOR, fg=self.TEXT_COLOR, 
                                   font=('Segoe UI', 11), 
                                   relief="flat", bd=1, highlightbackground=self.OUTLINE_COLOR, highlightthickness=1)
        self.btn_clear.grid(row=0, column=1, padx=15, ipadx=10)

    def paint(self, event):
        x, y = event.x, event.y
        r = 10 # Brush radius
        self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="white", outline="white")
        self.draw.ellipse([x-r, y-r, x+r, y+r], fill=255)

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image1 = Image.new("L", (self.canvas_width, self.canvas_height), 0)
        self.draw = ImageDraw.Draw(self.image1)
        self.label_result.config(text="Draw a digit (0-9)")
        self.label_confidence.config(text="")

    def predict(self):
        if not self.model:
            messagebox.showerror("Error", "Model not loaded.")
            return

        # Preprocessing: MNIST images are 28x28, centered, grayscale
        img = self.image1.resize((28, 28))
        img_array = np.array(img).reshape(1, 28, 28, 1).astype('float32') / 255
        
        # Predict
        prediction = self.model.predict(img_array)
        digit = np.argmax(prediction)
        confidence = np.max(prediction)

        self.label_result.config(text=f"PREDICTION: {digit}")
        self.label_confidence.config(text=f"Confidence: {confidence*100:.2f}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterRecognizerApp(root)
    root.mainloop()
