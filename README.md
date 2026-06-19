# 📂 File Organizer

A modern Python-based desktop application that automatically organizes files into categorized folders based on their file extensions.

Built with **Python**, **Tkinter**, and packaged as a standalone Windows application using **PyInstaller** and **Inno Setup**.

---
## 📥 Download

https://github.com/neeshoo/file-organizer/releases/download/v1.0.0/FileOrganizerSetup.exe

## ✨ Features

* 📁 Automatically organizes files by extension
* 👀 Preview mode before organizing files
* 🗂️ Custom categories support using `categories.json`
* 🔄 Duplicate file handling
* 📝 Activity logging with `log.txt`
* 🖥️ Simple and user-friendly GUI
* 📦 Standalone Windows installer (`setup.exe`)
* ⚙️ No Python installation required for end users

---

## 📸 Screenshots

### Main Interface


<img width="987" height="717" alt="2" src="https://github.com/user-attachments/assets/a60aa708-cc28-4b2d-9ecb-b25369479e30" />

### Preview Mode

<img width="1137" height="839" alt="preview" src="https://github.com/user-attachments/assets/869df31d-7f23-42a1-ae73-ef5e37213a30" />


### Before and After Organization

<img width="1688" height="893" alt="before" src="https://github.com/user-attachments/assets/db19a773-50b7-4ca6-a444-3e407f3f78bb" />

<img width="1754" height="784" alt="after" src="https://github.com/user-attachments/assets/6e004e1a-2aa4-43e8-bc52-a323f50da0c4" />



---

## 🛠️ Tech Stack

* Python 3.13
* Tkinter
* JSON
* PyInstaller
* Inno Setup
* Git & GitHub

---

## 📂 Project Structure

```text
file-organizer/
├── gui.py
├── organizer.py
├── categories.py
├── categories.json
├── README.md
├── .gitignore
├── dist/
└── installer/
```

---

## 🚀 Installation

### Option 1: Download Installer

1. Download the latest `FileOrganizerSetup.exe` from the Releases section.
2. Run the installer.
3. Follow the setup instructions.
4. Launch File Organizer from the desktop shortcut.

### Option 2: Run from Source Code

Clone the repository:

```bash
git clone https://github.com/neeshoo/file-organizer.git
cd file-organizer
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python gui.py
```

---

## ⚙️ Custom Categories

You can create your own categories by editing the `categories.json` file.

Example:

```json
{
  "Designs": [".psd", ".fig"],
  "Data": [".csv", ".xlsx"]
}
```

---

## 🔮 Future Improvements

* Dark mode support
* Drag and drop functionality
* Automatic Downloads folder monitoring
* Scheduled organization
* Undo last operation
* Modern UI with CustomTkinter

---

## 👨‍💻 Author

**Neeshoo Jangid**

GitHub: https://github.com/neeshoo

---

## 📄 License

This project is licensed under the MIT License.
