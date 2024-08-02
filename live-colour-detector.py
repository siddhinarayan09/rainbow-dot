import cv2
import numpy as np

cap = cv2.VideoCapture(0)

clicked_hsv_value = None
selected_colour_bgr = None

def pick_color(event, x, y, flags, param):
    global clicked_hsv_value
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        clicked_hsv_value = hsv[y, x]
        selected_colour_bgr = frame[y, x]
        print(f"Clicked HSV Value: {clicked_hsv_value}")
        print(f"Selected BGR Colour: {selected_colour_bgr}")

cv2.namedWindow('rt-color-detection')
cv2.setMouseCallback('rt-color-detection', pick_color)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    if clicked_hsv_value is not None:
        lower_hsv = np.array([clicked_hsv_value[0] - 10, 100, 100])
        upper_hsv = np.array([clicked_hsv_value[0] + 10, 255, 255])

        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (167, 49, 195), 2)
                cv2.putText(frame, f'Color', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (195, 86, 114), 2)

    if selected_colour_bgr is not None:
        cv2.rectangle(frame, (10, 10, 100, 100), (int(selected_colour_bgr[0]), int(selected_colour_bgr[1]), int(selected_colour_bgr[2])), -1)
        cv2.putText(frame, 'Selected Colour', (10, 125), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        
    cv2.imshow('rt-color-detection', frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()



