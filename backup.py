
"""
    backup.py

    Prevents data and files being damaged or currupted by using simple backup
    techniques.
"""
from os import path, mkdir
from shutil import copy2
from string import ascii_letters, digits

def backup(filename:str, destination:str=".", rename_to:str="")->bool:
    """
        * Copies a file; renaming and duplicating the original
        * file to serve as a simple backup procedure. Automatically
        * removes invalid characters from within a filename.
       
        ! Might cause errors

        TODO Create a method that allows reverting the files
        TODO Non-absolute files [./, ../, .\\, etc] need to be normalised for 
        TODO the OS being run on
    """

    # Returns a valid version of the file, if it cant, returns False
    filename = _force_valid_filename(filename) 

    if not filename:
        raise ValueError("The filename you are tring to use is not valid.")
    
    # Sets to the current directory the file is ran from as a default
    #   If a destination has been provided, the base path will change.
    #   If the directiry is valid, and does not exist, try to make one.
    if destination == ".":
        base_directory  = path.dirname(path.realpath(__file__)) + path.sep
    else:
        if not path.isdir(destination):
            mkdir(destination)
                  
        base_directory = destination + path.sep

    # Try and verify the renaming of the file, returns False if invalid
    renamed_file = _force_valid_filename(rename_to)
    
    if not renamed_file:
        raise ValueError("The filename you are tring to use is not valid.")

    # Full path names of the files
    original_file = path.abspath(filename)

    # Give the backup file a default filename if no rename was provided
    backup_file = path.abspath(
                    path.join(base_directory, 
                             (renamed_file or (filename + "__backup__.gpx"))))

    # Check to see if the file does exists.
    #   If it does, we can try and copy original to the backup
    #   if not, then we raise a file not found error
    if not path.isfile(original_file):
        raise FileNotFoundError("The file you specified was not found.")
    
    # Check to see if the backup file already exists.
    #   If it does, we do not want to override a backup file
    #       so we throw a FileExistsError
    if path.isfile(backup_file):
        raise FileExistsError("The backup destination file already exists.")

    # Original file exists, and backup filename is free to be used, so we
    # are free to make an attempt at backing up the file.
    if not copy2(original_file, backup_file):
        raise Exception(
                "An unknown error means this action could not be completed.")
    
    # Return True if the file was successfully copied,
    # Otherwise, and Exception will have been thrown.
    return True


def simple_backup(filename):
    """Quick version of the backup function with minimal typing"""
    backup(filename, ".")


def _force_valid_filename(filename:str)->str:
    """Tries to validify a filename that contains invalid characters"""
    
    chars_allowed = ascii_letters + digits + "() .-_"
    filename, file_extension = path.splitext(filename)

    valid_filename = ''.join(c for c in filename if c in chars_allowed)

    # Check at the end because removing invalid characters
    # might leave an empty string for either filename or
    # the file extention.
    if valid_filename == "" or file_extension == "":
        return False
    
    # Convert to string as filenames can be 1.png, 2.gpx, etc.
    return str(valid_filename + file_extension)