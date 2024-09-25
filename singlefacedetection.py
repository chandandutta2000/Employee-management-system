import cv2

# Path to your image file
image_path = 'singleimage.jpeg'  # Replace with the path to your image file

# Load the image
image = cv2.imread(image_path)
if image is None:
    print("Error: Could not load image.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Display the result
cv2.imshow('Face Detection', image)

cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()
