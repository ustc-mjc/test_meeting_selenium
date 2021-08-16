from selenium.webdriver.common.by import By
import time


def join_meeting(driver, meeting_id, user_name, audio: bool = True, video: bool = True):
    driver.find_element(By.XPATH, "//input[1]").send_keys(meeting_id)
    driver.find_element(By.XPATH, "//input[2]").send_keys(user_name)
    if not audio:
        driver.find_element(By.XPATH, "//button[1]").click()
    if not video:
        driver.find_element(By.XPATH, "//button[2]").click()
    time.sleep(1)
    driver.find_element(
        By.XPATH, "//button[@id='startMeeting']").click()
    time.sleep(1)
