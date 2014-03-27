pyConditions 
===========================

|Build Status|

Commenting sucks so let your code do it for you with preconditions that
actually do something.

Examples:

.. code:: python

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

The documenting is there with the code it self, and if you violate the
preconditions then a *PyCondition* exception is thrown with a much nicer
error message than broken code.

.. code:: python

    evenOdd( 3, 1 )

::

    pyconditions.exceptions.PyCondition: 3 did not pass the custom condition for parameter 'a' in function evenOdd

How about some postconditions?

.. code:: python

    from pyconditions.post import *

    @NotNone()
    def test( a ):
      return a

    @Custom( lambda a: a % 2 == 0 )
    def even( a ):
      return a

.. code:: python

    test( None )

::

    pyconditions.exception.PyCondition: The return value for uber.awesome.project.test was None 

You can also mix the two as well.

.. code:: python

    from pyconditions import pre
    from pyconditions import post

    @pre.Custom( "a", lamda a: a % 2 == 0 )
    @post.Custom( lambda a: a % 2 == 0 )
    def superSafeEven( a ):
      return a

Want some class invariant shenanigans?

.. code:: python

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

That last call to *add* will cause the invariant to fail and thus throw
the following:

::

    pyconditions.exceptions.PyCondition: Field "test" was None when it should not have been in invariant "notNone"

Need a custom invariant?

.. code:: python

    from pyconditions.invariant import CustomInvariant
    def invariant( self ):
       return self.test == 1 

    @CustomInvariant( "test", invariant )
    class Test( object ):
       def __init__( self ):
               self.test = 1
       def method1( self ):
               self.test

This is great but the conditions slow my code down a lot? No problem.

.. code:: python

    from pyconditions.stage import Stage

    stage = Stage()
    stage.prod()

Just set that somewhere in your code and you’ll be fine. There is still
some overhead, mainly there will be two function calls for each method,
the wrapper and the original function. But, for stacked Preconditions
and Invariants it will not execute into the other conditions and
invraiants when *prod* is called. If you want to go back to *Dev* then
call *dev()*.

Have conditions you want added? Open a PR with code.

Have an issue? Open a PR with fixed code.

.. |Build Status| image:: https://travis-ci.org/streed/pyConditions.png?branch=master
   :target: https://travis-ci.org/streed/pyConditions
