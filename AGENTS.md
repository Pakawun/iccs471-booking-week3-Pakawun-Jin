# Project guidance

- This is a Python 3.12 office-space booking app (models.py, rules.py, service.py). Only implement move_booking in service.py, and follow SPEC.md for the movement rules.
- Don't change how booking creation or conflict checks work. Keep booking IDs and existing records (including cancelled ones) as they are, and don't edit SPEC.md or add unrelated features.
- Run `uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student` after changes. The 6 baseline tests must still pass.
- Stop after move_booking and its tests are done, and show me the changed files and test results for review before committing.
