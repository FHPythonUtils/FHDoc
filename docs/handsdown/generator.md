# Generator

> Auto-generated documentation for [handsdown.generator](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py) module..

Main handsdown documentation generator.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / Generator
  - [Generator](#generator)
    - [Generator().cleanup_old_docs](#generatorcleanup_old_docs)
    - [Generator().generate_doc](#generatorgenerate_doc)
    - [Generator().generate_docs](#generatorgenerate_docs)
    - [Generator().generate_index](#generatorgenerate_index)
  - [GeneratorError](#generatorerror)

## Generator

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L34)

```python
class Generator(
    input_path,
    output_path,
    source_paths,
    logger=None,
    docstring_processor=None,
    loader=None,
    raise_errors=False,
    source_code_url=None,
    toc_depth=3,
)
```

Main handsdown documentation generator.

#### Arguments

- `input_path` - Path to repo to generate docs.
- `output_path` - Path to folder with auto-generated docs to output.
- `source_paths` - List of paths to source files for generation.
- `logger` - Logger instance.
- `docstring_processor` - Docstring converter to Markdown.
- `loader` - Loader for python modules.
- `raise_errors` - Raise [LoaderError](loader.md#loadererror) instead of silencing in.
- `ignore_unknown_errors` - Continue on any error.
- `source_code_url` - URL to source files to use instead of relative paths,
    useful for [GitHub Pages](https://pages.github.com/).
- `toc_depth` - Maximum depth of child modules ToC

- `LOGGER_NAME` - Name of logger: `handsdown`
- `INDEX_NAME` - Docs index filename: `README.md`
- `INDEX_TITLE` - Docs index title: `Index`
- `MODULES_NAME` - Modules ToC name in index: `Modules`

### Generator().cleanup_old_docs

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L129)

```python
def cleanup_old_docs()
```

Remove old docs generated for this module.

### Generator().generate_doc

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L163)

```python
def generate_doc(source_path)
```

Generate one module doc at once.

#### Arguments

- `source_path` - Path to source file.

#### Raises

- [GeneratorError](#generatorerror) - If `source_path` not found in current repo.

### Generator().generate_docs

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L274)

```python
def generate_docs()
```

Generate all doc files at once.

### Generator().generate_index

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L290)

```python
def generate_index()
```

Generate `<output>/README.md` file with title from `<root>/README.md` and `Modules`
section that contains a Tree of all modules in the project.

## GeneratorError

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/generator.py#L28)

```python
class GeneratorError(*args, **kwargs)
```

Main error for [Generator](#generator)
