#TO REMOVE NUMBERS FROM FILE NAMES.
import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir("/Users/johnsanchez/Downloads/prank")
    print(file_list)
    saved_path = os.getcwd()
    #THE PATHS IM A LITTLE CONFUSED ON, LIKE 17
    print ("Current Working Directory is "+saved_path)
    os.chdir("/Users/johnsanchez/Downloads/prank")
    #(2) for each file, rename filename
    for file_name in file_list:
        pint("Old Name - "+file_name)
        print("New Name -"+file_name.translate(None, "0123456789")
        #os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
    #THIS COMMAND RIGHT ABOVE, I HAVE NO CLUE WHY IT'S HERE.

rename_files()