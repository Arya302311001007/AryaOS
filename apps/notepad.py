import tkinter as tk
from core.process_manager import register_process, unregister_process

def open_notepad():

    window = tk.Toplevel()
    window.title("Notepad")
    window.geometry("500x400")

    register_process("Notepad")

    def on_close():
        unregister_process("Notepad")
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)

    text_area = tk.Text(window)
    text_area.pack(expand=True, fill="both")