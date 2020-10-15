# pylint: disable=missing-docstring
import unittest


from fhdoc.ast_parser.analyzers.base_analyzer import BaseAnalyzer


class TestBaseAnalyzer(unittest.TestCase):
	def test_init(self):
		analyzer = BaseAnalyzer()
		self.assertEqual(analyzer.related_names, [])
