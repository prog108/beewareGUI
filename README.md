# beewareGUI
#-------------------------------------------------------------------------------------
# FOR WINDOWS
#-------------------------------------------------------------------------------------

I uploaded two main files: one(Main_for_windows.py) that you can run in Windows(for example from Visual Studio Code) 
simply by choossing: "Run Or Debug..." and "Run Python File".
For this to run properly you must install: pip install DateTime
                                           pip install db-sqlite3
                                           pip install toga

#-------------------------------------------------------------------------------------
# FOR ANDROID ONLY
#-------------------------------------------------------------------------------------

Second file is Main_for_android.py. To run it, you must follow the instructions below.
The difference from the Main_for_windows.py is only in database positioning, in start of 
constructor of the main class and in calling the whole application to run it on the bottom
of the code in 2-3 last lines outside of the class. 
I.e: "Main execution and application startup".
You will deal  with this part only to put it on your android phone.
Main_for_android.py is in fact app.py when you install beeware project and briefcase new.
You can copy/paste the content of the file to app.py that will be found in projectname/src/projectname
Follow the steps below to success.


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
                                                           and in this way project is suitable for older versions of android phones)
        Then activate it from the folder:
        in cmd write: beeware-venv\Scripts\activate in cmd.   Watch out for difference in '\' and '/'.

All the steps are on: https://docs.beeware.org/en/latest/tutorial/tutorial-0.html


5)         Install briefcase if this is first time this is installed on your PC:
           python -m pip install briefcase
           If you already have it installed, you can skip it and type in cmd: 'briefcase new'


       Now be carefull what to type in: By default everything is set up for 'Hello World' project Beeware offers you for the start.
       Write down: Formal Name: 'Hello World' by default. That will be your main class name.
                    App Name. By default  it is 'helloworld'
                   Bundle identifier. By default: 'com.example'
       These two details showed needed when deleting your app with ADB SHELL from android device.


        In one step you choose framework to work with. Toga is by default. If you know some other from the list to
       work with, you are able to pick it.

        With this step you got the files to work with and a done 'Hello Wolrd' project.
       Navigate to project_name(helloworld)\src\project_name(helloworld).
       Here is app.py where you can make any update you want.


7)        Enter the project folder: cd project_name
          And run it in developers mode: briefcase dev
          Now you see your empty GUI.

9)         When you want to edit the application the file you can edit is in the path project_name/src/project_name/app.py
                If you want to check my application, copy paste the code from Main_for_android.py to that app.py.
       I left Formal name 'Hello World' simply to not complicate when first time starting it.
       Whenever you want quick check on what the app looks like when editing: choose 'briefcase dev' from root folder of project

11)            'Briefcase create' will make first packaging ready to publish.
               Any editing or even to start this application when makeing updates and new versions
               will require command in cmd: 'briefcase create' 
                As well for emulators and physical devices(android phones): 'briefcase create android'.
                 Choose: 'briefcase build (android)'. That will compile the project.
            To run all done project: execute 'briefcase run (android)'
                

13)        After "briefcase run android" you will be asked 1) Create a new Android emulator if you didn't install 
        one already. Third option is that you connect your android phone on usb port of your personal computer.
        On your phone go to SETTINGS, ABOUT PHONE: tap 7 times on version of device:"Version code" or "Intermediate version number".
        On my phone this is 'BROJ MEĐUVERZIJE' and you will enable DEVELOPER'S. Exit 'About phone' and enter "System", in my case "SUSTAV".
       There you will find 'OPTIONS FOR DEVELOPER'. A new option taht just appeared after that mentioned 7 times pressing.
       Enter to the 'Options for developers' and toogle to enable it. Scroll down and toogle 'UKLANJANJE POGREŠAKA PUTEM USB-A'.
       In English 'ENABLE DEBUGGING FROM/VIA USB'.
       Now you will be ready to transfer the application on your phone. If the error occurs you still should do these 2 things:
        Enable INSTALLATION VIA USB or INSTALLATION  FROM UNKOWN SOURCES(not obligatory on every android phone to do that).

       
14)          In cmd: 'Briefcase package' will create installer. It takes your application and prepares it for distribution, creating all the necessary installation files.
              Execute that before making it android ready. I.E. before 'briefcase create/build/run/ android'
15)              On the beeware tutorial site: for changing the app, it is enough every time to choose: 'briefcase update'
                or 'briefcase run update'. But that is not enough to update it for android distribution. For this purpose
                you should execute step 16).
16)       Shortly, to transfer the app on the phone use: 'briefcase create android' - every time you change something.
          Then type: 'briefcase run android'.

      Good luck.
             


       

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

THINGS TO CONSIDER:
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

Toga table doesn't have a lot of functions to edit the style.
The row that sums all the numbers is not possible to differenciate from the 
rest of the rows. Neither by color, font or to put it on the bottom of
the table.
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------

If you installed an application to your emulator or android and new version cannot overwrite it totally,
you need to erase it from the phone.
Uninstalling it will not erase some memory that might cause errors with new installation.
On Windows you can access your phone and emulator via ADB.

To install ADB visit: https://developer.android.com/tools/releases/platform-tools
Download and install SDK platform-tools for your device.

This step might be crucial: add it to PATH on Windows.
Otherwise you won't be able access it from everywhere.

On Windows open: System Properties > Advanced system settings > Environment Variables.
In section System variables, find variable Path and go to Edit.
Add the path to the directory where you unzipped platform-tools (e.g. C:\path\to\platform-tools).
Click OK and close all windows.
For Linux and Mac you have different way to add it to the PATH.

In cmd check the version od adb: 'adb version'

Turn on the emulator or android device through usb cable and check if it is recognized: 'adb devices'

With command 'adb shell pm list packages' you will find all apckages on your phone
If you used my application the package name will be: com.example.helloworld.
These are Bundle identifier followed by app Name which you specified after executing 'briefcase new'.

To uninstall the package: 'adb uninstall --user 0 com.example.helloworld' is usually enough.
To erase totally everything: 'adb shell pm clear com.example.helloworld'.

Check if the package is still on the emulator/android: 'adb shell pm list packages | findstr com.example.helloworld'.
When nothing appears in cmd that's ok.

You can install the application again with: 'briefcase create android', 'briefcase run android'. Choose number of the device
when it asks you.

When this is not enough, although the app works on PC with 'briefcase dev' or 'briefcase run',
try repeating all the steps above for cleaning the device from old versions of the app
and continue with this: 'adb shell rm -rf /data/data/com.example.helloworld'

Install it again on the device.

