import unittest
import sys
from unittest.mock import patch
sys.path.insert(0, '/Users/leona/python/Projects/scraper_files/scraper/script')
from make_soup import create_soup


class TestingSoup(unittest.TestCase):
    @patch('builtins.print')
    def test_returned_soup(self, mock_print):
        create_soup('https://ishi1834.github.io/pomodoro-clock/')
        mock_print.assert_called_with('<Response [200]>') #changed response to str so it can be compared

if __name__ == '__main__':
    unittest.main()