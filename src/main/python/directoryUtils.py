import os

def move_to_directory(directory_path):
    # Check if the directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")

    try:
        # Attempt to change the current working directory
        os.chdir(directory_path)
        return

    except PermissionError:
        # Raise permission error
        raise PermissionError(f"Permission denied: Unable to change the current working directory to {directory_path}")

    except Exception as e:
        # Raise other potential errors
        raise Exception(f"An error occurred: {e}")


def file_exists(filename):
    file_path = os.path.join(os.getcwd(), filename)

    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The directory {directory_path} does not exist.")
