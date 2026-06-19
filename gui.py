import customtkinter as ctk
from tkinter import filedialog, messagebox

from organizer import organize_files
from categories import load_categories, save_categories

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


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

            preview_text = "\n".join(result) if result else "No files found."

            messagebox.showinfo(
                "Preview",
                preview_text
            )

            status_label.configure(
                text="Preview generated successfully!"
            )

        else:

            organize_files(path)

            messagebox.showinfo(
                "Success",
                "Files organized successfully!"
            )

            status_label.configure(
                text="Files organized successfully!"
            )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

        status_label.configure(
            text=f"Error: {e}"
        )


def open_category_manager():

    manager = ctk.CTkToplevel(root)
    manager.title("Manage Categories")
    manager.geometry("400x300")

    ctk.CTkLabel(
        manager,
        text="Category Name"
    ).pack(pady=10)

    category_entry = ctk.CTkEntry(
        manager,
        width=250
    )
    category_entry.pack()

    ctk.CTkLabel(
        manager,
        text="Extensions (.psd,.fig)"
    ).pack(pady=10)

    extension_entry = ctk.CTkEntry(
        manager,
        width=250
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

    ctk.CTkButton(
        manager,
        text="Add Category",
        command=add_category
    ).pack(pady=20)


root = ctk.CTk()
root.title("File Organizer")
root.geometry("650x450")
root.resizable(False, False)

folder_path = ctk.StringVar()
preview_mode = ctk.BooleanVar()

title = ctk.CTkLabel(
    root,
    text="📂 File Organizer",
    font=("Arial", 28, "bold")
)
title.pack(pady=25)

entry = ctk.CTkEntry(
    root,
    textvariable=folder_path,
    width=500,
    height=40
)
entry.pack(pady=10)

ctk.CTkButton(
    root,
    text="Browse Folder",
    width=220,
    height=40,
    command=browse_folder
).pack(pady=10)

ctk.CTkCheckBox(
    root,
    text="Preview Mode",
    variable=preview_mode
).pack(pady=10)

ctk.CTkButton(
    root,
    text="Manage Categories",
    width=220,
    height=40,
    command=open_category_manager
).pack(pady=10)

ctk.CTkButton(
    root,
    text="Organize Files",
    width=220,
    height=45,
    command=start_organizing
).pack(pady=20)

status_label = ctk.CTkLabel(
    root,
    text="Ready"
)
status_label.pack(pady=10)

root.mainloop()