from tkinter import *
from tkinter import ttk
import random
import tkinter as tk

GUI = Tk()
GUI.title('Vocabulary')
GUI.geometry('500x400')

word = ['cat','dog','pen','window']

def random_word():
    global word_choice
    word_choice = random.choice(word)
    lb.config(text=word_choice)

def answer():
    if word_choice == 'cat':
        lb_answer.config(text='แมว')
    elif word_choice == 'dog':
        lb_answer.config(text='หมา')
    elif word_choice == 'pen':
        lb_answer.config(text='ปากกา')
    elif word_choice == 'window':
        lb_answer.config(text='หน้าต่าง')

        
random_button = ttk.Button(GUI,text='Random',command=random_word)
random_button.pack(ipadx=10,ipady=10)

answer_button = ttk.Button(GUI,text='Answer',command=answer)
answer_button.pack(ipadx=10,ipady=10)

lb = tk.Label(GUI,text='',font=16)
lb.pack()

lb_answer = tk.Label(GUI,text='',font=16,)
lb_answer.pack()


GUI.mainloop()


