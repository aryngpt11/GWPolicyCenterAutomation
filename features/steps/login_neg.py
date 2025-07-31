# from behave import given, when, then
# from features.pages.login_neg_page import LoginNegPage
# from time import sleep
#
# @given("user on the login page")
# def step_user_on_login_page(context):
#     context.login_neg_page = LoginNegPage(context)
#     context.login_neg_page.go_to_login_page()
#
# @when("user enters invalid username and valid password")
# def step_invalid_username(context):
#     context.login_neg_page.enter_username("qwert")
#     context.login_neg_page.enter_password("gw")
#
# @when("user enters valid username and invalid password")
# def step_invalid_password(context):
#     context.login_neg_page.enter_username("su")
#     context.login_neg_page.enter_password("asdfg")
#
# @when("user submits the login form without entering credentials")
# def step_empty_credentials(context):
#     context.login_neg_page.enter_username("")
#     context.login_neg_page.enter_password("")
#
# @when("user clicks the login button")
# def step_click_login(context):
#     context.login_neg_page.click_login()
#
# @then("user should see an error message for invalid login")
# def step_error_message_invalid(context):
#     assert context.login_neg_page.is_invalid_login_message_displayed()
#
#


from behave import given, when, then
from features.pages.login_neg_page import LoginNegPage

@given("user on the login page")
def step_user_on_login_page(context):
    context.login_neg_page = LoginNegPage(context)
    context.login_neg_page.go_to_login_page()

@when("user leaves the username and password fields empty")
def step_user_leaves_both_fields_empty(context):
    context.login_neg_page.enter_username("")
    context.login_neg_page.enter_password("")

@when("user clicks on the login button")
def step_click_login_button(context):
    context.login_neg_page.click_login()

@then("an error message should be displayed")
def step_verify_required_fields_error(context):
    assert context.login_neg_page.is_invalid_login_message_displayed()

@when('user enters username "admin" and leaves password empty')
def step_username_only(context):
    context.login_neg_page.enter_username("admin")
    context.login_neg_page.enter_password("")



@when('user leaves username empty and enters password "admin123"')
def step_password_only(context):
    context.login_neg_page.enter_username("")
    context.login_neg_page.enter_password("admin123")



@when('user enters invalid username "wronguser" and password "wrongpass"')
def step_invalid_credentials(context):
    context.login_neg_page.enter_username("wronguser")
    context.login_neg_page.enter_password("wrongpass")


