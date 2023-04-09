import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import secret

class Browser:
    browser, service = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)


    def open_page(self, url: str):
        self.browser.get(url)

    def close(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by = by, value = value)
        field.send_keys(text)
        time.sleep(1)
    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def click_button_by_text(self, text: str):
        button = self.browser.find_element(by=By.XPATH, value=f"//*[text()='{text}']")
        button.click()
        time.sleep(1)

    def create_twitch_acc(self, username: str, password: str, email:str):
        self.click_button_by_text('Sign Up')
        time.sleep(5)
        self.add_input(by=By.ID, value='signup-username', text = username)
        self.add_input(by=By.ID, value='password-input', text = password)


if __name__ == '__main__':
    browser = Browser('/Users/erfan/twitchAccCreator/twitchCreateAccBot/chromedriver')
    browser.open_page('https://twitch.tv/')
    time.sleep(10)

    browser.create_twitch_acc('erfan', 'erfan', 'erfan')
    time.sleep(10)


    browser.close()