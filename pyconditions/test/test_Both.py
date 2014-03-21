import unittest

from ..pre import Custom as PreCustom
from ..post import Custom as PostCustom
from ..exceptions import PyCondition

class TestBoth( unittest.TestCase ):

  def test_both_pre_and_post( self ):
    @PreCustom( "a", lambda a: a[0] == 2 )
    @PostCustom( lambda a: a % 2 == 0 )
    def test( a ):
      return sum( a )

    self.assertRaises( PyCondition, test, [ 1 ] )
    self.assertRaises( PyCondition, test, [ 2, 3 ] )
    self.assertEquals( 2, test( [ 2 ] ) )
