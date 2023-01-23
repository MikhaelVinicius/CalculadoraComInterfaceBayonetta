import tkinter as tk
from tkinter import *


def make_root() -> tk.Tk:



    def UI():
        root = tk.Tk()
        entry = tk.StringVar()

        def dimensions():
            root.title('Calculadora')

            root.geometry('400x450+50+50')
            root.resizable(False, False)
           # root.attributes('-alpha', 0.95)

        def frames():
            entry.barra = Frame(root)


        def icon():
            root.iconbitmap('img/umbrellaIcon.ico')

        def buttons():
            one = tk.Button(root, text="1", command= 1).place(x=20, y=30)
            two = tk.Button(root, text="2", command=2).place()
            three = tk.Button(root, text="3", command=3).place()
            four = tk.Button(root, text="4", command=4).place()
            five = tk.Button(root, text="5", command=5).place()
            six = tk.Button(root, text="6", command=6).place()
            seven = tk.Button(root, text="7", command=7).place()
            eight = tk.Button(root, text="8", command=8).place()
            nine = tk.Button(root, text="9", command=9).place()
            zero = tk.Button(root, text="0", command=0).place()

            plus = tk.Button(root, text="+").place()
            minus = tk.Button(root, text="-").place()
            times = tk.Button(root, text="X").place()
            divided = tk.Button(root, text="/").place()
            equals = tk.Button(root, text="=").place()
            clean = tk.Button(root, text="AC").place()
            pRight = tk.Button(root, text="(").place()
            pLeft = tk.Button(root, text=")").place()

        def input():
            cal = StringVar()
            expression_field = tk.Entry(root, textvariable=cal)
            expression_field.grid(columnspan=4, ipadx=70)





        dimensions()
        frames()
        icon()
        buttons()
        return root


    return UI()
