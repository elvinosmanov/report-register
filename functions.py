import os
# If Folder exist , function will return False value
# IF Folder does not exist, function will create folder and return True value
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:    
        return False