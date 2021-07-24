import tkinter as tk
import webbrowser
from tkinter import Menu, ttk
from tkinter.messagebox import showerror


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


class Window(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("About")
        self.geometry("250x105")

        self.label = tk.Label(
            self, text="This program was made\nby Carlos W. Mercado\nas a final project for CSE111 class.\nBYU-I Spring 2021.")
        self.label.pack()

        self.button = ttk.Button(self, text="Close", command=self.destroy)
        self.button.pack()


class ConverterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        # field options
        options = {'padx': 5, 'pady': 5}

        # Assign the widgets to the self object so that you can reference them in other methods of the ConverterFrame class.

        # MENU
        self.menu = Menu(self)
        container.config(menu=self.menu)

        self.helpmenu = Menu(self.menu, tearoff=False)

        self.menu.add_cascade(label='Menu', menu=self.helpmenu)

        self.menu.add_command(label='Exit program', command=self.quit)
        self.helpmenu.add_command(
            label='Python Documentation', command=self.open_python)
        self.helpmenu.add_command(label='About', command=self.about_window)

        # TEMPERATURE
        # temperature label
        self.temperature_label = ttk.Label(self, text='Fahrenheit to Celsius')
        self.temperature_label.grid(column=0, row=0, sticky=tk.W, **options)

        # temperature entry
        self.temperature = tk.StringVar()  # value holder object
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, **options)
        self.temperature_entry.focus()

        # convert button
        self.convert_button = ttk.Button(self, text='Convert')
        # Assign the command option of the convert button to the self.convert method
        self.convert_button['command'] = self.convert
        self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)

        # result label
        self.result_label = ttk.Label(self, text='Result appears here.')
        self.result_label.grid(row=1, columnspan=3, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def convert(self):
        """
                Handle button click event.
                Only numbers are allowed.
                """
        try:
            f = float(self.temperature.get())
            c = fahrenheit_to_celsius(f)
            print(f'TO CONSOLE: {f} Fahrenheit = {c:.2f} Celsius')
            result = f'{f} Fahrenheit = {c:.2f} Celsius'
            self.result_label.config(text=result)
        except ValueError as error:
            error_str = str(error)
            error_str_beautified = error_str.capitalize() + "\nPlease, use only numbers."
            showerror(title='Error', message=error_str_beautified)

    def open_python(self):
        url = 'https://docs.python.org/'
        webbrowser.open_new(url)

    def about_window(self):
        window = Window(self)
        window.grab_set()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Temperature Converter')
        self.geometry('365x75')
        self.resizable(False, False)
