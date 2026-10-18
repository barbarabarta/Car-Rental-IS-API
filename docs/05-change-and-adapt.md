# 5. Change, check and adapt

[← UML, objects and JSON](04-models-and-objects.md) · [Return to README →](../README.md)

## First make a small visible change

1. Predict the response from `GET /students/1002`.
2. Change Noah's name to `Noah Keller` in `data/students.json` and save.
3. Execute the same request again. The new response should contain the changed name.
4. Restore `Noah`. Explain why changing the name does not break the enrolment link, whereas changing the ID without updating enrolments would.

Keep the JSON valid: quoted property names, commas between records, no trailing comma. Use the [Python guide](python-reading-guide.md) to compare JSON and Python syntax.

## Optional: complete the registration scenario

This is a worked extension connecting the UML operation to persistent state. It is not a new assignment requirement or a POST endpoint.

Save a copy of `data/enrolments.json` before starting. Initially, `GET /enrolments/1002/DB101` returns 404. In another terminal run:

```sh
python registration_demo.py
```

Open `registration_demo.py` and follow the three numbered blocks: resolve Student/Course → reject a duplicate → call `student.enrol(course)` and save the new record. Repeat the GET: it now returns 200 with grade `null`. Run the demo again: it reports **No change: Student is already enrolled in this course**. The file should contain the pair once.

Restore your saved JSON copy to repeat from the beginning. This example is for a single writer. A database/transaction or a different persistence design is needed to make the same check reliable with simultaneous writers. Login and permissions are not implemented.

## Apply the read pattern to your own IS

Select a small information need from your existing project scenario, UML classes and JSON. Work in your own copy. Start with one entity's read-all and read-one operations; then decide what further basic CRUD operation supports your chosen scenario. These are practice steps, not a revised assessment checklist.

| Decide from your model | Example here |
| --- | --- |
| What information does the person need? | View a student's enrolment |
| What identifies a record? | Student: integer ID; Enrolment: student/course pair |
| Where are the example data? | A JSON array with the same fields and value types |
| What operation exposes them? | A GET route calling a load/search function |
| What should happen if the record is absent? | Explicit 404 after the search |
| Which model rules require extra checks? | Existing student/course; no duplicate enrolment |

Use your own names, fields and rules; renaming a file alone does not implement a new domain. Keep changes small enough to explain.

For an AI-assisted change, ask for an explanation or a small proposed edit, then **predict → inspect → run → compare**. Try one successful request and a missing/invalid input. Point to the lines and records that explain the result. Do not accept a working-looking answer without checking its consistency with your model.

Before coaching, keep your model, sample JSON and runnable code together with concise run instructions. Note the behaviour implemented and any unresolved question. Follow the actual assignment description for the deliverables; this learning path adds no deadline or required number of endpoints.

[← UML, objects and JSON](04-models-and-objects.md) · [Return to README →](../README.md)
