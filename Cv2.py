# from cv2 import *
import cv2
# import cv2* is used for calling the inbuilt functions of cv2. like cv2.insow
# from cv2 import* we can directly use the cv2's inbuilt function and there is no need to use cv2.function() again and again
# it will read the file like jpg

# operation...
# iamread()
# iamwrite()
# iamshow()
# waitKey()
# destroyAllWindows()

# a = iamread("")
# # "abc.jpg",1 for coloured image and 0 is for grey scale
# iamshow("MyWindow",a)
# iamshow("Cropped",cropped)
# waitKey(200)
# # 2000 is for the timing
# iamwrite("FileName.png",a)
#
# destroyallWindows()

# captured live stream from the webcam

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(* 'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))#fourcc is a code used to compress the frame
while(True):
    ret, frame = cap.read()# ret  will checjk if frame is available then  it will treturn true otherwise will return false
    # and frame variable will captured and save the video
    # converting the video into greyscale
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))


        out.write(frame)

        # grey = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('c'): #  0xFF == ord('q'): it is a mask for 64 bits
          break
    else:
       break
        


cap.release()
out.release()
cv2.destroyAllWindows()