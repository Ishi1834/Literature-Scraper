import unittest
import sys
sys.path.insert(0, '/Users/leona/python/Projects/scraper_files/scraper/script')
from process_keywords import keyword_analyser
from make_spreadsheet import initiate_spreedsheet

"""
This unit test tests if the process_keywords and the make_spreadsheet modules are working
"""

class TestingProcessKeywords(unittest.TestCase):
    def test_keyword_analyser(self):
        summary = """The LCA study for biomass gasification shows a reduction on the net carbon dioxide emissions 
compared to natural gas steam reforming, making this system preferable. Within the various 
feedstocks analysed, Hay is shown to have the biggest impacts in all categories making it unsuitable 
for the gasification processes. The feedstock that has the least impact on the environment are those 
that are by-products, making sawdust and wheat straw the most suitable feedstock for hydrogen 
production.
        """
        keywords = ['biomass', 'gasification']
        worksheet, workbook = initiate_spreedsheet(keywords)

        result = keyword_analyser(summary, 1, keywords, worksheet)
        self.assertEqual(result, 1.5)
        
    def test_keyword_analyser_wrongValue(self):
        summary = """The LCA study for biomass gasification shows a reduction on the net carbon dioxide emissions 
compared to natural gas steam reforming, making this system preferable. Within the various 
feedstocks analysed, Hay is shown to have the biggest impacts in all categories making it unsuitable 
for the gasification processes. The feedstock that has the least impact on the environment are those 
that are by-products, making sawdust and wheat straw the most suitable feedstock for hydrogen 
production.
        """
        keywords = ['biomass', 'gasification']
        worksheet, workbook = initiate_spreedsheet(keywords)

        result = keyword_analyser(summary, 1, keywords, worksheet)
        self.assertNotEqual(result, 5)

if __name__ == '__main__':
    unittest.main()