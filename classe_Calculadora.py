import math
import tkinter as tk
from typing import List
import re


class Calcu:
    def __init__(self, root: tk.Tk, label: tk.Label, display: tk.Entry, buttons: List[List[tk.Button]]):
        self.root= root
        self.label = label
        self.display = display
        self.buttons = buttons

    def start(self):

        self.config_buttons()
        self._config_display()
        self.root.mainloop()
    def config_buttons(self):
        buttons = self.buttons
        for row_values in buttons:
            for button in row_values:
                button_text = button['text']
                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)
                    if button_text in '=':
                        button.bind('<Button-1>', self.calculate)
    def _config_display(self):
       ...

    def _fix_text(self, text):
        #Expressões irregulares biblioteca re

        #substitui tudo que não estiver no teclado da cal

        text = re.sub(r'[^\d\.\/\*\-\+\*\^e]',r'', text,0)
        #substitui sinais repetidos


        text = re.sub(r'([\.\+\/\*\-\^])\1+', r'\1', text,0)

        #substitui iss () ou ** para nada
        text = re.sub(r'\*?\(\)', '',text)


        return text
    def clear(self, event = None):
        self.display.delete(0, 'end')

    def add_text_to_display(self, event=None):
        self.display.insert('end', event.widget['text'])


    def calculate(self,event= None):
        fixed_text = self._fix_text(self.display.get())
        equation = self._get_equations(fixed_text)

        try:
            if len(equation) == 1:
                result = eval(self._fix_text(equation[0]))
            else:
                result = eval(self._fix_text(equation[0]))
                for equation in equation[1:]:
                    result = math.pow(result, eval(self._fix_text(equation)))

            self.display.delete(0, 'end')
            self.display.insert('end', result)
            self.label.config(text=f'{fixed_text} = {result}')


        except OverflowError:
            self.label.config(text="Sorry, não posso realizar essa conta")
        except Exception:
            self.label.config(text = "Erro")

    def _get_equations(self, text):
        return re.split(r'\^', text, 0)




