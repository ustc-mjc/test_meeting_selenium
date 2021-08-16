import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_web.login import login
from test_web.register import register
from test_web.join_meeting import join_meeting
from test_web.leave_meeting import leave_meeting
from test_web.share_screen import share_screen
from test_web.record_screen import record_screen
from test_web.chat import chat
from test_web.share_file import share_file

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


class TestMeeting:
    # def test_register_1(self):
    #     driver1 = webdriver.Chrome(options=opt)
    #     driver1.maximize_window()
    #     driver1.get("http://localhost:8888")
    #     register(driver1, "mjc", "123", "123")
    #     time.sleep(2)
    #     driver1.quit()

    # def test_register_2(self):
    #     driver2 = webdriver.Chrome(options=opt)
    #     driver2.maximize_window()
    #     driver2.get("http://localhost:8888")
    #     register(driver2, "mjc", "123", "321")
    #     time.sleep(2)
    #     driver2.quit()

    # def test_register_3(self):
    #     driver3 = webdriver.Chrome(options=opt)
    #     driver3.maximize_window()
    #     driver3.get("http://localhost:8888")
    #     register(driver3, "123", "123", "123")
    #     time.sleep(2)
    #     driver3.quit()

    # def test_login_1(self):
    #     driver4 = webdriver.Chrome(options=opt)
    #     driver4.maximize_window()
    #     driver4.get("http://localhost:8888")
    #     login(driver4, "mjc", "123")
    #     time.sleep(2)
    #     driver4.quit()

    # def test_login_2(self):
    #     driver5 = webdriver.Chrome(options=opt)
    #     driver5.maximize_window()
    #     driver5.get("http://localhost:8888")
    #     login(driver5, "mjc", "321")
    #     time.sleep(2)
    #     driver5.quit()

    # def test_create_meeting(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test")
    #     time.sleep(2)
    #     driver.quit()

    # def test_join_meeting(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test")
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     driver.execute_script(js)
    #     handles = driver.window_handles
    #     driver.switch_to_window(handles[1])
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test1")
    #     driver.switch_to_window(cur_window)
    #     time.sleep(5)
    #     driver.quit()

    # def test_leave_meeting(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test")
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     driver.execute_script(js)
    #     handles = driver.window_handles
    #     driver.switch_to_window(handles[1])
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test1")
    #     time.sleep(5)
    #     leave_meeting(driver)
    #     driver.switch_to_window(cur_window)
    #     time.sleep(3)
    #     driver.quit()
    # def test_audio_chat(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test", True, False)
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     for i in range(2):
    #         driver.execute_script(js)
    #     handles = driver.window_handles
    #     for i in range(2):
    #         driver.switch_to_window(handles[i+1])
    #         login(driver, "mjc", "123")
    #         join_meeting(
    #             driver, "123456", "test"+str(i+1), True, False)
    #     driver.switch_to_window(cur_window)
    #     time.sleep(10)
    #     driver.quit()

    # def test_video_chat(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test", False, True)
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     for i in range(2):
    #         driver.execute_script(js)
    #     handles = driver.window_handles
    #     for i in range(2):
    #         driver.switch_to_window(handles[i+1])
    #         login(driver, "mjc", "123")
    #         join_meeting(
    #             driver, "123456", "test"+str(i+1), False, True)
    #     driver.switch_to_window(cur_window)
    #     time.sleep(10)
    #     driver.quit()

    # def test_audio_video_chat(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test")
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     for i in range(2):
    #         driver.execute_script(js)
    #     handles = driver.window_handles
    #     for i in range(2):
    #         driver.switch_to_window(handles[i+1])
    #         login(driver, "mjc", "123")
    #         join_meeting(
    #             driver, "123456", "test"+str(i+1))
    #     driver.switch_to_window(cur_window)
    #     time.sleep(10)
    #     driver.quit()

    # def test_screen_share(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test")
    #     share_screen(driver)
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     for i in range(2):
    #         driver.execute_script(js)
    #     handles = driver.window_handles
    #     for i in range(2):
    #         driver.switch_to_window(handles[i+1])
    #         login(driver, "mjc", "123")
    #         join_meeting(
    #             driver, "123456", "test"+str(i+1))
    #         share_screen(driver)
    #     driver.switch_to_window(cur_window)
    #     time.sleep(10)
    #     driver.quit()

    # def test_text_chat(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test")
    #     chat(driver, "你好，世界！")
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     for i in range(2):
    #         driver.execute_script(js)
    #     handles = driver.window_handles
    #     for i in range(2):
    #         driver.switch_to_window(handles[i+1])
    #         login(driver, "mjc", "123")
    #         join_meeting(
    #             driver, "123456", "test"+str(i+1))
    #         chat(driver, "你好，世界！")
    #     driver.switch_to_window(cur_window)
    #     time.sleep(10)
    #     driver.quit()
    # def test_file_share(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test")
    #     share_file(driver)
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     for i in range(2):
    #         driver.execute_script(js)
    #     handles = driver.window_handles
    #     for i in range(2):
    #         driver.switch_to_window(handles[i+1])
    #         login(driver, "mjc", "123")
    #         join_meeting(
    #             driver, "123456", "test"+str(i+1))
    #         share_file(driver)
    #     driver.switch_to_window(cur_window)
    #     time.sleep(100)
    #     driver.quit()

    # def test_record_meeting_1(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test")
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     for i in range(2):
    #         driver.execute_script(js)
    #     handles = driver.window_handles
    #     for i in range(2):
    #         driver.switch_to_window(handles[i+1])
    #         login(driver, "mjc", "123")
    #         join_meeting(
    #             driver, "123456", "test"+str(i+1))
    #     driver.switch_to_window(cur_window)
    #     record_screen(driver, 10)
    #     time.sleep(10)
    #     driver.quit()

    # def test_record_meeting_2(self):
    #     driver = webdriver.Chrome(options=opt)
    #     driver.maximize_window()
    #     driver.get("http://localhost:8888")
    #     login(driver, "mjc", "123")
    #     join_meeting(driver, "123456", "test")
    #     cur_window = driver.current_window_handle
    #     time.sleep(2)

    #     js = "window.open('http://localhost:8888')"
    #     for i in range(2):
    #         driver.execute_script(js)
    #     handles = driver.window_handles
    #     for i in range(2):
    #         driver.switch_to_window(handles[i+1])
    #         login(driver, "mjc", "123")
    #         join_meeting(
    #             driver, "123456", "test"+str(i+1))
    #     driver.switch_to_window(cur_window)
    #     record_screen(driver, 10, False)
    #     leave_meeting(driver)
    #     time.sleep(10)
    #     driver.quit()
    def test_meeting(self):
        driver = webdriver.Chrome(options=opt)
        driver.maximize_window()
        driver.get("http://localhost:8888")
        login(driver, "mjc", "123")
        join_meeting(driver, "123456", "test")
        cur_window = driver.current_window_handle
        time.sleep(1)

        js = "window.open('http://localhost:8888')"
        for i in range(9):
            driver.execute_script(js)
        handles = driver.window_handles
        for i in range(9):
            driver.switch_to_window(handles[i+1])
            login(driver, "mjc", "123")
            join_meeting(
                driver, "123456", "test"+str(i+1))
        driver.switch_to_window(cur_window)
        time.sleep(100)
        driver.quit()
