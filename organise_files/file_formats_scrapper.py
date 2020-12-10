import requests
import os
import pickle
from bs4 import BeautifulSoup
from organise_files.constants import EXTENSIONS_PICKLE_FILE_NAME
from organise_files.utils import save_pickle, load_pickle

# Used to initilally load the common extensions from file info.
# It contains many (but not all) extensions
def load_common_extensions():
    print(f"loading all common data from fileinfo..")
    source = requests.get("https://fileinfo.com/filetypes/common")
    soup = BeautifulSoup(source.content,'html.parser')

    file_categories = soup.find_all('table', class_="list common browselist")
    extensions = {}
    for category_data in file_categories:
        cateogry_name = category_data.select_one("th").get_text().lower()
        category_extensions = category_data.select("td a")
        for extension in category_extensions:
            extension = extension.get_text().lower()
            if cateogry_name in extensions.keys():
                extensions[cateogry_name].append(extension)
            else:
                extensions[cateogry_name] = [extension]
    save_pickle(EXTENSIONS_PICKLE_FILE_NAME, extensions)

# Loads specific extention data from fileInfo
def load_extension_data(extension):
    print(f"loading {extension} data from fileinfo..")
    source = requests.get(f"https://fileinfo.com/extension/{extension.split('.')[1]}")
    if(source.status_code != 200):
        return None
    soup = BeautifulSoup(source.content,'html.parser')
    current_pickle_data = load_pickle(EXTENSIONS_PICKLE_FILE_NAME)
    category = soup.select(".headerInfo tr:nth-child(3) a")[0].get_text().lower()
    if category in current_pickle_data.keys():
        current_pickle_data[category].append(extension)
    else:
        current_pickle_data[category] = [extension]
    save_pickle(EXTENSIONS_PICKLE_FILE_NAME, current_pickle_data)
    return category

