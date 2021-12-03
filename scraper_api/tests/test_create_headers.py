import unittest
import sys
sys.path.insert(0, '/Users/leona/python/Projects/scraper_files/scraper_api/script')
from create_headers import process_headers

class TestingHeaders(unittest.TestCase):
    def test_returned_headers(self):
        result = process_headers()[0] #access the dict in the returned list
        subset = {"Referer": "https://www.google.com/", "Upgrade-Insecure-Requests": "1"}

        self.assertGreaterEqual(result.items(), subset.items())

if __name__ == '__main__':
    unittest.main()