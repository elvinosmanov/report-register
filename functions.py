import os
# If Folder exist , function will return False value
# IF Folder does not exist, function will create folder and return True value
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        return True
    else:    
        return False

# two parameters:
# 1. df ---> Pandas DataFrame
# 2. column_names--> List<String>
# It will return dataframe with sepcific columns: 
def custom_df(df, column_names):
    return df.loc[:,column_names]
# Function will find the path according to filename:
def find_path(filename):
    company_id = filename[0:2]
    first = filename[5:7]
    second = filename[10:12]
    third = filename[13:16]


    if(company_id=='BP' or company_id == 'AC'):
        return glob.glob("R:\\Mechanical_Completion\\VND\\*"+filename+'*.pdf')[0]
    
    else:
        if(company_id == 'AF'):
            path = f'AZFEN\\Drawings\\HVAC\\{first}'
        elif(company_id == 'EM'):
            path = f'EMTUNGA\\Drawings\\{second}\\{third}'
        elif(company_id == 'BR'):
            path = f'KBR\\Drawings\\{second}\\{third}\\{first}'
        elif(company_id=="BP"):
            path = f'R:\\Mechanical_Completion\\VND'
        elif(company_id=='OV'):
            path = f'NOV\\Drawings\\{second}\\{third}\\{first}'
        return glob.glob("R:\\DCC\\ACE DCC\\"+path+'\\*'+filename+'*.pdf')[0]