import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
#from toga import Button, Box, App
#from toga import TextInput

#-----------------
import sqlite3
#-----------------

class MyApp(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title="My BeeWare App")
        
        button1 = toga.Button("Zabilježi plaćanje računa", on_press=self.open_new_window1, style=Pack(padding=10, background_color='lightblue',width=200, height=50))

        
        button3 = toga.Button("Prikaži mi sve", on_press=self.open_new_window3, style=Pack(padding=10, background_color='lightcoral', width=200))

        self.box = toga.Box(children=[button1, button2, button3], style=Pack(direction=COLUMN, padding=20, alignment=CENTER))
        

        self.main_window.content = self.box
        self.main_window.show()

        self.connect_db()




#NOVI PROZOR BROJ 1
    def open_new_window1(self, widget):
        new_box = toga.Box(style=Pack(padding=20, direction=COLUMN, alignment=CENTER))

        #GLOBAL STYLES:
        # Global styles for all labels
        label_style = Pack(font_size=14, color='blue', padding=10, width=200)
        
        # Global styles for all TextInput
        textinput_style = Pack(font_size=12, padding=5, background_color='lightgrey', width=200, text_align=CENTER)

        # Global styles for all Buttons
        button_style = Pack(font_size=12, padding=10, background_color='green', color='white', width=200)


        #ELEMENTI NOVOG PROZORA 1
        Lnaziv = toga.Label("Naziv tvrtke ", style=label_style)
        Enaziv = toga.TextInput(style=textinput_style)
        Liznos = toga.Label("Iznos ", style=label_style)
        Eiznos = toga.TextInput(style=textinput_style)
        Ldatum = toga.Label("Datum ", style=label_style)
        Edatum = toga.TextInput(style=textinput_style)
        return_button = toga.Button("Return to Main", on_press=self.return_to_main, style=button_style)

        #IZGLED NOVOG PROZORA 1
        new_box.add(Lnaziv)
        new_box.add(Enaziv)
        new_box.add(Liznos)
        new_box.add(Eiznos)
        new_box.add(Ldatum)
        new_box.add(Edatum)
        new_box.add(return_button)

        #ovdje mijenjamo saDRŽAJ PROZORA KAKO ne bismo stvarali novi prozor.
        self.main_window.content = new_box

    def open_new_window2(self, widget):
        new_box = toga.Box(style=Pack(padding=20))
        new_label = toga.Label("This is the content of Button 2", style=Pack(padding=10))
        return_button = toga.Button("Return to Main", on_press=self.return_to_main, style=Pack(padding=10))
        new_box.add(new_label)
        new_box.add(return_button)
        self.main_window.content = new_box

    def open_new_window3(self, widget):
        new_box = toga.Box(style=Pack(padding=20))
        new_label = toga.Label("This is the content of Button 3", style=Pack(padding=10))
        return_button = toga.Button("Return to Main", on_press=self.return_to_main, style=Pack(padding=10))
        new_box.add(new_label)
        new_box.add(return_button)
        self.main_window.content = new_box

    def return_to_main(self, widget):
        #self.startup()
        self.main_window.content = self.box

#DATABASE PART
    def connect_db(self):
        konekcija = sqlite3.connect('racuni.db')
        c = konekcija.cursor()

        table1 = '''
            CREATE TABLE IF NOT EXISTS Racuni_radnja(
            Redni_broj INTEGER PRIMARY KEY,
            Firma TEXT NOT NULL,
            Iznos INTEGER,
            Datum INTEGER
            )
        '''
        c.execute(table1)
        konekcija.commit()

def main():
    return MyApp("My BeeWare App", "org.beeware.myapp")

if __name__ == '__main__':
    main().main_loop()
