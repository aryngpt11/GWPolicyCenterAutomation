import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class AccountPage:
    def __init__(self, context):
        self.driver = context.driver
        self.wait = context.wait

    def open_account_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, "div[id='TabBar-AccountTab'] div[class='gw-action--expand-button']").click()

    def select_new_account(self):
        self.driver.find_element(By.XPATH, "//div[@id='TabBar-AccountTab-AccountTab_NewAccount']//div[@class='gw-label'][normalize-space()='New Account']").click()

    def enter_name(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='NewAccount-NewAccountScreen-NewAccountSearchDV-GlobalPersonNameInputSet-FirstName']").send_keys("Aryan")
        self.driver.find_element(By.XPATH, "//input[@name='NewAccount-NewAccountScreen-NewAccountSearchDV-GlobalPersonNameInputSet-LastName']").send_keys("Gupta")

    def click_search(self):
        self.driver.find_element(By.ID, "NewAccount-NewAccountScreen-NewAccountSearchDV-SearchAndResetInputSet-SearchLinksInputSet-Search").click()

    def click_create_new_account(self):
        self.driver.find_element(By.CSS_SELECTOR, "div[id='NewAccount-NewAccountScreen-NewAccountButton'] div[role='button']").click()
        time.sleep(5)

    def select_person_option(self):


        person_option = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div[aria-label='Person'] div[class='gw-label']")))
        person_option.click()


    def fill_personal_details(self):
        address_input = self.driver.find_element(By.CSS_SELECTOR,"div[class='gw-vw--value'] input[name='CreateAccount-CreateAccountScreen-CreateAccountDV-AddressInputSet-globalAddressContainer-GlobalAddressInputSet-AddressLine1']")
        address_input.send_keys("123 Main Street")
        StateValue = Select(self.driver.find_element(By.CSS_SELECTOR,"select[name='CreateAccount-CreateAccountScreen-CreateAccountDV-AddressInputSet-globalAddressContainer-GlobalAddressInputSet-State']"))
        StateValue.select_by_value("HI")
        AddressType = Select(self.driver.find_element(By.NAME, "CreateAccount-CreateAccountScreen-CreateAccountDV-AddressType"))
        AddressType.select_by_value("home")
        SSN_input = self.driver.find_element(By.CSS_SELECTOR,"div[class='gw-vw--value'] input[name='CreateAccount-CreateAccountScreen-CreateAccountDV-OfficialIDInputSet-OfficialIDDV_Input']")
        SSN_input.send_keys("123-45-6789")

        Organization_input = self.driver.find_element(By.ID,"CreateAccount-CreateAccountScreen-CreateAccountDV-ProducerSelectionInputSet-Producer-SelectOrganization")
        Organization_input.click()
        Org_name = self.driver.find_element(By.CSS_SELECTOR,"div[class='gw-vw--value'] input[name='OrganizationSearchPopup-OrganizationSearchPopupScreen-OrganizationSearchDV-GlobalContactNameInputSet-Name']")
        Org_name.send_keys("a")
        Search_button = self.driver.find_element(By.ID,"OrganizationSearchPopup-OrganizationSearchPopupScreen-OrganizationSearchDV-SearchAndResetInputSet-SearchLinksInputSet-Search")
        Search_button.click()

        producers = self.driver.find_elements(By.CSS_SELECTOR,"div[class='gw-ListView--table-wrapper'] tr[class='gw-RowWidget gw-styleTag--ListViewWidget gw-row gw-standard-row gw-isAlternateStyle']")

        for producer in producers:
            text = producer.find_element(By.CSS_SELECTOR,"div[class='gw-ListView--table-wrapper'] tr[class='gw-RowWidget gw-styleTag--ListViewWidget gw-row gw-standard-row gw-isAlternateStyle'] td:nth-child(2)").text
            if text == "ACV Property Insurance":
                producer.find_element(By.CSS_SELECTOR,"div[class='gw-SelectorCellValueWidget gw-styleTag--CellWidget gw-putSubMenusBelow gw-isTopLevelMenu gw-hasMinimizedView gw-action--outer'] div[role='button'] ").click()
                break

    def click_update(self):
        self.driver.find_element(By.CSS_SELECTOR, "#CreateAccount-CreateAccountScreen-Update").click()

    def is_on_summary_page(self):
        PageText = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"div[class='gw-TitleBar--titles--container'] div[role='heading']")))
        return PageText.is_displayed()

    def get_account_number(self):
        account_no = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='AccountFile_Summary-AccountSummaryDashboard-AccountDetailsDetailViewTile-AccountDetailsDetailViewTile_DV-AccountNumber'] div[class='gw-vw--value gw-align-h--left'] div[class='gw-value-readonly-wrapper']"))).text
        print("Account number",account_no)
        return account_no

