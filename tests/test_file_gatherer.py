from .cubist_test_case import CubistTestCase
from cubist_py.conf_file_gatherer import file_data


class TestConfFileGatherer(CubistTestCase):

    def test_gathers_all_conf_files_below_dir(self):
        p = self.data_dir() / 'conf/example1'
        d = file_data(p)
        self.assertEqual(len(d), 2)
