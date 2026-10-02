# REVIEW

## Identity
- Pakawun Jindawat, 6681453
- AI tool: GitHub Copilot (Plan mode, then Agent mode)
- Worked independently.

## Review decision
In `test_student.py`, Copilot's two tests covered a cancelled booking being
ignored and an old/new slot being released/blocked. These weren't the two
required cases and had no recorded expectations. I corrected this by replacing
them with my own tests: a same-room move that overlaps its own old time
(Room 201, 600-660 to 630-690) and an unchanged request (R4). Each has a
Given/When/Expect comment. I checked that the assertions confirm the same object
is returned, the ID and status stay the same, and the other booking and list
order are unchanged. I kept Copilot's `move_booking` in `service.py` because it
validates and checks conflicts before changing anything, excludes the target
from the conflict check, and updates the same object (R1-R3, R6). I also
restored SPEC.md after noticing stray backticks had been added to it.

## Checks
- Baseline commit: ce156d0
- Baseline: `uv run --python 3.12 python -m unittest -v test_baseline`
  -> Ran 6 tests, OK
- Final suite: `uv run --python 3.12 python -m unittest -v test_baseline test_move_smoke test_student`
  -> Ran 11 tests in 0.000s, OK

## Remaining uncertainty
R5 says a valid room name doesn't prove the room exists, and there is no room
catalogue. So move_booking will accept a move to a room the business doesn't
actually have, like "Room 999". My tests don't settle how staff should be
prevented from moving a booking into a non-existent room.