from selenium.webdriver.common.by import By
import time


def login(driver, username, password):
    username_input = driver.find_element(By.XPATH, "//input[1]")
    password_input = driver.find_element(By.XPATH, "//input[2]")
    signin_button = driver.find_element(By.XPATH, "//form/button")
    # create_new_account_button = driver.find_element(By.XPATH, "//div/button")
    username_input.send_keys(username)
    password_input.send_keys(password)
    time.sleep(1)
    signin_button.click()
    time.sleep(1)
