from selenium.webdriver.common.by import By
import time


def leave_meeting(driver):
    driver.find_element(
        By.XPATH, "//button[@id='leaveMeeting']").click()
    time.sleep(1)
