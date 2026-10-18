# 3. Trace a request through the application

[← A small API](02-first-api.md) · [Next: UML, objects and JSON →](04-models-and-objects.md)

Open `main.py` at `get_student`. Follow **GET /students/1002**:

```text
Browser / Swagger UI
    | GET /students/1002
    v
FastAPI: match the route and parse student_id as int
    v
get_student(1002): load records and find the matching student
    v
load_records("students.json") -> data/students.json
    | list of Python dictionaries
    v
handler returns {"student_id": 1002, "name": "Noah"}
    v
FastAPI sends HTTP 200 with a JSON response -> browser
```

This is **input → processing → output**: input 1002, processing load/search, output the matching record or a not-found response. File access is one part of the processing.

## Read the important lines

```python
students = load_records("students.json")
for student in students:
    if student["student_id"] == student_id:
        return student
raise HTTPException(status_code=404, detail="Student not found")
```

`students` is a list. Each `student` is a dictionary. `student["student_id"]` reads one value; `==` compares it with the requested ID. `return` ends the function as soon as a match is found. The `raise` line is **after the loop**, so a later record such as Noah can still match. Moving it inside the loop could incorrectly reject Noah after checking Alice.

422 means FastAPI could not accept the URL value as an integer. 404 means the integer was acceptable but our search found no record. Reading JSON does not automatically check uniqueness, references or permissions.

## Load, save and initial data

In `storage.py`, `json.load(file)` converts file text into Python lists/dictionaries. `json.dump(records, file)` writes Python data as JSON text. Returning a dictionary from an HTTP handler does **not** save it to disk.

The three `data/*.json` files already contain the initial teaching data. There is no hidden first-run seeding or automatic reset. `save_records` replaces the entire selected file; the optional registration demo loads the list and appends before saving. Save a copy before experimenting; restore that copy if you want to repeat a write exercise.

`DATA_DIR` is anchored to `storage.py`, not the terminal's working folder. The filenames passed to the helper are fixed by our code. A missing or malformed file is an error; inspect the terminal and repair the file.

## Responsibilities and deployment

| Responsibility | Where to find it here |
| --- | --- |
| Present a request and response | Browser / Swagger UI |
| Receive HTTP input and select an operation | FastAPI route and handler in `main.py` |
| Apply a decision | Lookup in the handler; duplicate/reference checks in the optional registration demo |
| Read or write stored records | Functions in `storage.py` |

These are **logical responsibilities**. This small demo keeps lookup logic in the handler for readability. It does not implement a separate service class or database server. The API and JSON files share the same runtime machine/container; a JSON file is not automatically a separate deployment tier.

**Your turn:** Trace `GET /enrolments/1001/IS101`. Locate both comparisons. Open the linked Student and Course records and explain how the identifiers implement the relationships from UML. Then try the initially absent pair `1002/DB101`.

References: [FastAPI errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) and [Python JSON conversion](https://docs.python.org/3.14/library/json.html).

[← A small API](02-first-api.md) · [Next: UML, objects and JSON →](04-models-and-objects.md)
