import sys

rr = None
try:
  xrange( 0 )
  rr = xrange
except:
  rr = range

class Gadget:

  def __init__( self, func ):
    self.func = func

    self.fields = self.gogoNames()

  def gogoNames( self ):
    if( sys.hexversion >= 0x03000000 ):
      return self.func.__code__.co_varnames
    else:
      return self.func.func_code.co_varnames

  def gogoIndexes( self ):
    if( sys.hexversion >= 0x03000000 ):
      return rr( self.func.__code__.co_argcount )
    else:
      return rr( self.func.func_code.co_argcount )

  def gogoMap( self ):
    names = self.gogoNames()
    indexes = self.gogoIndexes()

    ret = {}

    for i in indexes:
      ret[names[i]] = i

    return ret
