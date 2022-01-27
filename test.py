from most_active_cookie import CookieParser
import unittest


class TestMostActiveCookie(unittest.TestCase):

    def test_given_testcase(self):
        parser = CookieParser("./most_active_cookie.py TestCSVs/given_testcase.csv -d 2018-12-09".split())
        self.assertEqual(parser.find_max_from_args(), ['AtY0laUfhglK3lC7'])

    def test_multiple_cookies(self):
        parser = CookieParser("./most_active_cookie.py TestCSVs/multiple_cookies.csv -d 2018-12-09".split())
        self.assertEqual(parser.find_max_from_args(), ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '5UAVanZf6UtGyKVS'])

    def test_empty(self):
        parser = CookieParser("./most_active_cookie.py TestCSVs/empty.csv -d 2018-12-09".split())
        with self.assertRaises(ValueError):
            parser.find_max_from_args()

    def test_wrong_datatype(self):
        parser = CookieParser("./most_active_cookie.py TestCSVs/wrong_datatype.csv -d 2018-12-09".split())
        with self.assertRaises(ValueError):
            parser.find_max_from_args()

    def test_multiple_of_each(self):
        parser = CookieParser("./most_active_cookie.py TestCSVs/multiple_of_each.csv -d 2018-12-09".split())
        self.assertEqual(parser.find_max_from_args(), ['AtY0laUfhglK3lC7', 'SAZuXPGUrfbcn5UA'])


if __name__ == '__main__':
    unittest.main()