from PyQt5.QtWidgets import *
from karaktersiniri import *
import threading
import firebase_admin
from firebase_admin import credentials,firestore
import time


class karakter(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        self.Id = credentials.Certificate(r'./key2.json')
        self.app = firebase_admin.initialize_app(self.Id)
        self.db = firestore.client()

        liste=list()


        # -------------------------------------- DUYURU1--------------------------------------

        callback = threading.Event()

        delete_done = threading.Event()

        def on_snapshot(col_snapshot, changes, read_time):

            for change in changes:

                if change.type.name == 'ADDED':

                    print(f'New duyuru: {change.document.to_dict()}')

                    data = change.document.to_dict()


                    b = data["duyuru"]
                    if len(b) >= 15:
                        liste.append(b[:10]+"...")
                        print(liste)

                    else:
                        liste.append(b[:10])

                    for i in liste:

                        print(i)

                        self.ui.label.setText(i)

                        #self.ui.yazialani.appendPlainText(i)
                        #self.ui.textEdit.append(i)


                elif change.type.name == 'MODIFIED':

                    #self.ui.textEdit.clear()

                    print(f'Modified duyuru: {change.document.to_dict()}')
                    data = change.document.to_dict()
                    print(len(data))


                    liste.clear()


                    b = data["duyuru"]
                    if len(b) >= 15:
                        liste.append(b[:10] + "...")


                    else:
                        liste.append(b[:10])

                    for i in liste:
                        print(i)
                        self.ui.label.setText(i)



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
                        self.ui.yazialani.appendPlainText(i)
                        #self.ui.textEdit.append(i)

                delete_done.set()

            callback.set()


        doc = self.db.collection(u'data').document(u'tumduyuru1')

        query_watch = doc.on_snapshot(on_snapshot)


app=QApplication([])
window=karakter()
window.show()
app.exec_()