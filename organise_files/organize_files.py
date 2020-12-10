import os
import sys
import shutil  # for moving and copyinf items
from pathlib import Path
from os import listdir
from os.path import isfile, join
from utils import get_file_extension
from file_extensions_handler import getExtensionCategory

def organise(filelist, directory):
    # moves files in folders accordind to their extentions
    for my_file in filelist:
        file_category = getExtensionCategory(get_file_extension(my_file))
        loc = directory+"\\"
        if file_category != None:
            loc += file_category
        else:
            loc += "Unknown Extensions" # not in the file formats
        Path(loc).mkdir(exist_ok=True)
        shutil.move(my_file, loc)
        print(f"moved {my_file} to {loc}")

def organise_directory(directory):
    files = [join(directory, f) for f in listdir(directory) if isfile(join(directory, f))]
    organise(files, directory)
    print(f"Organised {len(files)} files into their directories")
            
def main():
    directory_tobe_cleaned = ""
    if len(sys.argv) < 2:
        print(f"""Please enter a directory to clean. 
        as \"py {sys.argv[0]} path/to/directory\"""")
        exit()
    else:
        directory_tobe_cleaned = sys.argv[1]
    organise_directory(directory_tobe_cleaned)
    print("Done!")

main()