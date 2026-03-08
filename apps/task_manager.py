import tkinter as tk
from core.process_manager import get_processes

def open_task_manager():

    window = tk.Toplevel()
    window.title("Task Manager")
    window.geometry("400x300")

    listbox = tk.Listbox(window)
    listbox.pack(expand=True, fill="both")

    processes = get_processes()

    for process in processes:
        listbox.insert(tk.END, process)