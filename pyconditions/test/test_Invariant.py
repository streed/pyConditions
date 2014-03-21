import unittest

from ..invariant import Invariant, NoopInvariant, InvariantMeta

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
