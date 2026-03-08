import tkinter as tk
import time

def start_boot():
    root = tk.Tk()
    root.title("AryaOS Bootloader")
    root.geometry("600x400")
    root.configure(bg="black")

    label = tk.Label(
        root,
        text="Starting AryaOS...",
        fg="lime",
        bg="black",
        font=("Consolas", 20)
    )

    label.pack(expand=True)

    root.update()
    time.sleep(2)

    root.destroy()

    from login import start_login
    start_login()