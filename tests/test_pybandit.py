from unittest import TestCase

from pybandit import __version__


class TestPybandit(TestCase):

    def __init__(self, *args, **kwargs):
        super(TestPybandit, self).__init__(*args, **kwargs)

    def test_version(self):
        self.assertEqual(__version__, '0.0.1')
