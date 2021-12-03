import unittest
import sys
from unittest import mock
sys.path.insert(0, '/Users/leona/python/Projects/scraper_files/scraper/script')
from user_inputs import process_input

class TestingUserInputs(unittest.TestCase):
    @mock.patch('user_inputs.input', create=True)
    def test_no_input(self, mocked_input):
        mocked_input.side_effect = ['','','']
        result = process_input()
        self.assertEqual(result, ('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=life+cycle+assessment+of+hydrogen+production+from+biomass+gasification', ['biomass', 'syngas', 'life cycle assessment', 'hydrogen', 'emissions', 'impacts', 'results', 'iso'], 20))
        
    @mock.patch('user_inputs.input', create=True)
    def test_inputs(self, mocked_input):
        mocked_input.side_effect = ['hydrogen production', 'hydrogen energy', '10']
        result = process_input()
        self.assertEqual(result, ('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=hydrogen+production', ['hydrogen', 'energy'], 10))

    @mock.patch('user_inputs.input', create=True)
    def test_wrong_input(self, mocked_input):
        mocked_input.side_effect = ['wrong input given', 'life test', '3']
        result = process_input()
        self.assertNotEqual(result, ('','',3))
        
if __name__ == '__main__':
    unittest.main()