# pylint: disable=missing-docstring
import unittest
from unittest.mock import patch

from fhdoc.utils import make_title, extract_md_title, render_asset


class TestUtils(unittest.TestCase):
	def test_make_title(self):
		self.assertEqual(make_title("my_path.py"), "My Path Py")
		self.assertEqual(make_title("my_title"), "My Title")
		self.assertEqual(make_title("__init__.py"), "Init Py")
		self.assertEqual(make_title("__main__"), "Module")

	def test_extract_md_title(self):
		self.assertEqual(extract_md_title("# test\ncontent"), ("test", "content"))
		self.assertEqual(extract_md_title("# test\n\ncontent"), ("test", "\ncontent"))
		self.assertEqual(
			extract_md_title("## test\n\ncontent"), ("", "## test\n\ncontent")
		)
		self.assertEqual(extract_md_title("# test"), ("test", ""))

	@patch("fhdoc.utils.Path")
	def test_render_asset(self, PathMock):
		target_path = PathMock("target")
		PathMock().__truediv__().read_text.return_value = "this is {title}"
		self.assertIsNone(render_asset("name", target_path, {"title": "My title"}))
		target_path.write_text.assert_called_with("this is My title")
