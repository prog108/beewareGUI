"""
My first application
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
#-----------------
import sqlite3
#-----------------
from datetime import datetime
#----------------
import os
#----------------


class HelloWorld(toga.App):
    def startup(self):
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        







    def startup(self):
        self.main_window = toga.MainWindow(title="My BeeWare App")
        #--------------------
        # BUTTONS' STYLES
        #--------------------
        self.button_style_return = Pack(font_size=12, padding=10, background_color='lime', color='white')
        self.button_style_1 = Pack(font_size=12, padding=10, background_color='pink')
        self.button_style_2 = Pack(font_size=12, padding=10, background_color='yellow')
        self.button_style_3 = Pack(font_size=12, padding=10, background_color='lime')
        self.button_style_4 = Pack(font_size=12, padding=10, background_color='pink')
        self.button_style_5 = Pack(font_size=12, padding=10, background_color='lightblue')
        self.button_style_6 = Pack(font_size=12, padding=10, background_color='wheat')
        self.button_style_7 = Pack(font_size=12, padding=10, background_color='violet')
        self.button_style_8 = Pack(font_size=12, padding=10, background_color='blue')

        #--------------------
        # LABELS' STYLES
        #--------------------
        self.label_style_choose = Pack(font_size=10, font_family='Arial', font_weight='bold', color='black')
        self.label_style_1 = Pack(font_size=14, color='blue', padding=10, width=200)
        self.label_style_2 = Pack(font_size=14, color='black', padding=10, width=200)

        #--------------------
        # TEXT INPUTS' STYLES
        #--------------------
        self.text_input_style = Pack(font_size=10, font_family='Arial', font_weight='bold', color='black', text_align=CENTER, width=40)
        self.text_input_style_2 = Pack(font_size=12, padding=5, background_color='lightgrey', width=200, text_align=CENTER)
        self.text_input_style_3 = Pack(font_size=12, padding=5, background_color='yellow', width=200, text_align=CENTER)

        #--------------------
        # TABLES STYLES
        #--------------------
        self.tabel_style_1 = Pack(background_color='lightblue', padding=30, margin=10)
        self.tabel_style_2 = Pack(flex=1, background_color='aliceblue', padding=30, margin=10)
        self.tabel_style_3 = Pack(flex=1, background_color='antiquewhite', padding=30, margin=10)
        self.tabel_style_4 = Pack(flex=1, background_color='transparent',  padding=30, margin=10)

        button1 = toga.Button("BILLS", on_press=self.open_second_window_for_work, style=self.button_style_2)
        button2 = toga.Button("LUXURY EXPENSES", on_press=self.open_second_window_for_home, style=self.button_style_5)

        

        self.box = toga.Box(children=[toga.Box(style=Pack(flex=1)),button1, button2,toga.Box(style=Pack(flex=1))], style=Pack(direction=COLUMN, padding=20, alignment=CENTER, flex=1))
        

        self.main_window.content = self.box

        self.main_window.show()
        self.connect_db()

        #FUNCTIONAL VARIABLES THAT ARE NEEDED FROM METHODS BELOW: 
        self.stored_variable_for_order_switch = 0
        self.job_or_apart = 0

#_______________
#SECOND WINDOW AFTER 2 BIG BUTTONS
#_______________ 

    def go_back(self, widget=None):
        self.main_window.content = self.box

    def open_second_window_for_work(self, widget=None):
        self.job_or_apart = 1
        self.second_window()

    def open_second_window_for_home(self, widget=None):
        self.job_or_apart = 2
        self.second_window()

    def second_window(self, widget=None):
        self.second_window_box = toga.Box(style=Pack(padding=20, direction=COLUMN, alignment=CENTER))

        if self.job_or_apart == 1:
            button1 = toga.Button("Mark a bill - home", on_press=self.write_to_work_table, style=self.button_style_2)
        else:
            button1 = toga.Button("Mark a bill - luxury", on_press=self.open_win_mark_apartment, style=self.button_style_5)
        if self.job_or_apart == 1:
            button3 = toga.Button("Show all - home", on_press=self.open_new_window3, style=self.button_style_2)
        else:
            button3 = toga.Button("Show all -luxury", on_press=self.show_buttons_apartm, style=self.button_style_5)
        if self.job_or_apart == 1:
            button5= toga.Button("Delete - home", on_press=self.open_new_window4, style=self.button_style_2)
        else:            
            button5 = toga.Button("Delete - luxury", on_press=self.delete_wind_apartm, style=self.button_style_5)

        self.return_button = toga.Button("Return", on_press=self.go_back, style=self.button_style_return)


        self.second_window_box = toga.Box(children=[button1, button3, button5, self.return_button], 
                                     style=Pack(direction=COLUMN, padding=20, alignment=CENTER))
        self.main_window.content = self.second_window_box


#_______________
#FIRST WINDOW TO FULLFILL THE INPUT FIELDS
#_______________ 
    def write_to_work_table(self, widget):
        self.job_or_apart = 1
        self.open_new_window1()

    def open_new_window1(self, widget=None):
        new_box = toga.Box(style=Pack(padding=20, direction=COLUMN, alignment=CENTER))

        #ELEMENTI NOVOG PROZORA 1
        Lnaziv = toga.Label("Company name", style=self.label_style_1)
        self.Enaziv = toga.TextInput(style=self.text_input_style_2)
        Liznos = toga.Label("Amount",style=self.label_style_1)
        self.Eiznos = toga.TextInput(style=self.text_input_style_2)
        Ldatum = toga.Label("Date", style=self.label_style_1)
        self.Edatum = toga.TextInput(style=self.text_input_style_2)
        if self.job_or_apart == 1:
            insert_button = toga.Button("Mark - home", on_press=self.write_to_db, style=self.button_style_1)
        else:
            insert_button = toga.Button("Mark - lux", on_press=self.write_to_db, style=self.button_style_6)

        self.return_button = toga.Button("Return", on_press=self.return_to_main, style=self.button_style_return)

        #IZGLED NOVOG PROZORA 1
        new_box.add(Lnaziv)
        new_box.add(self.Enaziv)
        new_box.add(Liznos)
        new_box.add(self.Eiznos)
        new_box.add(Ldatum)
        new_box.add(self.Edatum)
        new_box.add(insert_button)
        new_box.add(self.return_button)

        #ovdje mijenjamo saDRŽAJ PROZORA KAKO ne bismo stvarali novi prozor.
        self.main_window.content = new_box


#_______________
#SHOW DATA WINDOW #WITH BUTTONS ONLY
#_______________    
    def open_new_window3(self, widget):  

        self.show_data_window = toga.Box(style=Pack(padding=20, direction=COLUMN))
        output_button = toga.Button("Show all home", on_press = self.output_from_db , style=self.button_style_1)
        out_date_button = toga.Button("Order by date", on_press = self.window_with_ordered_by_date , style=self.button_style_2)
        out_firm_button = toga.Button("Order by company", on_press = self.window_with_ordered_by_firm, style=self.button_style_1)
        #out_history_button = toga.Button("Pokaži brisanja", on_press = self.output_from_db , style=self.button_style_4)
        return_button = toga.Button("Return", on_press=self.return_to_main, style=self.button_style_return)
        #Loutput = toga.Label("Pokaži ispis")

        self.show_data_window.add(output_button)
        self.show_data_window.add(out_date_button)
        self.show_data_window.add(out_firm_button)
        #self.new_box.add(out_history_button)

        self.show_data_window.add(return_button)
        #self.new_box.add(Loutput)

        self.main_window.content = self.show_data_window
        self.job_or_apart = 1
#-------------------
#FUNCTION FOR RETURN BUTTON
#------------------
    def return_to_main(self, widget):
        #self.startup()
        self.main_window.content = self.second_window_box


    

#________________
#DELETE WINDOW FIRST SET OF ENTRIES
#________________
    def open_new_window4(self, widget = None):
        if self.job_or_apart == 1:
            task = '''SELECT * FROM Bills_home'''
        else:
            task = '''SELECT * FROM Bills_luxury'''

        self.rows = list(self.c.execute(task))

        column_names = [description[0] for description in self.c.description]
        # Ako želite prikazati samo prvih 4 stupca:
        self.rows_filtered = [tuple(row[:4]) for row in self.rows]
        column_names_filtered = column_names[:4]
            
        
        # Pretpostavimo da imate listu podataka i nazive stupaca
        # Izračunajte maksimalnu širinu sadržaja za svaki stupac
     
        sirina, visina = self.main_window.size
        # Zatim postavite column_widths
#TABLE
        self.table = toga.Table(
            headings=column_names_filtered,
            data=self.rows_filtered,
            width = sirina - 20,
            style= self.tabel_style_2
        )

# Prilagodba širine stupaca putem stilova (ako je dostupno)
# npr. za svaki stupac napraviti zasebni stil
      
        # Scroll container s fleksibilnim širinama
        self.scroll = toga.ScrollContainer(content=self.table, style=Pack(flex=1))
        Lodabir = toga.Label('Delete ordinal number', style=self.label_style_choose)
        self.Eodabir = toga.TextInput(placeholder="number", style=self.text_input_style)
        if self.job_or_apart == 1:
            Bbrisanje = toga.Button("Delete", on_press=self.delete_from_db, style=self.button_style_7)
        else:
            Bbrisanje = toga.Button("Delete", on_press=self.delete_from_db, style=self.button_style_3)

        self.return_button = toga.Button("Return",  on_press=self.return_to_main, style=self.button_style_return)
       
        # Kontejner za gumbe
        buttons_container = toga.Box(
            children=[Lodabir, self.Eodabir, Bbrisanje, self.return_button],
            style=Pack(direction=ROW, alignment=CENTER, padding=10)
        )
        return_button_container = toga.Box(
            children = [self.return_button],
            style=Pack(alignment=CENTER, padding=10)
        )

        # Glavni kontejner s scrollom i gumbima ispod
        self.okvir_prvi_za_brisanje = toga.Box(
            children=[
                self.scroll,
                buttons_container,
                return_button_container
            ],
            style=Pack(flex=1, alignment=CENTER, direction=COLUMN)
        )

        self.main_window.content = self.okvir_prvi_za_brisanje



    
    
    def delete_from_db(self, widget = None):
        broj_za_brisanje = self.Eodabir.value
        
        if self.job_or_apart == 1:
            task = '''DELETE FROM Bills_home
            WHERE Ordinal = ?'''
        else:
            task = '''DELETE FROM Bills_luxury
            WHERE Ordinal = ?'''

        self.c.execute(task, (broj_za_brisanje,))
        #be aware of this. if you put 2-cifre numbers it will be recognized as to arguments.
        #Then we use second argument in c.execute as tuple! with shape: (broj_za_brisanje,)
        self.konekcija.commit()

        self.open_new_window4()


     

#_______________
#_______________
#_______________
#_______________
#_______________
#_______________
#CONNECTION TO DATABASE
#_______________
#_______________
#_______________
#_______________
#_______________
#_______________
#_______________
      
    def connect_db(self):
        app_dir = os.path.expanduser('~')  #When you start it on Windows the path where it approximates the file.db installation 
        #might be difficult to find. That's why we  use print('Path to the database', db_path) later on.
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
            CREATE TABLE IF NOT EXISTS Bills_home(
            Ordinal INTEGER PRIMARY KEY,
            Company TEXT NOT NULL,
            Amount FLOAT,
            Date TEXT,
            Date_to_order TEXT
            )
        '''

        table2 = '''
            CREATE TABLE IF NOT EXISTS Bills_luxury(
            Ordinal INTEGER PRIMARY KEY,
            Company TEXT NOT NULL,
            Amount FLOAT,
            Date TEXT,
            Date_to_order TEXT

            )
        '''
        self.c.execute(table1)
        self.konekcija.commit()
        self.c.execute(table2)
        self.konekcija.commit()

#_______________
#WRITE TO DB FUNCTION
#_______________   
    def write_to_db(self, widget=None): #ovdje je problem bio
        ime = self.Enaziv.value.upper()
        # Provera i konverzija za iznos

        iznos = self.Eiznos.value
        if self.Eiznos.value == '':
            iznos = 0
              
        # Provera i konverzija za datum
        datum = str(self.Edatum.value)
        if not self.Edatum.value:
            datum = self.get_datum(self.Edatum.value)
        novi_datum = self.convert_date_format(datum)

#datum za poredak
        datum_za_poredak = self.convert_for_ranking(novi_datum)

        # Ako je sve ispravno, izvrši unos
        podaci = (ime, iznos, novi_datum, datum_za_poredak)
        if self.job_or_apart == 1:
            task = '''
                INSERT INTO Bills_home (Company, Amount, Date, Date_to_order)
                VALUES (?, ?, ?, ?)
            '''
        else:
            task = '''
                INSERT INTO Bills_luxury (Company, Amount, Date, Date_to_order)
                VALUES (?, ?, ?, ?)
            '''

        try:
            self.c.execute(task, podaci)
            self.konekcija.commit()
            print("Data succesfully entered")
        except sqlite3.Error as e:
            print("Error when entering the data:", e)

        self.Enaziv.value = ''
        self.Eiznos.value = ''
        self.Edatum.value = ''

#još napraviti situaciju gdje je broj znamenaka maxx 2-2-4
    def convert_date_format(self, inputed_date):
        konverted_string = inputed_date.strip().replace('.', '-').replace('/', '-').replace(',', '-')
        if not konverted_string[-1].isdigit():
            konverted_string = konverted_string[:-1]

        dijelovi=konverted_string.split('-') #ovako smo dobili listu
        
        if int(dijelovi[0]) < 10 and '0' not in dijelovi[0]:
            dijelovi[0] = '0' + dijelovi[0]
        if int(dijelovi[1]) < 10 and '0' not in dijelovi[1]:
            dijelovi[1] = "0" + dijelovi[1]

        if len(dijelovi) < 3 or not dijelovi[2].isdigit(): 
            # Ako nema godine ili nije broj
            trenutna_godina = datetime.now().year
            if len(dijelovi) < 3:
                dijelovi.append(str(trenutna_godina))
            else:
                # Ako postoji, ali nije broj, zameniti ga current
                dijelovi[2] = str(trenutna_godina)
         
        konverted_string = "-".join(dijelovi)
        return konverted_string
    
    def convert_for_ranking(self, novi_datum):
        konvertirani_datum=self.convert_date_format(novi_datum)
        u_str = str(konvertirani_datum)
        dijelovi = u_str.split('-')
        novi_datum = f'{dijelovi[2]}-{dijelovi[1]}-{dijelovi[0]}'
        return novi_datum
#_______________
#OUTPUT  WINDOW
#_______________
    def output_from_db(self, widget=None):
        if self.job_or_apart == 1:
            task = '''SELECT * FROM Bills_home'''
        else:
             task = '''SELECT * FROM Bills_luxury'''

        rows = list(self.c.execute(task))
        
        column_names = [description[0] for description in self.c.description]

                
        # Ako želite prikazati samo prvih 4 stupca:
        self.rows_filtered = [tuple(row[:4]) for row in rows]
        column_names_filtered = column_names[:4]
            
        
        # Pretpostavimo da imate listu podataka i nazive stupaca
        # Izračunajte maksimalnu širinu sadržaja za svaki stupac
     
        sirina, visina = self.main_window.size
        # Zatim postavite column_widths

#ROW FOR SUMMING THE AMOUNT
# Izračun zbroja kolone
        line_row = ['' for _ in column_names_filtered]
        line_row[0] = '-'*10
        line_row[1] = '-'*10
        line_row[2] = '-'*10
        line_row[3] = '-'*10

        self.rows_filtered.append(line_row)
        column_index = 2  # indeks kolone koju želite zbrajati
        suma = sum(row[column_index] for row in self.rows_filtered if isinstance(row[column_index], (int, float)))
        total_row = ['' for _ in column_names_filtered]
        total_row[2] = f'{suma}'
        total_row[0] = 'SUM:'
        self.rows_filtered.append(total_row)


#TABLE
        self.table = toga.Table(
            headings=column_names_filtered,
            data=self.rows_filtered,
            width = sirina - 20,
            style= self.tabel_style_2
        )

# Prilagodba širine stupaca putem stilova (ako je dostupno)
# npr. za svaki stupac napraviti zasebni stil
      
        # Scroll container s fleksibilnim širinama
        scroll = toga.ScrollContainer(content=self.table, style=Pack(flex=1))
        #button1 = toga.Button("Prikaži sve", on_press=self.return_to_main, style=self.button_style_1)
        if self.job_or_apart == 1:
            self.return_button = toga.Button("Return",  on_press=self.open_new_window3, style=self.button_style_return)
        else:
            self.return_button = toga.Button("Return",  on_press=self.show_buttons_apartm, style=self.button_style_return)



        # Kontejner za gumbe
        buttons_container = toga.Box(
            children=[self.return_button],
            style=Pack(direction=ROW, alignment=CENTER, padding=10)
        )

        # Glavni kontejner s scrollom i gumbima ispod
        container = toga.Box(
            children=[
                scroll,
                buttons_container
            ],
            style=Pack(flex=1, alignment=CENTER, direction=COLUMN)
        )

        self.main_window.content = container
#_______________
#GET DATE FUNCTION FOR EMPTY DATE FIELD
#_______________
    def get_datum(self, datum_str):
        if not datum_str or datum_str.strip() == "":
            return datetime.now().strftime("%d-%m-%Y")
        else:
            return datum_str
            
                

#_______________
#METHOD FOR ORDERING THE TABLE BY NAME OF FIRM
#_______________


    def window_with_ordered_by_firm(self, widget=None):
        if self.stored_variable_for_order_switch == 0:
            self.ordered_rows_firm = list(self.order_by_firm())
        else:
            self.ordered_rows_firm = list(self.change_order_by_firm())



        column_names = [description[0] for description in self.c.description]

        rows_filtered = [tuple(row[:4]) for row in self.ordered_rows_firm]
        column_names_filtered = column_names[:4]

        sirina, visina = self.main_window.size
#TABLE
        table = toga.Table(
            padding=20,
            headings = column_names_filtered,
            data = rows_filtered,
            width=sirina - 50,
            style=self.tabel_style_3
        )


        scroll = toga.ScrollContainer(content = table, style=Pack(flex=1))
        self.reorder_button = toga.Button(
            'Turn around',  # Tekst dugmeta
            on_press= self.on_press_toogle_reorder,
            style=Pack(padding=10)
        )
        if self.job_or_apart == 1:
            self.return_button = toga.Button("Return",  on_press=self.open_new_window3, style=self.button_style_return)
        else:
            self.return_button = toga.Button("Return",  on_press=self.show_buttons_apartm, style=self.button_style_return)


        buttons_container = toga.Box(
            children=[self.reorder_button, self.return_button],
            style=Pack(direction=ROW, alignment=CENTER, padding=10)

        )

        new_window = toga.Box(
            children=[scroll,
                      buttons_container],
            style=Pack(flex=1, alignment=CENTER, direction=COLUMN)

        )

        self.main_window.content = new_window

    def order_by_firm(self):
        if self.job_or_apart == 1:
            task = '''
                SELECT * FROM Bills_home
                ORDER BY Company ASC
            '''
        else:
                task = '''
                SELECT * FROM Bills_luxury
                ORDER BY Company ASC
            '''

        return self.c.execute(task)
    
    def change_order_by_firm(self, widget=None):
        if self.job_or_apart == 1:

            task = '''
                SELECT * FROM Bills_home
                ORDER BY Company DESC
            '''
        else:
                task = '''
                SELECT * FROM Bills_luxury
                ORDER BY Company DESC
            '''

        return self.c.execute(task)
        
    def on_press_toogle_reorder(self, widget=None):
        # Promijeni redoslijed
        if self.stored_variable_for_order_switch == 0:
            self.stored_variable_for_order_switch = 1
        else:
            self.stored_variable_for_order_switch = 0
        self.window_with_ordered_by_firm()



#_______________
#METHOD FOR ORDERING THE TABLE BY DATE
#_______________


    def window_with_ordered_by_date(self, widget=None):
        if self.stored_variable_for_order_switch == 0:
            self.ordered_rows_firm = list(self.order_by_date())
        else:
            self.ordered_rows_firm = list(self.change_order_by_date())


        column_names = [description[0] for description in self.c.description]

        rows_filtered = [tuple(row[:4]) for row in self.ordered_rows_firm]
        column_names_filtered = column_names[:4]

        sirina, visina = self.main_window.size
#TABLE
        table = toga.Table(
            headings = column_names_filtered,
            data = rows_filtered,
            width=sirina - 10,
            style=self.tabel_style_4
        )


        scroll = toga.ScrollContainer(content = table, style=Pack(flex=1))
        self.reorder_button = toga.Button(
            'Turn around',  # Tekst dugmeta
            on_press= self.on_press_toogle_time_reorder,
            style=Pack(padding=10)
        )
        if self.job_or_apart == 1:
            self.return_button = toga.Button("Return",  on_press=self.open_new_window3, style=self.button_style_return)
        else:
            self.return_button = toga.Button("Return",  on_press=self.show_buttons_apartm, style=self.button_style_return)




        buttons_container = toga.Box(
            children=[self.reorder_button, self.return_button],
            style=Pack(direction=ROW, alignment=CENTER, padding=10)

        )

        new_window = toga.Box(
            children=[scroll,
                      buttons_container],
            style=Pack(flex=1, alignment=CENTER, direction=COLUMN)

        )

        self.main_window.content = new_window

    def order_by_date(self):
        if self.job_or_apart == 1:
            task = '''
                SELECT * FROM Bills_home
                ORDER BY Date_to_order ASC
            '''
        else:
                task = '''
                SELECT * FROM Bills_luxury
                ORDER BY Date_to_order ASC
            '''

        return self.c.execute(task)
    
    def change_order_by_date(self, widget=None):
        if self.job_or_apart == 1:
            task = '''
                SELECT * FROM Bills_home
                ORDER BY Date_to_order DESC
            '''
        else:
                task = '''
                SELECT * FROM Bills_luxury
                ORDER BY Date_to_order DESC
            '''

        return self.c.execute(task)
        
    def on_press_toogle_time_reorder(self, widget=None):
        # Promijeni redoslijed
        if self.stored_variable_for_order_switch == 0:
            self.stored_variable_for_order_switch = 1
        else:
            self.stored_variable_for_order_switch = 0
        self.window_with_ordered_by_date()



#DRUGI SET PROZORA: ZA STAN
    def open_win_mark_apartment(self, windget=None):
        self.job_or_apart = 2
        self.open_new_window1(widget=None)
        
    def write_to_apartm_table(self, widget = None):
        self.write_to_db(widget)
        

#_______________
#SHOW DATA WINDOW #WITH BUTTONS ONLY
#_______________    
    def show_buttons_apartm(self, widget):  

        self.show_data_apartm = toga.Box(style=Pack(padding=20, direction=COLUMN))
        out_apart_button = toga.Button("Show all", on_press = self.table_all_apartm , style=self.button_style_7)
        out_apart_date_button = toga.Button("Order by date", on_press = self.window_with_ordered_by_date , style=self.button_style_3)
        out_apart_firm_button = toga.Button("Order by company", on_press = self.window_with_ordered_by_firm, style=self.button_style_7)
        #out_history_button = toga.Button("Pokaži brisanja", on_press = self.output_from_db , style=self.button_style_4)
        return_button = toga.Button("Return", on_press=self.return_to_main, style=self.button_style_return)
        #Loutput = toga.Label("Pokaži ispis")

        self.show_data_apartm.add(out_apart_button)
        self.show_data_apartm.add(out_apart_date_button)
        self.show_data_apartm.add(out_apart_firm_button)
        #self.new_box.add(out_history_button)

        self.show_data_apartm.add(return_button)
        #self.new_box.add(Loutput)

        self.main_window.content = self.show_data_apartm
        self.job_or_apart = 2

#------------------------------------------------------------------------------------------------------
#ONLY SHOW WHAT'S IN THE TABLE APARTMENT
#-------------------------------------------------------------------------------------------------------
    def table_all_apartm(self, widget = None): #interesantno je kako ovu i istu funkciju spojiit u jednu.
        self.output_from_db()

    def delete_wind_apartm(self, widget=None):
        self.job_or_apart = 2
        self.open_new_window4()
        

    def delete_from_apartm(self, widget = None):
        self.job_or_apart = 2
        self.delete_from_db()

        self.table_all_apartm()


def main():
    return HelloWorld()

if __name__ == '__main__':
    main().main_loop()
