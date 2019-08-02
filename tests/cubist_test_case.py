import unittest
from pathlib import Path


class CubistTestCase(unittest.TestCase):

    def data_dir(self):
        return Path(__file__).parent / 'data'
