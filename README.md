# CSC-126-MIDTERM-PROJECT-PRIVACY-BLUR-AND-FACE-COUNTER-
SECTION/COURSE: BJY11
MEMBERS:
    HARVEY KENT B. TANILON
    JOANA ANDREA L. PALISOC
    JOYCE BACO

# OpenCV Face Detection and Head Blur

## Project Description

This project is a simple Python application that uses OpenCV to process images, detect human faces, blur detected faces for privacy, and display the results. It allows users to select a photo from their computer using a file selection dialog.

The application uses the Haar Cascade face detection method to identify faces in an image. It also applies image transformations and annotations to make the results easier to understand.

## Objectives

- Load and resize an image using OpenCV.
- Convert an image to grayscale and reduce noise.
- Detect human faces using Haar Cascade.
- Apply a Gaussian blur effect to detected faces.
- Draw rectangles and labels around detected faces.
- Count the number of detected faces.
- Save and display the processed images.

## Technologies Used

- **Python** – Main programming language.
- **OpenCV** – Image processing, face detection, Gaussian blur, and image display.
- **Tkinter** – Allows users to select an image from their computer.
- **OS module** – Handles file paths and creates the output folder.
- **Haar Cascade XML** – Pre-trained model used for face detection.

## Project Structure

The project folder should contain the following files:

```text
OpenCV-Face-Detection/
│
├── main.py
├── requirements.txt
├── haarcascade_frontalface_default.xml
├── README.md
│
└── Modified output/
    ├── output_grayscale.jpg
    ├── output_head_effect.jpg
    └── output_faces.jpg
```

The `Modified output` folder is created automatically when the program runs. The three image files are also generated automatically.

## Requirements

Before running the application, make sure you have:

- Python installed on your computer.
- OpenCV installed.
- Tkinter available in your Python installation.
- The Haar Cascade XML file inside your project folder.

## Setup Instructions

### 1. Install Python

Download and install Python from the official website:

https://www.python.org/downloads/

During installation on Windows, enable **Add Python to PATH**.

### 2. Install the Dependencies

Open your terminal or command prompt inside the project folder and run:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file should contain:

```text
opencv-python
```

Tkinter and the `os` module are included with standard Python installations in most cases, so they do not need to be installed through pip.

### 3. Check the Haar Cascade File

Make sure `haarcascade_frontalface_default.xml` is located in the same folder as `main.py`.

The program needs this file to detect faces. If it is missing or cannot be loaded, the application will stop and display an error message.

## How to Run the Application

1. Open the project in your preferred Python IDE, such as PyCharm, or open a terminal in the project folder.
2. Run the Python program:

   ```bash
   python main.py
   ```

3. A file selection window will appear.
4. Choose a photo from your computer.
5. Wait for the program to process the selected image.
6. View the results in the OpenCV image windows.
7. Press any key while an image window is active to close the windows.
8. Open the `Modified output` folder to view the saved images.

## Image Processing Features

### 1. Image Operations

The program loads the selected photo, checks whether it was loaded successfully, and resizes large images while maintaining their proportions.

### 2. Haar Cascade Face Detection

The program converts the image to grayscale and applies Gaussian blur to reduce small variations in pixel values. Haar Cascade then searches for possible faces at different scales.

### 3. Head Blur Effect

The application applies a strong Gaussian blur to detected face regions. This can help protect privacy by making faces less recognizable.

### 4. Face Annotation

Green rectangles and labels identify detected faces. The program also displays the total number of faces detected in the image.

### 5. Save and Display Results

The program displays the original image, grayscale image, blurred-face image, and annotated image. It saves the grayscale, head blur, and face detection results in the `Modified output` folder.

## Limitations

- Face detection may fail when faces are turned sideways, covered, too small, or poorly lit.
- Haar Cascade may miss some faces or detect objects that are not faces.
- The blur effect only applies to detected face regions. Undetected faces will remain unblurred.
- The program processes still images rather than live video.
- The privacy protection is not guaranteed because face detection is not always accurate.

## Conclusion

This project demonstrates how OpenCV can be used for image processing, face detection, image transformation, annotation, and saving results. It also shows how Python libraries can work together to create a simple image-processing application.

Possible improvements include improving face detection accuracy, adding more image filters, allowing users to adjust the blur strength, and supporting video processing.
