import cv2
import numpy as np
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk

class ColorRecognitionApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.vid = cv2.VideoCapture(0)
        
        self.canvas = tk.Canvas(window, width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH), height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        self.selected_color_label = Label(window, text="Selected BGR Color: ", bg="white", fg="black", font=("Helvetica", 12))
        self.selected_color_label.pack(anchor=tk.CENTER, expand=True)
        
        self.clicked_hsv_value = None
        self.selected_colour_bgr = None
        
        self.canvas.bind("<Button-1>", self.pick_color)
        
        self.update()
        self.window.mainloop()

    def pick_color(self, event):
        ret, frame = self.vid.read()
        if ret:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            self.clicked_hsv_value = hsv[event.y, event.x]
            self.selected_colour_bgr = frame[event.y, event.x]
            self.selected_color_label.config(text=f"Selected BGR Color: {self.selected_colour_bgr}")

    def update(self):
        ret, frame = self.vid.read()
        if ret:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            if self.clicked_hsv_value is not None:
                lower_hsv = np.array([self.clicked_hsv_value[0] - 10, 100, 100])
                upper_hsv = np.array([self.clicked_hsv_value[0] + 10, 255, 255])
                
                mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
                contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                
                for contour in contours:
                    area = cv2.contourArea(contour)
                    if area > 500:
                        x, y, w, h = cv2.boundingRect(contour)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (167, 49, 195), 2)
                        cv2.putText(frame, 'Color', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (195, 86, 114), 2)
            
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        
        self.window.after(10, self.update)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

if __name__ == "__main__":
    ColorRecognitionApp(tk.Tk(), "Tkinter and OpenCV")



