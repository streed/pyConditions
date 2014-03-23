from functools import wraps

from .exceptions import PyCondition

def wrap_method( func ):
  @wraps( func )
  def wrapper( *args, **kwargs ):
    ret = func( *args, **kwargs )

    for invariant in args[0].__invariant__:
      invariant.assertInvariant( args[0] )

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
  def __init__( self ):
    self.condition = lambda a: True

  def __call__( self, klass ):
    self.name = "%s.%s" % ( klass.__module__, klass.__name__ )
    dct = dict( klass.__dict__ )

    if( not hasattr( klass, "__invariant__" ) ):
      dct["__invariant__"] = []
    dct["__invariant__"].append( self )

    t = InvariantMeta( klass.__name__, klass.__bases__, dct )

    return t

class NoopInvariant( Invariant ):
  def __init__( self ):
    super( NoopInvariant, self ).__init__()

    self.condition = lambda a: True

  def assertInvariant( self, s ):
    return True

class FieldsNotNone( Invariant ):
  def __init__( self, fields ):
    super( FieldsNotNone, self ).__init__()

    self.fields = fields
 
  def assertInvariant( self, s ):
    for f in self.fields:
      if( getattr( s, f ) == None ):
        raise PyCondition( "Field \"%s\" was None when it should not have been in invariant \"%s\"" % ( f, self.name ) )

class CustomInvariant( Invariant ):
  def __init__( self, name, condition ):
    super( CustomInvariant, self ).__init__()

    self.name = name
    self.condition = condition

  def assertInvariant( self, s ):
    if( not self.condition( s ) ):
      raise PyCondition( "The Custom invariant for \"%s\" did not hold." % self.name )

