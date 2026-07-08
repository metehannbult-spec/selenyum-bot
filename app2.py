from dbmanager import DBManager


class App2:
    def __init__(self):
        self.db_manager = DBManager()

    def initApp(self):
        msg = "***\n1-öğrenci listesi\n2-öğrenci ekle\n3-öğrenci güncele\n4-öğrenci sil\n5-öğretmen ekle\n6-sınıflara göre dersleri listele\n7-çıkış"
        while True:
            print(msg)
            islem = input("İşlem seçiniz: ")
            if islem == "1":
                pass
            elif islem == "2":
                pass
            elif islem == "3":
                pass
            elif islem == "E" or islem == "ç":
                break
            else:
                print("Geçersiz işlem seçimi. Lütfen tekrar deneyin.")


app2 = App2()
app2.initApp()
        