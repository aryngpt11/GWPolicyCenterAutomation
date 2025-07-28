Feature: Complete End-to-End Flow in PolicyCenter

  Scenario: Login to application
    Given user is on the login page
    When user enters valid username and password
    Then user should be redirected to the dashboard

  Scenario: Create account for a person
    When user clicks on the "Account" dropdown
    And user selects the "New Account" option
    And user enters the first name and last name
    And user clicks on the "Search" button
    And user selects "Create New Account"
    And user chooses the "Person" account type
    And user fills in all required personal details
    And user clicks the "Update" button
    Then user should be navigated to the Account Summary page
    And user stores the created Account Number

  Scenario: Create a policy for the created account
    When user clicks on the "Policy" dropdown
    And user selects the "New Submission" option
    And user enters the stored Account Number
    And user clicks on the "Account Search" button
    And user clicks on "Installed Products"
    And user selects the "PersonalAuto" policy
    And user chooses a plan from the Offerings dropdown
    And user clicks "Next" to proceed
    And user enters the "Date Quote Needed"
    And user adds an existing driver from the Add dropdown
    And user enters license number and selects license state
    And user opens the Roles tab and fills Year First Licensed
    And user checks the agreement checkbox
    And user creates a new vehicle
    And user enters basic vehicle information
    And user clicks the "Quote" button
    And user clicks on Bind Options dropdown and selects "Issue Policy"
    And user accepts the confirmation alert
    Then user should be navigated to the Submission Bound page
