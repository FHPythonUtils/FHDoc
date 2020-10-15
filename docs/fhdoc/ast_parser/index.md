# ast_parser

> Auto-generated documentation for [fhdoc.ast_parser](../../../fhdoc/ast_parser/__init__.py) module.

Collection of tools for analyzing AST and also rendering it back to a valid Python code.

- [Fhdoc](../../README.md#fhdoc-index) / [Modules](../../README.md#fhdoc-modules) / [fhdoc](../index.md#fhdoc) / ast_parser
    - [Usage](#usage)
        - [Examples](#examples)
    - Modules
        - [analyzers](analyzers/index.md#analyzers)
        - [enums](enums.md#enums)
        - [module_record_list](module_record_list.md#module_record_list)
        - [node_records](node_records/index.md#node_records)
        - [type_defs](type_defs.md#type_defs)

## Usage

Use `fhdoc.ast_parser.node_records.ModuleRecord` to parse the source code.

### Examples

```python
from pathlib import Path

from fhdoc.utils.import_string import ImportString
from fhdoc.ast_parser.node_records import ModuleRecord

source_path = Path("my_module.py")
import_string = ImportString("my_module")
module_record = ModuleRecord.create_from_source(source_path, import_string)
module_record.build_children() # generate records for imports, classes, attributes and function in module

function_record = module_record.function_records[0] # get the first function in module
print(function_record.render(allow_multiline=True)) # print function definition
print(function_record.return_type_hint.render()) # print function return type annotation
```
