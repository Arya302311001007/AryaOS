import tkinter as tk
import subprocess
import os

def open_terminal():

    window = tk.Toplevel()
    window.title("AryaOS Terminal")
    window.geometry("700x450")
    window.configure(bg="black")

    text = tk.Text(
        window,
        bg="black",
        fg="lime",
        insertbackground="white",
        font=("Consolas", 11)
    )
    text.pack(expand=True, fill="both")

    current_dir = os.getcwd()

    # Linux → Windows command translation
    def translate_command(command):

        parts = command.strip().split()

        if len(parts) == 0:
            return command

        cmd = parts[0]

        if cmd == "ls":
            return "dir"

        elif cmd == "clear":
            return "cls"

        elif cmd == "pwd":
            return "cd"

        elif cmd == "rm":
            return "del " + " ".join(parts[1:])

        elif cmd == "cp":
            return "copy " + " ".join(parts[1:])

        elif cmd == "mv":
            return "move " + " ".join(parts[1:])

        else:
            return command

    def show_prompt():
        text.insert("end", f"{current_dir} > ")
        text.mark_set("insert", "end")

    text.insert("end", "AryaOS Terminal (Linux + Windows supported)\n")
    show_prompt()

    def run_command(event):

        nonlocal current_dir

        line = text.get("insert linestart", "insert lineend")

        command = line.split(">")[-1].strip()

        if command == "":
            text.insert("end", "\n")
            show_prompt()
            return "break"

        # Handle cd separately
        if command.startswith("cd "):
            path = command[3:]
            try:
                os.chdir(path)
                current_dir = os.getcwd()
            except:
                text.insert("end", "\nDirectory not found\n")
            show_prompt()
            return "break"

        # Translate Linux command → Windows
        command = translate_command(command)

        if command == "cls":
            text.delete("1.0", "end")
            show_prompt()
            return "break"

        result = subprocess.getoutput(command)

        text.insert("end", "\n" + result + "\n")

        show_prompt()
        text.see("end")

        return "break"

    text.bind("<Return>", run_command)