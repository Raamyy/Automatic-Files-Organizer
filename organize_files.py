import os
import sys
import shutil  # for moving and copyinf items
from pathlib import Path
from os import listdir
from os.path import isfile, join
from utils import get_file_extension
from file_extensions import getExtensionCategory

def organise(filelist, directory):
    # moves files in folders accordind to their extentions
    for my_file in filelist:
        file_category = getExtensionCategory(get_file_extension(my_file))
        loc = directory+"\\"
        if file_category != None:
            loc += file_category
        else:
            loc += "Misc" # not in the file formats
        Path(loc).mkdir(exist_ok=True)
        shutil.move(my_file, loc)
        print(f"moved {my_file} to {loc}")
        
            
if __name__=='__main__':
    directory_tobe_cleaned = ""
    if len(sys.argv) < 2:
        print(f"""Please enter a directory to clean. 
        as \"py {sys.argv[0]} path/to/directory\"""")
        exit()
    else:
        directory_tobe_cleaned = sys.argv[1]
    files = [join(directory_tobe_cleaned, f) for f in listdir(directory_tobe_cleaned) if isfile(join(directory_tobe_cleaned, f))]
    organise(files, directory_tobe_cleaned)
    print("Done!")
    print(f"Organised {len(files)} files into their directories")