import tkinter as tk


def main():
    root = tk.Tk()
    frm_main = tk.Frame(root)
    frm_main.master.title("Circle Area")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)
    populate_main_window(root)

    root.mainloop()
    

def populate_main_window(window):
    # SECTION 1: FOLDER PATH
    label_path = tk.Label(window, text="Folder Location")
    label_path.grid(row=0, column=0)

    input_path = tk.StringVar()
    entry_path = tk.Entry(window, textvariable=input_path)
    entry_path.grid(row=0, column=1)

    button_path = tk.Button(window, text="Open Path", width=12)
    button_path.grid(row=0, column=2)

    # SECTION 2: LEVEL 1
    label_1 = tk.Label(window, text="Level 1")
    label_1.grid(row=1, column=0)

    input_1 = tk.StringVar()
    entry_1 = tk.Entry(window, textvariable=input_1)
    entry_1.grid(row=1, column=1)

    # SECTION 3, Options
    checkbox_1 = tk.Checkbutton(window)
    checkbox_1.grid(row=2, column=0)

    label_checkbox_1 = tk.Label(
        window, text="Make just text for the folder structure")
    label_checkbox_1.grid(row=2, column=1)

    # DEFINE LISTBOX, scrollbar for the list
    list_1 = tk.Listbox(window, height=6, width=45)
    list_1.grid(row=3, column=0, rowspan=6, columnspan=2)

    # Attach scrollbar to list
    scrollbar_1 = tk.Scrollbar(window)
    scrollbar_1.grid(row=3, column=2, rowspan=6)

    list_1.configure(yscrollcommand=scrollbar_1.set)
    scrollbar_1.configure(command=list_1.yview)

    # BOTTOM
    button_copy_result = tk.Button(text="Copy")
    button_copy_result.grid(row=3, column=2)

    # DISPLAY THE WINDOW
    window.wm_title("Folder Structure Maker")


if "__name__" == "__main__":
    main()

