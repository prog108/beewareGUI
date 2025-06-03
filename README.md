# beewareGUI
A GUI made with beeware, android ready, usefull app to mark bills.

First of all check version of Python you will work with.
Beeware doesn't support Python 3.13 which is newest version at the moment.
To be able posting the app on older: 32-bytes devices I recommend Python 3.10

Make a project folder and activate virtual enviroment with:
Install the enviroment in the folder.
project_name\Scripts\activate in cmd.






IMPORTANT HINTS:

#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

The path on your android for database I resolved by importing os, and using relative path determinator:

def connect_db(self):
        app_dir = os.path.expanduser('~') #this line will determine suitable directory for database(file .db)
        #You can use it for Windows as  well, as for Android.

        
        data_dir = os.path.join(app_dir, 'my_app_data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        db_path = os.path.join(data_dir, 'database_name.db')

        konekcija = sqlite3.connect(db_path)
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------





        
