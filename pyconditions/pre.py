from functools import wraps
from .inspector import  Gadget
from .exceptions import PyCondition

class Pre( object ):
  """
    Pre is simply a constructor of the decorators but it is also
    the context itself. Only one context is required per file.

    TODO: Remove the need to create this at all. Maybe key __file__.<func_name>?
  """
  def __init__( self ):
    self.funcTable = {}

class PreCondition( object ):
  context = Pre()
  def __init__( self, name ):
    self.name = name

  def _map( self, func ):
    try:
      func = func._original_func
    except:
      pass
    gadget = Gadget( func )
    m = gadget.gogoMap()
    params = [ ( i, v ) for v, i in m.items() ]
    params.sort( key=lambda a: a[0] )
    params = [ v[1] for v in params ]
    name = ( func.__module__, func.__name__, "( %s )" % ",".join( params ) )
    self.funcName = "%s.%s%s" % name

    if( name in self.context.funcTable ):
      self.argMap = PreCondition.context.funcTable[name]
    else:
      gadget = Gadget( func )
      self.argMap = gadget.gogoMap()

      PreCondition.context.funcTable[name] = self.argMap

  def assertCondition( self, *args, **kwargs ):
    pass

  def __call__( self, func ):
    self._map( func )
    
    @wraps( func )
    def wrapper( *args, **kwargs ):
      self.assertCondition( *args, **kwargs )
      return func( *args, **kwargs )

    wrapper._original_func = func

    return wrapper

class NotNone( PreCondition ):

  def __init__( self, name ):
    super( NotNone, self ).__init__( name )
    self.name = name

  def assertCondition( self, *args, **kwargs ):
      if( args[self.argMap[self.name]] == None ):
        raise PyCondition( "%s is None in %s" % ( self.name, self.funcName ) )

class Between( PreCondition ):
  def __init__( self, name, lower, upper ):
    super( Between, self ).__init__(  name )
    self.lower = lower
    self.upper = upper

  def assertCondition( self, *args, **kwargs ):
    v = args[self.argMap[self.name]]

    if( not ( self.lower <= v <= self.upper ) ):
      raise PyCondition( "%s <= %s <= %s did not hold in %s" % ( self.lower, v, self.upper, self.name ) )

class GreaterThan( PreCondition ):
  def __init__( self, name, lower ):
    super( GreaterThan, self ).__init__( name )
    self.lower = lower

  def assertCondition( self, *args, **kwargs ):
    v = args[self.argMap[self.name]]

    if( not ( self.lower < v ) ):
      raise PyCondition( "%s < %s did not hold in %s" % ( self.lower, v, self.name ) )

class LessThan( PreCondition ):
  def __init__( self, name, upper ):
    super( LessThan, self ).__init__( name )
    self.upper = upper

  def assertCondition( self, *args, **kwargs ):
    v = args[self.argMap[self.name]]

    if( not ( self.upper > v ) ):
      raise PyCondition( "%s > %s did not hold %s" % ( self.upper, v, self.name ) )

class Custom( PreCondition ):
  def __init__( self, name, check ):
    super( Custom, self ).__init__( name ) 
    self.check = check

  def assertCondition( self, *args, **kwargs ):
    v = args[self.argMap[self.name]]

    if( not self.check( v ) ):
      raise PyCondition( "%s did not pass the custom condition in %s" % ( v, self.name ) )

class Instance( PreCondition ):
  def __init__( self, name, klass ):
    super( Instance, self ).__init__( name )
    self.klass = klass

  def assertCondition( self, *args, **kwargs ):
    v = args[self.argMap[self.name]]

    if( not isinstance( v, self.klass ) ):
      raise PyCondition( "%s is not a %s in %s" % ( v, self.klass, self.name ) )

