import tkinter as tk

def make_root() -> tk.Tk:
    root = tk.Tk()
    root.title("Calculadora")
    root.config(padx=10, pady=10, background='#fff')
    root.resizable(False, False)

    return root

def Mlabel(root) -> tk.Label:
    label = tk.Label(root, text='0', anchor='e', justify='right', background='#fff')
    label.grid(row = 0, column=0, columnspan=5, sticky='news')
    return label

def make_display(root) -> tk.Entry:
    display = tk.Entry(root)
    display = tk.Entry(root)
    display.grid