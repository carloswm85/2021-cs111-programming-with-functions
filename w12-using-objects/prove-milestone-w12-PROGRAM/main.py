from resources.classes import *


def main():
    app = App()
    ConverterFrame(app)
    app.mainloop()


if __name__ == "__main__":
    main()


# TODO: Use .bind method somewhere
# TODO: Use label.configure(text="")  method to clear the field