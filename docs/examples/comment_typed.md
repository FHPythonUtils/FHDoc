# Comment Typed

> Auto-generated documentation for [examples.comment_typed](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py) module.

- [Handsdown](../README.md#-handsdown---python-documentation-generator) / [Modules](../MODULES.md#modules) / [Examples](index.md#examples) / Comment Typed
  - [MyValue](#myvalue)
  - [Typed](#typed)
    - [Typed.classmethod](#typedclassmethod)
  - [func](#func)
  - [func_any](#func_any)

## MyValue

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L4)

```python
class MyValue():
```

## Typed

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L8)

```python
class Typed():
    def __init__(
        _value: Union[List[Text], Text, MyValue] = MyValue(),
        _name: Text = 'default',
    ) -> Dict[Text, MyValue]:
```

#### See also

- [Typed](#typed)

### Typed.classmethod

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L17)

```python
@classmethod
def classmethod(_my_value: Any, *_args: Text, **_kwargs: MyValue) -> Typed:
```

#### See also

- [Typed.classmethod](#typedclassmethod)

## func

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L23)

```python
def func(
    _list: None,
    _my_value_cls: Type[MyValue] = MyValue,
    **_kwargs: Tuple[List[Text], ...],
) -> Any:
```

#### See also

- [func](#func)

## func_any

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/examples/comment_typed.py#L28)

```python
def func_any(
    _list: None,
    _my_value_cls: Any = MyValue,
    **_kwargs: Tuple[List[Text], ...],
) -> Any:
```

#### See also

- [func_any](#func_any)
