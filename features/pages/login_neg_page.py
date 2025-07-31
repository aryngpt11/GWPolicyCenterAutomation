import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class LoginNegPage:
    def __init__(self,context):
        self.driver = context.driver
        self.wait = context.wait

    def go_to_login_page(self):
        self.driver.get("http://localhost:8180/pc/PolicyCenter.do")

    def enter_username(self, username):
        self.driver.find_element(By.CSS_SELECTOR,"input[name='Login-LoginScreen-LoginDV-username']").send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR,"input[name='Login-LoginScreen-LoginDV-password']").send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR,"div[aria-label='Log In']").click()

    def is_invalid_login_message_displayed(self):
        text= self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='Login-LoginScreen-LoginFormMessage'] div[class='gw-VerbatimWidget--inner']"))).text
        print(text)
        return "incorrect" in text or "Please try again" in text

