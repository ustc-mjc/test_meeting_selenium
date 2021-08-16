import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_web.login import login
from test_web.join_meeting import join_meeting
from test_web.share_screen import share_screen
from test_web.record_screen import record_screen
from test_web.chat import chat


def video_chat(number: int):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", {
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        # "profile.default_content_setting_values.geolocation": 1,
        # "profile.default_content_setting_values.notifications": 1
    })
    opt.add_argument('--use-fake-ui-for-media-stream')
    opt.add_argument('--enable-usermedia-screen-capturing')
    opt.add_argument('--auto-select-desktop-capture-source=屏幕1')
    driver = webdriver.Chrome(chrome_options=opt)
    driver.maximize_window()
    driver.get("http://localhost:8888")

    meeting_id = "123456"
    login(driver)
    join_meeting(driver, meeting_id, "test")
    share_screen(driver)

    time.sleep(1)
    cur_window = driver.current_window_handle

    # 打开多个窗口
    if (number > 1):
        js = "window.open('http://localhost:8888')"
        for i in range(number-1):
            driver.execute_script(js)

        # 切换到每个窗口，加入会议
        handles = driver.window_handles
        for i in range(number-1):
            driver.switch_to_window(handles[i+1])
            join_meeting(driver, meeting_id, "test"+str(i))
            time.sleep(1)

        # 切换回到当前窗口
        driver.switch_to_window(cur_window)

    record_screen(driver, 10)
    chat(driver, '你好，世界！')

    time.sleep(10)
    driver.quit()


if __name__ == "__main__":
    video_chat(1)
