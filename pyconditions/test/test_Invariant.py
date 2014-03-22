import unittest

from ..exceptions import PyCondition
from ..invariant import Invariant, NoopInvariant, FieldsNotNone, InvariantMeta

class TestInvariant( unittest.TestCase ):

  def test_Invariant_properly_sets_metaclass_and_invariant_list( self ):
    @NoopInvariant( "test" )
    @NoopInvariant( "test2" )
    class Test( object ):
      pass

    self.assertEquals( [ "test2", "test" ], [ i.name for i in Test.__invariant__ ] )

  def test_Invariant_properly_wraps_each_method( self ):
    @NoopInvariant( "test" )
    class Test( object ):
      def test( self ):
        pass

      def test2( self ):
        pass

      def testing( self, a, b ):
        pass

    t = Test()
  
    self.assertTrue( t.test.is_wrapped )
    self.assertTrue( t.test2.is_wrapped )
    self.assertTrue( t.testing.is_wrapped )

  def test_FieldsNotNone( self ):
    @FieldsNotNone( "notNone", [ "test", "test2" ] )
    class Test( object ):
      def __init__( self ):
        self.test = 1
        self.test2 = 2

      def test3( self ):
        pass

    t = Test()
    t.test = None

    self.assertRaises( PyCondition, t.test3 )

    t.test = 1
    t.test2 = None

    self.assertRaises( PyCondition, t.test3 )
