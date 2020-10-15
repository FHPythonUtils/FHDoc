# module_record_list

> Auto-generated documentation for [fhdoc.ast_parser.module_record_list](../../../fhdoc/ast_parser/module_record_list.py) module.

Aggregation of `ModuleRecord` objects.

- [Fhdoc](../../README.md#fhdoc-index) / [Modules](../../README.md#fhdoc-modules) / [fhdoc](../index.md#fhdoc) / [ast_parser](index.md#ast_parser) / module_record_list
    - [ModuleRecordList](#modulerecordlist)
        - [ModuleRecordList().\_\_iter\_\_](#modulerecordlist__iter__)
        - [ModuleRecordList().add](#modulerecordlistadd)
        - [ModuleRecordList().find_module_record](#modulerecordlistfind_module_record)
        - [ModuleRecordList().get_package_names](#modulerecordlistget_package_names)

## ModuleRecordList

[[find in source code]](../../../fhdoc/ast_parser/module_record_list.py#L15)

```python
class ModuleRecordList():
    def __init__() -> None:
```

Aggregation of `ModuleRecord` objects.

### ModuleRecordList().\_\_iter\_\_

[[find in source code]](../../../fhdoc/ast_parser/module_record_list.py#L70)

```python
def __iter__() -> Generator[ModuleRecord, None, None]:
```

Iterate over all added `ModuleRecord` entries.

#### Yields

`ModuleRecord` entries.

#### See also

- [ModuleRecord](node_records/module_record.md#modulerecord)

### ModuleRecordList().add

[[find in source code]](../../../fhdoc/ast_parser/module_record_list.py#L59)

```python
def add(module_record: ModuleRecord) -> None:
```

Add new `ModuleRecord`.

#### Arguments

- `module_record` - A new `ModuleRecord`

#### See also

- [ModuleRecord](node_records/module_record.md#modulerecord)

### ModuleRecordList().find_module_record

[[find in source code]](../../../fhdoc/ast_parser/module_record_list.py#L26)

```python
def find_module_record(import_string: ImportString) -> Optional[ModuleRecord]:
```

Find `ModuleRecord` by it's import string.

#### Arguments

- `import_string` - Object import string.

#### Returns

Found `NodeRecord` instance or None.

#### See also

- [ImportString](../utils/import_string.md#importstring)
- [ModuleRecord](node_records/module_record.md#modulerecord)

### ModuleRecordList().get_package_names

[[find in source code]](../../../fhdoc/ast_parser/module_record_list.py#L49)

```python
def get_package_names() -> Set[Text]:
```

Get top level import strings.

#### Returns

A set of top level imports as strings.
