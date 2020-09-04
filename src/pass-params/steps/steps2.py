from behave import given, when, step, then


@given("I'm in a call")
def i_am_in_a_call(context):
    print("I'm in a call with client ")


@when("I click transfer")
def step_impl(context):
    print('I click transfer')


@step("I see non empty list of agent online")
def step_impl(context):
    if ('agent_list') in context:
        assert False, 'variable agent_clist already exists'
    context.agent_list = ["Merry", "Joly", "Ben", "Tim"]
    print("Agents: {}".format(context.agent_list))


@step("When I select one agent from list")
def step_impl(context):
    if ('agent_list' not in context or len(context.agent_list) == 0):
        assert False, 'There is no agent list or is empty'
    context.selected_agent = context.agent_list[0]
    print('selected first agent from list: {}'.format(context.agent_list[0]))


@then("Caller is put on hold")
def step_impl(context):
    print("caller is on hold")


@step("Phone is ringing to selected agent")
def step_impl(context):
    print("Phone is ringing to {}".format(context.selected_agent))
    assert 'Merry' == context.selected_agent
