
name = "None"

class Stage( object ):
  def __init__( self ):
    pass

class Development( Stage ):
  def __init__( self ):
    global name
    super( Development, self ).__init__()
    name = "Dev"

class Production( Stage ):
  def __init__( self ):
    global name
    super( Production, self ).__init__()
    name = "Prod"

stage = Development()

print name
