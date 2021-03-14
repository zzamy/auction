import tkinter
from tkinter import *
import openpyxl
from openpyxl import Workbook
import operator
import pandas as pd
import numpy as np
from playsound import playsound
import datetime
from datetime import datetime
from PIL import Image, ImageTk
import os.path
import cv2

def img_change():
    path = inputBox.get()
    img=tkinter.PhotoImage(file = path)
    label_Img.configure(image=img)
    label_Img.image=img

This_folder = os.path.dirname(os.path.abspath(__file__)) #패스설정
Img_file = os.path.join(This_folder, '0.png')

win = tkinter.Tk()
win.title("이미지 버튼별 표시")
py_Img = tkinter.PhotoImage(file=Img_file)

label_Img = tkinter.Label(win, text="이미지가 표시되는 부분", image=py_Img)
label_Img.pack()

inputBox = tkinter.Entry(win, text="이미지 파일 이름을 입력 하세요")
inputBox.pack()

button = tkinter.Button(win, text = "확인", command=img_change)
button.pack()

win.mainloop