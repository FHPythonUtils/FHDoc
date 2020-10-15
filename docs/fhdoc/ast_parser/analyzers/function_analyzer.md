# function_analyzer

> Auto-generated documentation for [fhdoc.ast_parser.analyzers.function_analyzer](../../../../fhdoc/ast_parser/analyzers/function_analyzer.py) module.

AST analyzer for `ast.FunctionDef` records.

- [Fhdoc](../../../README.md#fhdoc-index) / [Modules](../../../README.md#fhdoc-modules) / [fhdoc](../../index.md#fhdoc) / [ast_parser](../index.md#ast_parser) / [analyzers](index.md#analyzers) / function_analyzer
    - [FunctionAnalyzer](#functionanalyzer)
        - [FunctionAnalyzer().generic_visit](#functionanalyzergeneric_visit)
        - [FunctionAnalyzer().visit_AsyncFunctionDef](#functionanalyzervisit_asyncfunctiondef)
        - [FunctionAnalyzer().visit_FunctionDef](#functionanalyzervisit_functiondef)
        - [FunctionAnalyzer().visit_arguments](#functionanalyzervisit_arguments)

## FunctionAnalyzer

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/function_analyzer.py#L14)

```python
class FunctionAnalyzer(BaseAnalyzer):
    def __init__() -> None:
```

AST analyzer for `ast.FunctionDef` records.

#### See also

- [BaseAnalyzer](base_analyzer.md#baseanalyzer)

### FunctionAnalyzer().generic_visit

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/function_analyzer.py#L168)

```python
def generic_visit(_node: ast.AST) -> None:
```

Do nothing for unknown `ast.AST` nodes.

#### Arguments

- `node` - AST node.

### FunctionAnalyzer().visit_AsyncFunctionDef

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/function_analyzer.py#L148)

```python
def visit_AsyncFunctionDef(node: ast.AsyncFunctionDef) -> None:
```

Entrypoint for the analyzer for asynchronous functions.

Visits each node from `node.args`.
Adds new `ast.expr` entry to `decorator_nodes` for each node
from `node.decorator_list`.
Sets `return_type_hint` to `node.returns` if it defined.

#### Examples

```python
async def my_func():
    return await result
```

#### Arguments

- `node` - AST node.

### FunctionAnalyzer().visit_FunctionDef

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/function_analyzer.py#L128)

```python
def visit_FunctionDef(node: ast.FunctionDef) -> None:
```

Entrypoint for the analyzer.

Visits each node from `node.args`.
Adds new `ast.expr` entry to `decorator_nodes` for each node
from `node.decorator_list`.
Sets `return_type_hint` to `node.returns` if it defined.

#### Examples

```python
def my_func():
    return result
```

#### Arguments

- `node` - AST node.

### FunctionAnalyzer().visit_arguments

[[find in source code]](../../../../fhdoc/ast_parser/analyzers/function_analyzer.py#L42)

```python
def visit_arguments(node: ast.arguments) -> None:
```

Parse info about class method statements.

Adds new `ArgumentRecord` entry to `argument_records` for each argument.

#### Examples

```python
# simple arguments
def my_func(
    arg1,
    arg_default="value",
    *args,
    **kwargs,
):
    pass

# type annotated arguments
def my_func_typed(
    arg1: Text,
    arg_default: Text="value",
):
    pass

# keyword-only arguments
def my_func_kw_only(
    *,
    kw_only_arg
):
    pass

# pos-only arguments for py38
def my_func_kw_only(
    pos_only_arg,
    /
):
    pass
```

#### Arguments

- `node` - AST node.
