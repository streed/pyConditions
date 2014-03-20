pyConditions |Build Status|
===========================

Guava like precondition enforcing for Python.

Has been tested against:

- 2.6
- 2.7
- 3.2
- 3.3
- pypy

Decorate functions with preconditions so that your code documents itself and at the same time
removes the boilerplate code that is typically required when checking parameters.

An Example:

.. code:: python

  def divideAby1or10( a, b ):
      if not ( 1 <= b <= 10 ):
          <raise some error>
      else:
          return a / b

Simply becomes the following:

.. code:: python

  from pyconditions.pre import Pre
  pre = Pre()

  @pre.between( "b", 1, 10 )
  def divideAbyB( a, b )
    return a / b

In the above example the precondition *pre.between* ensures that the *b*
variable is between (1, 10) inclusive. If it is not then a *PyCondition*
exception is thrown with the error message detailing what went wrong.

More Examples:

.. code:: python

  from pyconditions.pre import Pre
  pre = Pre()

  @pre.notNone( "a" )
  @pre.between( "a", "a", "n" )
  @pre.notNone( "b" )
  @pre.between( "b", "n", "z" )
  def concat( a, b ):
    return a + b

The above ensures that the variables *a* and *b* are never *None* and
that *a* is between ( ?a?, ?n? ) inclusively and *b* is between ( ?n?,
?z? ) inclusively.

.. code:: python

    from pyconditions.pre import Pre
    pre = Pre()

    BASES = [ 2, 3, 4 ]

    @pre.custom( a, lambda x: x in BASES )
    @pre.custom( b, lambda x: x % 2 == 0 )
    def weirdMethod( a, b ):
        return a ** b

Using the custom precondition you are able to pass in any function that receives a single parameter and perform whatever condition checking you need.

.. |Build Status| image:: https://travis-ci.org/streed/pyConditions.png?branch=master :target: https://travis-ci.org/streed/pyConditions