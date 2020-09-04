Feature: Demonstrate passing parameters between steps
  Use context as "variable holder" between steps

  Scenario: Transfer call to another agent
    Given I'm in a call
    When I click transfer
    And I see non empty list of agent online
    And When I select one agent from list
    Then Caller is put on hold
    And Phone is ringing to selected agent
