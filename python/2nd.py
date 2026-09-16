import cv2
import playsound

sound_file = 'sound.wav'

cam = cv2.VideoCapture(0)

while cam.isOpened():
    ret, frame1 = cam.read()
    if not ret:
        break

    
    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    
    ret, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    prev_frame = thresh.copy() 

  
    current_frame = thresh.copy()
    diff = cv2.absdiff(prev_frame, current_frame)

    prev_frame = current_frame

   
    contours, _ = cv2.findContours(diff, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Play sound on motion detection
        playsound.playsound(sound_file)

    # Display the frame with detected motion (optional)
    cv2.imshow('my cam', frame1)

    if cv2.waitKey(200) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()