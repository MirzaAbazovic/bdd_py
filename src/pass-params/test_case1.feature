Feature: Demonstrate passing params to steps

  Scenario: Disable login while having call

    Given user is on page: https://portal.com/conversations
    And there is popup with text: calling...
    When user clicks on button: Log out
    Then user should see Error


  Scenario: Call number

    Given I call number 387611232334
    And I wait for 2 seconds
    And I dial number 9
    Then I should find 'From: sip:387611232334@10.10.10.11' in log query 'some_query_of_log_to_find_from_387611232334'
    And I should hear file you_dialed_3.wav

  Scenario: Add 2 more participants in the call

    Given I start a call with 10 participants
    When I add 2 more participants
    Then I have 12 participants in call