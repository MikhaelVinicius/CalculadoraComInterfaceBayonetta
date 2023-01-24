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
        for row_values in (buttons):
            for button in row_values:
                button_text = button['text']
                if button_text == 'C':
                    button.bind('<Button-1>', self.clear)
                if button_text in '0123456789.+-/*()^':
                    button.bind('<Button-1>', self.add_text_to_display)
                    if button_text in '=':
                        button.bind('<Button-1>', self.calculate)
    def _config_display(self):
        fixed_text = self._fix_text(self.display.get())

    def _fix_text(self, text):
        #Expressões irregulares biblioteca re

        #substitui tudo que não estiver no teclado da cal

        text = re.sub(r'[^\d\.\/\*\-\+\*\^e]',r'', text)
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
        print('Realizando conta')





