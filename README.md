pyConditions
============

Guava like precondition enforcing for Python.

An Example:
```python
pre = Pre()
@pre.between( "b", 1, 10 )
def divideAbyB( a, b )
  return a / b
```

In the above example the precondition _pre.between_ ensures that the _b_ variable is between (1, 10) inclusive. If it is not then a _PyCondition_ exception is thrown with the error message detailing what went wrong.

More Examples:
```python
pre = Pre()

@pre.notNone( "a" )
@pre.between( "a", "a", "n" )
@pre.notNone( "b" )
@pre.between( "b", "n", "z" )
def concat( a, b ):
  return a + b
```

The above ensures that the variables _a_ and _b_ are never _None_ and that _a_ is between ( "a", "n" ) inclusively and _b_ is between ( "n", "z" ) inclusively.
