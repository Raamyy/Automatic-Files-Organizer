import pickle
import os
from utils import load_pickle
from file_formats_scrapper import load_common_extensions, load_extension_data
from constants import EXTENSIONS_PICKLE_FILE_NAME

extensions = {}

# updates the golbal extensions object with data in pickle file.
def load_extensions_object():
    global extensions
    extensions = load_pickle(EXTENSIONS_PICKLE_FILE_NAME)

# If there exist pickle file just use it. Else load common data from fileInfo.
if os.path.isfile(EXTENSIONS_PICKLE_FILE_NAME):
    load_extensions_object()
else:
    load_common_extensions()
    load_extensions_object()


def getExtensionCategory(extension):
    extension = extension.lower()
    category = list(filter(lambda cat: extension in cat[1], extensions.items())) # Some magical python to check if a category contains the extension
    if len(category) == 0:
        category = load_extension_data(extension) # not found in the local extension, What about checking it in fileInfo servers?
        load_extensions_object()
        return category
    else:
        return category[0][0]
