from PyQt5.QtWidgets import *
from mesaj import Ui_MainWindow
import firebase_admin
from firebase_admin import credentials,firestore
import re



class mesajekran(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


        string = "(   )-(Geeks)-(   )"
        string = re.sub("\(.*?\)", "(   )", string)
        print(string)
        self.ui.Telefon_yazialani.setText(string)


        """print("1")
        self.Id = credentials.Certificate(r'./key2.json')
        print("2")

        self.app = firebase_admin.initialize_app(self.Id)
        print("3")

        self.db = firestore.client()
"""

        self.ui.Temizle.clicked.connect(self.yaziyitemizle)
        #self.ui.Gonder.clicked.connect(self.mesajgonder)
        self.ui.Iptal.clicked.connect(self.iptalet)



    def yaziyitemizle(self):
        self.ui.ad_soyad_yazialani.clear()
        self.ui.Telefon_yazialani.clear()
        self.ui.eposta_yazialani.clear()
        self.ui.mesaj_yazialani.clear()

    #def mesajgonder(self):



        """ if len(self.ui.ad_soyad_yazialani.text()) == 0 or len(self.ui.Telefon_yazialani.text()) == 0 or len(self.ui.eposta_yazialani.text()) == 0 or len(self.ui.mesaj_yazialani.toPlainText())== 0:
            print("boşluk var")
            self.ui.bilgi_yazialani.setText("Lütfen bilgilerinizi eksiksiz doldurun !")

        else:
            from veritabanı import baglanti_olustur
            from AnaEkran_page import anaekran

            self.AnaEkran_page=anaekran()
            self.veritabanı = baglanti_olustur()

            self.AnaEkran_page.col_query.close()


            self.ui.bilgi_yazialani.clear()


            #document=self.db.collection(u'data').document(u'mesaj')
            document=self.veritabanı.db.collection(u'data').document(u'mesaj')



            print("sorun yok")
            document.set({

                "Ad/Soyad": self.ui.ad_soyad_yazialani.text(),
                "E-posta": self.ui.eposta_yazialani.text(),
                "Mesaj": self.ui.mesaj_yazialani.toPlainText(),
                "Telefon": self.ui.Telefon_yazialani.text()


            })

            self.close()
            self.ui.ad_soyad_yazialani.clear()
            self.ui.Telefon_yazialani.clear()
            self.ui.eposta_yazialani.clear()
            self.ui.mesaj_yazialani.clear()

"""
    def iptalet(self):
        self.close()















