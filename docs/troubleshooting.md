# When the demo does not run

[← Setup and learning path](../README.md)

| What you see | What to check |
| --- | --- |
| `Run: not found` | Copy only `python run.py`, without the label `Run:` or a shell prompt. |
| `can't open file ... run.py` | Open the terminal in the repository root, where `run.py` is located. |
| `No module named fastapi` or `uvicorn` | With the intended Python active, run `python -m pip install -r requirements.txt`. In Codespaces first check whether container setup has finished successfully. |
| An editor underlines an installed import | Select the correct Python interpreter in VS Code; editor and terminal can be using different environments. |
| Port 8000 already in use | Stop the other demo with Ctrl+C in its own terminal. Do not run tutorial and school app together on the same port. |
| Browser cannot connect in Codespaces | Keep the application running and use **Ports → 8000 → Open in Browser**. Add `/docs` to that address; your computer's localhost is a different machine. |
| 404 at an ID | Try a known ID. Then inspect the stored records and the lookup; this can be the expected application response. |
| 422 at an ID | Use an integer for `student_id`, such as 1002. `course_id` is a string, such as IS101. |
| 500 / traceback after editing data | Inspect the terminal. Check JSON punctuation, required keys and filenames. Restore your saved copy if necessary. |
| Tutorial accepts ID 9999 | Expected: it only echoes the input. Stop it and run `python run.py` for the real lookup. |

Only port 8000 is needed. `/docs`, `/openapi.json` and all API routes are paths on the same running application. A private forwarded port requires the appropriate signed-in access; do not make it public just to fix an unrelated code error.

Reference: [GitHub's port-forwarding guide](https://docs.github.com/en/codespaces/developing-in-a-codespace/forwarding-ports-in-your-codespace).
