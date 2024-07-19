import unittest
from services.parse import *


class TestParseCommand(unittest.TestCase):
    def test_parse_command_add_1_day(self):
        test_command = 'now()+1d'
        self.assertEqual(parse_command(test_command), (['now()'], [('+1d', '+', '1', 'd')], []))

    def test_parse_command_minus_1_day(self):
        test_command = 'now()-1d'
        self.assertEqual(parse_command(test_command), (['now()'], [('-1d', '-', '1', 'd')], []))

    def test_parse_command_snap_day(self):
        test_command = 'now()@d'
        self.assertEqual(parse_command(test_command), (['now()'], [], [('@d', 'd')]))

    def test_parse_command_minus_1_year_snap_month(self):
        test_command = 'now()-1y@mon'
        self.assertEqual(parse_command(test_command), (['now()'], [('-1y', '-', '1', 'y')], [('@mon', 'mon')]))

    def test_parse_command_plus_10_days_plus_12_hours(self):
        test_command = 'now()+10d+12h'
        self.assertEqual(parse_command(test_command),
                         (['now()'], [('+10d', '+', '10', 'd'), ('+12h', '+', '12', 'h')], []))


class TestAmendDateTime(unittest.TestCase):
    def test_amend_date_time_plus_1_day(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(amend_date_time(start_date_time, ('+1d', '+', '1', 'd')), datetime(2020, 1, 2, 1, 1, 1, 234, tzinfo=timezone.utc))

    def test_amend_date_time_minus_1_day(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(amend_date_time(start_date_time, ('-1d', '-', '1', 'd')), datetime(2019, 12, 31, 1, 1, 1, 234, tzinfo=timezone.utc))

    def test_parse_command_minus_1_year(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(amend_date_time(start_date_time, ('-1y', '-', '1', 'y')), datetime(2019, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc))

    def test_parse_command_plus_10_days_plus_12_hours(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        amended_date_time = amend_date_time(start_date_time, ('+10d', '+', '10', 'd'))
        amended_date_time = amend_date_time(amended_date_time, ('+12h', '+', '12', 'h'))
        self.assertEqual(amended_date_time, datetime(2020, 1, 11, 13, 1, 1, 234, tzinfo=timezone.utc))


class TestSnapDateTime(unittest.TestCase):
    def test_snap_date_time_day(self):
        start_date_time = datetime(2020, 1, 1, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(snap_date_time(start_date_time, 'd'), datetime(2020, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))

    def test_snap_date_time_month(self):
        start_date_time = datetime(2020, 1, 5, 1, 1, 1, 234, tzinfo=timezone.utc)
        self.assertEqual(snap_date_time(start_date_time, 'mon'), datetime(2020, 1, 1, 0, 0, 0, 0, tzinfo=timezone.utc))


if __name__ == '__main__':
    unittest.main()
