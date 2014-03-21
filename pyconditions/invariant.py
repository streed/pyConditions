from functools import wraps

def wrap_method( func ):
  @wraps( func )
  def wrapper( *args, **kwargs ):
    ret = func( *args, **kwargs )

    for invariant in args[0].__invariant__:
      if( not invariant.assertInvariant( args[0] ) ):
        raise PyCondition( "Invariant %s did not hold for %s" % ( invariant.name, args[0] ) )

    return ret

  wrapper.is_wrapped = True

  return wrapper

class InvariantMeta( type, object ):
  def __new__(cls, name, bases, attrs):
    for a in attrs:
      if( a != "__metaclass__" and hasattr( attrs[a], "__call__" ) ):
        attrs[a] = wrap_method( attrs[a] )

    return super( InvariantMeta, cls).__new__( cls, name, bases, attrs)

class Invariant( object ):
  def __init__( self, name ):
    self.name = name
    self.condition = lambda a: True

  def __call__( self, klass ):
    dct = dict( klass.__dict__ )

    if( not hasattr( klass, "__invariant__" ) ):
      dct["__invariant__"] = []
    dct["__invariant__"].append( self )

    t = InvariantMeta( klass.__name__, klass.__bases__, dct )

    return t

class NoopInvariant( Invariant ):
  def __init__( self, name ):
    super( NoopInvariant, self ).__init__( name )

    self.condition = lambda a: True

  def assertInvariant( self, s ):
    return True
