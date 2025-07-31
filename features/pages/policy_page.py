import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class PolicyPage:
    def __init__(self, context):
        self.driver = context.driver
        self.wait = context.wait

    def open_policy_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, "div[id='TabBar-PolicyTab'] div[class='gw-icon gw-icon--expand']").click()

    def new_submission(self):
        self.driver.find_element(By.CSS_SELECTOR, "div[id='TabBar-PolicyTab-PolicyTab_NewSubmission']  div[class='gw-label']").click()

    def enter_account_number(self, account_number):
        self.driver.find_element(By.CSS_SELECTOR, "div[id='NewSubmission-NewSubmissionScreen-SelectAccountAndProducerDV-Account'] input[type='text']").send_keys(account_number)

    def search_account(self):
        self.driver.find_element(By.CSS_SELECTOR,"div[id='NewSubmission-NewSubmissionScreen-SelectAccountAndProducerDV-Account-SelectAccount']").click()

    def click_installed_products(self):
        self.driver.find_element(By.CSS_SELECTOR, "div[id='NewSubmission-NewSubmissionScreen-InstalledTab'] div[class='gw-label']").click()

    def select_policy(self):
        products = self.driver.find_elements(By.CSS_SELECTOR,"tbody tr[class='gw-RowWidget gw-styleTag--ListViewWidget gw-row gw-standard-row gw-isAlternateStyle']")
        for product in products:
            text = product.find_element(By.CSS_SELECTOR,"tr[class='gw-RowWidget gw-styleTag--ListViewWidget gw-row gw-standard-row gw-isAlternateStyle'] td:nth-child(2)").text
            if text == "Personal Auto":
                product.find_element(By.CSS_SELECTOR,"tr[class='gw-RowWidget gw-styleTag--ListViewWidget gw-row gw-standard-row gw-isAlternateStyle'] td[class='gw-LinkCellWidget gw-styleTag--ListViewWidget gw-align-h--center gw-align-v--middle gw-first-cell'] div[class='gw-LinkWidget gw-styleTag--LinkCellWidget gw-mini-button gw-actionable']").click()
                break

    def select_plan(self):
        offerings=Select(self.driver.find_element(By.NAME,"SubmissionWizard-OfferingScreen-OfferingSelection"))
        offerings.select_by_value("Premium Program")

    def click_next(self):
        self.driver.find_element(By.CSS_SELECTOR, "div[id='SubmissionWizard-Next'] div[class='gw-action--inner gw-hasDivider']").click()

    def enter_date_quote_needed(self):
        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-Next'] div[class='gw-action--inner gw-hasDivider']").click()
        today = datetime.today().strftime("%m/%d/%Y")
        date_input = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='SubmissionWizard-LOBWizardStepGroup-SubmissionWizard_PolicyInfoScreen-SubmissionWizard_PolicyInfoDV-DateQuoteNeeded']")))
        date_input.send_keys(today)
        self.driver.find_element(By.CSS_SELECTOR, "div[id='SubmissionWizard-Next'] div[class='gw-action--inner gw-hasDivider']").click()



    def add_existing_driver(self):
        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriversLV_tb-AddDriver'] div[aria-label='Add']").click()
        element = self.wait.until(EC.presence_of_element_located((By.ID,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriversLV_tb-AddDriver-AddExistingContact")))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriversLV_tb-AddDriver-AddExistingContact-0-UnassignedDriver'] div[class='gw-action--inner gw-hasDivider']").click()
        time.sleep(5)



    def enter_license_details(self):
        self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriverDetailsCV-PolicyContactDetailsDV-PolicyContactRoleNameInputSet-DateOfBirth").send_keys("01/01/1990")
        self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriverDetailsCV-PolicyContactDetailsDV-LicenseInputSet-LicenseNumber").send_keys("1234567890")
        LisState=Select(self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriverDetailsCV-PolicyContactDetailsDV-LicenseInputSet-LicenseState"))
        LisState.select_by_value("HI")

    def fill_roles_info(self):
        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriverDetailsCV-RolesCardTab'] div[class='gw-action--inner gw-hasDivider']").click()
        self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriverDetailsCV-1-PolicyContactRolePanelSet-PolicyDriverInfoDV-yearlicensed").send_keys("2018")
        NOAccidentPL=Select(self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriverDetailsCV-1-PolicyContactRolePanelSet-PolicyDriverNumberOfAccidents"))
        NOAccidentPL.select_by_value("0")

        NOAccidentAL=Select(self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriverDetailsCV-1-PolicyContactRolePanelSet-DriverNumberOfAccidents"))
        NOAccidentAL.select_by_value("0")

        NOVoilationsAL=Select(self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriverDetailsCV-1-PolicyContactRolePanelSet-PolicyDriverNumberOfViolations"))
        NOVoilationsAL.select_by_value("0")

        NOVoilationsPL=Select(self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriverDetailsCV-1-PolicyContactRolePanelSet-DriverNumberOfViolations"))
        NOVoilationsPL.select_by_value("0")

    def agree_checkbox(self):
        self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PADriversScreen-PADriversPanelSet-DriversListDetailPanel-DriversLV-0-_Checkbox").click()
        self.driver.find_element(By.CSS_SELECTOR, "div[id='SubmissionWizard-Next'] div[class='gw-action--inner gw-hasDivider']").click()


    def create_vehicle(self):
        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PAVehiclesScreen-PAVehiclesPanelSet-VehiclesListDetailPanel_tb-Add'] div[class='gw-action--inner gw-hasDivider']").click()


    def enter_vehicle_info(self):
        self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PAVehiclesScreen-PAVehiclesPanelSet-VehiclesListDetailPanel-VehiclesDetailsCV-PersonalAuto_VehicleDV-Vin_DV").send_keys("123456789")
        self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PAVehiclesScreen-PAVehiclesPanelSet-VehiclesListDetailPanel-VehiclesDetailsCV-PersonalAuto_VehicleDV-CostNew_DV").send_keys("173")
        LS=Select(self.driver.find_element(By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PAVehiclesScreen-PAVehiclesPanelSet-VehiclesListDetailPanel-VehiclesDetailsCV-PersonalAuto_VehicleDV-LicenseState_DV"))
        LS.select_by_value("HI")
        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PAVehiclesScreen-PAVehiclesPanelSet-VehiclesListDetailPanel-VehiclesDetailsCV-PersonalAuto_VehicleDV-PersonalAuto_AssignDriversInputSet-DriverPctLV_tb-AddDriver'] div[class='gw-action--inner']").click()
        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PAVehiclesScreen-PAVehiclesPanelSet-VehiclesListDetailPanel-VehiclesDetailsCV-PersonalAuto_VehicleDV-PersonalAuto_AssignDriversInputSet-DriverPctLV_tb-AddDriver-0-Driver']  div[class='gw-action--inner gw-hasDivider']").click()
        self.wait.until(EC.element_to_be_clickable((By.NAME,"SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PAVehiclesScreen-PAVehiclesPanelSet-VehiclesListDetailPanel-VehiclesDetailsCV-PersonalAuto_VehicleDV-PersonalAuto_AssignDriversInputSet-DriverPctLV-0-_Checkbox"))).click()
        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PAVehiclesScreen-PAVehiclesPanelSet-VehiclesListDetailPanel-VehiclesLV-0-_Checkbox'] input[type='checkbox']").click()
        self.driver.find_element(By.CSS_SELECTOR, "div[id='SubmissionWizard-Next'] div[class='gw-action--inner gw-hasDivider']").click()



    def click_quote(self):
        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-LOBWizardStepGroup-LineWizardStepSet-PersonalAutoScreen-JobWizardToolbarButtonSet-QuoteTypeToolbarButtonSet-Quote'] div[class='gw-action--inner gw-hasDivider']").click()


    def select_issue_policy(self):
        self.driver.find_element(By.CSS_SELECTOR,"div[id='SubmissionWizard-SubmissionWizard_QuoteScreen-JobWizardToolbarButtonSet-BindOptions'] div[class='gw-action--inner']").click()
        self.driver.find_element(By.CSS_SELECTOR,"div[aria-label='Issue Policy'] div[class='gw-label']").click()

    def accept_alert(self):
        self.driver.switch_to.alert.accept()


    def is_submission_bound(self):
        self.driver.switch_to.default_content()
        element = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[id='JobComplete-JobCompleteScreen-ttlBar'] div[class='gw-TitleBar--title']")))
        return "Submission Bound" in element.text
