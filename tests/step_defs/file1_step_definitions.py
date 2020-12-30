
from pytest_bdd import given, when, then


@given(u'Step name 1_1 long')
@when(u'Step name 1_1 long')
@then(u'Step name 1_1 long')
def step_impl():
    """
    Description of step1_1
    Example:
        Example of step1_1
    """
    a, b = 0, 1
    # Some code
    pass

