import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import logging
from selenium.webdriver.common.by import By

logging.getLogger('selenium').setLevel(logging.WARNING)

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

chrome_options.add_argument("--disable-blink-features=AutomationControlled")

chrome_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

def get_internet_speed():
    try:
        driver.get("https://fast.com/")
        time.sleep(11)  # Wait for the page to load
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "speed-value")))
        speed_value = driver.find_element(By.ID, "speed-value").text
        return speed_value
    
    except Exception as e:
        print(e)
