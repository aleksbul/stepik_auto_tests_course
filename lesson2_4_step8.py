import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 100).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()

    x = browser.find_element(By.ID, 'input_value').text
    result = calc(x)
    browser.find_element(By.ID, "answer").send_keys(result)
    browser.find_element(By.ID, "solve").click()
finally:
    time.sleep(10)
    browser.quit()