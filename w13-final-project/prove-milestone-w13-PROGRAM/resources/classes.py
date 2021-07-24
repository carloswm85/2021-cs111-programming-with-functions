import tkinter as tk
import webbrowser
from tkinter import Menu, ttk
from tkinter.messagebox import showerror

"""
Main class.
Creates the application window.
"""


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Temperature Converter')
        self.geometry('390x90')
        self.resizable(False, False)


"""
Main frame for the application.
Widgets are set here.
"""


class ConverterFrame(ttk.Frame):

    current_state = "fahrenheit"

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
        self.temperature_button = ttk.Button(
            self, text='Fahrenheit to Celsius', padding=5)
        self.temperature_button['command'] = self.switch_text
        self.temperature_button.grid(column=0, row=0, sticky=tk.W, **options)

        # temperature entry
        self.temperature = tk.StringVar()  # value holder object
        self.temperature_entry = ttk.Entry(self, textvariable=self.temperature)
        self.temperature_entry.grid(column=1, row=0, **options)
        self.temperature_entry.focus()

        # convert button
        self.convert_button = ttk.Button(self, text='Convert', padding=5)
        # Assign the command option of the convert button to the self.convert method
        self.convert_button['command'] = self.convert
        self.convert_button.grid(column=2, row=0, sticky=tk.W, **options)

        # result label
        self.result_label = ttk.Label(self, text='Result appears here.')
        self.result_label.grid(row=1, columnspan=3, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def switch_text(self):
        """
                Switches places of some words
                in a string.
                """
        if self.current_state == "fahrenheit":
            self.temperature_button.config(text='Celsius to Fahrenheit')
            self.current_state = "celsius"
        elif self.current_state == "celsius":
            self.temperature_button.config(text='Farenheit to Celsius')
            self.current_state = "fahrenheit"

    def convert(self):
        """
                Handle button click event.
                Only numbers are allowed.
        """
        try:
            temperature_input = float(self.temperature.get())
            result = "Temperature..."
            if self.current_state == "fahrenheit":
                temperature_output = fahrenheit_to_celsius(temperature_input)
                print(f'TO CONSOLE: {temperature_input} Fahrenheit = {temperature_output:.2f} Celsius')
                result = f'{temperature_input} Fahrenheit = {temperature_output:.2f} Celsius'
            elif self.current_state == "celsius":
                temperature_output = celsius_to_fahrenheit(temperature_input)
                print(f'TO CONSOLE: {temperature_input} Celsius = {temperature_output:.2f} Fahrenheit')
                result = f'{temperature_input} Fahrenheit = {temperature_output:.2f} Celsius'
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


"""
Top Level Window, for displaying
information about the program.
"""


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


"""
Main methods for the application.
"""
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius):
    return celsius * (9/5) + 32

