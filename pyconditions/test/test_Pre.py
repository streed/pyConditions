import unittest

from ..pre import *
from ..exceptions import PyCondition

class TestPre( unittest.TestCase ):

  def test_notNone_works_with_proper_value( self ):
    pre = Pre()
    @pre.notNone( "a" )
    def test( a ):
      return a

    self.assertEquals( 1, test( 1 ) )

  def test_notNone_works_with_multiple_arguements( self ):
    pre = Pre()

    @pre.notNone( "a" )
    @pre.notNone( "b" )
    def test( a, b ):
      return a + b

    self.assertEquals( 2, test( 1, 1 ) )

  def test_notNone_raises( self ):
    pre = Pre()

    @pre.notNone( "a" )
    def test( a ):
      pass

    self.assertRaises( PyCondition, test, None )

  def test_between_works_correctly( self ):
    pre = Pre()

    @pre.between( "a", 0, 10 )
    def test( a ):
      pass

    self.assertRaises( PyCondition, test, -1 )
    self.assertRaises( PyCondition, test, 11 )

  def test_between_multiple_decorators( self ):
    pre = Pre()

    @pre.between( "a", "a", "z" )
    @pre.between( "b", 0, 5 )
    def test( a, b ):
      return "%s%d" % ( a, b )

    self.assertEquals( "n2", test( "n", 2 ) )

  def test_greaterThan_works_correctly( self ):
    pre = Pre()

    @pre.greaterThan( "b", 0 )
    def test( a, b ):
      return a / b

    self.assertRaises( PyCondition, test, 1, 0 ) 
    self.assertEquals( 1, test( 1, 1 ) )

  def test_lessThan_works_correctly( self ):
    pre = Pre()

    @pre.lessThan( "b", 0 )
    def test( a, b ):
      return a / b

    self.assertRaises( PyCondition, test, 1, 0 ) 
    self.assertEquals( -1, test( 1, -1 ) )

  def test_custom_works( self ):
    pre = Pre()

    @pre.custom( "a", lambda a: 0 <= a <= 10 )
    def test( a ):
      return a

    self.assertRaises( PyCondition, test, 11 )
    self.assertEquals( 5, test( 5 ) )

  def test_instance_works( self ):
    pre = Pre()

    @pre.instance( "a", int )
    def test( a ):
      return a

    self.assertRaises( PyCondition, test, "a" )
    self.assertEquals( 10, test( 10 ) )
