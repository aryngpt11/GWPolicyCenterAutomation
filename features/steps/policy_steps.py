from behave import when, then
from features.pages.policy_page import PolicyPage

@when('user clicks on the "Policy" dropdown')
def policyMenu(context):
    PolicyPage(context).open_policy_menu()

@when('user selects the "New Submission" option')
def newPolicySubmission(context):
    PolicyPage(context).new_submission()

@when("user enters the stored Account Number")
def accNum(context):
    account_no = context.config.userdata.get('account_number')
    print("🧾 Using stored account number:", account_no)
    PolicyPage(context).enter_account_number(account_no)

@when('user clicks on the "Account Search" button')
def searchBtn(context):
    PolicyPage(context).search_account()

@when('user clicks on "Installed Products"')
def installedProd(context):
    PolicyPage(context).click_installed_products()

@when('user selects the "PersonalAuto" policy')
def selPolicy(context):
    PolicyPage(context).select_policy()

@when('user chooses a plan from the Offerings dropdown')
def Offerings(context):
    PolicyPage(context).select_plan()

@when('user clicks "Next" to proceed')
def NextBtn(context):
    PolicyPage(context).click_next()

@when('user enters the "Date Quote Needed"')
def quoteDate(context):
    PolicyPage(context).enter_date_quote_needed()

@when('user adds an existing driver from the Add dropdown')
def addDriver(context):
    PolicyPage(context).add_existing_driver()

@when('user enters license number and selects license state')
def licenseDetails(context):
    PolicyPage(context).enter_license_details()

@when('user opens the Roles tab and fills Year First Licensed')
def roleData(context):
    PolicyPage(context).fill_roles_info()

@when('user checks the agreement checkbox')
def agreeChkBox(context):
    PolicyPage(context).agree_checkbox()

@when('user creates a new vehicle')
def createVehicle(context):
    PolicyPage(context).create_vehicle()

@when('user enters basic vehicle information')
def vehicleDetails(context):
    PolicyPage(context).enter_vehicle_info()

@when('user clicks the "Quote" button')
def clickQuote(context):
    PolicyPage(context).click_quote()

@when('user clicks on Bind Options dropdown and selects "Issue Policy"')
def issuePolicy(context):
    PolicyPage(context).select_issue_policy()

@when('user accepts the confirmation alert')
def acceptAlert(context):
    PolicyPage(context).accept_alert()

@then('user should be navigated to the Submission Bound page')
def VerifyingDashboard(context):
    assert PolicyPage(context).is_submission_bound()
