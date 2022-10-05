from behave import *
import string_utility

@given('a string')
def step_impl(context):
    context.string = "asdf"

@when('the string is reversed')
def step_impl(context):
    context.reversed_string = string_utility.reverse_string(context.string)

@then('the string will be reversed')
def step_impl(context):
    assert (context.reversed_string == "fdsa")



