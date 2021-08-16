from selenium.webdriver.common.by import By
import time


def register(driver, username, password, confir_password):
    time.sleep(1)
    create_new_account_button = driver.find_element(By.XPATH, "//div/button")
    create_new_account_button.click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[1]").send_keys(username)
    driver.find_element(By.XPATH, "//input[2]").send_keys(password)
    driver.find_element(By.XPATH, "//input[3]").send_keys(confir_password)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[1]").click()
    time.sleep(2)
