from flask import Flask, request, render_template, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO
import PIL.Image as pil_image
import tensorflow as tf

app = Flask(__name__)

# Load your trained model
model = load_model('vgg16_model.keras')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Convert the file to a BytesIO object
        img = pil_image.open(BytesIO(file.read()))
        img = img.resize((240, 240))
        
        # Convert grayscale to RGB if model expects RGB input
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        # Make prediction
        prediction = model.predict(img_array)
        result = 'Positive' if prediction[0][0] > 0.5 else 'Negative'

        # Clear the session to free up memory
        tf.keras.backend.clear_session()

        return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
