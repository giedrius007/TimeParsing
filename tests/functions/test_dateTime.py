import unittest
from functions.dateTime import *
from datetime import timezone


class TestAddUnitsToDateTime(unittest.TestCase):
    def test_add_seconds(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_seconds(start_date_time, 5), datetime(2020, 1, 1, 0, 0, 5, tzinfo=timezone.utc))

    def test_minus_seconds(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_seconds(start_date_time, -5), datetime(2019, 12, 31, 23, 59, 55, tzinfo=timezone.utc))

    def test_add_minutes(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_minutes(start_date_time, 5), datetime(2020, 1, 1, 0, 5, 0, tzinfo=timezone.utc))

    def test_minus_minutes(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_minutes(start_date_time, -5), datetime(2019, 12, 31, 23, 55, 0, tzinfo=timezone.utc))

    def test_add_hours(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_hours(start_date_time, 5), datetime(2020, 1, 1, 5, 0, 0, tzinfo=timezone.utc))

    def test_minus_hours(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_hours(start_date_time, -5), datetime(2019, 12, 31, 19, 0, 0, tzinfo=timezone.utc))

    def test_add_days(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_days(start_date_time, 5), datetime(2020, 1, 6, 0, 0, 0, tzinfo=timezone.utc))

    def test_minus_days(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_days(start_date_time, -5), datetime(2019, 12, 27, 0, 0, 0, tzinfo=timezone.utc))

    def test_add_months(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_months(start_date_time, 5), datetime(2020, 6, 1, 0, 0, 0, tzinfo=timezone.utc))

    def test_add_months_less_days(self):
        start_date_time = datetime(2024, 1, 31, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_months(start_date_time, 1), datetime(2024, 2, 29, 0, 0, 0, tzinfo=timezone.utc))


    def test_minus_months(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_months(start_date_time, -5), datetime(2019, 8, 1, 0, 0, 0, tzinfo=timezone.utc))

    def test_add_years(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_years(start_date_time, 5), datetime(2025, 1, 1, 0, 0, 0, tzinfo=timezone.utc))

    def test_minus_years(self):
        start_date_time = datetime(2020, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_years(start_date_time, -5), datetime(2015, 1, 1, 0, 0, 0, tzinfo=timezone.utc))

    def test_add_years_with_month_having_less_days(self):
        start_date_time = datetime(2024, 2, 29, 0, 0, 0, tzinfo=timezone.utc)
        self.assertEqual(add_years(start_date_time, 1), datetime(2025, 2, 28, 0, 0, 0, tzinfo=timezone.utc))


class TestSnapToDateTime(unittest.TestCase):
    def test_snap_seconds(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(snap_seconds(start_date_time), datetime(2020, 1, 1, 1, 1, 1, 0, tzinfo=timezone.utc))

    def test_snap_minutes(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(snap_minutes(start_date_time), datetime(2020, 1, 1, 1, 1, 0, 0, tzinfo=timezone.utc))

    def test_snap_hours(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(snap_hours(start_date_time), datetime(2020, 1, 1, 1, 0, 0, 0, tzinfo=timezone.utc))

    def test_snap_days(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(snap_days(start_date_time), datetime(2020, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))

    def test_snap_months(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(snap_months(start_date_time), datetime(2020, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))

    def test_snap_years(self):
        start_date_time = datetime(2020, 2, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(snap_years(start_date_time), datetime(2020, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))


if __name__ == '__main__':
    unittest.main()
