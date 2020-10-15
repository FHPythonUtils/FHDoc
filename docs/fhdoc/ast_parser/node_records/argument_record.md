# argument_record

> Auto-generated documentation for [fhdoc.ast_parser.node_records.argument_record](../../../../fhdoc/ast_parser/node_records/argument_record.py) module.

Wrapper for an `ast.arg` node.

- [Fhdoc](../../../README.md#fhdoc-index) / [Modules](../../../MODULES.md#fhdoc-modules) / [fhdoc](../../index.md#fhdoc) / [ast_parser](../index.md#ast_parser) / [node_records](index.md#node_records) / argument_record
    - [ArgumentRecord](#argumentrecord)
        - [ArgumentRecord().default](#argumentrecorddefault)
        - [ArgumentRecord().related_names](#argumentrecordrelated_names)
        - [ArgumentRecord().set_default](#argumentrecordset_default)

## ArgumentRecord

[[find in source code]](../../../../fhdoc/ast_parser/node_records/argument_record.py#L15)

```python
class ArgumentRecord(NodeRecord):
    def __init__(
        node: ast.arg,
        name: Text,
        type_hint: Optional[ast.expr] = None,
        prefix: Text = '',
    ) -> None:
```

Wrapper for an `ast.arg` node.

#### Arguments

- `node` - AST node.
- `name` - Argument name.
- `type_hint` - Argument type hint.
- `prefix` - Prefix for arguemnt name, used for starargs.

#### See also

- [NodeRecord](node_record.md#noderecord)

### ArgumentRecord().default

[[find in source code]](../../../../fhdoc/ast_parser/node_records/argument_record.py#L42)

```python
@property
def default() -> Optional[ExpressionRecord]:
```

Default value of the argument.

#### Returns

Default exression or None.

#### See also

- [ExpressionRecord](expression_record.md#expressionrecord)

### ArgumentRecord().related_names

[[find in source code]](../../../../fhdoc/ast_parser/node_records/argument_record.py#L66)

```python
@property
def related_names() -> Set[Text]:
```

### ArgumentRecord().set_default

[[find in source code]](../../../../fhdoc/ast_parser/node_records/argument_record.py#L53)

```python
def set_default(node: Node) -> None:
```

Set default expression from test or `ast.AST` node.

#### Arguments

- `node` - Text or AST node.

#### See also

- [Node](../type_defs.md#node)
