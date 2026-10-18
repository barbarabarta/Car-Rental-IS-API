# 2. A small FastAPI example

[← Run and observe](01-run-and-observe.md) · [Next: trace a request →](03-trace-a-request.md)

Stop the school app with **Ctrl+C**. From the same root folder run:

```sh
python run.py tutorial
```

Use port **8000** again and open `/docs`. We run one example at a time; this is the smaller app in `tutorial.py`.

```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/students/{student_id}")
def show_input(student_id: int):
    return {"requested_student_id": student_id}
```

1. `import` makes the framework's `FastAPI` class available.
2. `FastAPI()` creates an application object.
3. The **decorator** `@app.get(...)` registers the function for a GET path.
4. The **path parameter** `{student_id}` is supplied to the Python parameter with the same name.
5. `int` is a type hint. FastAPI uses it here to parse and validate the incoming value.
6. The **handler** (or path operation function) returns a dictionary. FastAPI produces the HTTP JSON response.

The framework calls the handler when a matching request arrives. You do not call `show_input()` from the browser. Uvicorn runs the application and handles the server connection; FastAPI defines the routes and request/response behaviour.

**Predict, try, explain:** Request student 9999. It returns 200 here because this small tutorial only echoes the input. It has no student file and performs no existence check. Compare this with the school app's 404. Request `abc` and observe FastAPI's type-validation response.

Change the welcome message in `tutorial.py`, save, then refresh `/`. The development server reloads Python changes. Changes to JSON data are read by the school app on each request.

Stop the tutorial with **Ctrl+C**, then restore the full example:

```sh
python run.py
```

Adapted from [FastAPI First Steps](https://fastapi.tiangolo.com/tutorial/first-steps/) and [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/). Our tutorial uses school names and a synchronous `def`; it does not introduce asynchronous programming.

[← Run and observe](01-run-and-observe.md) · [Next: trace a request →](03-trace-a-request.md)
