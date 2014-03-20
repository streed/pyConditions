pyConditions [![Build Status](https://travis-ci.org/streed/pyConditions.png?branch=master)](https://travis-ci.org/streed/pyConditions)
============

Commenting sucks so let your code do it for you with preconditions that actually do something.

Examples:

```python
@Between( "b", 1, 10 )
def divideAbyB( a, b )
  return a / b

@NotNone( "a" )
@Between( "a", "a", "n" )
@NotNone( "b" )
@Between( "b", "n", "z" )
def concat( a, b ):
  return a + b
  
@Custom( "a", lambda x: x % 2 == 0 )
@Custom( "b", lambda x: not x % == 0 )
def evenOdd( a, b ):
  return a * b
```

The documenting is there with the code it self, and if you violate the preconditions then a
_PyCondition_ exception is thrown with a much nicer error message than broken code.


Have conditions you want added? Open a PR with code.
Have an issue? Open a PR with fixed code.
