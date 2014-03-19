import unittest

from ..inspector import Gadget

def f( test, test2 ):
  pass

class TestGadget( unittest.TestCase ):

  def test_Gadget_retreives_the_parameter_names( self ):

    gadget = Gadget( f )

    self.assertEquals( ( "test", "test2", ), gadget.gogoNames() )

  def test_Gadget_maps_the_name_to_its_index( self ):
    gadget = Gadget( f )

    self.assertEquals( { "test": 0, "test2": 1 }, gadget.gogoMap() )
