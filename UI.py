import numpy as np
import cv2
import tkinter as tk
from tkinter import *
from tkinter import ttk

window=tk.Tk()
window.title("Tabs")
window.geometry('300x300')    
frame = Frame(window)  
frame.pack()  
cap = cv2.VideoCapture(0)

ment = StringVar()






TAB_CONTROL=ttk.Notebook(window)

TAB1  = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text = 'TAB1')

TAB_CONTROL.pack(expand=1, fill="both")

v = tk.IntVar()

tk.Label(TAB1,text="""Enter following data - """,justify = tk.LEFT,padx = 20)

b1 = Button(TAB1,text = "CAPTURE FACE",command = func1,activeforeground = "red",activebackground = "pink",pady=10).pack()

b2 = Button(TAB1,text = "FACE DETECT",command = func,activeforeground = "red",activebackground = "pink",pady=10).pack() 




window.mainloop()
