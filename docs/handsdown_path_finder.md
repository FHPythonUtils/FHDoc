# PathFinder

> Auto-generated documentation for [handsdown.path_finder](../handsdown/path_finder.py) module.

- [Handsdown](./README.md#handsdown) / [Handsdown](./handsdown_index.md#handsdown) / PathFinder
  - [PathFinder](#pathfinder)
    - [PathFinder().\_\_iter\_\_](#pathfinder__iter__)
    - [PathFinder().exclude](#pathfinderexclude)
    - [PathFinder().include](#pathfinderinclude)
    - [PathFinder().list](#pathfinderlist)

## PathFinder

[🔍 find in source code](../handsdown/path_finder.py#L9)

```python
class PathFinder(root: pathlib.Path, glob_expr: str)
```

Find matching paths inside `root` path.

#### Examples

```python
path_finder = PathFinder(root=Path.cwd(), glob_expr='*.txt')
path_finder.list()
['my_new.txt', 'my.txt', 'new.txt']

path_finder.include('my*').list()
['my_new.txt', 'my.txt']

path_finder.exclude('*new*').list()
['my.txt']
```

#### Arguments

- `root` - Path to root folder.
- `glob_expr` - `glob` expression to lookup in `root`

### PathFinder().\_\_iter\_\_

[🔍 find in source code](../handsdown/path_finder.py#L108)

```python
def __iter__() -> Generator[pathlib.Path, NoneType, NoneType]
```

Iterate over matched paths respecting `include` and `exclude` patterns.

#### Returns

A generator of matched paths.

### PathFinder().exclude

[🔍 find in source code](../handsdown/path_finder.py#L66)

```python
def exclude(*fn_exrps: str) -> handsdown.path_finder.PathFinder
```

Add `fnmatch` expression to black list.
If black list is empty - no black list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

fn_exrps - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

#### See also

- [PathFinder](#pathfinder)

### PathFinder().include

[🔍 find in source code](../handsdown/path_finder.py#L46)

```python
def include(*fn_exrps: str) -> handsdown.path_finder.PathFinder
```

Add `fnmatch` expression to white list.
If white list is empty - no white list filtration applied.
If expression does not have `*` or `.` characters, appends `/*` to it.

#### Arguments

fn_exrps - One or more `fnmatch` expressions.

#### Returns

A copy of itself.

#### See also

- [PathFinder](#pathfinder)

### PathFinder().list

[🔍 find in source code](../handsdown/path_finder.py#L124)

```python
def list() -> List[pathlib.Path]
```

Return all matching paths as a list.

#### Returns

A list of all matched paths.
