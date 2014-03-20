pyConditions |Build Status|
===========================

Guava like precondition enforcing for Python.

An Example:

.. code:: python

  pre = Pre()

  @pre.between( "b", 1, 10 )
  def divideAbyB( a, b )
    return a / b

In the above example the precondition *pre.between* ensures that the *b*
variable is between (1, 10) inclusive. If it is not then a *PyCondition*
exception is thrown with the error message detailing what went wrong.

More Examples:

.. code:: python

  pre = Pre()

  @pre.notNone( "a" )
  @pre.between( "a", "a", "n" )
  @pre.notNone( "b" )
  @pre.between( "b", "n", "z" )
  def concat( a, b ):
   return a + b

The above ensures that the variables *a* and *b* are never *None* and
that *a* is between ( “a”, “n” ) inclusively and *b* is between ( “n”,
“z” ) inclusively.

.. |Build Status| image:: https://travis-ci.org/streed/pyConditions.png?branch=master
  :target: https://travis-ci.org/streed/pyConditions
