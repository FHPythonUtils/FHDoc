# settings

> Auto-generated documentation for [fhdoc.settings](../../fhdoc/settings.py) module.

Various project constants.

- [Fhdoc](../README.md#fhdoc-index) / [Modules](../README.md#fhdoc-modules) / [fhdoc](index.md#fhdoc) / settings

#### Attributes

- `fhdoc_PATH` - Path to fhdoc root directory.: `os.path.dirname(__file__)`
- `ASSETS_PATH` - Path to `assets` directory from root.: `os.path.join(fhdoc_PATH, 'assets')`
- `LOGGER_NAME` - Global `logging.Logger` name.: `'fhdoc'`
- `EXCLUDE_EXPRS` - Paths to exclude from docs generation.: `['build/*', 'tests/*', 'test/*', '*/__pycache__/*', '.*/*']`
- `SOURCES_GLOB` - `glob.glob` expression to ind all Python sources in current directory.: `'**/*.py'`
- `FIND_IN_SOURCE_LABEL` - Find in code link label.: `'[find in source code]'`
