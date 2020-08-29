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

