import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver import Firefox
import pyautogui
import pyperclip
import secret
import winsound
import time
import chime



# xyz.84.7.83

class Browser:
    browser, service = None, None

    # I am using chrome
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    #I am using firefox
    # def __init__(self, driver: str):
    #     self.service = FirefoxService(executable_path=driver)
    #     self.browser = Firefox(service=self.service)

    # #I am using edge
    # def __init__(self, driver: str):
    #     self.browser = webdriver.Edge(driver)


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

    def create_twitch_acc(self, username: str, password: str, email: str):
        self.click_button_by_text('Sign Up')
        time.sleep(1)
        self.add_input(by=By.ID, value='signup-username', text = username)
        self.add_input(by=By.ID, value='password-input', text = password)
        time.sleep(1)
        self.click_button_by_text('Next Step')
        time.sleep(1)
        self.click_button_by_text('Use email instead')
        self.add_input(by=By.ID, value='email-input', text=email)
        self.click_button_by_text('Next Step')
        pyautogui.press('down')
        pyautogui.press('tab')
        pyautogui.press('1')
        pyautogui.press('tab')
        pyautogui.press('2')
        pyautogui.press('0')
        pyautogui.press('0')
        pyautogui.press('0')
        time.sleep(1)
        # self.click_button(by=By.CLASS_NAME, value='Layout-sc-1xcs6mc-0 ktFzpA')


    def find_email(self):
        print('I am here')
        time.sleep(3)
        email = self.browser.find_element(by=By.ID, value='mail_address').get_attribute('value')

        return email

    def find_verification_code(self):
        time.sleep(3)
        verification_code_element = self.browser.find_element(by=By.XPATH, value="//span[contains(text(),'Verification Code')]/following-sibling::p")
        print(verification_code_element.text)
        verification_code = verification_code_element.text.strip()
        return verification_code

    def create_kick_acc(self, username: str, password: str, email: str):
        self.click_button_by_text('Sign Up')
        time.sleep(1)
        self.add_input(by=By.ID, value='email', text = email)
        pyautogui.press('tab')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('tab')
        pyautogui.press('down')
        pyautogui.press('enter')
        pyautogui.press('tab')
        for i in range(0, 23):
            pyautogui.press('down')
        pyautogui.press('enter')
        self.add_input(by=By.ID, value='username', text = username)
        self.add_input(by=By.ID, value='password', text = password)
        self.add_input(by=By.ID, value='password_confirmation', text = password)
        # self.click_button_by_text('Sign Up')
        time.sleep(5)

    chime.theme('zelda')
    def create_visa_acc(self):
        while(True):
            message = self.browser.find_element(by=By.CLASS_NAME, value='alert alert-info border-0 rounded-0').get_attribute('value')

            if message != 'We are sorry, but no appointment slots are currently available. Please try again later':
                print('found')
                while(True):
                    chime.success()
                    time.sleep(1)
                break
            else:
                time.sleep(10)
                pyautogui.press('down')
                print('down')
                time.sleep(10)
                pyautogui.press('up')
                print('up')


        time.sleep(5)




# def make_sound():
#     winsound.Beep(1000, 100000)
#     print('found!!!')






if __name__ == '__main__':
    browser = Browser('twitchCreateAccBot/chromedriver.exe')
    # browser2 = Browser('twitchCreateAccBot/chromedriver.exe')
    # browser2.open_page('https://twitch.tv/')
    # browser2.open_page('https://kick.com/')
    chime.success()
    browser.open_page('https://visa.vfsglobal.com/can/en/fra/login')
    time.sleep(60)


    # email = browser.open_page('https://10minutemail.com/')
    # email = browser.find_email()
    # time.sleep(5)
    # browser2.create_twitch_acc('goodarz12', 'Goodarz@22', email)
    # browser2.create_kick_acc('goodarz12', 'Goodarz@22', email)
    browser.create_visa_acc()
    time.sleep(10)


    # browser.close()