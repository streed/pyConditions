import unittest

from ..invariant import Invariant, NoopInvariant, InvariantMeta

class TestInvariant( unittest.TestCase ):

  def test_Invariant_properly_sets_metaclass_and_invariant_list( self ):
    @NoopInvariant( "test" )
    @NoopInvariant( "test2" )
    class Test( object ):
      pass

    self.assertEquals( InvariantMeta, Test.__metaclass__ )
    self.assertEquals( [ "test2", "test" ], [ i.name for i in Test.__invariant__ ] )

  def test_Invariant_properly_wraps_each_method( self ):
    @NoopInvariant( "test" )
    class Test( object ):
      def test( self ):
        pass

    t = Test()

    t.test()
