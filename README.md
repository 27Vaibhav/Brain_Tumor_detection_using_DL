# Brain Tumor Detection using Deep Learning

## Project Overview
This project involves the development of a deep learning model for brain tumor detection. The model is designed to analyze MRI images and predict the presence of a tumor. Various convolutional neural network (CNN) architectures were used to train and evaluate the model, with VGG16 providing the best performance. The project includes a Flask-based web application for user interaction and local deployment.

## Table of Contents
- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Data](#data)
- [Model](#model)
- [Deployment](#deployment)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Introduction
This project focuses on developing a deep learning model to detect brain tumors from MRI images. The model leverages advanced CNN architectures to achieve high accuracy in classification, distinguishing between images with and without tumors.

## Technologies Used
- **Deep Learning Models:** CNN, VGG16, ResNet
- **Libraries:** TensorFlow, Keras, scikit-learn, OpenCV, NumPy, Matplotlib, Flask
- **Web Framework:** Flask

## Data
The dataset used for training and testing the model consists of MRI images of the brain. The images are preprocessed and split into training and testing sets to evaluate the model's performance.

## Model
- **CNN:** 
- **VGG16:** 
- **ResNet:** 

VGG16 was chosen as the final model due to its superior performance compared to other architectures.

## Deployment
The project includes a Flask-based web application that allows users to upload MRI images and receive predictions on the presence of a brain tumor. The application is designed for local deployment and provides an intuitive interface for interaction.

### Steps to Deploy
1. **Clone the Repository:**
    ```sh
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies:**
    Ensure you have Python installed. Then, install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```sh
    python app.py
    ```

5. **Access the application in your web browser:**
    Navigate to `http://127.0.0.1:5000`.

## Usage
To use the web application:

1. Navigate to the homepage.
2. Upload an MRI image of the brain using the file upload button.
3. Click the "Predict" button to receive the prediction result.

## Results
- **CNN:** Accuracy - 78%
- **VGG16:** Accuracy - 94% (Best model)
- **ResNet:** Accuracy - 83%

The results show that the VGG16 model outperforms other architectures in detecting brain tumors.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
