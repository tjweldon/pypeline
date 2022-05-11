# Pypeline

## Installing

Copy the damn code, it's less than 20 lines!

## Usage

### Importing

```python
from pypeline import x
```

### Constructing Value Pipelines

This class allows function pipelining (see the example below).
Functions are evaluated ltr bash style (hence the syntax).

Constructing with a value i.e. x(10) means that the callable 
returned by the pipeline takes no arguments:

```python
from pypeline import x

f = x(10) | lambda y: y - 1 | str

print(f())
# '9'
```
It can be evaluated by terminating it with an ellipsis:
 
```python
from pypeline import x

f1 = lambda y: (y+98, y+101, y+98)
f2 = lambda y: [chr(el) for el in y]

result = x(10) | f1 | f2 | "".join | ...

print(result)
# 'lol'
```

### Constructing Function Pipelines

Constructing with x(...) means evaluation is deferred, and returns a 
function of one parameter:

```python
from pypeline import x

f = x(...) | lambda y: y - 1 | str

print(f(43))
# '42'
```

Similar to the non-deferred case above, these expressions can be 
evaluated inline by terminating the pipeline with the parameter:

```python
from pypeline import x

f1 = lambda y: (y+98, y+101, y+98)
f2 = lambda y: [chr(el) for el in y]

result = x(...) | f1 | f2 | "".join | 10

print(result)
# 'lol'
```
