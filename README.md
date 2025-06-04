# beewareGUI
A GUI made with beeware, android ready, usefull app to mark bills.

1)        First of all check version of Python you will work with.
        Beeware doesn't support Python 3.13 which is newest version at the moment.
        To be able posting the app on older: 32-bytes devices I recommend Python 3.10
        
        You can use python versions 3.9 - 3.12

2)        You must have git installed on Windows

3)    Make a project folder and enter to it with cmd

4)        Install and activate virtual enviroment with:
        Install the enviroment in the folder: in cmd: py -3.12 -m venv beeware-venv
                                                      (or any other version of python. I use 'py -3.10'
                                                           and this project is suitable for older versions of android phones)
        Then activate it from the folder:
        in cmd: project_name\Scripts\activate in cmd.

All the steps are on: https://docs.beeware.org/en/latest/tutorial/tutorial-0.html


5)         Install briefcase if this is first time this is installed on your PC:
           python -m pip install briefcase
           If you already have it installed, you can type in cmd: briefcase new

6)        Enter the project folder: cd project_name
          And run it in developers mode: briefcase dev

7)




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

        print('Path to the database is ', db_path) #Wheather you use the application on windows, without android in 'briefcase create (android)', or on android
        #device, you will be able to found out where the database_name.db is created.
 
        konekcija = sqlite3.connect(db_path)
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------





        
