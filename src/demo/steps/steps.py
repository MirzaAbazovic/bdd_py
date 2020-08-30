from behave import given, when, then
import logging as log

@given('I am at conversations page')
def at_conversations_page(context):
    """Arrange: step to position on conversation page"""
    print('At conversations page ')
    log.info('login and go to page')


@when('I click call audio button')
def click_call_audio_button(context):
    """Act: to click button"""
    print('click call button')
    log.info('click call button on page')


@then('I hear waiting strategy')
def hear_waiting_strategy(context):
    """Assert: Check conditions needed to pass the step as successfully"""
    print('asserting values')
    log.info('Direct assertion: Check stuff that you can get handle in code (this process)')
    log.info('Indirect assertion: Check some logs or query other system to determine is all OK')
    error_log = ''
    assert error_log == '', 'there are no errors'
    assert 1 == 1, "one is equal to one :)"
