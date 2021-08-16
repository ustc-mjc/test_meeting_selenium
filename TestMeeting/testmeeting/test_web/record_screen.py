from selenium.webdriver.common.by import By
import time


def record_screen(driver, record_time: int, is_end: bool = True):
    driver.find_element(By.XPATH, "//button[@id='recordScreen']").click()
    time.sleep(record_time)
    if (is_end):
        driver.find_element(By.XPATH, "//button[@id='recordScreen']").click()
