import os
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("Directory " , dirName1 ,  " Created ")
    else:    
        print("Directory " , dirName1 ,  " already exists")