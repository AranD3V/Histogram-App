# --- Python ML Service for Image Classification ---
# This is a simple Flask server that exposes a /predict endpoint.
# It simulates loading a model and performing inference on an uploaded image.

import os
from flask import Flask, request, jsonify
from PIL import Image
import io
import random # To simulate model predictions

# 1. Initialize Flask App
app = Flask(__name__)

# --- SIMULATED MODEL LOADING ---
# In a real application, you would load your trained model here.
# For example, using TensorFlow/Keras:
# from tensorflow.keras.models import load_model
# model = load_model('path/to/your/model.h5')
# Or using PyTorch:
# model = torch.load('path/to/your/model.pth')
print("Simulating the loading of a large deep learning model...")
# This is where you'd have your actual model object.
model = "Simulated_ResNet50_Model" 
print("Model ready.")

def preprocess_image(image_bytes):
    """
    Simulates the preprocessing steps required for the model.
    - Opens the image
    - Resizes to the model's expected input size (e.g., 224x224)
    - Converts to a NumPy array
    - Normalizes the pixel values
    """
    try:
        image = Image.open(io.BytesIO(image_bytes))
        # A real model would require resizing, e.g., image = image.resize((224, 224))
        print(f"Image preprocessed successfully. Original size: {image.size}")
        return image
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None

# 2. Define the /predict Endpoint
@app.route('/predict', methods=['POST'])
def predict():
    """
    Handles the image classification request.
    """
    print("Received a request to /predict")
    
    # Check if an image file was uploaded
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided.'}), 400
        
    file = request.files['image']
    
    # Read the image file as bytes
    img_bytes = file.read()
    
    # Preprocess the image
    preprocessed_image = preprocess_image(img_bytes)
    if preprocessed_image is None:
        return jsonify({'error': 'Invalid or corrupt image file.'}), 400

    # --- SIMULATED MODEL INFERENCE ---
    # In a real application, you'd run the actual model prediction here.
    # e.g., prediction_scores = model.predict(preprocessed_image)
    # Then you would interpret the scores to get the final class.
    print("Running simulated model inference...")
    is_malignant = random.choice([True, False])
    confidence = 85 + random.random() * 14 # Between 85% and 99%

    result = {
        'prediction': 'Malignant' if is_malignant else 'Benign',
        'confidence': f"{confidence:.2f}",
        'classColor': 'red' if is_malignant else 'green',
        'recommendation': (
            'High probability of malignancy detected. Urgent review recommended.' 
            if is_malignant 
            else 'Low probability of malignancy detected. Routine follow-up suggested.'
        )
    }
    # --- END OF SIMULATION ---

    print(f"Prediction complete. Result: {result['prediction']}")
    
    # 3. Return the Result as JSON
    return jsonify(result)

# 4. Run the Flask App
if __name__ == '__main__':
    # Use 0.0.0.0 to make it accessible from outside the container
    app.run(host='0.0.0.0', port=5000)
