import mysql.connector

class DBManager:
    def __init__(self):
        try:
            # Buradaki bilgileri kendi veritabanınıza göre güncelleyin
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="sifreniz",      # MySQL şifrenizi buraya yazın
                database="schooldb"       # Kullanacağınız veritabanı adı
            )
            self.cursor = self.connection.cursor()
            print("Veritabanı bağlantısı başarılı!")
            
        except mysql.connector.Error as err:
            print(f"Veritabanı bağlantı hatası: {err}")

    # 1. İşlem: Öğrenci Listesini Getirme
    def ogrenci_listesi(self):
        sql = "SELECT * FROM student" # Tablo adınızı 'student' veya 'ogrenci' olarak güncelleyin
        self.cursor.execute(sql)
        try:
            ogrenciler = self.cursor.fetchall()
            for ogrenci in ogrenciler:
                print(ogrenci)
        except mysql.connector.Error as err:
            print(f"Hata: {err}")

    # 2. İşlem: Öğrenci Ekleme
    def ogrenci_ekle(self, ad, soyad):
        sql = "INSERT INTO student (ad, soyad) VALUES (%s, %s)"
        values = (ad, soyad)
        try:
            self.cursor.execute(sql, values)
            self.connection.commit()
            print(f"{self.cursor.rowcount} öğrenci eklendi.")
        except mysql.connector.Error as err:
            print(f"Hata: {err}")

    # Bağlantıyı kapatmak için (uygulama kapanırken çağrılabilir)
    def baglantiyi_kapat(self):
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Veritabanı bağlantısı kapatıldı.")