import unittest
from datetime import datetime
from src.errors.generator_errors import errors
from src.generators.date.generator import generate_date, GeneratedDate


class TestGeneratedDate(unittest.TestCase):

    def test_generate_date_with_defaults(self):
        date_obj = generate_date()
        self.assertIsInstance(date_obj, GeneratedDate)
        self.assertTrue(1970 <= date_obj.date.year <= 2050)
        self.assertTrue(1 <= date_obj.date.month <= 12)
        self.assertTrue(1 <= date_obj.date.day <= 28)
        self.assertEqual(date_obj.date.hour, 0)
        self.assertEqual(date_obj.date.minute, 0)
        self.assertEqual(date_obj.date.second, 0)

    def test_generate_date_with_specific_date(self):
        date_obj = generate_date(day=15, month=6, year=2022)
        self.assertEqual(date_obj.date.year, 2022)
        self.assertEqual(date_obj.date.month, 6)
        self.assertEqual(date_obj.date.day, 15)
        self.assertEqual(date_obj.date.hour, 0)
        self.assertEqual(date_obj.date.minute, 0)
        self.assertEqual(date_obj.date.second, 0)

    def test_generate_date_with_specific_time(self):
        date_obj = generate_date(hour=14, minute=30, second=45)
        self.assertTrue(1970 <= date_obj.date.year <= 2050)
        self.assertTrue(1 <= date_obj.date.month <= 12)
        self.assertTrue(1 <= date_obj.date.day <= 28)
        self.assertEqual(date_obj.date.hour, 14)
        self.assertEqual(date_obj.date.minute, 30)
        self.assertEqual(date_obj.date.second, 45)

    def test_generate_date_with_full_date_and_time(self):
        date_obj = generate_date(day=15, month=6, year=2022, hour=14, minute=30, second=45)
        self.assertEqual(date_obj.date.year, 2022)
        self.assertEqual(date_obj.date.month, 6)
        self.assertEqual(date_obj.date.day, 15)
        self.assertEqual(date_obj.date.hour, 14)
        self.assertEqual(date_obj.date.minute, 30)
        self.assertEqual(date_obj.date.second, 45)

    def test_invalid_day_for_february(self):
        with self.assertRaises(errors.DateGetError):
            generate_date(day=29, month=2, year=2022)

    def test_invalid_day(self):
        with self.assertRaises(errors.DateGetError):
            generate_date(day=32)

    def test_invalid_month(self):
        with self.assertRaises(errors.DateGetError):
            generate_date(month=13)

    def test_invalid_hour(self):
        with self.assertRaises(errors.DateGetError):
            generate_date(hour=24)

    def test_invalid_minute(self):
        with self.assertRaises(errors.DateGetError):
            generate_date(minute=60)

    def test_invalid_second(self):
        with self.assertRaises(errors.DateGetError):
            generate_date(second=60)


if __name__ == '__main__':
    unittest.main()
