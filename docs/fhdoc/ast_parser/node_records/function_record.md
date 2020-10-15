# FunctionRecord

> Auto-generated documentation for [fhdoc.ast_parser.node_records.function_record](../../../../fhdoc/ast_parser/node_records/function_record.py) module.

Wrapper for an `ast.FunctionDef` node.

- [Fhdoc](../../../README.md#fhdoc-index) / [Modules](../../../MODULES.md#modules) / [Fhdoc](../../index.md#fhdoc) / [AST Parser](../index.md#ast-parser) / [Node Records](index.md#node-records) / FunctionRecord
    - [FunctionRecord](#functionrecord)
        - [FunctionRecord().parse_type_comments](#functionrecordparse_type_comments)
        - [FunctionRecord().related_names](#functionrecordrelated_names)

## FunctionRecord

[[find in source code]](../../../../fhdoc/ast_parser/node_records/function_record.py#L19)

```python
class FunctionRecord(NodeRecord):
    def __init__(node: ASTFunctionDef, is_method: bool) -> None:
```

Wrapper for an `ast.FunctionDef` and `ast.AsyncFunctionDef` node.

#### Arguments

- `node` - AST node.

#### See also

- [ASTFunctionDef](../type_defs.md#astfunctiondef)
- [NodeRecord](node_record.md#noderecord)

### FunctionRecord().parse_type_comments

[[find in source code]](../../../../fhdoc/ast_parser/node_records/function_record.py#L102)

```python
def parse_type_comments(lines: List[Text]) -> None:
```

Extract comment type annotations from a function definiition lines.

Sets `arguemnts_record` to a new `TextRecord` for each found type annotaiton.
Also sets `return_type_hint` to a `TextRecord` if fucntion return type found.

### FunctionRecord().related_names

[[find in source code]](../../../../fhdoc/ast_parser/node_records/function_record.py#L45)

```python
@property
def related_names() -> Set[Text]:
```
