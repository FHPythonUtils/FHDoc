# text_record

> Auto-generated documentation for [fhdoc.ast_parser.node_records.text_record](../../../../fhdoc/ast_parser/node_records/text_record.py) module.

Wrapper for a text-only `ast.expr` node.

- [Fhdoc](../../../README.md#fhdoc-index) / [Modules](../../../README.md#fhdoc-modules) / [fhdoc](../../index.md#fhdoc) / [ast_parser](../index.md#ast_parser) / [node_records](index.md#node_records) / text_record
    - [TextRecord](#textrecord)
        - [TextRecord().related_names](#textrecordrelated_names)

## TextRecord

[[find in source code]](../../../../fhdoc/ast_parser/node_records/text_record.py#L14)

```python
class TextRecord(ExpressionRecord):
    def __init__(node: ast.AST, text: Text) -> None:
```

Wrapper for a text-only `ast.expr` node.

#### Arguments

- `node` - Related AST node.
- `text` - Text to represent it.

#### See also

- [ExpressionRecord](expression_record.md#expressionrecord)

### TextRecord().related_names

[[find in source code]](../../../../fhdoc/ast_parser/node_records/text_record.py#L31)

```python
@property
def related_names() -> Set[Text]:
```

A list of fake `ast.Name.id` records inside the node.

#### Examples

```python
TextRecord(ast_node, 'Union[Text, MyClass]').related_names
{'Union', 'Text', 'MyClass'}
```

#### Returns

A set of related names.
