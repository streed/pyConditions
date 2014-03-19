
class Gadget:

  def __init__( self, func ):
    self.func = func

    self.fields = self.gogoNames()

  def gogoNames( self ):
    return self.func.func_code.co_varnames

  def gogoIndexes( self ):
    return xrange( self.func.func_code.co_argcount )

  def gogoMap( self ):
    names = self.gogoNames()
    indexes = self.gogoIndexes()

    ret = {}

    for i in indexes:
      ret[names[i]] = i

    return ret
