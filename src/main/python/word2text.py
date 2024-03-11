import os
import re
from wordUtils import extract as extract_word
from pdfSelectableUtils import extract as extract_pdf

def extract_first_three_words(text):
    """
    Extracts and returns the first two words from a given text.
    """
    return '_'.join(re.findall(r'\w+', text)[:3])


def func_target_file(file, extensions_doc=['.doc', '.docx'], extensions_pdf=['.pdf']):
    """
    Determines if the file has one of the specified extensions and calls
    the appropriate function.
    """
    if any(file.endswith(ext) for ext in extensions_doc):
        return extract_word
    elif any(file.endswith(ext) for ext in extensions_pdf):
        return extract_pdf
    else:
        return None


def processDummy(file_path):
    """
    Dummy process function. Replace or modify this with actual processing logic.
    """
    print(f"Processing {file_path}")


def process_files_in_directory(directory):
    """
    Iterates over items in the specified directory.
    If an item is a directory, it extracts the first two words of the directory name and calls the process_function for each target file inside.
    """
    try:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)

            if os.path.isdir(item_path):
                id_student = extract_first_three_words(item)
                print(f"Directory: {item} (Student id: {id_student})")

                for file in os.listdir(item_path):
                    function = func_target_file(file)
                    data_student = function(os.path.join(item_path, file))
                    print(data_student)

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == '__main__':
    Path_31_Irakurketa_1 = "/home/ilopez077/scratch/Gatai/Data/Albumen interpretazioak/31 TALDEKOEN ALBUMEN INTERPRETAZIOAK/1. IRAKURKETA/20220_254_GPRIMA20_25868_31-Album ilustratuen interpretazioa (I)-6380571"
    Path_31_Irakurketa_2 = ...

    Path_32_Hemendik_Irakurketa_1 = ...
    Path_32_Hemendik_Irakurketa_2 = ...

    Path_32_Piztien_Irakurketa_1 = ...
    Path_32_Piztien_Irakurketa_2 = ...


    process_files_in_directory(Path_31_Irakurketa_1)
