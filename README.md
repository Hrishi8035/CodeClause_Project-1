# Image Recognition using OpenCV, TensorFlow, and Keras
This project demonstrates image recognition and object detection using OpenCV, TensorFlow, and Keras. The model processes an input image and identifies objects within it, displaying the top three potential matches along with their confidence percentages in the terminal. The identified image is also plotted using Matplotlib for easy visualization.

## Features
**Object Detection:** Utilizes a deep learning model built with TensorFlow and Keras to detect objects or patterns within images.
Top 3 Identifications: Displays the top three recognized objects along with confidence percentages in the terminal. 

*For example:*
1: tiger_cat (35.49%)
2: Egyptian_cat (34.88%)
3: tabby (20.31%)

**Image Plotting:** After identification, the image is plotted with Matplotlib to visually represent the detected objects.
Technologies Used
**OpenCV:** For image processing.
**TensorFlow & Keras:** For building and training the deep learning model.
**Matplotlib:** For visualizing the image post-identification.

## Installation

### Clone this repository:

```bash
$ git clone https://github.com/Hrishi8035/CodeClause_Project-1
$ cd image-recognition-opencv
```

### Install the required dependencies:

```bash
$ pip install -r requirements.txt
```

### Make sure to install the required libraries:
```bash
OpenCV
TensorFlow
Keras
Matplotlib
NumPy
```
### You can install these with:
```bash
$ pip install opencv-python tensorflow keras matplotlib numpy
```

## How to Use

### 1. Upload an image for recognition.

### 2. Run the python script:
```bash
$ python main.py
```

The terminal will display the top 3 identifications with their confidence levels, like so:
```bash
1: tiger_cat (35.49%)
2: Egyptian_cat (34.88%)
3: tabby (20.31%)
```
The identified image will also be plotted using Matplotlib.

### Example
When an image of a cat is uploaded, the terminal might display:
```bash
1: tiger_cat (35.49%)
2: Egyptian_cat (34.88%)
3: tabby (20.31%)
```
The identified image will be plotted as output.

### 3. Quit the app: 

Hit Ctrl + C (Windows) or Cmd + C (MacOS) or the correct keyboard interrupt combination for your operating system.

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request with your improvements.