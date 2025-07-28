from behave import *
from features.pages.login_page import LoginPage

@given("user is on the login page")
def LaunchBrowser(context):
    context.driver.get("http://localhost:8180/pc/PolicyCenter.do")  # Replace with your real URL

@when("user enters valid username and password")
def Creds(context):
    context.login_page=LoginPage(context)
    context.login_page.login()

@then("user should be redirected to the dashboard")
def VerifyDashboard(context):
    title=context.login_page.get_dashboard_title()
    assert "My Summary" in title, "Wrong Page"
