import sys

rr = None
try:
  xrange( 0 )
  rr = xrange
except:
  rr = range

class Gadget:
  """
    A Gadget is a utility class that is used to gather the information
    to perform the conditional checks on specific parameters.
  """

  def __init__( self, func ):
    self.func = func

    self._varnames = None
    self._argcounts = None
    self._map = None
    self.name = func.__name__
    self.module = func.__module__

  def gogoNames( self ):
    """
      This will return the names of the parameters. But, because in 
      python > 3.* the attribute of the function changed from
      func_code to __code__ the version check is required.
    """
    if( not self._varnames ):
      if( sys.hexversion >= 0x03000000 ):
        self._varnames = self.func.__code__.co_varnames
      else:
        self._varnames = self.func.func_code.co_varnames

    return self._varnames

  def gogoIndexes( self ):
    """
      This will return the indexes of the parameters which can be used 
      to get the values themselves. The system version needs to be checked
      because of the change from func_code to __code__.
    """
    if( not self._argcounts ):
      if( sys.hexversion >= 0x03000000 ):
        self._argcounts = rr( self.func.__code__.co_argcount )
      else:
        self._argcounts = rr( self.func.func_code.co_argcount )

    return self._argcounts

  def gogoMap( self ):
    """
      Used to build up a dict that maps parameter name to 
      it's associated index.
    """
    if( not self._map ):
      names = self.gogoNames()
      indexes = self.gogoIndexes()

      ret = {}

      for i in indexes:
        ret[names[i]] = i

      self._map = ret
    
    return self._map

  def gogoDoc( self ):
    return self.func.__doc__
