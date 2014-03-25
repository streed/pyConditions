from functools import wraps
from .exceptions import PyCondition, PyConditionError

from .stage import stage

class PostCondition( object ):
  def __call__( self, func ):
    if( stage.name == "Dev" ):
      self.name = "%s.%s" % ( func.__module__, func.__name__ )
      @wraps( func )
      def wrapper( *args, **kwargs ):
        returnValue = func( *args, **kwargs )
        self.assertCondition( returnValue )
        return returnValue
      wrapper._original_func = func
    elif( stage.name == "Prod" ):
      wrapper = func
    else:
      raise PyConditionError( "Invalid Stage: %s" % stage.name )

    return wrapper

  def assertCondition( self, returnValue ):
    pass

class NotNone( PostCondition ):
  def assertCondition( self, returnValue ):
    if( returnValue == None ):
      raise PyCondition( "The return value for %s was None" % self.name )

class Custom( PostCondition ):
  def __init__( self, custom ):
    self.custom = custom

  def assertCondition( self, returnValue ):
    if( not self.custom( returnValue ) ):
      raise PyCondition( "The custom condition did not hold for %s" % self.name )

class NotEmpty( PostCondition ):
  def assertCondition( self, returnValue ):
    if( len( returnValue ) == 0 ):
      raise PyCondition( "The return value was empty, meaning the length was 0 for %s" % self.name )
