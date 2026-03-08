import tkinter as tk
import os

def open_file_explorer():

    window = tk.Toplevel()
    window.title("File Explorer")
    window.geometry("600x400")

    path_label = tk.Label(window, text="C:\\", font=("Segoe UI", 12))
    path_label.pack()

    listbox = tk.Listbox(window)
    listbox.pack(expand=True, fill="both")

    def load_directory(path):
        listbox.delete(0, tk.END)
        path_label.config(text=path)

        try:
            files = os.listdir(path)
            for file in files:
                listbox.insert(tk.END, file)
        except:
            pass

    load_directory(os.getcwd())