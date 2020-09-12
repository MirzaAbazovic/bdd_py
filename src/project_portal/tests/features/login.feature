# Created by mabazovic at 6.9.20.
Feature: Verify home page url has elements for login
  Check is there username and password text input on main page

  Scenario: Login page should have fields to enter credentials

    Given I go to the site https://portal.infobip.com/
    Then page should have element with id username
    And page should have element with id password