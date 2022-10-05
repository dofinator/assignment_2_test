from behave import *
import string_utility

@given('an uppercased string')
def step_impl(context):
    context.string = "ASDF"

@when('the string is lowercased')
def step_impl(context):
    context.lowercased_string = string_utility.lower_letters(context.string)

@then('the string will return with lowecased letters')
def step_impl(context):
    assert (context.lowercased_string == "asdf")
