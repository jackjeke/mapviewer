from kivymd.app import MDApp
from farmersmapview import FarmersMapView
import sqlite3




class MainApp(MDApp):
    conn=None
    curs=None

    def on_start(self):
        ##connect to database
        self.conn=sqlite3.connect('My_DBASE.db')
        self.curs=self.conn.cursor()
        


MainApp().run()
