import time
from datetime import datetime
import firebase_admin
from firebase_admin import credentials,firestore
import threading
from AnaEkran import *
from mesaj_page import mesajekran
from tüm_duyurular_page import tümduyurularekran
from kullanıcı_bilgileri_page import kullanicibilgileri_ekran
from iletisim_bilgileri_page import *
from mesaj_iletildi_page import mesajiletimi
from yüz_tanıma_alanı_page import yuztanima_ekran
from hosgeldin_sahip_page import hosgeldin_ekrani
from duyuruDialog_page import duyuru

class anaekran(QMainWindow):


    def __init__(self):

        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #--------------------------FİREBASE VERİTABANI BAĞLANTISI--------------------------

        self.Id = credentials.Certificate(r'./dosyanızın_adi.json')
        self.app = firebase_admin.initialize_app(self.Id)
        self.db = firestore.client()

        document = self.db.collection(u'data').document(u'kapi')


        #--------------------------STATUSBAR--------------------------
        self.ui.statusbar.showMessage("869Tech")


        self.timer = QtCore.QTimer(self)

        self.timer.start(1000)

        time = QtCore.QDateTime.currentDateTime()

        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')

        self.ui.hour = QLabel()

        self.ui.hour.setText(timeDisplay)


        self.ui.statusbar.addPermanentWidget(self.ui.hour,stretch=0)

        """now = datetime.now()
        dt = now.strftime("%H:%M:%S")
        self.hour=QLabel(dt)

        self.ui.statusbar.addPermanentWidget(self.hour, stretch=0)"""


        # --------------------------DERS PROGRAMI--------------------------

        liste = list()
        liste1 = list()

        callback_done = threading.Event()

        delete_done = threading.Event()

        def on_snapshot(col_snapshot, changes, read_time):


            for change in changes:
                if change.type.name == 'ADDED':

                    print(f'New day: {change.document.to_dict()}')
                    data = change.document.to_dict()

                    liste1.append(data)
                    liste.append(data["pazartesi"])
                    liste.append(data["salı"])
                    liste.append(data["çarşamba"])
                    liste.append(data["perşembe"])
                    liste.append(data["cuma"])

                    a = -1
                    # enumerate() methodu itere edilebilir bir objenin(list, string, tuple vb) itemlarına birer index numarası verir.
                    for satir_sayi, satir_data in enumerate(liste):
                        a += 1
                        # satırı doğrudan tabloya ekler
                        self.ui.Ders_programi.insertRow(satir_sayi)

                        self.ui.Ders_programi.setItem(0, a, QtWidgets.QTableWidgetItem(str(satir_data)))

                    b = -1
                    for satir_sayi, satir_data in enumerate(liste1):
                        # tabloya 'satir_sayi' kadar sayı ekler
                        self.ui.Ders_programi.insertRow(satir_sayi)
                        # tabloda kaç satır görünmesini istediğimizi bu şekilde tanımlarız.
                        self.ui.Ders_programi.setRowCount(5)
                        for data in satir_data:
                            b += 1
                            self.ui.Ders_programi.setItem(0, b, QtWidgets.QTableWidgetItem(str(data)))


                elif change.type.name == 'MODIFIED':

                    
                    print(f'Modified day: {change.document.to_dict()}')
                    data = change.document.to_dict()
                    liste1.append(data)
                    liste.append(data["pazartesi"])
                    liste.append(data["salı"])
                    liste.append(data["çarşamba"])
                    liste.append(data["perşembe"])
                    liste.append(data["cuma"])

                    a = -1
                    # enumerate() methodu itere edilebilir bir objenin(list, string, tuple vb) itemlarına birer index numarası verir.
                    for satir_sayi, satir_data in enumerate(liste):
                        a += 1
                        # satırı doğrudan tabloya ekler
                        self.ui.Ders_programi.insertRow(satir_sayi)

                        self.ui.Ders_programi.setItem(0, a, QtWidgets.QTableWidgetItem(str(satir_data)))

                    b = -1
                    for satir_sayi, satir_data in enumerate(liste1):
                        # tabloya 'satir_sayi' kadar sayı ekler
                        self.ui.Ders_programi.insertRow(satir_sayi)
                        # tabloda kaç satır görünmesini istediğimizi bu şekilde tanımlarız.
                        self.ui.Ders_programi.setRowCount(5)
                        for data in satir_data:
                            b += 1
                            self.ui.Ders_programi.setItem(0, b, QtWidgets.QTableWidgetItem(str(data)))

                elif change.type.name == 'REMOVED':
                    print(f'Removed day: {change.document.to_dict()}')
                    data = change.document.to_dict()
                    liste1.append(data)
                    liste.append(data["pazartesi"])
                    liste.append(data["salı"])
                    liste.append(data["çarşamba"])
                    liste.append(data["perşembe"])
                    liste.append(data["cuma"])
                    delete_done.set()
            callback_done.set()

        self.col_query = self.db.collection(u'data').document(u'test')

        query_watch = self.col_query.on_snapshot(on_snapshot)



        # --------------------------ÖNEMLİ DUYURULAR--------------------------

        callback = threading.Event()

        delete_done = threading.Event()


        def on_snapshot(col_snapshot, changes, read_time):

            for change in changes:

                if change.type.name == 'ADDED':

                    print(f'New duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()
                    print(len(data))
                    for i in data:
                        self.ui.onemli_duyurular_yazialani.appendPlainText(data[i])


                elif change.type.name == 'MODIFIED':
                    print("değişti")


                    self.ui.onemli_duyurular_yazialani.clear()

                    print("ALAN:",self.ui.onemli_duyurular_yazialani.toPlainText())

                    print(f'Modified duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()


                    for i in data:

                        self.ui.onemli_duyurular_yazialani.appendPlainText(data[i])


                elif change.type.name == 'REMOVED':

                    print(f'Removed duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()

                    self.ui.onemli_duyurular_yazialani.appendPlainText(data["1.duyuru"])


                    delete_done.set()


            callback.set()


        doc = self.db.collection(u'data').document(u'duyuru')

        query_watch = doc.on_snapshot(on_snapshot)



        self.mesaj_page = mesajekran()
        self.tüm_duyurular_page = tümduyurularekran()
        self.kullanıcı_bilgileri_page = kullanicibilgileri_ekran()
        self.iletisim_bilgileri_page = iletisimbilgileri()
        self.yüz_tanıma_alanı_page=yuztanima_ekran()
        self.mesaj_iletildi_page=mesajiletimi()
        self.hosgeldin_sahip=hosgeldin_ekrani()
        self.duyuruDialog_page=duyuru()


        self.ui.mesaj_birakin.clicked.connect(self.mesaj_birak)
        self.ui.Tum_Duyurular.clicked.connect(self.tum_duyuru_gor)
        self.ui.Fotograf.clicked.connect(self.kullanici_girisi)
        self.ui.Iletisim_Bilgileri.clicked.connect(self.iletisim_bilgileri)
        self.mesaj_page.ui.Gonder.clicked.connect(self.mesajgonder)
        self.kullanıcı_bilgileri_page.ui.Onayla.clicked.connect(self.bilgileri_onayla)
        self.hosgeldin_sahip.ui.kapiyi_ac.clicked.connect(self.kapi_ac)
        self.tüm_duyurular_page.ui.Detay1.clicked.connect(self.Detay1_Button)



    def Detay1_Button(self):
        # -------------------------------------- DUYURU1 BAŞLIĞI --------------------------------------
        self.duyuruDialog_page.show()

        self.duyuruDialog_page.ui.duyuru_basligi_yazialani.clear()


        callback = threading.Event()

        delete_done = threading.Event()

        def on_snapshot(col_snapshot, changes, read_time):

            for change in changes:

                if change.type.name == 'ADDED':

                    print(f'New duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()

                    print(len(data))
                    for i in data:
                        self.duyuruDialog_page.ui.duyuru_basligi_yazialani.append(data[i])

                elif change.type.name == 'MODIFIED':



                    print(f'Modified duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()
                    for i in data:
                        self.duyuruDialog_page.ui.duyuru_basligi_yazialani.append(data[i])


                elif change.type.name == 'REMOVED':

                    print(f'Removed duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()

                    self.duyuruDialog_page.ui.duyuru_basligi_yazialani.append(data[i])

                    delete_done.set()

            callback.set()

        doc = self.db.collection(u'data').document(u'tümduyurubaslik1')

        query_watch = doc.on_snapshot(on_snapshot)

        # -------------------------------------- DUYURU1--------------------------------------

        self.duyuruDialog_page.ui.duyuru_mesaji_yazialani.clear()

        callback = threading.Event()

        delete_done = threading.Event()

        def on_snapshot(col_snapshot, changes, read_time):

            for change in changes:

                if change.type.name == 'ADDED':

                    print(f'New duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()

                    print(len(data))
                    for i in data:
                        self.duyuruDialog_page.ui.duyuru_mesaji_yazialani.append(data[i])

                elif change.type.name == 'MODIFIED':


                    print(f'Modified duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()
                    for i in data:
                        self.duyuruDialog_page.ui.duyuru_mesaji_yazialani.append(data[i])


                elif change.type.name == 'REMOVED':

                    print(f'Removed duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()

                    self.duyuruDialog_page.ui.duyuru_mesaji_yazialani.append(data[i])

                    delete_done.set()

            callback.set()

        doc = self.db.collection(u'data').document(u'tumduyuru1')

        query_watch = doc.on_snapshot(on_snapshot)



    def mesaj_birak(self):

        self.mesaj_page.show()

        """time.sleep(3)
        print("ekran açıldı")

        for i in range(10,0,-1):
            #self.mesaj_page.show()

            #self.mesaj_page.ui.sayac.clear()
            time.sleep(1)
            print(i)

        self.mesaj_page.close()"""


    def tum_duyuru_gor(self):

        self.tüm_duyurular_page.show()

        # -------------------------------------- TÜM DUYURULAR EKRANI DUYURU1 BAŞLIĞI --------------------------------------

        callback = threading.Event()

        delete_done = threading.Event()

        def on_snapshot(col_snapshot, changes, read_time):

            for change in changes:

                if change.type.name == 'ADDED':

                    print(f'New duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()
                    print(len(data))
                    for i in data:
                        self.tüm_duyurular_page.ui.Duyuru_Baslik_1.setText(data[i])


                elif change.type.name == 'MODIFIED':



                    print(f'Modified duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()

                    for i in data:
                        self.tüm_duyurular_page.ui.Duyuru_Baslik_1.setText(data[i])


                elif change.type.name == 'REMOVED':

                    print(f'Removed duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()

                    self.tüm_duyurular_page.ui.Duyuru_Baslik_1.setText(data[i])

                    delete_done.set()

            callback.set()

        doc = self.db.collection(u'data').document(u'tümduyurubaslik1')

        query_watch = doc.on_snapshot(on_snapshot)



        # --------------------------TÜM DUYURULAR EKRANI DUYURU_1--------------------------

        liste = list()
        self.tüm_duyurular_page.ui.Duyuru_1.clear()

        callback = threading.Event()

        delete_done = threading.Event()

        def on_snapshot(col_snapshot, changes, read_time):

            for change in changes:

                if change.type.name == 'ADDED':


                    print(f'New duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()
                    print(len(data))
                    b = data["duyuru"]
                    if len(b) >= 15:
                        liste.append(b[:10] + "...")
                        print(liste)

                    else:
                        liste.append(b[:10])

                    for i in liste:
                        print(i)

                        self.tüm_duyurular_page.ui.Duyuru_1.appendPlainText(i)


                elif change.type.name == 'MODIFIED':

                    time.sleep(2)

                    self.tüm_duyurular_page.ui.Duyuru_1.clear()
                    time.sleep(2)

                    print(f'Modified duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()
                    liste.clear()

                    b = data["duyuru"]
                    if len(b) >= 15:
                        liste.append(b[:10] + "...")
                        print(liste)

                    else:
                        liste.append(b[:10])

                    for i in liste:
                        print(i)

                        self.tüm_duyurular_page.ui.Duyuru_1.appendPlainText(i)
                        # self.ui.textEdit.append(i)


                elif change.type.name == 'REMOVED':

                    print(f'Removed duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()

                    b = data["duyuru"]
                    if len(b) >= 15:
                        liste.append(b[:10] + "...")
                        print(liste)

                    else:
                        liste.append(b[:10])

                    for i in liste:
                        print(i)

                        self.tüm_duyurular_page.ui.Duyuru_1.appendPlainText(i)
                        # self.ui.textEdit.append(i)

                    delete_done.set()

            callback.set()


        docum = self.db.collection(u'data').document(u'tumduyuru1')

        query_watch = docum.on_snapshot(on_snapshot)

    def kullanici_girisi(self):

        self.kullanıcı_bilgileri_page.show()

    def iletisim_bilgileri(self):

        self.iletisim_bilgileri_page.show()

    def mesajgonder(self):

        if len(self.mesaj_page.ui.ad_soyad_yazialani.text()) == 0 or len(self.mesaj_page.ui.Telefon_yazialani.text()) == 0 or len(
                self.mesaj_page.ui.eposta_yazialani.text()) == 0 or len(self.mesaj_page.ui.mesaj_yazialani.toPlainText()) == 0:

            self.mesaj_page.ui.bilgi_yazialani.setText("Lütfen bilgilerinizi eksiksiz doldurun !")

        else:

            self.mesaj_page.ui.bilgi_yazialani.clear()

            document = self.db.collection(u'data').document(u'mesaj')


            document.set({

                "Ad/Soyad": self.mesaj_page.ui.ad_soyad_yazialani.text(),
                "E-posta": self.mesaj_page.ui.eposta_yazialani.text(),
                "Mesaj": self.mesaj_page.ui.mesaj_yazialani.toPlainText(),
                "Telefon": self.mesaj_page.ui.Telefon_yazialani.text()

            })


            self.mesaj_page.ui.ad_soyad_yazialani.clear()
            self.mesaj_page.ui.Telefon_yazialani.clear()
            self.mesaj_page.ui.eposta_yazialani.clear()
            self.mesaj_page.ui.mesaj_yazialani.clear()

            #mesaj ekranını kapanması

            self.mesaj_page.close()

            #Diyalog ekranının açılması

            #self.mesaj_iletildi_page.show()

            #Diyalog ekranının 3 saniye görüntülenmesi

            #time.sleep(3)

            #Diyalog ekranının kapanması

            #self.mesaj_iletildi_page.close()

            """self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.mesaj_iletildi_page.close)
            self.timer.setInterval(1000)
            self.timer.start()
"""


    def bilgileri_onayla(self):

        self.kullanıcı_bilgileri_page.ui.sifre_yazialani.setEchoMode(self.kullanıcı_bilgileri_page.ui.sifre_yazialani.Password)

        self.document = self.db.collection(u'data').document(u'kullanici_bilgileri')



        data = self.document.get().to_dict()

        kullanici_adi = data["kullanici_adi"]
        sifre = data["sifre"]


        if self.kullanıcı_bilgileri_page.ui.kullaniciadi_yazialani.text() != kullanici_adi:
            print("ad yanlış")

            self.kullanıcı_bilgileri_page.ui.bilgi_yazialani.setText("Lütfen kullanıcı adınızı tekrar kontrol ediniz")

        if self.kullanıcı_bilgileri_page.ui.sifre_yazialani.text() != sifre:
            print("sifre yanlış")

            self.kullanıcı_bilgileri_page.ui.bilgi_yazialani.setText("Lütfen şifrenizi tekrar kontrol ediniz.")

        if self.kullanıcı_bilgileri_page.ui.kullaniciadi_yazialani.text() == kullanici_adi and self.kullanıcı_bilgileri_page.ui.sifre_yazialani.text() == sifre:
            print("doğru")

            # self.ui.bilgi_yazialani.setText("Lütfen kullanıcı adınızı tekrar kontrol ediniz.")


            self.kullanıcı_bilgileri_page.close()
            self.kullanıcı_bilgileri_page.ui.kullaniciadi_yazialani.clear()
            self.kullanıcı_bilgileri_page.ui.sifre_yazialani.clear()
            self.kullanıcı_bilgileri_page.ui.bilgi_yazialani.clear()

            self.yüz_tanıma_alanı_page.show()

            print("5")

            import dlib
            import cv2
            import face_recognition

            cap = cv2.VideoCapture(0)


            # çözünürlük ayarları
            cap.set(3, 400)
            cap.set(4, 200)

            # pencere konumu ayarları

            cv2.namedWindow("frame")
            cv2.moveWindow("frame",650,350)

            # yüz tespiti için

            detector = dlib.get_frontal_face_detector()

            # Yüzünü tanımasını istediğim profillerin tanıtılması

            elon = face_recognition.load_image_file("elon.jpg")
            elon_encoding = face_recognition.face_encodings(elon)[0]

            # Döngüyle her görüntü incelenir.

            while True:
                # Kameradan alınan görüntü okunur
                _, frame = cap.read()
                face_locations = []

                faces = detector(frame)

                # Yüz tespit ettikten sonra sınırlama çizgilerinin tanımı
                for face in faces:
                    x = face.left()
                    y = face.top()
                    w = face.right()
                    h = face.bottom()
                    face_locations.append([y, w, h, x])


                # tespit edilmiş yüzler encoding edilir
                faces_encodigs = face_recognition.face_encodings(frame, face_locations)

                i = 0

                # encoding edilen yüzler üzerinde gezilir
                for face in faces_encodigs:
                    y, w, h, x = face_locations[i]
                    i += 1

                    # önce bilinen yüzü sonra bilinmeyen yüzü değer atadık

                    result2 = face_recognition.compare_faces([elon_encoding], face)

                    # Belirlenen yüz resmi aktif görüntü içerisindeki lokasyonda gösterilmek için çerçeve oluşturulur.

                    if result2[0] == True:
                        cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
                        cv2.rectangle(frame, (x, h), (w, h + 30), [0, 0, 255], -1)
                        cv2.putText(frame, "elon musk", (x, h + 25), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

                        self.yüz_tanıma_alanı_page.close()

                        self.hosgeldin_sahip.show()



                    else:
                        cv2.rectangle(frame, (x, y), (w, h), (0, 0, 255), 2)
                        cv2.rectangle(frame, (x, h), (w, h + 30), [0, 0, 255], -1)
                        cv2.putText(frame, "bilinmiyor", (x, h + 25), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)


                # Bulunan yüz video üzerinde gösterilir

                cv2.imshow("frame", frame)

                # Videoyu kapatmak için klavyeden ‘q’ ya basılması gerekir

                if cv2.waitKey(1) & 0xff == ord("q") or result2[0] == True:
                    break

            # kamera serbest bırakılır.

            # cap.release()

            # tüm pencereleri kapatır.

            cv2.destroyAllWindows()

            print("yüz tanıma sistemi sorunsuz çalıştı.")


        if self.kullanıcı_bilgileri_page.ui.kullaniciadi_yazialani.text() != kullanici_adi and self.kullanıcı_bilgileri_page.ui.sifre_yazialani.text() != sifre:
            print("ikisi de yanlış")

            self.kullanıcı_bilgileri_page.ui.bilgi_yazialani.setText("Lütfen kullanıcı adınızı ve şifrenizi tekrar kontrol ediniz.")

    def kapi_ac(self):

        document = self.db.collection(u'data').document(u'kapi')

        data = document.get().to_dict()
        if data["durum"] == "off":
            print("KAPI AÇILDI ")
            document.update({"durum": "on"})

        elif data["durum"] == "on":
            print("KAPI ZATEN AÇIK ")









