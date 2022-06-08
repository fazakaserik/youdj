from multiprocessing.connection import wait
from turtle import left, right
import webbrowser
from numpy import size
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

# Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--hide-scrollbars")
chrome_options.add_argument("--content-shell-hide-toolbar")
chrome_options.add_argument("--disable-infobars")

class YouTubePlayer:
    def __init__(self, search_term="a8bQ8-do6a8", width=640, height=360, x_pos=0, y_pos=0, ):
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        self.driver.get("https://www.youtube.com/watch?v="+search_term)
        self.driver.implicitly_wait(10)
        self.driver.set_window_size(width, height)
        self.driver.set_window_position(x_pos,y_pos)
        self.driver.find_element_by_xpath('/html/body/ytd-app/ytd-consent-bump-v2-lightbox/tp-yt-paper-dialog/div[4]/div/div[6]/div[1]/ytd-button-renderer[2]/a/tp-yt-paper-button').click()

    def search(self, search_term):
        search_box = self.driver.find_element_by_xpath("//input[@id='search']")
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.ENTER)

    def play_video(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Play']").click()

    def pause_video(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Pause']").click()

    def play_next_video(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Next']").click()

    def play_previous_video(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Previous']").click()

    def mute_video(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Mute']").click()

    def unmute_video(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Unmute']").click()

    def fullscreen_video(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Full screen']").click()

    def exit_fullscreen_video(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Exit full screen']").click()

    def close_video(self):
        self.driver.find_element_by_xpath("//button[@aria-label='Close']").click()

    def get_video_title(self):
        return self.driver.find_element_by_xpath("//h1[@id='video-title']").text

    def get_video_length(self):
        # TODO: not good?
        return self.driver.find_element_by_xpath("//div[@id='player-timestamp']").text

    def get_video_current_time(self):
        return self.driver.find_element_by_xpath("//div[@id='player-timestamp']").text

    def set_volume(self, volume_percentage):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_class_name("ytp-mute-button")).perform()
        ActionChains(self.driver).drag_and_drop_by_offset(self.driver.find_element_by_class_name("ytp-volume-slider"), (volume_percentage/100)*40-20, 0).perform()

    def get_volume(self):
        return self.driver.find_element_by_xpath("//div[@id='player-volume-level']").get_attribute("style")

    def close_browser(self):
        self.driver.quit()
