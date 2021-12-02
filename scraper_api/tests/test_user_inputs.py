import unittest
import sys
sys.path.insert(0, '/Users/leona/python/Projects/scraper_files/scraper_api')
from user_inputs import process_input

class TestingUserInputs(unittest.TestCase):

    def test_no_input(self):
        title = ''
        keywords = ''
        result = process_input(title, keywords)
        self.assertEqual(result, ('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=life+cycle+assessment+of+hydrogen+production+from+biomass+gasification', ['biomass', 'syngas', 'life cycle assessment', 'hydrogen', 'emissions', 'impacts', 'results', 'iso'], 20))
        
    def test_inputs(self):
        title = 'hydrogen production'
        keywords =  'hydrogen energy'
        result = process_input(title, keywords)
        self.assertEqual(result, ('https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=hydrogen+production', ['hydrogen', 'energy'], 20))

    def test_wrong_input(self):
        title = 'wrong title'
        keywords =  'life test'
        result = process_input(title, keywords)
        self.assertNotEqual(result, ('','', 20))
        
if __name__ == '__main__':
    unittest.main()