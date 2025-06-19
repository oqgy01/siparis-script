from bs4 import BeautifulSoup
import pandas as pd
from io import BytesIO
from colorama import init, Fore, Style
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import datetime
import colorama
from copy import copy
from openpyxl.worksheet.table import Table, TableStyleInfo

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

username = "mustafa_kod@haydigiy.com"
password = "123456"
login_url = "https://www.siparis.haydigiy.com/kullanici-giris/?ReturnUrl=%2Fadmin"
desired_page_url = "https://www.siparis.haydigiy.com/admin/exportorder/edit/154/"

try:
    # 2.1) Giriş
    driver.get(login_url)
    time.sleep(2)
    driver.find_element(By.NAME, "EmailOrPhone").send_keys(username)
    driver.find_element(By.NAME, "Password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(3)

    # 2.2) İlgili sayfaya gidip tarih ayarlarını girmek
    driver.get(desired_page_url)
    time.sleep(2)

    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    formatted_date_no_leading = f"{yesterday.day}.{yesterday.month}.{yesterday.year}"

    end_date_input = driver.find_element(By.ID, "EndDate")
    end_date_input.clear()
    end_date_input.send_keys(formatted_date_no_leading)

    start_date_input = driver.find_element(By.ID, "StartDate")
    start_date_input.clear()
    start_date_input.send_keys(formatted_date_no_leading)

    save_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary[name="save"]')
    save_button.click()

    time.sleep(10)

except Exception as e:
    print(colorama.Fore.RED + f"Giriş veya tarih ayarı sırasında hata: {e}" + colorama.Style.RESET_ALL)
    raise  # Hata sonrası kodun tamamen durması için hatayı tekrar fırlatıyoruz

finally:
    driver.quit()