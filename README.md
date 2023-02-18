# Python101
UncleEngineer 

คำสั่งใน GUI 
  -from tkinter import *          
  -from tkinter import ttk
  -import random
  -import tkinter as tk
  -GUI = Tk()     #สร้างหน้าต่าง
  -GUI.title('Vocabulary')      #ตั่งชื่อหน้าต่าง
  -GUI.geometry('500x400')      #กำหนดขนาดหน้าต่าง
  -random_button = ttk.Button(GUI,text='Random',command=random_word)      #สร้างปุ่ม
  -random_button.pack(ipadx=10,ipady=10)      #ตำแหน่งของปุ่ม
  -GUI.mainloop()
