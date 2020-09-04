# Passing parameters to steps

This is very straight-forward

If You have in feature file step like this
```gherkin
Then I have 10 messages on page https://portal.com/messages
```
Then in step You can use {} to mark words or numbers that You pass as parameters to python method
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

**Instead of using @given, @when, @then You can use generic @step.  
The step decorator matches the step to any step type, “given”, “when” or “then”.**


Examples:

- [features](src/pass-params/test_case1.feature)
- [steps](src/pass-params/steps/steps.py)

# Passing parameters between steps

For passing parameters between steps use context that is passed as first parameter in every step.
Context is shared in one scenario not between them, You can use it to share state between steps from one scenario. 

Tip: Check is variable already set/used (in order to do not override it)

'my_shared_var' in context 

Examples:

- [features](src/pass-params/test_case2.feature)
- [steps](src/pass-params/steps/steps2.py)



