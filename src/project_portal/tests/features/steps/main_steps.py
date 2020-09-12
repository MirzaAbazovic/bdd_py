from behave import given, then, step
from steps import steps_common

@given("Given I go to the site {site}")
def go_to_site(context, site):
    steps_common.go_to_url(context, site)


@then("Then page should have element with id {username}")
def page_have_element_with_id(context, username):
    steps_common.page_has_element_with_id(context, username)


@step("And page should have element with id {username}")
def page_have_element_with_id(context, username):
    steps_common.page_has_element_with_id(context, username)
