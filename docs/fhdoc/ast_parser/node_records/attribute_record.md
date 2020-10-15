# AttributeRecord

> Auto-generated documentation for [fhdoc.ast_parser.node_records.attribute_record](../../../../fhdoc/ast_parser/node_records/attribute_record.py) module.

Wrapper for an `ast.Assign` node of a module or class attribute.

- [Fhdoc](../../../README.md#fhdoc-index) / [Modules](../../../MODULES.md#modules) / [Fhdoc](../../index.md#fhdoc) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / AttributeRecord
    - [AttributeRecord](#attributerecord)
        - [AttributeRecord().related_names](#attributerecordrelated_names)

## AttributeRecord

[[find in source code]](../../../../fhdoc/ast_parser/node_records/attribute_record.py#L14)

```python
class AttributeRecord(NodeRecord):
    def __init__(node: ast.Assign) -> None:
```

Wrapper for an `ast.Assign` node of a module or class attribute.

#### Arguments

- `node` - AST node.

#### See also

- [NodeRecord](node_record.md#noderecord)

### AttributeRecord().related_names

[[find in source code]](../../../../fhdoc/ast_parser/node_records/attribute_record.py#L32)

```python
@property
def related_names() -> Set[Text]:
```
