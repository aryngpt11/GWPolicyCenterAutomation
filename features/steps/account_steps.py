from behave import when, then


from features.pages.account_page import AccountPage

@when('user clicks on the "Account" dropdown')
def AccountDD(context):
    AccountPage(context).open_account_menu()

@when('user selects the "New Account" option')
def NewAcc(context):
    AccountPage(context).select_new_account()

@when('user enters the first name and last name')
def EnterData(context):
    context.account_page=AccountPage(context)
    context.account_page.enter_name()

@when('user clicks on the "Search" button')
def SearchButton(context):
    AccountPage(context).click_search()

@when('user selects "Create New Account"')
def CreateAcc(context):
    AccountPage(context).click_create_new_account()

@when('user chooses the "Person" account type')
def RoleOfAccn(context):
    AccountPage(context).select_person_option()

@when('user fills in all required personal details')
def UserDetails(context):
    AccountPage(context).fill_personal_details()

@when('user clicks the "Update" button')
def Updatee(context):
    AccountPage(context).click_update()

@then('user should be navigated to the Account Summary page')
def SummaryPage(context):
    assert AccountPage(context).is_on_summary_page()

@then("user stores the created Account Number")
def GetAccNo(context):
    accnt_no= AccountPage(context).get_account_number()
    context.account_number = accnt_no
    context.config.userdata['account_number'] =accnt_no
