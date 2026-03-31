 
import cv2 


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') 

# capture frames from a camera
cap = cv2.VideoCapture(0)

# loop runs if capturing has been initialized.
while 1: 

    # reads frames from a camera
    ret, img = cap.read()
    img=cv2.flip(img,1)

    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)==0:
        warning_text="PAY ATTENTION!!!!!"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        thickness = 2
        (text_w, text_h), _ = cv2.getTextSize(warning_text, font, font_scale, thickness)
        img_h, img_w = img.shape[:2]
        text_x = (img_w - text_w) // 2
        text_y = (img_h + text_h) // 2
        cv2.putText(img, warning_text, (text_x, text_y), font, font_scale, (0, 0, 255), thickness)
    else:

        for (x,y,w,h) in faces:
        # To draw a rectangle in a face 
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            # Detects eyes of different sizes in the input image
            eyes = eye_cascade.detectMultiScale(roi_gray) 
            if len(eyes)==0:
                warning_text="PAY ATTENTION!!!!!"
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                thickness = 2
                (text_w, text_h), _ = cv2.getTextSize(warning_text, font, font_scale, thickness)
                img_h, img_w = img.shape[:2]
                text_x = (img_w - text_w) // 2
                text_y = (img_h + text_h) // 2
                cv2.putText(img, warning_text, (text_x, text_y), font, font_scale, (0, 0, 255), thickness)
            else:

                #To draw a rectangle in eyes
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
    corrected_=cv2.flip(img,1)
    #corrected_=cv2.flip(corrected_,1)

    # Display an image in a window
    cv2.imshow('img',img)

    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()