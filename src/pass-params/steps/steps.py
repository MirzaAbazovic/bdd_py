import time

from behave import given, when, then


# Steps for scenario: Disable login while having call

@given('user is on page: {page}')
def at_the_page(context, page):
    print('drive user to the page: {}'.format(page))


@given('there is popup with text: {text}')
def i_have_popup(context, text):
    print('popup with text: {}'.format(text))


@when('user clicks on button: {button_name}')
def user_click_on(context, button_name):
    print('user clicked on {} '.format(button_name))


@then('user should see {message}')
def user_should_see(context, message):
    print('Assert there is text: {} on page'.format(message))
    assert 'Error' == message


# Steps for scenario: Call number

@given("I call number {number}")
def step_impl(context, number):
    print("Calling number {}...".format(number))


@given("I wait for {number_sec} seconds")
def step_impl(context, number_sec):
    print('Waiting for {} seconds'.format(number_sec))
    time.sleep(int(number_sec))


@given("I dial number {dialed_number}")
def step_impl(context, dialed_number):
    print('I dialed {}'.format(dialed_number))
    assert 0 <= int(dialed_number) < 10


@then("I should find '{log_text}' in log query '{log_query}'")
def step_impl(context, log_text, log_query):
    print('Check does query of log: "{}" contains "{}"?'.format(log_query, log_text))


@then("I should hear file {audio_file}")
def step_impl(context, audio_file):
    print("Check did you hear file {}".format(audio_file))
    assert 'you_dialed_3.wav' == audio_file


@given('I start a call with {participants_count} participants')
def step_impl(context, participants_count):
    print('create call with {} participants'.format(participants_count))

@when("I add {new_participants_count} more participants")
def step_impl(context, new_participants_count):
    print('Add {} participants to call'.format(new_participants_count))

@then("I have {participants_count} participants in call")
def step_impl(context, participants_count):
    print('Now i have {} participants in call'.format(participants_count))
    assert 12 == int(participants_count)


