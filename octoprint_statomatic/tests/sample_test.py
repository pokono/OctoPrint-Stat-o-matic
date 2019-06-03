from unittest import TestCase

import octoprint_statomatic


class TestSample(TestCase):
	def test_is_string(self):
		s = 11
		self.assertTrue(isinstance(s, basestring))
