#----File Information-----------------------------------------------------------
#   
#   Project:        Face Detector
#   Filename:       face-detector.py
#   Author:         Nicholas Bellman
#   Author Email:   nbellman95@gmail.com
#   Description:    
#
#-------------------------------------------------------------------------------

#----Imports--------------------------------------------------------------------
from tkinter.constants import CENTER
import cv2
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
#-------------------------------------------------------------------------------

#----Constants/Globals----------------------------------------------------------
DARK = '#3B3B3B'
LIGHT = '#FFFFFF'

CV2_RED = (0, 0, 255)
CV2_GREEN = (0, 255, 0)
CV2_BLUE = (255, 0, 0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 
                                     'haarcascade_frontalface_default.xml')
#-------------------------------------------------------------------------------

if (__name__ == "__main__"):

    #----GUI Setup----------------------------------------------------------
    window = tk.Tk()
    window.title("Face Detector")
    window.resizable(0, 0)
    window.config(bg = DARK, padx = 10, pady = 10)

    # Graphics Window
    img_frame = tk.Frame(window, width = 640, height = 480, bg = DARK)
    img_frame.grid(row = 0, column = 0, padx = 5, rowspan = 2)

    face_frame = tk.Frame(window, width = 240, height = 240)
    face_frame.grid(row = 0, column = 1, padx = 10)

    ctrl_frame = tk.Frame(window, width = 240, height = 240, bg = DARK)
    ctrl_frame.grid(row = 1, column = 1, padx = 10)

    # Video Capture
    display_main = tk.Label(img_frame, bg = DARK)
    display_main.grid(row = 0, column = 0, rowspan = 1)

    display_face = tk.Label(face_frame, bg = DARK, width = 240, height = 240)
    display_face.grid(row = 1, column = 1)

    v_cap = cv2.VideoCapture(0)
    #-----------------------------------------------------------------------

    #----Functions----------------------------------------------------------
    def show_frame():
        ret, frame = v_cap.read()
        frame = cv2.flip(frame, 1)
        blank = frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        global face_img
        faces = face_cascade.detectMultiScale(gray, 1.2, 4)
        for (x, y, w, h) in faces:
            #cv2.rectangle(frame, (x,y), (x+w, y+h), CV2_GREEN, 2)
            a, b = (250 - w) // 2, (250 - h) // 2
            face_img = blank[y-b:y+h+b, x-a:x+w+a]
        
        cv2_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2_img)
        tk_img = ImageTk.PhotoImage(image = img)
        
        display_main.image = tk_img
        display_main.configure(image = tk_img)
        
        try:
            cv2_face = cv2.cvtColor(face_img, cv2.COLOR_BGR2RGB)
            f_img = Image.fromarray(cv2_face)
            f_img.resize((240,240))
            f_tk_img = ImageTk.PhotoImage(image = f_img)

            display_face.image = f_tk_img
            display_face.configure(image = f_tk_img, anchor = CENTER)
        except:
            pass
        
        window.after(33, show_frame)
    #-----------------------------------------------------------------------


    show_frame()
    window.mainloop()

#----End File-------------------------------------------------------------------