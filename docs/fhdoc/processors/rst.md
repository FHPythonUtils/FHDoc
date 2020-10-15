# rst

> Auto-generated documentation for [fhdoc.processors.rst](../../../fhdoc/processors/rst.py) module.

Docstring processor for restructured text docstring format.

- [Fhdoc](../../README.md#fhdoc-index) / [Modules](../../MODULES.md#fhdoc-modules) / [fhdoc](../index.md#fhdoc) / [processors](index.md#processors) / rst
    - [RSTDocstringProcessor](#rstdocstringprocessor)

Supported features:

- `:param <name> <?type>: <?description>` directive is added to `Arguments` section
- `:type: <?description>` directive transformed to `Type: <type>`
- `:returns <?type>: <?description>` directive is added to `Returns` section
- `:rtype: <?description>` directive transformed to `Type: <type>`
- `:raises: <?description>` directive is added to `Raises` section
- `.. seealso::` directive is added to `See also` section
- `.. note::` directive is added to `Notes` section
- `.. warning:: <version>` directive is added to `Warnings` section
- `.. versionadded:: <version>` directive is formatted in Sphinx-style and added to `Notes` section
- `.. versionchanged:: <version>` directive is formatted in Sphinx-style and added to `Notes` section
- `.. deprecated::` directive is formatted in Sphinx-style and added to `Notes` section
- `.. code-block::` directive is formatted as Markdown Python codeblock
- `.. code-block:: <language>` directive is formatted as Markdown codeblock
- `.. math::` directive is formatted as Markdown Python codeblock
- `.. highlight::` directive is formatted as Markdown Python codeblock
- `.. highlight:: <language>` directive is formatted as Markdown codeblock

## RSTDocstringProcessor

[[find in source code]](../../../fhdoc/processors/rst.py#L32)

```python
class RSTDocstringProcessor(BaseDocstringProcessor):
```

Docstring processor for restructured text docstring format.

#### See also

- [BaseDocstringProcessor](base.md#basedocstringprocessor)
