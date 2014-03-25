
class Stage( object ):
  name = "None"
  def __init__( self ):
    pass

class Development( Stage ):
  def __init__( self ):
    super( Development, self ).__init__()
    Development.name = "Dev"

class Production( Stage ):
  def __init__( self ):
    super( Production, self ).__init__()
    Production.name = "Prod"

stage = Development()
