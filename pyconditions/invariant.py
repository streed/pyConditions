import inspect
from functools import wraps

from .exceptions import PyCondition, PyConditionError

from .stage import Stage

def wrap_method( func ):
  stage = Stage()
  """
    Wraps a method so that each invariant is called with the 
    self argument.
  """
  @wraps( func )
  def wrapper( *args, **kwargs ):
    ret = func( *args, **kwargs )

    if( stage.name == "Dev" ):
      for invariant in args[0].__invariant__:
        invariant.assertInvariant( args[0] )

    return ret

  wrapper.is_wrapped = True

  return wrapper

class InvariantMeta( type, object ):
  """
    Used to wrap each method in a class.
    It returns the newly created class to be created 
    before it is added to a class as an invariant.
  """
  def __new__(cls, name, bases, attrs):
    for a in attrs:
      if( a != "__metaclass__" and hasattr( attrs[a], "__call__" ) ):
        attrs[a] = wrap_method( attrs[a] )

    return super( InvariantMeta, cls).__new__( cls, name, bases, attrs)

class Invariant( object ):
  """
    This creates a new class that is passed through the InvariantMeta class.
  """
  def __init__( self ):
    self.condition = lambda a: True

  def __call__( self, klass ):
    """
      Ensures that the invriant is applied to only classes.
      Sets the name of the invariant to the class, can be override.
      Add's this invariant to the __invariant__ variable.
    """
    if( not inspect.isclass( klass ) ):
      raise PyConditionError( "Can only put invariant's on classes." )
    self.name = "%s.%s" % ( klass.__module__, klass.__name__ )
    dct = dict( klass.__dict__ )

    if( not hasattr( klass, "__invariant__" ) ):
      dct["__invariant__"] = []
    dct["__invariant__"].append( self )

    t = InvariantMeta( klass.__name__, klass.__bases__, dct )

    return t

class NoopInvariant( Invariant ):
  """
    Does nothing, just returns true.
  """
  def __init__( self ):
    super( NoopInvariant, self ).__init__()

    self.condition = lambda a: True

  def assertInvariant( self, s ):
    return True

class FieldsNotNone( Invariant ):
  """
    Given the fields passed into this invriant they are ensured to be not None
    after each method is called.
  """
  def __init__( self, fields ):
    super( FieldsNotNone, self ).__init__()

    self.fields = fields
 
  def assertInvariant( self, s ):
    for f in self.fields:
      if( getattr( s, f ) == None ):
        raise PyCondition( "Field \"%s\" was None when it should not have been in invariant \"%s\"" % ( f, self.name ) )

class CustomInvariant( Invariant ):
  """
    Allows for a custom method to be passed. The method that is passed must take
    one parameter.
  """
  def __init__( self, name, condition ):
    super( CustomInvariant, self ).__init__()

    self.name = name
    self.condition = condition

  def assertInvariant( self, s ):
    if( not self.condition( s ) ):
      raise PyCondition( "The Custom invariant for \"%s\" did not hold." % self.name )

