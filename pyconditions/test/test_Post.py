import unittest

from ..post import *
from ..exceptions import PyCondition

class TestPost( unittest.TestCase ):

  def test_NotNone( self ):

    @NotNone()
    def test():
      return None

    self.assertRaises( PyCondition, test )

  def test_Custom( self ):

    @Custom( lambda a: a % 2 == 0 )
    def even( a ):
      return a

    self.assertRaises( PyCondition, even, 3 )
    self.assertEquals( 2, even( 2 ) )

  def test_NotEmpty( self ):

    @NotEmpty()
    def empty( a ):
      return a

    self.assertRaises( PyCondition, empty, [] )
    self.assertEquals( [ 1 ], empty( [ 1 ] ) )

  def test_decorators_stacked( self ):
    
    @Custom( lambda a: a[0] == 2 )
    @NotEmpty()
    def stacked( a ):
      return a

    self.assertRaises( PyCondition, stacked, [] )
    self.assertRaises( PyCondition, stacked, [ 3 ] )
    self.assertEquals( [ 2 ], stacked( [ 2 ] ) )
