from functools import wraps
from .inspector import  Gadget
from .exceptions import PyCondition

class Pre( object ):
  def __init__( self ):
    self.funcTable = {}

  def notNone( self, name ):
    return notNone( self, name )

  def between( self, name, lower, upper ):
    return between( self, name, lower, upper )

class PreCondition( object ):
  def __init__( self, context, name ):
    self.context = context
    self.name = name

  def _map( self, func ):
    if( func.__name__ in self.context.funcTable ):
      self.argMap = self.context.funcTable[func.__name__]
    else:
      self.funcName = func.__name__
      self.gadget = Gadget( func )
      self.argMap = self.gadget.gogoMap()

      self.context.funcTable[func.__name__] = self.argMap

  def assertCondition( self, *args, **kwargs ):
    pass

  def __call__( self, func ):
    self._map( func )
    
    @wraps( func )
    def wrapper( *args, **kwargs ):
      self.assertCondition( *args, **kwargs )
      return func( *args, **kwargs )

    wrapper.func = func

    return wrapper

class notNone( PreCondition ):

  def __init__( self, context, name ):
    super( notNone, self ).__init__( context, name )
    self.name = name

  def assertCondition( self, *args, **kwargs ):
      if( args[self.argMap[self.name]] == None ):
        raise PyCondition( "%s is None in %s" % ( self.name, self.funcName ) )

class between( PreCondition ):
  def __init__( self, context, name, lower, upper ):
    super( between, self ).__init__(  context, name )
    self.lower = lower
    self.upper = upper

  def assertCondition( self, *args, **kwargs ):
    v = args[self.argMap[self.name]]

    if( not ( self.lower <= v <= self.upper ) ):
      raise PyCondition( "%s <= %s <= %s did not hold." % ( self.lower, v, self.upper ) )

