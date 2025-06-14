#https://www.google.com/search?q=weather+delhi
#user agent =Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36
# span id="wob_tm" 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def weather():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113 Safari/537.36"
    )

    service = Service(ChromeDriverManager().install(), log_path='NUL')
    driver = webdriver.Chrome(service=service, options=options)

    query = "delhi"
    url = f"https://www.google.com/search?q=weather+{query}"
    driver.get(url)

    try:
        wait = WebDriverWait(driver, 20)
        temp = wait.until(EC.presence_of_element_located((By.ID, "wob_tm"))).text
        unit = driver.find_element(By.CSS_SELECTOR, "div.vk_bk.wob-unit span.wob_t").text
        desc = driver.find_element(By.ID, "wob_dc").text
        return temp + "" + unit + "  " + desc

    except Exception as e:
        driver.save_screenshot("weather_error.png")
        return "❌ Could not fetch weather data."

    finally:
        driver.quit()
