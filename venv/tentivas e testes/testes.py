from tkinter import *
import tkinter.font as font

root = Tk()
root.geometry("380x400")
root.title("Calculator")
root.resizable(0, 0)
inp = StringVar()
myFont = font.Font(size=15)

screen = Entry(root, text=inp, width=30,
               justify='right', font=(10), bd=4)
screen.grid(row=0, columnspan=4, padx=15,
            pady=15, ipady=5)
key_matrix = [["c", u"\u221A", "/", "<-"],
              ["7", "8", "9", "*"],
              ["4", "5", "6", "-"],
              ["1", "2", "3", "+"],
              ["!", 0, ".", "="]]