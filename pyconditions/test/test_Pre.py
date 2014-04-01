import unittest

from ..pre import *
from ..exceptions import PyCondition

class TestPre( unittest.TestCase ):

  def test_NotNone_works_with_proper_value( self ):

    @NotNone( "a" )
    def test( a ):
      return a

    self.assertEquals( 1, test( 1 ) )

  def test_NotNone_works_with_multiple_arguements( self ):

    @NotNone( "a" )
    @NotNone( "b" )
    def test( a, b ):
      return a + b

    self.assertEquals( 2, test( 1, 1 ) )

  def test_NotNone_raises( self ):

    @NotNone( "a" )
    def test( a ):
      pass

    self.assertRaises( PyCondition, test, None )

  def test_Between_works_correctly( self ):


    @Between( "a", 0, 10 )
    def test( a, b ):
      pass

    self.assertRaises( PyCondition, test, -1 )
    self.assertRaises( PyCondition, test, 11 )

  def test_Between_multiple_decorators( self ):


    @Between( "a", "a", "z" )
    @Between( "b", 0, 5 )
    def test( b, a ):
      return "%s%d" % ( a, b )

    self.assertEquals( "n2", test( 2, "n" ) )

  def test_GreaterThan_works_correctly( self ):


    @GreaterThan( "b", 0 )
    def test( a, b ):
      return a / b

    self.assertRaises( PyCondition, test, 1, 0 ) 
    self.assertEquals( 1, test( 1, 1 ) )

  def test_LessThan_works_correctly( self ):

    @LessThan( "b", 0 )
    def test( a, b ):
      return a / b

    self.assertRaises( PyCondition, test, 1, 0 ) 
    self.assertEquals( -1, test( 1, -1 ) )

  def test_Custom_works( self ):


    @Custom( "a", lambda a: 0 <= a <= 10 )
    def test( a ):
      return a

    self.assertRaises( PyCondition, test, 11 )
    self.assertEquals( 5, test( 5 ) )

  def test_Instance_works( self ):


    @Instance( "a", int )
    def test( a ):
      return a

    self.assertRaises( PyCondition, test, "a" )
    self.assertEquals( 10, test( 10 ) )

  def test_decorators_work_on_classes( self ):
    class T:

      @NotNone( "a" )
      def __init__( self, a ):
        self.a = a

      @NotNone( "a" )
      def t( self, a ):
        return self.a * a

    t = T( 1 )

    t.t( 10 )

    self.assertRaises( PyCondition, T, None )
    self.assertRaises( PyCondition, t.t, None )
    self.assertEquals( 10, t.t( 10 ) )

