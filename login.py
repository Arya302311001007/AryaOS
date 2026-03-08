import tkinter as tk

def start_login():

    def login():
        username = entry.get()

        if username:
            root.destroy()
            from desktop import start_desktop
            start_desktop(username)

    root = tk.Tk()
    root.title("AryaOS Login")
    root.geometry("600x400")

    label = tk.Label(root, text="Enter Username")
    label.pack(pady=20)

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Login", command=login)
    button.pack(pady=20)

    root.mainloop()