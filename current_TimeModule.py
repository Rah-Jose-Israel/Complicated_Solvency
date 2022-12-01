import os
from datetime import date as dt
from threading import current_thread



class TimeModule:
    
    def __init__ (self):
        current_TimeDay = dt.today().day
        old_name = r"Account_Average_08_30.py"
        new_name = rf"/Users/israel/Dropbox/Apps/RahBanks/Script_Archive/Account_Average_08_30"

        if os.path.isfile(new_name):
            print("The file already exists")
        else:
            print('here')
            # Rename the file
            #os.rename(old_name, new_name)
