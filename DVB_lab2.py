import cv2

cap = cv2.VideoCapture('cam_video.mp4')

while 1:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    ret, thresh = cv2.threshold(gray, 105, 255, cv2.THRESH_BINARY_INV)

    conturs, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(conturs) > 0:
        c = max(conturs, key = cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.circle(frame, (x + h // 2, y + w // 2), w // 2, (0, 0, 255), 2)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

