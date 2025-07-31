Feature: Login - Negative Scenarios

  Scenario: Login with empty username and password
    Given user on the login page
    When user leaves the username and password fields empty
    And user clicks on the login button
    Then an error message should be displayed

  Scenario: Login with only username filled
    Given user on the login page
    When user enters username "admin" and leaves password empty
    And user clicks on the login button
    Then an error message should be displayed

  Scenario: Login with only password filled
    Given user on the login page
    When user leaves username empty and enters password "admin123"
    And user clicks on the login button
    Then an error message should be displayed

  Scenario: Login with invalid username and password
    Given user on the login page
    When user enters invalid username "wronguser" and password "wrongpass"
    And user clicks on the login button
    Then an error message should be displayed