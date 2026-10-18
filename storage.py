"""JSON file access. See docs/03-trace-a-request.md for load versus save."""
import json
from pathlib import Path

# Relative to this file, so starting Python in another folder still works.
DATA_DIR = Path(__file__).resolve().parent / "data"


def load_records(filename: str):
    """Read JSON text and return Python lists/dictionaries."""
    with (DATA_DIR / filename).open(encoding="utf-8") as file:
        return json.load(file)


def save_records(filename: str, records):
    """Replace the file with the supplied records. Used by the optional demo."""
    with (DATA_DIR / filename).open("w", encoding="utf-8") as file:
        json.dump(records, file, indent=2, ensure_ascii=False)
        file.write("\n")

# Filenames come from our code, never from arbitrary user input.
# Missing/invalid files are errors, not silently treated as an empty school.
# JSON files do not enforce foreign keys or support concurrent transactions.
