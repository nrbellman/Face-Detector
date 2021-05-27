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
import cv2
from PIL import Image, ImageTk
import numpy as np
import tkinter as tk
#-------------------------------------------------------------------------------

if (__name__ == "__main__"):

    #----GUI Setup----------------------------------------------------------
    window = tk.Tk()
    window.wm_title("Face Detector")
    window.config(bg='#FFFFFF', padx = 10, pady = 10)

    # Graphics Window
    img_frame = tk.Frame(window, width = 640, height = 480)
    img_frame.grid(row = 0, column = 0, padx = 5, rowspan = 2)

    face_frame = tk.Frame(window, width = 240, height = 240)
    face_frame.grid(row = 0, column = 1, padx = 10)

    ctrl_frame = tk.Frame(window, width = 240, height = 240)
    ctrl_frame.grid(row = 1, column = 1, padx = 10)

    # Video Capture
    lmain = tk.Label(img_frame)
    lmain.grid(row = 0, column = 0, rowspan = 1)

    v_cap = cv2.VideoCapture(0)
    #-----------------------------------------------------------------------

    #----Functions----------------------------------------------------------
    def show_frame():
        ret, frame = v_cap.read()
        frame = cv2.flip(frame, 1)

        cv2_img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2_img)
        tk_img = ImageTk.PhotoImage(image = img)

        lmain.imgtk = tk_img
        lmain.configure(image = tk_img)
        lmain.after(10, show_frame)
    #-----------------------------------------------------------------------


    show_frame()
    window.mainloop()

#----End File-------------------------------------------------------------------