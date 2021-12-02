import unittest
import sys
sys.path.insert(0, '/Users/leona/python/Projects/scraper_files/scraper_api')
from process_keywords import keyword_analyser

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
        result = keyword_analyser(summary, keywords)
        self.assertEqual(result, 1.5)

if __name__ == '__main__':
    unittest.main()
