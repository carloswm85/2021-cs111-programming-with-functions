import tkinter as tk

class hello(tk):
    def __init__(self):
        super(hello, self).__init__()
        self.btn = tk.Button(text="Click me", command=self.close())
        self.btn.pack()

    def close(self):
        self.destroy()


app = hello()
app.mainloop()
