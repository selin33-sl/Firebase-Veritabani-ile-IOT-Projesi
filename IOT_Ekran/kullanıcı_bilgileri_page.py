from PyQt5.QtWidgets import *
from kullanıcı_bilgileri import Ui_MainWindow
import firebase_admin
from firebase_admin import credentials, firestore
from time import sleep
from yüz_tanıma_alanı_page import yuztanima_ekran


class kullanicibilgileri_ekran(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.Temizle.clicked.connect(self.temizle)
        self.ui.iptal.clicked.connect(self.iptalet)
        #self.ui.Onayla.clicked.connect(self.bilgileri_onayla)


        
    def temizle(self):
        self.ui.kullaniciadi_yazialani.clear()
        self.ui.sifre_yazialani.clear()

    def iptalet(self):
        self.close()
        self.ui.kullaniciadi_yazialani.clear()
        self.ui.sifre_yazialani.clear()
        self.ui.bilgi_yazialani.clear()

    """def bilgileri_onayla(self):
        self.ui.sifre_yazialani.setEchoMode(self.ui.sifre_yazialani.Password)


        self.document = self.db.collection(u'data').document(u'kullanici_bilgileri')
        print("4")


        data = self.document.get().to_dict()

        kullanici_adi=data["kullanici_adi"]
        sifre=data["sifre"]



        if self.ui.kullaniciadi_yazialani.text() != kullanici_adi:

            print("ad yanlış")


            self.ui.bilgi_yazialani.setText("Lütfen kullanıcı adınızı tekrar kontrol ediniz")



        if self.ui.sifre_yazialani.text() != sifre:

            print("sifre yanlış")


            self.ui.bilgi_yazialani.setText("Lütfen şifrenizi tekrar kontrol ediniz.")



        if self.ui.kullaniciadi_yazialani.text() == kullanici_adi  and self.ui.sifre_yazialani.text() == sifre:

            print("doğru")


            #self.ui.bilgi_yazialani.setText("Lütfen kullanıcı adınızı tekrar kontrol ediniz.")
            self.yüz_tanıma_alanı_page=yuztanima_ekran()

            self.close()
            self.yüz_tanıma_alanı_page.show()
            self.ui.kullaniciadi_yazialani.clear()
            self.ui.sifre_yazialani.clear()
            self.ui.bilgi_yazialani.clear()



        if self.ui.kullaniciadi_yazialani.text() != kullanici_adi and self.ui.sifre_yazialani.text() != sifre:

            print("ikisi de yanlış")

            
            self.ui.bilgi_yazialani.setText("Lütfen kullanıcı adınızı ve şifrenizi tekrar kontrol ediniz.")"""

