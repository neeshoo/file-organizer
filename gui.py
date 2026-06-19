import tkinter as tk
from tkinter import filedialog, messagebox

from organizer import organize_files




def browse_folder():
    folder = filedialog.askdirectory()

    if folder:
        folder_path.set(folder)


def start_organizing():

    path = folder_path.get()

    if not path:
        messagebox.showwarning(
            "Warning",
            "Please select a folder first."
        )
        return

    try:
        organize_files(path)

        status_label.config(
            text="Files organized successfully!",
            fg="green"
        )

    except Exception as e:

        status_label.config(
            text=f"Error: {e}",
            fg="red"
        )

root = tk.Tk()
root.title("File Organizer")
root.geometry("500x200")
root.resizable(False, False)
root.configure(bg="#f5f5f5")


folder_path = tk.StringVar()

title = tk.Label(
    root,
    text="Python File Organizer",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)
title = tk.Label(
    root,
    text="Python File Organizer",
    font=("Arial", 18, "bold"),
    bg="#f5f5f5"
)

entry = tk.Entry(
    root,
    textvariable=folder_path,
    width=50
)
entry.pack(pady=5)

browse_btn = tk.Button(
    root,
    text="Browse Folder",
    command=browse_folder
)
browse_btn.pack(pady=5)

organize_btn = tk.Button(
    root,
    text="Organize Files",
    command=start_organizing
)
organize_btn.pack(pady=10)
status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=5)
browse_btn.config(width=20)
organize_btn.config(width=20)


root.mainloop()