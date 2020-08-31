# Passing parameters to steps

This is very straight-forward
If you have in feature file step like this
```gherkin
Then I have 10 messages on page https://portal.com/messages
```
Then in step you can use {} to mark words or numbers that you pass as parameters to python method
```python
@then('I have {message_number} new messages on page {page}')
def i_have_messages(context, messages_number, page):
    """
    Step to confirm that there are new messages on message page
    :param context: 
    :param messages_number: Number of new messages 
    :param page: Messaging page url 
    :return: 
    """
    print("I have {}  messages on page {}".format(messages_number,page))
    assert int(messages_number) > 0
```
All passed values are strings

Tip: 

**Instead of using @given, @when, @then you can use generic @step.  
The step decorator matches the step to any step type, “given”, “when” or “then”.**


Examples:

- [features](src/pass-params/test_case1.feature)
- [steps](src/pass-params/steps/steps.py)




