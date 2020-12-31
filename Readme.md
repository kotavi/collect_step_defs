The project is in progress


What I get 

```python
{
  "file1_step_definitions": {
    "Step name 1_1 long": "Description of step1_1\nExample:\nExample of step1_1\n"
  },
  "file2_step_definitions": {},
  "p2_steps": {
    "file3_step_definitions": {
      "Step name 1": "Description of step1Example:Example of step1",
      "Step name 2": "Description of step2with several linesExample:Example1 of step2Example2 of step2"
    }
  },
  "b1_steps": {
    "file4_step_definitions": {
      "Step name 1": "Description of step1Example:Example of step1",
      "Step name 2": "Description of step2with several linesExample:Example1 of step2Example2 of step2"
    }
  },
  "b2_steps": {
    "file5_step_definitions": {
      "Step name 1": "Description of step1Example:Example of step1",
      "Step name 2": "Description of step2with several linesExample:Example1 of step2Example2 of step2"
    }
  },
  "c1_steps": {
    "file6_step_definitions": {
      "Step name 6": "Description of step6Example:Example of step6",
      "Step name 6_2": "Description of step6_2with several linesExample:Example1 of step6_@Example2 of step6_2"
    }
  }
}
```

what I want to get
```python
{
  "file1_step_definitions": {
    "Step name 1_1 long": "Description of step1_1\nExample:\nExample of step1_1\n"
  },
  "file2_step_definitions": {
    "Step name 2_1 long": "Description of step2_1\nExample:\nExample of step2_1"
  },
  "p2_steps": {
    "file3_step_definitions": {
      "Step name 1": "Description of step1\nExample:\nExample of step1",
      "Step name 2": "Description of step2\nwith several lines\nExample:\nExample1 of step2\nExample2 of step2"
    }
  },
  "p1_steps": {
    "a1_steps": {
      "b1_steps": {
        "file4_step_definitions": {
          "Step name 1": "Description of step1\nExample:\nExample of step1",
          "Step name 2": "Description of step2\nwith several lines\nExample:\nExample1 of step2\nExample2 of step2"
        }
      },
      "b2_steps": {
        "c1_steps": {
          "file6_step_definitions": {
            "Step name 6": "Description of step6\nExample:\nExample of step6",
            "Step name 6_2": "Description of step6_2with several lines\nExample:\nExample1 of step6_@\nExample2 of step6_2"
          }
        },
        "file5_step_definitions": {
          "Step name 1": "Description of step1\nExample:\nExample of step1",
          "Step name 2": "Description of step2\nwith several lines\nExample:\nExample1 of step2\nExample2 of step2"
        }
      }
    }
  }
}
```