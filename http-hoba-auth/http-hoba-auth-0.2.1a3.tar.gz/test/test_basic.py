# standard imports
import unittest
import logging

# local imports
from http_hoba_auth import Hoba

logging.basicConfig(level=logging.DEBUG)
logg = logging.getLogger()

class Test(unittest.TestCase):

    auth_example = 'APAeYTSy7MGaALMr+hm1OzdHdAzA4se26p9WHMHXyVE=.5xIfu0aBxBPHS/31wf9i2mxR098=.MyliXAfcRKy/NO/QnhumoMWNhSvce+Sq8MQefVOlgNY=.TlzNAnX6fPX+MEV2wb+yl+M7HldmZ12wS7flIIZBbrQl41WoTB+E0qM4wB3I8sbIXaQx+gfLuKLx1Mb+k5pg3Bw='

    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_parse(self):
        h = Hoba('http://localhost:5555', 'GE')
        h.parse(self.auth_example)
        s = h.to_be_signed()
        logg.debug('signed {}'.format(s))


    def test_parse_after_dump(self):
        h = Hoba('http://localhost:5555', 'GE')
        h.parse(self.auth_example)
        self.assertEqual(self.auth_example, str(h))


if __name__ == '__main__':
    unittest.main()
