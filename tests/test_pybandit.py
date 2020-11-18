from unittest import TestCase

from pybandit import __version__


class TestPybandit(TestCase):
    def test_version(self):
        assert __version__ == '0.0.1'
