# module_record

> Auto-generated documentation for [fhdoc.ast_parser.node_records.module_record](../../../../fhdoc/ast_parser/node_records/module_record.py) module.

Wrapper for an `ast.Module` node with corresponding node info.

- [Fhdoc](../../../README.md#fhdoc-index) / [Modules](../../../MODULES.md#fhdoc-modules) / [fhdoc](../../index.md#fhdoc) / [ast_parser](../index.md#ast_parser) / [node_records](index.md#node_records) / module_record
    - [ModuleRecord](#modulerecord)
        - [ModuleRecord().build_children](#modulerecordbuild_children)
        - [ModuleRecord.create_from_source](#modulerecordcreate_from_source)
        - [ModuleRecord().find_record](#modulerecordfind_record)
        - [ModuleRecord().iter_records](#modulerecorditer_records)

## ModuleRecord

[[find in source code]](../../../../fhdoc/ast_parser/node_records/module_record.py#L19)

```python
class ModuleRecord(NodeRecord):
    def __init__(node: ast.Module) -> None:
```

Wrapper for an `ast.Module` node with corresponding node info.

Responsible for parsing Python source as well.

#### Arguments

- `node` - Result of `ast.parse`.

#### See also

- [NodeRecord](node_record.md#noderecord)

### ModuleRecord().build_children

[[find in source code]](../../../../fhdoc/ast_parser/node_records/module_record.py#L153)

```python
def build_children() -> None:
```

Collect full information about Module child records.

Used only when doc for this ModuleRecord is building.

### ModuleRecord.create_from_source

[[find in source code]](../../../../fhdoc/ast_parser/node_records/module_record.py#L44)

```python
@classmethod
def create_from_source(
    source_path: Path,
    import_string: ImportString,
) -> ModuleRecord:
```

Create new [ModuleRecord](#modulerecord) from path.

#### Arguments

- `source_path` - Path to a Python source file.
- `import_string` - File absolute import string.

#### Returns

New [ModuleRecord](#modulerecord) instance.

#### See also

- [ImportString](../../utils/import_string.md#importstring)

### ModuleRecord().find_record

[[find in source code]](../../../../fhdoc/ast_parser/node_records/module_record.py#L68)

```python
def find_record(import_string: ImportString) -> Optional[NodeRecord]:
```

Find child in the Module by an absolute or relative import string.

#### Attributes

- `import_string` - record import string.

#### Returns

Found child record on None.

#### See also

- [ImportString](../../utils/import_string.md#importstring)
- [NodeRecord](node_record.md#noderecord)

### ModuleRecord().iter_records

[[find in source code]](../../../../fhdoc/ast_parser/node_records/module_record.py#L88)

```python
def iter_records() -> Generator[NodeRecord, None, None]:
```

Iterate over Module class, method and fucntion records.

#### Yields

A child record.

#### See also

- [NodeRecord](node_record.md#noderecord)
