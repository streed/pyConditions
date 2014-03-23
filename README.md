pyConditions [![Build Status](https://travis-ci.org/streed/pyConditions.png?branch=master)](https://travis-ci.org/streed/pyConditions)
============

Commenting sucks so let your code do it for you with preconditions that actually do something.

Examples:

```python
from pyconditions.pre import *

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
@Custom( "b", lambda x: not x % 2 == 0 )
def evenOdd( a, b ):
  return a * b
```

The documenting is there with the code it self, and if you violate the preconditions then a
_PyCondition_ exception is thrown with a much nicer error message than broken code.

```python
evenOdd( 3, 1 )
```

    pyconditions.exceptions.PyCondition: 3 did not pass the custom condition for parameter 'a' in function evenOdd

How about some postconditions?

```python
from pyconditions.post import *

@NotNone()
def test( a ):
  return a

@Custom( lambda a: a % 2 == 0 )
def even( a ):
  return a
```

```python
test( None )
```

    pyconditions.exception.PyCondition: The return value for uber.awesome.project.test was None 

You can also mix the two as well.

```python
from pyconditions import pre
from pyconditions import post

@pre.Custom( "a", lamda a: a % 2 == 0 )
@post.Custom( lambda a: a % 2 == 0 )
def superSafeEven( a ):
  return a
```

Want some class invariant shenanigans?

```python
from pyconditions.invariant import Invariant, FieldsNotNone
@FieldsNotNone( [ "test" ] )
class Test:
    def __init__( self ):
            self.test = 1
    def add( self ):
            return self.test + 1
    def set( self, v ):
            self.test = v

t = Test()
print t.add()
t.set( None )
```

That last call to _add_ will cause the invariant to fail and thus throw the following:

    pyconditions.exceptions.PyCondition: Field "test" was None when it should not have been in invariant "notNone"
    
Need a custom invariant? 

```python
from pyconditions.invariant import CustomInvariant
def invariant( self ):
   return self.test == 1 

@CustomInvariant( "test", invariant )
class Test( object ):
   def __init__( self ):
           self.test = 1
   def method1( self ):
           self.test
```

Have conditions you want added? Open a PR with code.

Have an issue? Open a PR with fixed code.
