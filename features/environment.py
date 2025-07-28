from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def before_all(context):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(10)
    context.wait = WebDriverWait(context.driver, 15)
    context.account_number = None

def after_all(context):
    context.driver.quit()