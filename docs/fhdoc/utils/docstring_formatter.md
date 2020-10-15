# DocstringFormatter

> Auto-generated documentation for [fhdoc.utils.docstring_formatter](../../../fhdoc/utils/docstring_formatter.py) module.

Translator of docstrings to Markdown format.

- [Fhdoc](../../README.md#fhdoc-index) / [Modules](../../MODULES.md#modules) / [Fhdoc](../index.md#fhdoc) / [Utils](index.md#utils) / DocstringFormatter
    - [DocstringFormatter](#docstringformatter)
        - [DocstringFormatter().render](#docstringformatterrender)

## DocstringFormatter

[[find in source code]](../../../fhdoc/utils/docstring_formatter.py#L13)

```python
class DocstringFormatter():
    def __init__(docstring: Text) -> None:
```

Translator of docstrings to Markdown format.

#### Arguments

- `docstring` - Raw docstring.

### DocstringFormatter().render

[[find in source code]](../../../fhdoc/utils/docstring_formatter.py#L63)

```python
def render() -> Text:
```

Get Markdown-friendly docstring.

#### Returns

A cleaned up docstring.
