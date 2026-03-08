import tkinter as tk

def open_calculator():

    window = tk.Toplevel()
    window.title("Calculator")
    window.geometry("300x400")

    entry = tk.Entry(window, font=("Arial", 20), justify="right")
    entry.pack(fill="both", padx=10, pady=10)

    def click(value):
        entry.insert("end", value)

    def clear():
        entry.delete(0, "end")

    def calculate():
        try:
            result = eval(entry.get())
            entry.delete(0, "end")
            entry.insert("end", result)
        except:
            entry.delete(0, "end")
            entry.insert("end", "Error")

    buttons = [
        "7","8","9","/",
        "4","5","6","*",
        "1","2","3","-",
        "0",".","=","+"
    ]

    frame = tk.Frame(window)
    frame.pack()

    row = 0
    col = 0

    for btn in buttons:

        action = lambda x=btn: click(x) if x != "=" else calculate()

        tk.Button(
            frame,
            text=btn,
            width=5,
            height=2,
            command=action
        ).grid(row=row, column=col)

        col += 1

        if col > 3:
            col = 0
            row += 1

    tk.Button(window, text="Clear", command=clear).pack(fill="both")