# pylint: disable=missing-docstring
import unittest
from unittest.mock import patch

from fhdoc.utils.logger import get_logger


class TestLogging(unittest.TestCase):
	@patch("fhdoc.utils.logger.logging")
	def test_get_logger(self, logging_mock):
		logging_mock.getLogger().handlers = []

		self.assertTrue(get_logger(level=10))
		logging_mock.getLogger.assert_called_with("fhdoc")
		logging_mock.getLogger().setLevel.assert_called_with(10)
		logging_mock.StreamHandler().setLevel.assert_called_with(10)
