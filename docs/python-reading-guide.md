# Python refresher alongside the API

[← README](../README.md) · [Trace the actual handler →](03-trace-a-request.md)

Read only the parts needed for the file you are inspecting. Try tiny expressions in the Python terminal if helpful; stop it with `exit()` before entering shell commands such as `python run.py`.

## Variables, values and collections

```python
student_id = 1002                    # int: a whole number
name = "Noah"                       # str: text
grade = None                        # no grade yet
student = {"student_id": 1002, "name": "Noah"}  # dict
students = [student]                # list containing one dictionary
print(student["name"])             # Noah
print(students[0]["student_id"])    # 1002: lists start at index 0
```

`=` assigns a value; `==` compares two values. A missing dictionary key raises `KeyError`. JSON looks similar but uses `null`, `true`, `false` and quoted member names; Python uses `None`, `True`, `False`. `json.load` converts between their representations.

## Functions and indentation

```python
def describe(student):
    return student["name"]

name = describe({"student_id": 1002, "name": "Noah"})
```

`def` defines a function. `student` is a parameter; the dictionary in the call is an argument. The indented lines form the function body. A colon starts this block. `return` sends a result to the caller and ends the call; `print` displays text in a terminal. Printing alone is not an API response.

## Loops and conditions

```python
for student in students:
    if student["student_id"] == 1002:
        print(student["name"])
```

The loop takes each list item in turn. The condition is checked for that item. `and` requires both conditions to be true, as in the enrolment lookup. In the API, the 404 exception belongs after the entire loop, not after checking only the first item.

## Imports, files and exceptions

`from storage import load_records` imports our function from `storage.py`. `from fastapi import FastAPI` imports an installed package. `import json` uses Python's standard library.

```python
with path.open(encoding="utf-8") as file:
    records = json.load(file)
```

`with` closes the file when the block ends, including if an error occurs. `encoding` is a named argument. The default file mode reads; `"w"` writes and replaces existing contents. See `save_records` before using it.

`raise` stops normal execution and signals an exception. FastAPI handles our `HTTPException` as an HTTP error response. The optional command-line registration demo catches `ValueError` with `try` / `except` and prints the explanation. Arbitrarily swallowing errors would hide the problem.

## Type hints and decorators

```python
@app.get("/students/{student_id}")
def get_student(student_id: int):
    ...
```

The decorator registers a route. `: int` annotates a parameter. Python itself does not universally enforce type hints; FastAPI reads this annotation and uses it for URL validation. `float | None` allows a number or no value in the documented type. This is different from a quoted JSON string such as `"1002"`.

## Objects and methods

```python
student = Student(1002, "Noah")
enrolment = student.enrol(course)
```

Calling a class constructs an instance. Its `__init__` method initialises attributes such as `self.name`. `self` refers to the instance receiving the method call; Python supplies it when you write `student.enrol(course)`. A method can return a different object, as this one returns an Enrolment. An object's attributes are accessed with dots; dictionary entries are accessed using square brackets.

## Looking up a known example

```python
row = next(item for item in records if item["student_id"] == 1002)
```

Read this as "take the first item whose student ID is 1002". The expression inside `next` supplies matching items one at a time. Without a match it raises `StopIteration`. `objects_demo.py` uses it for fixed teaching records; the API and registration example handle missing records explicitly.

## Running a file

`if __name__ == "__main__":` runs the following block when the file is started directly, rather than imported. This keeps importing our classes/helpers from unexpectedly executing the demo.

`python run.py` is a terminal command. Do not copy `$`, `PS ...>`, a comment such as `Run:`, or the Markdown backticks with it. Installing with `python -m pip` uses pip associated with that Python interpreter.

Further reading: [Python control flow and functions](https://docs.python.org/3.14/tutorial/controlflow.html), [data structures](https://docs.python.org/3.14/tutorial/datastructures.html), [classes](https://docs.python.org/3.14/tutorial/classes.html), [JSON](https://docs.python.org/3.14/library/json.html).

[← README](../README.md) · [Trace the actual handler →](03-trace-a-request.md)
