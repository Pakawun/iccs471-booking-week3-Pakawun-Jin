"""Add your two tests here. Keep the supplied baseline and smoke tests intact."""
import unittest
from models import Booking
from service import move_booking


class MoveStudentTests(unittest.TestCase):
    # Given: booking #17 in Room 201, 600-660, and booking #18 in Room 203, 600-660.
    # When: move #17 to Room 201, 630-690 (overlaps its own old time, no other blocker).
    # Expect: move succeeds; the same object is returned with ID 17, Room 201,
    #         630-690, still active; #18 and the list order are unchanged.
    def test_move_overlapping_own_old_time_succeeds(self):
        target = Booking(17, "Room 201", 600, 660)
        other = Booking(18, "Room 203", 600, 660)
        bookings = [target, other]

        result = move_booking(bookings, 17, "Room 201", 630, 690)

        self.assertIs(result, target)
        self.assertEqual(target, Booking(17, "Room 201", 630, 690))
        self.assertEqual(target.status, "active")
        self.assertEqual(len(bookings), 2)
        self.assertIs(bookings[0], target)
        self.assertIs(bookings[1], other)
        self.assertEqual(other, Booking(18, "Room 203", 600, 660))

    # Given: booking #17 in Room 201, 600-660, and booking #18 in Room 203, 600-660.
    # When: move #17 to its current position (Room 201, 600-660).
    # Expect: succeeds with no change (R4); same object, same ID, room, times and
    #         status; #18 and the list order are unchanged.
    def test_unchanged_request_succeeds_without_change(self):
        target = Booking(17, "Room 201", 600, 660)
        other = Booking(18, "Room 203", 600, 660)
        bookings = [target, other]

        result = move_booking(bookings, 17, "Room 201", 600, 660)

        self.assertIs(result, target)
        self.assertEqual(target, Booking(17, "Room 201", 600, 660))
        self.assertEqual(target.status, "active")
        self.assertEqual(len(bookings), 2)
        self.assertIs(bookings[0], target)
        self.assertIs(bookings[1], other)
        self.assertEqual(other, Booking(18, "Room 203", 600, 660))


if __name__ == "__main__":
    unittest.main()