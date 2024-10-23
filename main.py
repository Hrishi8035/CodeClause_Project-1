import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from matplotlib import pyplot as plt

# Load the pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

def classify_image(img_path):
    # Load the image and resize it to 224x224 as required by MobileNetV2
    img = image.load_img(img_path, target_size=(224, 224))
    
    # Convert the image to a numpy array and preprocess it
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension
    img_array = preprocess_input(img_array)  # Preprocess for MobileNetV2
    
    # Use the model to predict the object
    predictions = model.predict(img_array)
    
    # Decode the predictions to get human-readable labels
    decoded_preds = decode_predictions(predictions, top=3)[0]
    
    return decoded_preds

# List of images to classify
image_paths = ['image.jpeg', 'image1.jpg', 'image2.jpeg']  # Replace with actual image filenames

# Loop through each image and classify it
for img_path in image_paths:
    try:
        print(f"Classifying {img_path}:")
        predictions = classify_image(img_path)
        
        # Display the top 3 predictions
        for i, (imagenet_id, label, score) in enumerate(predictions):
            print(f"{i+1}: {label} ({score * 100:.2f}%)")
        
        # Load and display the image with predictions
        img = cv2.imread(img_path)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.imshow(img_rgb)
        plt.title(f"Top prediction: {predictions[0][1]} ({predictions[0][2] * 100:.2f}%)")
        plt.show()
        
    except Exception as e:
        print(f"Error processing {img_path}: {e}")