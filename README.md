# BDD Behaviour-driven development

Agile software development process that encourages collaboration among developers, QA and non-technical or business participants in a software project. (Wiki)

[Cucumber BDD with Python 3 Behave and Selenium WebDriver
](
https://www.udemy.com/course/bdd-testing-with-python/)


Tools:

- [Python](https://www.python.org/)
- [Virual env.](https://virtualenv.pypa.io/en/latest/installation.html)
- [pipx](https://github.com/pipxproject/pipx)
- [Behave (clone of Cucumber writen in python)](https://behave.readthedocs.io/en/latest/)
- [Gherkin](https://cucumber.io/docs/gherkin/reference/)
- [Selenium](https://www.selenium.dev/)
- [VS Code](https://code.visualstudio.com/)
- [PyCharm](https://www.jetbrains.com/pycharm/)

Test are writen before kode and Gherkin is scripting language used to write tests that business(Stakeholders, PO, PM, EM) can understand.

One file has one feature and multiple scenarios each with multiple steps.

```gherkin
Feature : Login as valid user

    Scenario: login as an existing user

        Given I'm a user with walid credentials
        When I login with my credentials
        Then I should se the text "Welcome" and my full name
```

BDD frameworks for the python: Behave(maintained and good docs.), Pytest-bdd, Freshen(not maintained) and Lettuce.

## Python

### Virtual env

Way to isolate projects and have specific libs/packages versions for each (not global).

Keep default python clean.

Crates a copy of Python in specific folder and for that env. 

Check installed packages

```pip freeze```

Install virtual env.

```pip install virtualenv```

Create virt. env. 

```bash
# inspect python on system
❯ python -V
Python 2.7.18rc1
❯ python3 -V
Python 3.8.2
❯ which python3
/usr/bin/python3
# cd into project folder create vir. env. using /usr/bin/python3
virtualenv -python=/usr/bin/python3 venv_py3
❯ source venv_py3/bin/activate
❯ python -V
Python 3.8.2
❯ which python
/home/mabazovic/projects/bdd/python-bdd/venv_py3/bin/python
```

## Behave

Install [behave](https://github.com/behave/behave)

```bash
pip install behave
```

Use [gherkin] (https://cucumber.io/docs/gherkin/reference/) syntax to write *.feature file
Under folder steps put python implementations of steps.

```gherkin
Feature:

  Scenario: When I call conversations on webrtc page i hear waiting strategy

    Given I am at conversations page
    When I click call audio button
    Then I hear waiting strategy

```
```python
from behave import given, when, then


@given('I am at conversations page')
def at_conversations_page(context):
    """Arrange: step to position on conversation page"""
    print('At conversations page ')


@when('I click call audio button')
def click_call_audio_button(context):
    """Act: to click button"""
    print('click call buton')


@then('I hear waiting strategy')
def hear_waiting_strategy(context):
    """Assert: Check conditions needed to pass the step as successfully"""
    assert 1 == 1, "one is equal to one :)"

```
 
run all features:
```shell script
behave
```
run specific features:
```shell script
behave demo.feature
```

display print (--no-capture) and logs (--no-logcapture):

```shell script
behave --no-capture --no-logcapture
```

For options more see

```shell
behave --help
```

**Steps names and functions in python file are linked by annotations above function**

Step in feature file:

```gherkin
When I click call audio button
```

Method in py file

```python
@when('I click call audio button')
def click_call_audio_button(context):
    """performing actions that will click the call audio button"""
```

[context](https://behave.readthedocs.io/en/latest/context_attributes.html) is (as always) passed by framework to transfer state and additional data and behaviour (functions).

Beside **Given** **When** and **Then** there are also **And** and **But**.

- Given: Used for preconditions, set up, prepare (Arrange)
- When: Interaction with app, Act on something (Act)
- Then: Verification, Expectation (Assert)
- And & But: represent preceding key word

```gherkin
 Scenario: Agent answers to call

    Given I am at portal at conversations page
    And My status is Available
    And Calling popup window appears
    And I click to answer
    Then Popup windows changes
    And I can hear person on the other side
    And I can hagnup call
```
