## Collect pytest-bdd step definitions with description

1. Collect all the filenames with \*collect_step_definition_files*.py from the specified path (line #13)
2. Goes through every file and creates a tree with all the step definitions based on their location in the path
3. Fills in the dictionary with the description
4. Result is stored in data.json and in StepDefinitions.xlsx

### Step definition rules
* Must be on one line
```python
@when(parsers.cfparse('Step name 2_1 long'))
``` 
* Description has to be in triple quotes
```python
def step_impl():
    """
    Description of step2_1
    Example:
        Example of step2_1
    """
```