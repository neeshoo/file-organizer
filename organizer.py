import os
import shutil
from datetime import datetime
from categories import FILE_CATEGORIES


def get_unique_filename(destination_path):
    """
    If a file with the same name already exists,
    create a new unique filename.
    Example:
    resume.pdf -> resume_1.pdf
    """

    if not os.path.exists(destination_path):
        return destination_path

    file_name, extension = os.path.splitext(destination_path)
    counter = 1

    while os.path.exists(destination_path):
        new_path = f"{file_name}_{counter}{extension}"

        if not os.path.exists(new_path):
            return new_path

        counter += 1


def write_log(folder_path, file_name, category):

    log_file = os.path.join(folder_path, "log.txt")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", encoding="utf-8") as log:
        log.write(
            f"{timestamp} - Moved: {file_name} -> {category}\n"
        )

def organize_files(folder_path, preview=False):
    preview_data = []
       
    IGNORE_FILES = ["log.txt"]

    for file in os.listdir(folder_path):

        if file in IGNORE_FILES:
            continue

        file_path = os.path.join(folder_path, file)

        # Ignore folders, process only files
        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        moved = False

        # Check file category
        for category, extensions in FILE_CATEGORIES.items():

            if extension in extensions:

                category_folder = os.path.join(folder_path, category)
                os.makedirs(category_folder, exist_ok=True)

                destination = os.path.join(category_folder, file)
                destination = get_unique_filename(destination)

                if preview:
                      preview_data.append(
                      f"{file} -> {category}"
                      )
                      moved = True
                      break

                shutil.move(file_path, destination)
                write_log(folder_path, os.path.basename(destination), category)

                moved = True
                break

        # If extension not found in categories
        if not moved:

            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)

            destination = os.path.join(other_folder, file)
            destination = get_unique_filename(destination)

            if preview:
                 preview_data.append(
                 f"{file} -> Others"
                 )
                 continue

            shutil.move(file_path, destination)
            write_log(folder_path, os.path.basename(destination), "Others")
    
    if preview:
     return preview_data

if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()

    if os.path.exists(folder):
        organize_files(folder)
        print("Files organized successfully!")
    else:
        print("Invalid folder path.")