__author__ = "Kavindu Narathota"
__maintainer__ = "Kavindu Narathota"
__email__ = "kavindu@narathota.com"

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(5)
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(5)

    def like_photo(self, hashtag):
        driver = self.driver
        # if you want to like photos in a profile, update the url accordingly
        # driver.get("https://www.instagram.com/" + hashtag + "/")
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(5)
        for i in range(1, 3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)

        # find image link
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        # pic_hrefs = [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' photos: ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                span_ = driver.find_element_by_xpath("//span[@aria-label='Like']")
                span_.find_element_by_xpath('..').click()
                # driver.find_element_by_class_name("dCJp8").click()
                time.sleep(25)
            except Exception as err:
                print(err)
                time.sleep(2)


bot = InstagramBot("username", "password")
bot.login()
bot.like_photo('hashtag')
