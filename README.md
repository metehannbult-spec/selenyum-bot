 import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Chrome ayarlarını yapılandırma
options = Options()
# options.add_argument("--headless")  # Tarayıcının ekranda görünmeden arka planda çalışmasını sağlar (şu an kapalı)
options.add_argument("--disable-gpu") # GPU hızlandırmasını devre dışı bırakır (Headless modda hataları önler)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# WebDriver'ı başlatma ve ayarları uygulama
driver = webdriver.Chrome(options=options)

# Hedef web sitesine gitme
driver.get("https://www.amazon.com")

# Sayfanın yüklenmesi için bekleme
time.sleep(3)

# Sayfa başlığını çekip terminale yazdırma
print("Page title:", driver.title)

# Tarayıcıyı kapatmadan önce bekleme
time.sleep(5)

# İşlem bitince tarayıcıyı tamamen kapatma
driver.quit()
