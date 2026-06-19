# 📂 File Organizer

A modern Python-based desktop application that automatically organizes files into categorized folders based on their file extensions.

Built with **Python**, **Tkinter**, and packaged as a standalone Windows application using **PyInstaller** and **Inno Setup**.

---

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

*Add screenshot here*

### Preview Mode

*Add screenshot here*

### Before and After Organization

*Add screenshots here*

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
