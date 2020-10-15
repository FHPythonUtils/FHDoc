# pylint: disable=missing-docstring
import unittest
from unittest.mock import patch
from pathlib import Path

from fhdoc.main import main


class TestMain(unittest.TestCase):
	@patch("fhdoc.main.get_logger")
	@patch("fhdoc.main.PathFinder")
	@patch("fhdoc.main.Generator")
	def test_main(self, generator_mock, path_finder_mock, _get_logger_mock):

		with patch(
			"fhdoc.main.sys.argv",
			[
				"fhdoc",
				"-i",
				"/",
				"-o",
				"/output-path",
				"include",
				"--exclude",
				"exclude",
			],
		):
			self.assertIsNone(main())

		path_finder_mock.assert_called_once_with(Path("/"))
		path_finder_mock().exclude.assert_called_once_with(
			"build/*", "tests/*", "test/*", "*/__pycache__/*", ".*/*", "exclude"
		)
		path_finder_mock().exclude().include.assert_called_once_with("include")
		generator_mock.assert_called_once_with(
			input_path=Path("/"),
			output_path=Path("/output-path"),
			project_name="fhdoc",
			raise_errors=False,
			source_code_url=None,
			source_paths=path_finder_mock().exclude().include().glob(),
			toc_depth=1,
		)
