"""
app for data entering
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER

#-----------------
import sqlite3
#-----------------

import os

#-----------
import os
#from pathlib import Path




class AppRacuni(toga.App):
    def startup(self):
     
        #main_box = toga.Box() #this is by default in your file: replace it as I did.

        self.main_window = toga.MainWindow(title=self.formal_name)
        

        button1 = toga.Button("Mark a bill", on_press=self.open_new_window1, style=Pack(padding=10, background_color='lightblue', width=200))
        
        button3 = toga.Button("Show me", on_press=self.open_new_window3, style=Pack(padding=10, background_color='lightcoral', width=200))

        self.box = toga.Box(children=[button1, button2, button3], style=Pack(direction=COLUMN, padding=20, alignment=CENTER))

        self.main_window.content = self.box
        self.main_window.show()

        self.connect_db()

    def open_new_window1(self, widget):
        new_box = toga.Box(style=Pack(padding=20, direction=COLUMN, alignment=CENTER))

        #GLOBAL STYLES:
        # Global styles for all labels
        label_style = Pack(font_size=14, color='blue', padding=10, width=200)
        
        # Global styles for all TextInput
        textinput_style = Pack(font_size=12, padding=5, background_color='lightgrey', width=200, text_align=CENTER)

        # Global styles for all Buttons
        button_style = Pack(font_size=12, padding=10, background_color='green', color='white', width=200)


       .
        self.main_window.content = new_box

    def open_new_window2(self, widget):
        pass
    def open_new_window3(self, widget):
        pass
        
    def return_to_main(self, widget):
            self.main_window.content = self.box


        self.konekcija.commit()


def main():
    return AppRacuni()


if __name__ == '__main__':
    main().main_loop()
