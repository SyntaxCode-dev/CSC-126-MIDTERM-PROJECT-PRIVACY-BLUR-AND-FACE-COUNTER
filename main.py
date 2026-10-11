
# Libraries needed for the program
import cv2    # open cv used for image processing, blurring, face detection, and displaying images.
import os     # Python find files in your project folder, especially the Haar Cascade XML file.
import tkinter as tk  # Imports Tkinter, which creates a simple graphical interface for selecting a photo.
from tkinter import filedialog  # Imports the file dialog that lets the user browse their computer and choose an image.

# TOPIC 1: IMAGE OPERATIONS


# SELECT A PHOTO BEFORE PROCESSING
root = tk.Tk()
root.withdraw()
root.update()
# root = tk.Tk()   Creates the main Tkinter window.
# root.withdraw()  Hides the main window because we only need the file-selection dialog.
# root.update()    Processes pending Tkinter window events before opening the dialog.
image_path = filedialog.askopenfilename(
    parent=root,
    title="Choose a photo",
    filetypes=[
        ("Image files", "*.png *.jpg *.jpeg *.bmp"),
        ("All files", "*.*")
    ]
)
# image_path = — Stores the path of the selected file in a variable.
# filedialog.askopenfilename() — Opens the file-selection window.
# parent=root — Associates the dialog with the Tkinter window.

root.destroy()
# Closes the hidden Tkinter window after the file picker finishes.

if not image_path:
    print("No photo selected. Program stopped.")
    raise SystemExit    # raise SystemExit —Stops the program, so it does not continue without a photo.

image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load the selected photo.")
    raise SystemExit

print("Photo selected:", image_path)

# This checks whether the image was loaded successfully.
# If it wasn't found, the program stops instead of continuing with an invalid image.


# Resize the image if it is too large
height, width = image.shape[:2]
# image.shape— Gets the image's height width, measured in pixels and color channels (Blue, Green, Red, or BGR)
# [:2] This selects only the first two values from the shape.
max_width = 600
max_height = 300

scale = min(max_width / width, max_height / height, 1.0)

# max_width / width   # 600 / 1200 = 0.5
# max_height / height # 400 / 800 = 0.5
# 1.0                 # 1.0
#
# scale = min(0.5, 0.5, 1.0)
# # scale = 0.5

# scale — calculates how much to shrink the image while preserving its proportions.
if scale < 1.0:  # 1.0 — prevents the image from becoming larger than its original size.
    image = cv2.resize(
        image,
        (int(width * scale), int(height * scale))
    )
    # If the image is too large, it becomes smaller.
    # If it already fits, its size stays the same.

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Reduce noise before face detection
gray = cv2.GaussianBlur(gray, (3, 3), 0)
# This applies a slight blur to the grayscale image to
# reduce small variations or noise that may interfere with face detection.
# gray — the grayscale image to process.
# (3, 3) — the Gaussian kernel size, covering a 3 × 3 neighborhood around each pixel.
# 0 — lets OpenCV automatically calculate the Gaussian standard deviation (sigmaX).

# ==========================================
# TOPIC 2: HAAR CASCADE FACE DETECTION
# ==========================================

# A. Find the XML file

# CascadeClassifier() loads the face-detection model.
# empty() checks whether it loaded successfully.
# If it failed, the program displays an error and stops.


cascade_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "haarcascade_frontalface_default.xml"
)

face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print("Error: Could not load Haar Cascade!")
    print("Check that the XML file is in your project folder.")
    raise SystemExit

 # Detect faces using the grayscale image
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)
# face_cascade — the pre-trained face detection model loaded earlier.
# detectMultiScale() — searches for faces at different scales.
# gray — the grayscale image that the detector analyzes.
# faces — stores the detected face locations and dimensions.

# scaleFactor=1.1
# Controls how much the image scale changes during detection.

# minNeighbors=5
# Determines how many neighboring detection results must support
# a candidate before it is accepted.
# Higher values usually reduce false detections but may miss some faces.

# minSize=(30, 30)
# Sets the minimum face-detection window to 30 pixels wide and 30 pixels tall.

# ==========================================
# TOPIC 3: IMAGE ANALYSIS AND TRANSFORMATION
# ==========================================

# x	- Horizontal position of the face
# y - Vertical
# w- width of the detected face
# h - height of the detected face
def head_effect(img, detected_faces):
    """Blur detected face regions to help protect privacy."""
    result = img.copy()

    for (x, y, w, h) in detected_faces:
        # Extract the detected face region
        face_region = result[y:y+h, x:x+w]

        # Apply strong Gaussian blur
        blurred_face = cv2.GaussianBlur(
            face_region,
            (51, 51),
            5
        )

        # Replace the original face region
        result[y:y+h, x:x+w] = blurred_face

    return result


# Apply the head blur effect
head_effect_image = head_effect(image, faces)


# ==========================================
# TOPIC 4: FACE ANNOTATION
# ==========================================

output = image.copy()

for number, (x, y, w, h) in enumerate(faces, start=1):

    # Draw a green rectangle around each face
    cv2.rectangle(
        output,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    # Add a label to each detected face
    cv2.putText(
        output,
        f"Face {number}",
        (x, max(y - 10, 20)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 255, 0),
        2
    )

# Count the detected faces
face_count = len(faces)

# Display the total face count
cv2.putText(
    output,
    f"Faces detected: {face_count}",
    (15, 35),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.9,
    (0, 0, 255),
    2
)


# ==========================================
# TOPIC 5: SAVE AND DISPLAY RESULTS
# ==========================================

print("Total faces detected:", face_count)

# Create a folder for saved images
output_folder = "Modified output"
os.makedirs(output_folder, exist_ok=True)
# Save all results
cv2.imwrite(os.path.join(output_folder, "output_grayscale.jpg"), gray)
cv2.imwrite(os.path.join(output_folder, "output_head_effect.jpg"), head_effect_image)
cv2.imwrite(os.path.join(output_folder, "output_faces.jpg"), output)
print("Images saved successfully!")

# Display the results
cv2.imshow("1. Original Image", image)
cv2.imshow("2. Grayscale Image (improve Face Detection)", gray)
cv2.imshow("3. Head Blur Effect (used for privacy)", head_effect_image)
cv2.imshow("4. Face Detection (detect faces,count faces)", output)

print("Press any key on an image window to close.")

cv2.waitKey(0)
cv2.destroyAllWindows()
