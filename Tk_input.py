from tkinter import *
from tkinter import ttk
from tkinter import messagebox

STR = "str"
INT = "int"
FLOAT = "float"
ALL = "all"

def input_tk(type_func = NONE, icon = None, title = "Title your gui", text = "Here your info", fg = "black", justify = LEFT,
              title_msg = "None", message = "None"):
    """
    This function accept only your choosed, and parameter this function is :
    type_func: constant, icon: str, title: str, text: str, fg: str, justify: constant, title_msg: str, message: str
    
    and the result of this function is True or False

    Note : You must write a variable and put this function inside it to be able to use the result
    """
    return_num = 0

    gui_tk = Tk()
    if type_func == NONE:
        gui_tk.withdraw()
        gui_tk.quit()
        messagebox.showerror(title="Function Type Error", message="Please choose type your function")
    else:
        gui_tk.iconbitmap(icon)
        gui_tk.title(title)
        gui_tk.resizable(False, False)
        sc1 = gui_tk.winfo_screenwidth()
        show_sc1 = str(round(sc1 / 2 - 115))
        SC2 = gui_tk.winfo_screenheight()
        SHOW_SC2 = str(round(SC2 / 2 - 59.5))
        width_window = 230
        HEIGHT_WINDOW = 119
        gui_tk.geometry(f"{width_window}x{HEIGHT_WINDOW}+{show_sc1}+{SHOW_SC2}")

        gui_tk["bg"] = "#E5E7E9"

        add_text = Text(gui_tk, height=3, bd=0, fg=fg, bg="#E5E7E9", font=("Calibri", 13), state="disabled")
        add_text.place(x=0, y=0, relwidth=1)

        add_text["state"] ="normal"

        add_text.insert(END, text)

        add_text["state"] ="disabled"

        entry = ttk.Entry(gui_tk, justify=justify)
        entry.focus_set()
        entry.place(x=0, y=71, relwidth=1)

        def cancel():
            gui_tk.quit()

        bt_cancel = ttk.Button(gui_tk, text="Cancel", width=7, takefocus=0, command=cancel)
        bt_cancel.place(x=0, y=94)

        def done():
            nonlocal return_num

            if type_func == STR:
                if all(word.isalpha() for word in entry.get().split()) and not entry.get().isspace() and entry.get() != "":
                    return_num = 1
                    gui_tk.quit()
                else:
                    title_msg = "Only text"
                    message = "This is not a text"
                    messagebox.showerror(title=title_msg, message=message)

            elif type_func == INT:
                if  entry.get().isdigit():
                    return_num = 1
                    gui_tk.quit()
                else:
                    title_msg = "Only whole number"
                    message = "This is not an integer"
                    messagebox.showerror(title=title_msg, message=message)

            elif type_func == FLOAT:
                try:
                    if not isinstance(float(entry.get()), int) and "." in entry.get():
                        return_num = 1
                        gui_tk.quit()
                    else:
                        title_msg = "Only decimal number"
                        message = "This is not decimal number"
                        messagebox.showerror(title=title_msg, message=message)
                except ValueError:
                    title_msg = "Only decimal number"
                    message = "This is not decimal number"
                    messagebox.showerror(title=title_msg, message=message)

            elif type_func == ALL:
                if not entry.get() == "" and not entry.get().isspace():
                    return_num = 1
                    gui_tk.quit()
                else:
                    title_msg = "Nothing"
                    message = "This is nothing"
                    messagebox.showerror(title=title_msg, message=message)
        
        bt_done_str = ttk.Button(gui_tk, text="Done", width=6, takefocus=0, command=done)
        bt_done_str.pack(side=BOTTOM)

        def shortcuts(event):
            done()

        entry.bind("<Return>", shortcuts)

        def agin():
            entry.delete(0, END)

        bt_agin = ttk.Button(gui_tk, text="Agin", width=6, takefocus=0, command=agin)
        bt_agin.place(x=184, y=94)

        for cycle_if in range(6):
            if len(title) >= 7:
                width_window += len(title) - 7
                HEIGHT_WINDOW = 119

                sc1 = gui_tk.winfo_screenwidth()
                show_sc1 = str(round(sc1 / 2 - width_window / 2))
                SC2 = gui_tk.winfo_screenheight()
                SHOW_SC2 = str(round(SC2 / 2 - 59.5))
                gui_tk.geometry(f"{width_window}x{HEIGHT_WINDOW}+{show_sc1}+{SHOW_SC2}")

                gui_tk.update_idletasks()
                get_width_window_str = gui_tk.winfo_width()
                width_bt_agin_x_str = bt_agin.winfo_width()
                new_bt_agin_x_str = get_width_window_str - width_bt_agin_x_str
                bt_agin.place(x=new_bt_agin_x_str, y=94)
            else:
                sc1 = gui_tk.winfo_screenwidth()
                show_sc1 = str(round(sc1 / 2 - 115))
                SC2 = gui_tk.winfo_screenheight()
                SHOW_SC2 = str(round(SC2 / 2 - 59.5))
                width_window = 230
                HEIGHT_WINDOW = 119
                gui_tk.geometry(f"{width_window}x{HEIGHT_WINDOW}+{show_sc1}+{SHOW_SC2}")
                bt_agin.place(x=184, y=94)

        gui_tk.mainloop()
        if return_num == 1:
            return True
