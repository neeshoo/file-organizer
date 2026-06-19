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

        if preview_mode.get():

            result = organize_files(
                path,
                preview=True
            )

            if result:
                messagebox.showinfo(
                    "Preview",
                    "\n".join(result)
                )
            else:
                messagebox.showinfo(
                    "Preview",
                    "No files found to organize."
                )

            status_label.config(
                text="Preview generated successfully!",
                fg="blue"
            )

        else:

            organize_files(path)

            messagebox.showinfo(
                "Success",
                "Files organized successfully!"
            )

            status_label.config(
                text="Files organized successfully!",
                fg="green"
            )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

        status_label.config(
            text=f"Error: {e}",
            fg="red"
        )


# Main Window
root = tk.Tk()
root.title("File Organizer")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

folder_path = tk.StringVar()
preview_mode = tk.BooleanVar()

# Title
title = tk.Label(
    root,
    text="Python File Organizer",
    font=("Arial", 18, "bold"),
    bg="#f5f5f5"
)
title.pack(pady=15)

# Folder Path Entry
entry = tk.Entry(
    root,
    textvariable=folder_path,
    width=55
)
entry.pack(pady=5)

# Browse Button
browse_btn = tk.Button(
    root,
    text="Browse Folder",
    width=20,
    command=browse_folder
)
browse_btn.pack(pady=10)

# Preview Checkbox
preview_check = tk.Checkbutton(
    root,
    text="Preview Mode",
    variable=preview_mode,
    bg="#f5f5f5"
)
preview_check.pack()

# Organize Button
organize_btn = tk.Button(
    root,
    text="Organize Files",
    width=20,
    command=start_organizing
)
organize_btn.pack(pady=15)

# Status Label
status_label = tk.Label(
    root,
    text="",
    bg="#f5f5f5",
    fg="green",
    font=("Arial", 10)
)
status_label.pack()

root.mainloop()