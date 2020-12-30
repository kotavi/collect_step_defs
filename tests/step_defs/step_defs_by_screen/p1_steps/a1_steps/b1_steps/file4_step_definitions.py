
from pytest_bdd import given, when, then


@given(u'Step name 1')
@when(u'Step name 1')
@then(u'Step name 1')
def step_impl():
    """
    Description of step1
    Example:
        Example of step1
    """
    a, b = 0, 1
    # Some code
    pass


@given(u'Step name 2')
@when(u'Step name 2')
@then(u'Step name 2')
def step_impl():
    """
    Description of step2
    with several lines
    Example:
        Example1 of step2
        Example2 of step2
    """
    a, b = 0, 1
    # Some code
    pass
