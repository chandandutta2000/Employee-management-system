import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Webcam not working")
    exit()
else:
    print("Webcam activated")

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()
    if not ret:
        print("Error: could not captured the image")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))

    if len(faces)>0:
        (x,y,w,h) = faces[0]
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('SingleFaceDetection', frame)

        if cv2.waitKey(1)==27:
            break
cap.release()
cv2.destroyAllWindows()