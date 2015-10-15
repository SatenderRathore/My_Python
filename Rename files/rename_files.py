import os
def rename_files():
    file_list = os.listdir(r"/home/satender/Downloads/python/photos/prank/prank")
    #print(file_list)
    save_path = os.getcwd()
    os.chdir(r"/home/satender/Downloads/python/photos/prank/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
 
    os.chdir(save_path)       



rename_files()



    

