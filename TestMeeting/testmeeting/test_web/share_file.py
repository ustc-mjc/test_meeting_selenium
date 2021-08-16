from selenium.webdriver.common.by import By
import time


def share_file(driver):
    driver.find_element(By.XPATH, "//button[@id='fileShare']").click()
    # driver.find_element(By.XPATH, "//span[@class='sc-hKFxyN kksiKu']").click()
    time.sleep(2)
