
from pytest_bdd import given, when, then


@given(u'Step name 6')
@when(u'Step name 6')
@then(u'Step name 6')
def step_impl():
    """
    Description of step6
    Example:
        Example of step6
    """
    a, b = 0, 1
    # Some code
    pass


@given(u'Step name 6_2')
@when(u'Step name 6_2')
@then(u'Step name 6_2')
def step_impl():
    """
    Description of step6_2
    with several lines
    Example:
        Example1 of step6_@
        Example2 of step6_2
    """
    a, b = 0, 1
    # Some code
    pass
