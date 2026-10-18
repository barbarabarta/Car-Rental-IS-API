# 1. Run and observe

[← README / setup](../README.md) · [Next: a small API →](02-first-api.md)

**Scenario:** Noah wants to view his enrolment in Information Systems. The stored enrolment links student 1002 to course IS101. We first implement this read scenario; creating a new enrolment is a separate action.

Start with `python run.py` in the repository root. Open `/docs` using the [setup instructions](../README.md#start-the-application). Expand a GET operation, choose **Try it out**, enter its parameters and press **Execute**.

| Request | Expected result with the supplied data |
| --- | --- |
| `GET /students` | 200; an array with Alice and Noah |
| `GET /students/1002` | 200; Noah's record |
| `GET /courses/IS101` | 200; the Information Systems offering |
| `GET /enrolments/1002/IS101` | 200; both IDs and grade 4.5 |
| `GET /students/9999` | 404; `{"detail": "Student not found"}` |
| `GET /students/abc` | 422; the path parameter is not an integer |

**Pause and explain:** Which request returns several records? Why does the enrolment request use two identifiers? Does viewing the enrolment change it?

The use case expresses the person's goal. These HTTP requests are implementation steps supporting that goal; a use case is not necessarily one endpoint.

## What is on your screen?

- **Editor:** lets you read and change the source files.
- **Terminal:** runs commands and shows server logs; it must stay running while you try requests.
- **Browser at `/docs`:** Swagger UI, an interactive client for the API.
- **Browser at `/openapi.json`:** the generated OpenAPI description of the interface, not the stored school records.

A Git repository records versions of files. GitHub hosts repositories. A clone is a local copy with history; a fork is your repository copy on GitHub. Codespaces provides a remote development environment with an editor and terminal. These have different roles.

**Try before reading further:** Change the student ID from 1001 to 1002. Predict the result before executing. Use the response and code to check your prediction; an AI explanation alone does not verify behaviour.

Reference: [FastAPI automatic documentation](https://fastapi.tiangolo.com/tutorial/first-steps/).

[← README](../README.md) · [Next: a small API →](02-first-api.md)
