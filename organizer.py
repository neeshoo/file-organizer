import os
import shutil
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


def organize_files(folder_path):

    for file in os.listdir(folder_path):

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

                shutil.move(file_path, destination)

                moved = True
                break

        # If extension not found in categories
        if not moved:

            other_folder = os.path.join(folder_path, "Others")
            os.makedirs(other_folder, exist_ok=True)

            destination = os.path.join(other_folder, file)
            destination = get_unique_filename(destination)

            shutil.move(file_path, destination)


if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()

    if os.path.exists(folder):
        organize_files(folder)
        print("Files organized successfully!")
    else:
        print("Invalid folder path.")