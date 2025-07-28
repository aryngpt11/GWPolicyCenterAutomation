from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, context):
        self.driver = context.driver

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR,"input[name='Login-LoginScreen-LoginDV-username']").send_keys("su")
        self.driver.find_element(By.CSS_SELECTOR,"input[name='Login-LoginScreen-LoginDV-password']").send_keys("gw")
        self.driver.find_element(By.CSS_SELECTOR,"div[aria-label='Log In']").click()

    def get_dashboard_title(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".gw-TitleBar--title").text
