
from pytest_bdd import given, when, then, parsers


@given(parsers.cfparse(
    'Step name 2_1 long'))
@then(parsers.cfparse(
    'Step name 2_1 long'))
@when(parsers.cfparse(
    'Step name 2_1 long'))
def step_impl():
    """
    Description of step2_1
    Example:
        Example of step2_1
    """
    a, b = 0, 1
    # Some code
    pass

