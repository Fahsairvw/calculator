import tkinter as tk
from keypad import Keypad
from tkinter import ttk
import pygame
from math import log, log2, sqrt, exp


class CalculatorUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.init_component()
        self.config(bg='#E3F4F4')
        pygame.mixer.init()

    def init_component(self):
        self.history = []
        self.display = tk.Label(self, text='', anchor="e", bg='#E3F4F4')
        history = tk.Label(self, text='history', font=("Courier", 10, 'bold'), bg='#97FFF4', anchor="e")
        self.history_list = ttk.Combobox(self, values=self.history, state='readonly', width=5)

        keypad = Keypad(self, ['%', 'ln', 'log2', 'log', '(', ')', 'sqrt', 'DEL', 'CLR'] + list('789456123 0.'), 3)
        operator_pad = Keypad(self, ['exp', '*', '/', '+', '-', '^', '='], 1)

        keypad.bind('<Button>', self.handler_keypress)
        operator_pad.bind('<Button>', self.handler_keypress)
        self.history_list.bind('<<ComboboxSelected>>', self.choose_history)

        history.pack(side=tk.TOP, padx=5, pady=5, anchor='w')
        self.history_list.pack(side=tk.TOP, padx=5, pady=5, anchor='w')
        self.display.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        keypad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        operator_pad.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

    def choose_history(self, event):
        choose = self.history_list.get()
        text = self.display['text'] + choose
        self.display.config(text=text, font=("Courier", 35, 'bold'))

    def handler_keypress(self, event: tk.Event):
        if event.widget['text'] == '=':
            try:
                expression = self.display['text']
                self.history.append(self.display['text'])
                self.history_list['value'] = self.history
                result = eval(expression.replace('ln', 'log'))
                self.display.config(text=str(result), font=("Courier", 35, 'bold'))
            except:
                self.display.config(text="Error:", font=("Courier", 35, 'bold'), fg='red')
                pygame.mixer.Sound(file='sound.mp3').play()
        elif event.widget['text'] == 'DEL':
            functions_to_handle = ['sqrt(', 'ln(', 'log(', 'log2(', 'exp(']
            current_text = self.display['text']
            for func in functions_to_handle:
                le = len(func)-1
                if current_text.endswith(func):
                    text = self.display['text'][:-le]
                    self.display.config(text=text, font=("Courier", 35, 'bold'), fg='black')
            text = self.display['text'][:-1]
            self.display.config(text=text, font=("Courier", 35, 'bold'), fg='black')
        elif event.widget['text'] == 'CLR':
            self.display.config(text='', font=("Courier", 35, 'bold'), fg='black')
        elif event.widget['text'] in ['sqrt', 'ln', 'log2', 'log', 'exp']:
            if self.display['text'][-1].isdigit():
                text = f"sqrt({self.display['text']})"
                self.display.config(text=text, font=("Courier", 35, 'bold'))
            else:
                text = self.display['text'] + event.widget['text'] + '('
                self.display.config(text=text, font=("Courier", 35, 'bold'))

        else:
            text = self.display['text'] + event.widget['text']
            self.display.config(text=text, font=("Courier", 35, 'bold'))

    def run(self):
        self.mainloop()

