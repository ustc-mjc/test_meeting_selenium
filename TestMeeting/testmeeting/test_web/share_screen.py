from selenium.webdriver.common.by import By
import time


def share_screen(driver):
    driver.find_element(By.XPATH, "//button[@id='toggleScreen']").click()
    time.sleep(2)
