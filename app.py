# save as app.py
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import base64, io
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)
CORS(app)

# Load your trained Keras best_model (h5 / SavedModel)
try:
    model = tf.keras.models.load_model('best_model.h5', compile=False)  # change path
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    print("Model loaded successfully!")
except Exception as e:
    print(f"Model loading failed: {e}")
    print("Running with demo predictions...")
    model = None

CLASS_NAMES = ["melanoma","nevus","seborrheic_keratosis","basal_cell_carcinoma","actinic_keratosis","benign_keratosis","dermatofibroma"]
INPUT_SIZE = (224,224)

def preprocess_pil(img: Image.Image, size):
    img = img.convert('RGB').resize(size, Image.BILINEAR)
    arr = np.array(img) / 255.0
    arr = np.expand_dims(arr, 0).astype(np.float32)
    return arr

@app.route('/')
def index():
    return send_file('interface.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    if 'image' not in data:
        return jsonify({'error':'no image provided'}), 400
    img_b64 = data['image'].split(',',1)[-1]
    try:
        decoded = base64.b64decode(img_b64)
        img = Image.open(io.BytesIO(decoded))
        
        if model is not None:
            # Use real model
            x = preprocess_pil(img, INPUT_SIZE)
            preds = model.predict(x)[0]  # shape (num_classes,)
            probs = preds.tolist()
        else:
            # Demo predictions if model failed to load
            import random
            probs = [random.uniform(0.1, 0.9) for _ in range(len(CLASS_NAMES))]
            total = sum(probs)
            probs = [p/total for p in probs]
        
        result = [{'label': CLASS_NAMES[i], 'prob': float(probs[i])} for i in range(len(probs))]
        # sort by prob desc on client; we keep original order as well
        return jsonify({'predictions': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)