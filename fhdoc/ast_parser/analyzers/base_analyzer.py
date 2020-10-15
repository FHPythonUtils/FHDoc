"""
Base AST analyzer.
"""
from typing import List, Text, TYPE_CHECKING

import ast

if TYPE_CHECKING:  # pragma: no cover
	from fhdoc.ast_parser.node_records.function_record import FunctionRecord
	from fhdoc.ast_parser.node_records.attribute_record import AttributeRecord
	from fhdoc.ast_parser.node_records.class_record import ClassRecord
	from fhdoc.ast_parser.node_records.import_record import ImportRecord
	from fhdoc.ast_parser.node_records.argument_record import ArgumentRecord
	from fhdoc.ast_parser.node_records.argument_record import ExpressionRecord


class BaseAnalyzer(ast.NodeVisitor):
	"""
	Base AST analyzer.

	Has lists for all objects for different analyzers.
	"""

	def __init__(self):
		# type: () -> None
		self.related_names = []  # type: List[Text]
