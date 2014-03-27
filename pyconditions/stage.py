class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
    if cls not in cls._instances:
      cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
    return cls._instances[cls]

_STAGE = Singleton( "_STAGE", ( object, ), {} )

class Stage( _STAGE ):
  def __init__( self ):
    self._name = "Dev"

  @property
  def name( self ):
    return self._name

  def prod( self ):
    self._name = "Prod"

  def dev( self ):
    self._name = "Dev"


