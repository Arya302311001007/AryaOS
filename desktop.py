import tkinter as tk
import sys
import time

# Import apps
from apps.notepad import open_notepad
from apps.terminal import open_terminal
from apps.file_explorer import open_file_explorer
from apps.task_manager import open_task_manager
from apps.jarvis_app import open_jarvis
from apps.calculator import open_calculator
from apps.browser import open_browser


def start_desktop(username):

    root = tk.Tk()
    root.title("AryaOS Desktop")
    root.geometry("1000x700")
    root.configure(bg="#1e90ff")

    # ======================
    # WELCOME TEXT
    # ======================

    welcome = tk.Label(
        root,
        text=f"Welcome {username}",
        font=("Segoe UI", 18),
        bg="#1e90ff",
        fg="white"
    )
    welcome.place(x=20, y=20)

    # ======================
    # DESKTOP ICONS
    # ======================

    icon_frame = tk.Frame(root, bg="#1e90ff")
    icon_frame.place(x=20, y=70)

    tk.Button(
        icon_frame,
        text="Notepad",
        width=12,
        height=2,
        command=open_notepad
    ).pack(pady=5)

    tk.Button(
        icon_frame,
        text="Terminal",
        width=12,
        height=2,
        command=open_terminal
    ).pack(pady=5)

    tk.Button(
        icon_frame,
        text="Calculator",
        width=12,
        height=2,
        command=open_calculator
    ).pack(pady=5)

    tk.Button(
        icon_frame,
        text="Browser",
        width=12,
        height=2,
        command=open_browser
    ).pack(pady=5)

    tk.Button(
        icon_frame,
        text="Jarvis AI",
        width=12,
        height=2,
        command=open_jarvis
    ).pack(pady=5)

    # ======================
    # TASKBAR
    # ======================

    taskbar = tk.Frame(
        root,
        bg="#202020",
        height=40
    )
    taskbar.pack(side="bottom", fill="x")

    # ======================
    # START MENU
    # ======================

    start_menu = tk.Frame(
        root,
        bg="#2b2b2b",
        width=200,
        height=400
    )

    start_menu_visible = False

    def toggle_start_menu():
        nonlocal start_menu_visible

        if start_menu_visible:
            start_menu.place_forget()
            start_menu_visible = False
        else:
            root.update_idletasks()
            menu_height = 400
            taskbar_height = 40
            y_position = root.winfo_height() - menu_height - taskbar_height
            start_menu.place(x=0, y=y_position)
            start_menu_visible = True

    start_menu.place_forget()

    # ======================
    # SYSTEM FUNCTIONS
    # ======================

    def shutdown():
        root.destroy()
        sys.exit()

    def restart():
        root.destroy()
        from boot import start_boot
        start_boot()

    # ======================
    # START BUTTON
    # ======================

    start_button = tk.Button(
        taskbar,
        text="Start",
        bg="#202020",
        fg="white",
        border=0,
        font=("Segoe UI", 10),
        command=toggle_start_menu
    )

    start_button.pack(side="left", padx=10)

    # ======================
    # CLOCK
    # ======================

    clock_label = tk.Label(
        taskbar,
        fg="white",
        bg="#202020",
        font=("Segoe UI", 10)
    )

    clock_label.pack(side="right", padx=10)

    def update_clock():
        current_time = time.strftime("%H:%M:%S")
        clock_label.config(text=current_time)
        root.after(1000, update_clock)

    update_clock()

    # ======================
    # START MENU BUTTONS
    # ======================

    tk.Button(
        start_menu,
        text="Notepad",
        width=20,
        command=open_notepad
    ).pack(pady=5)

    tk.Button(
        start_menu,
        text="Terminal",
        width=20,
        command=open_terminal
    ).pack(pady=5)

    tk.Button(
        start_menu,
        text="File Explorer",
        width=20,
        command=open_file_explorer
    ).pack(pady=5)

    tk.Button(
        start_menu,
        text="Task Manager",
        width=20,
        command=open_task_manager
    ).pack(pady=5)

    tk.Button(
        start_menu,
        text="Calculator",
        width=20,
        command=open_calculator
    ).pack(pady=5)

    tk.Button(
        start_menu,
        text="Browser",
        width=20,
        command=open_browser
    ).pack(pady=5)

    tk.Button(
        start_menu,
        text="Jarvis AI",
        width=20,
        command=open_jarvis
    ).pack(pady=5)

    tk.Button(
        start_menu,
        text="Shutdown",
        width=20,
        command=shutdown
    ).pack(pady=5)

    tk.Button(
        start_menu,
        text="Restart",
        width=20,
        command=restart
    ).pack(pady=5)

    # ======================
    # MAIN LOOP
    # ======================

    root.mainloop()