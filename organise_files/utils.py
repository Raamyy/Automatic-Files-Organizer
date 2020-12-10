import os.path
import pickle

def get_file_extension(filePath):
    extension = os.path.splitext(filePath)[1]
    return extension

    
def load_pickle(file_name):
    pickle_file = open(file_name,"rb")
    pickle_data = pickle.load(pickle_file)
    pickle_file.close()
    return pickle_data

def save_pickle(file_name, data):
    pickle_file = open(file_name, "wb")
    pickle.dump(data,pickle_file)
    pickle_file.close()