from unittest import TestCase

import octoprint_statomatic


class TestJoke(TestCase):
	def test_is_string(self):
		s = "something"
		self.assertTrue(isinstance(s, basestring))
