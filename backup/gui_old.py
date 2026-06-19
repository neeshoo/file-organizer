import tkinter as tk
from tkinter import filedialog, messagebox

from organizer import organize_files
from categories import load_categories, save_categories


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


def open_category_manager():

    manager = tk.Toplevel(root)
    manager.title("Manage Categories")
    manager.geometry("400x250")
    manager.resizable(False, False)

    tk.Label(
        manager,
        text="Category Name"
    ).pack(pady=5)

    category_entry = tk.Entry(
        manager,
        width=35
    )
    category_entry.pack()

    tk.Label(
        manager,
        text="Extensions (comma separated)"
    ).pack(pady=5)

    extension_entry = tk.Entry(
        manager,
        width=35
    )
    extension_entry.pack()

    def add_category():

        category = category_entry.get().strip()

        extensions = [
            ext.strip().lower()
            for ext in extension_entry.get().split(",")
            if ext.strip()
        ]

        if not category or not extensions:
            messagebox.showwarning(
                "Warning",
                "Please fill all fields."
            )
            return

        categories = load_categories()

        categories[category] = extensions

        save_categories(categories)

        messagebox.showinfo(
            "Success",
            "Category added successfully!"
        )

        manager.destroy()

    tk.Button(
        manager,
        text="Add Category",
        width=20,
        command=add_category
    ).pack(pady=20)


# Main Window
root = tk.Tk()
root.title("File Organizer")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

folder_path = tk.StringVar()
preview_mode = tk.BooleanVar()

title = tk.Label(
    root,
    text="Python File Organizer",
    font=("Arial", 18, "bold"),
    bg="#f5f5f5"
)
title.pack(pady=15)

entry = tk.Entry(
    root,
    textvariable=folder_path,
    width=55
)
entry.pack(pady=5)

browse_btn = tk.Button(
    root,
    text="Browse Folder",
    width=20,
    command=browse_folder
)
browse_btn.pack(pady=10)

preview_check = tk.Checkbutton(
    root,
    text="Preview Mode",
    variable=preview_mode,
    bg="#f5f5f5"
)
preview_check.pack()

manage_btn = tk.Button(
    root,
    text="Manage Categories",
    width=20,
    command=open_category_manager
)
manage_btn.pack(pady=10)

organize_btn = tk.Button(
    root,
    text="Organize Files",
    width=20,
    command=start_organizing
)
organize_btn.pack(pady=10)

status_label = tk.Label(
    root,
    text="",
    fg="green",
    bg="#f5f5f5",
    font=("Arial", 10)
)
status_label.pack(pady=10)

root.mainloop()