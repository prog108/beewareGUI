"""
app za racune
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
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        #main_box = toga.Box()

        self.main_window = toga.MainWindow(title=self.formal_name)
        

        button1 = toga.Button("Zabilježi plaćanje radnja", on_press=self.open_new_window1, style=Pack(padding=10, background_color='lightblue', width=200))
        button2 = toga.Button("Zabilježi plaćanje stan", on_press=self.open_new_window2, style=Pack(padding=10, background_color='lightgreen', width=200))
        button3 = toga.Button("Prikaži mi sve", on_press=self.open_new_window3, style=Pack(padding=10, background_color='lightcoral', width=200))

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


        #ELEMENTI NOVOG PROZORA 1
        Lnaziv = toga.Label("Naziv tvrtke ", style=label_style)
        self.Enaziv = toga.TextInput(style=textinput_style)
        Liznos = toga.Label("Iznos ", style=label_style)
        self.Eiznos = toga.TextInput(style=textinput_style)
        Ldatum = toga.Label("Datum ", style=label_style)
        self.Edatum = toga.TextInput(style=textinput_style)
        insert_button = toga.Button("Zabilježi", on_press=self.write_to_db, style=button_style)

        return_button = toga.Button("Return to Main", on_press=self.return_to_main, style=button_style)

        #IZGLED NOVOG PROZORA 1
        new_box.add(Lnaziv)
        new_box.add(self.Enaziv)
        new_box.add(Liznos)
        new_box.add(self.Eiznos)
        new_box.add(Ldatum)
        new_box.add(self.Edatum)
        new_box.add(insert_button)
        new_box.add(return_button)

        #ovdje mijenjamo saDRŽAJ PROZORA KAKO ne bismo stvarali novi prozor.
        self.main_window.content = new_box

    def open_new_window2(self, widget):
        pass
    def open_new_window3(self, widget):
        pass
        
    def return_to_main(self, widget):
            self.main_window.content = self.box

#DATABASE PART
    def connect_db(self):
        app_dir = os.path.expanduser('~')
        #konekcija = sqlite3.connect(r'C:\Users\Korisnik\Desktop\programiranje\M-appbee\appracuni\src\appracuni\racuni.db')
        data_dir = os.path.join(app_dir, 'my_app_data')
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        db_path = os.path.join(data_dir, 'racuni.db')
        #print(os.path.abspath('racuni.db'))
        print("Put do baze:", db_path)

        self.konekcija = sqlite3.connect(db_path) #Direktno na Androidu, os.path.expanduser('~') će najčešće odrediti odgovarajući direktorij za pohranu podataka.
#Na Windowsu, to će biti tvoj korisnički direktorij, dok na Androidu će biti odgovarajući privatni direktorij aplikacije.

        self.c = self.konekcija.cursor()

        table1 = '''
            CREATE TABLE IF NOT EXISTS Racuni_radnja(
            Redni_broj INTEGER PRIMARY KEY,
            Firma TEXT NOT NULL,
            Iznos INTEGER,
            Datum INTEGER
            )
        '''
        self.c.execute(table1)
        self.konekcija.commit()

    def write_to_db(self, widget=None): #ovdje je problem bio
        ime = self.Enaziv.value
        # Provera i konverzija za iznos
        if not self.Eiznos.value:
            print("Polje za iznos je prazno.")
            return
        try:
            iznos = int(self.Eiznos.value)
        except ValueError:
            print("Neispravan unos za iznos.")
            return
        
        # Provera i konverzija za datum
        if not self.Edatum.value:
            print("Polje za datum je prazno.")
            return
        try:
            datum = int(self.Edatum.value)
        except ValueError:
            print("Neispravan unos za datum.")
            return
        
        # Ako je sve ispravno, izvrši unos
        podaci = (ime, iznos, datum)
        task = '''
            INSERT INTO Racuni_radnja (Firma, Iznos, Datum)
            VALUES (?, ?, ?)
        '''
        try:
            self.c.execute(task, podaci)
            self.konekcija.commit()
            print("Podaci uspešno uneseni.")
        except sqlite3.Error as e:
            print("Greška prilikom unosa u bazu:", e)


def main():
    return AppRacuni()


if __name__ == '__main__':
    main().main_loop()
