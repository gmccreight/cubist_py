import unittest
from pathlib import Path
from cubist_py.conf_file_gatherer import file_data


class TestConfFileGatherer(unittest.TestCase):

    def test_loading_data(self):
        p = Path(__file__).parent / 'data/conf/example1'
        d = file_data(p)
        self.assertEqual(len(d), 2)
