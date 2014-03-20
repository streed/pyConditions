pyConditions [![Build Status](https://travis-ci.org/streed/pyConditions.png?branch=master)](https://travis-ci.org/streed/pyConditions)
============

Commenting sucks so let your code do it for you with preconditions that actually do something.

Examples:

```python
pre = Pre()
@pre.between( "b", 1, 10 )
def divideAbyB( a, b )

@pre.notNone( "a" )
@pre.between( "a", "a", "n" )
@pre.notNone( "b" )
@pre.between( "b", "n", "z" )
def concat( a, b ):
  return a + b
  
@pre.custom( "a", lambda x: x % 2 == 0 )
@pre.custom( "b", lambda x: not x % == 0 )
def evenOdd( a, b ):
  return a * b
```

The documenting is there with the code it self, and if you violate the preconditions then a
_PyCondition_ exception is thrown with a much nicer error message than broken code.


Have conditions you want added? Open a PR with code.
Have an issue? Open a PR with fixed code.
