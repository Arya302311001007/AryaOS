# AryaOS

AryaOS is a Python-based GUI Operating System simulation built using Tkinter.
It simulates the basic components of a modern operating system such as a desktop environment, taskbar, start menu, system applications, and AI assistant integration.

This project is designed to demonstrate concepts of operating systems, GUI development, and AI integration using Python.

---

## Features

* Bootloader simulation
* Login system
* Desktop environment
* Taskbar and Start Menu
* Window management system
* Built-in applications:

  * Notepad
  * Terminal
  * File Explorer
  * Task Manager
* Jarvis AI Assistant integration
* Modular architecture for easy expansion

---

## Technologies Used

* Python 3
* Tkinter (GUI framework)
* VS Code
* Git & GitHub

Optional libraries used in extended features:

* speech_recognition
* pyttsx3
* gTTS
* pygame
* requests
* Google Gemini API

---

## Project Structure

AryaOS is organized into multiple modules for maintainability.

```
AryaOS
│
├── core
│   ├── bootloader.py
│   ├── desktop.py
│   └── window_manager.py
│
├── apps
│   ├── notepad.py
│   ├── terminal.py
│   ├── file_explorer.py
│   └── task_manager.py
│
├── ai
│   └── jarvis_integration.py
│
├── assets
│
├── main.py
├── README.md
└── requirements.txt
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/Arya302311001007/AryaOS.git
```

2. Navigate to the project folder

```
cd AryaOS
```

3. Create a virtual environment

```
python -m venv .venv
```

4. Activate the environment

Windows:

```
.venv\Scripts\activate
```

5. Install dependencies

```
pip install -r requirements.txt
```

---

## Running AryaOS

Run the main file:

```
python main.py
```

The AryaOS desktop environment will start.

---

## Future Improvements

* Built-in web browser
* System settings panel
* File system simulation
* Notification center
* Multi-window management
* Improved Jarvis AI integration
* Better UI inspired by Windows 11

---

## Learning Goals

This project explores concepts related to:

* Operating System design
* Desktop environments
* Window management
* Process simulation
* GUI programming with Tkinter
* AI integration into system software

---

## Author

Arya Das
Python Developer | AI Enthusiast

GitHub: https://github.com/Arya302311001007

---

## License

This project is for educational and experimental purposes.
