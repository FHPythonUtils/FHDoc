# expression_record

> Auto-generated documentation for [fhdoc.ast_parser.node_records.expression_record](../../../../fhdoc/ast_parser/node_records/expression_record.py) module.

Wrapper for an `ast.expr` node.

- [Fhdoc](../../../README.md#fhdoc-index) / [Modules](../../../MODULES.md#fhdoc-modules) / [fhdoc](../../index.md#fhdoc) / [ast_parser](../index.md#ast_parser) / [node_records](index.md#node_records) / expression_record
    - [ExpressionRecord](#expressionrecord)
        - [ExpressionRecord().related_names](#expressionrecordrelated_names)

## ExpressionRecord

[[find in source code]](../../../../fhdoc/ast_parser/node_records/expression_record.py#L15)

```python
class ExpressionRecord(NodeRecord):
    def __init__(node: ast.AST) -> None:
```

Wrapper for an `ast.expr` node.

#### Arguments

- `node` - AST node.

#### See also

- [NodeRecord](node_record.md#noderecord)

### ExpressionRecord().related_names

[[find in source code]](../../../../fhdoc/ast_parser/node_records/expression_record.py#L31)

```python
@property
def related_names() -> Set[Text]:
```
