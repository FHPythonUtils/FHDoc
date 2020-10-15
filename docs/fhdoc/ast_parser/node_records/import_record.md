# import_record

> Auto-generated documentation for [fhdoc.ast_parser.node_records.import_record](../../../../fhdoc/ast_parser/node_records/import_record.py) module.

Wrapper for an `ast.Import` and `ast.ImportFrom` nodes.

- [Fhdoc](../../../README.md#fhdoc-index) / [Modules](../../../MODULES.md#fhdoc-modules) / [fhdoc](../../index.md#fhdoc) / [ast_parser](../index.md#ast_parser) / [node_records](index.md#node_records) / import_record
    - [ImportRecord](#importrecord)
        - [ImportRecord().get_import_string](#importrecordget_import_string)
        - [ImportRecord().match](#importrecordmatch)

## ImportRecord

[[find in source code]](../../../../fhdoc/ast_parser/node_records/import_record.py#L14)

```python
class ImportRecord(NodeRecord):
    def __init__(node: ASTImport, alias: ast.alias) -> None:
```

Wrapper for an `ast.Import` and `ast.ImportFrom` nodes.

#### Arguments

- `node` - AST node.
- `alias` - AST node with import alias.

#### See also

- [ASTImport](../type_defs.md#astimport)
- [NodeRecord](node_record.md#noderecord)

### ImportRecord().get_import_string

[[find in source code]](../../../../fhdoc/ast_parser/node_records/import_record.py#L35)

```python
def get_import_string() -> ImportString:
```

Get import string from a node.

#### Returns

An absolute import string.

#### See also

- [ImportString](../../utils/import_string.md#importstring)

### ImportRecord().match

[[find in source code]](../../../../fhdoc/ast_parser/node_records/import_record.py#L64)

```python
def match(name: Text) -> Optional[ImportString]:
```

Check if `name` matches or stats with a local name.

#### Examples

```python
import_node = ast.parse('from my_module import Name as LocalName')
import_record = ImportRecord(import_node)

import_record.match('LocalName')
True

import_record.match('LocalName.child')
True

import_record.match('OtherName')
False

import_record.match('LocalNameOther')
False
```

#### Returns

True if name is imported object itself on one of his children.

#### See also

- [ImportString](../../utils/import_string.md#importstring)
