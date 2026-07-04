import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
#options.add_argument("--headless")  # Run Chrome in headless mode
options.add_argument("--disable-gpu")  # Disable GPU acceleration

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")  # Bypass OS security model
driver = webdriver.Chrome(options=options)
driver.get("https://www.amazon.com")  
time.sleep(3)  
print("page title:", driver.title)  
time.sleep(5)  
driver.quit()