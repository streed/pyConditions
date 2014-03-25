import unittest

from ..exceptions import PyCondition, PyConditionError
from ..invariant import *

class TestInvariant( unittest.TestCase ):

  def test_Invariant_properly_sets_metaclass_and_invariant_list( self ):
    @NoopInvariant()
    @NoopInvariant()
    class Test( object ):
      pass

    self.assertTrue( len( Test.__invariant__ ) == 2 )

  def test_Invariant_properly_wraps_each_method( self ):
    @NoopInvariant()
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
    @FieldsNotNone( [ "test", "test2" ] )
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

  def test_CustomInvariant( self ):
    def invariant( self ):
      return self.test == 1

    @CustomInvariant( "test", invariant )
    class Test( object ):
      def __init__( self ):
        self.test = 1

      def test2( self ):
        self.test = 2

    t = Test()

    self.assertRaises( PyCondition, t.test2 )

  def test_Invariant_cannot_be_applied_to_non_classes( self ):
    def test():
      @FieldsNotNone( [ "test" ] )
      def testing():
        pass

    self.assertRaises( PyConditionError, test )
