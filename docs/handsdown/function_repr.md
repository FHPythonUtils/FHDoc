# FunctionRepr

> Auto-generated documentation for [handsdown.function_repr](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py) module.

- [Index](../README.md#modules) / [Handsdown](index.md#handsdown) / FunctionRepr
  - [ClassRepr](#classrepr)
  - [DefaultValueData](#defaultvaluedata)
    - [DefaultValueData().get_class_names](#defaultvaluedataget_class_names)
    - [DefaultValueData().render](#defaultvaluedatarender)
  - [FunctionData](#functiondata)
    - [FunctionData().render](#functiondatarender)
  - [FunctionRepr](#functionrepr)
    - [FunctionRepr().get_defaults](#functionreprget_defaults)
    - [FunctionRepr().get_type_hints](#functionreprget_type_hints)
    - [FunctionRepr().render](#functionreprrender)
  - [ParameterData](#parameterdata)
    - [ParameterData().render](#parameterdatarender)
  - [TypeHintData](#typehintdata)
    - [TypeHintData().get_class_names](#typehintdataget_class_names)
    - [TypeHintData().render](#typehintdatarender)

## ClassRepr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L321)

```python
class ClassRepr(inspect_class: Any) -> None
```

## DefaultValueData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L53)

```python
class DefaultValueData(value: Any) -> None
```

### DefaultValueData().get_class_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L77)

```python
def get_class_names() -> List[Text]
```

### DefaultValueData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L60)

```python
def render() -> Text
```

## FunctionData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L123)

```python
class FunctionData(name: Text) -> None
```

### FunctionData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L131)

```python
def render(multi_line: bool = False) -> Text
```

## FunctionRepr

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L151)

```python
class FunctionRepr(func: Any) -> None
```

### FunctionRepr().get_defaults

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L283)

```python
def get_defaults() -> Dict[Text, DefaultValueData]
```

### FunctionRepr().get_type_hints

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L275)

```python
def get_type_hints() -> Dict[Text, TypeHintData]
```

### FunctionRepr().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L305)

```python
def render() -> Text
```

## ParameterData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L96)

```python
class ParameterData(name: Text) -> None
```

### ParameterData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L105)

```python
def render() -> Text
```

## TypeHintData

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L11)

```python
class TypeHintData(type_hint: Any) -> None
```

### TypeHintData().get_class_names

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L34)

```python
def get_class_names() -> List[Text]
```

### TypeHintData().render

[🔍 find in source code](https://github.com/vemel/handsdown/blob/master/handsdown/function_repr.py#L18)

```python
def render() -> Text
```
