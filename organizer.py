import os
import shutil
from categories import FILE_CATEGORIES


def organize_files(folder_path):
    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file)[1].lower()

            moved = False

            for category, extensions in FILE_CATEGORIES.items():

                if extension in extensions:

                    category_folder = os.path.join(folder_path, category)

                    os.makedirs(category_folder, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(category_folder, file)
                    )

                    moved = True
                    break

            if not moved:

                other_folder = os.path.join(folder_path, "Others")

                os.makedirs(other_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(other_folder, file)
                )


if __name__ == "__main__":
    folder = input("Enter folder path: ")
    organize_files(folder)