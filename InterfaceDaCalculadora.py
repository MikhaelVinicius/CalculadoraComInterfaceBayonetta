import tkinter as tk


def make_root() -> tk.Tk:

    def UI():
        root = tk.Tk()

        def dimensions():
            root.title('Calculadora')
            root.geometry('400x450+50+50')
            root.resizable(False, False)

        def icon():
            root.iconbitmap('img/umbrellaIcon.ico')


        dimensions()
        icon()
        return root


    return UI()
