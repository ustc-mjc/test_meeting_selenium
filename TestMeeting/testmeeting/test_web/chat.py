from selenium.webdriver.common.by import By
import time


def chat(driver, message: str):
    driver.find_element(By.XPATH, "//button[@id='chat']").click()
    messageInput = driver.find_element(By.XPATH, "//input[@id='messageInput']")
    messageInput.send_keys(message)
    driver.find_element(By.XPATH, "//button[@id='sendMessage']").click()
    time.sleep(2)
