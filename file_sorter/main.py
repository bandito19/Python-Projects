import os
import shutil

def create_folder(path, extension):
    folder_name = extension[1:]
    folder_path = os.path.join(path, folder_name)

    if not os.exists(folder_path):
        os.makedirs(folder_path)

    return folder_path


