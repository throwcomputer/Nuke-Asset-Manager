
# CREATE DIRS ON RENDER IF NOT EXISTANT
def createOutDirs():
    trgDir = os.path.dirname( nuke.filename( nuke.thisNode() ) )
    if not os.path.isdir( trgDir ):
        os.makedirs( trgDir )
		
# GLOBAL CALLBACK ON RENDER TO CHECK/MAKE DIRS IF NOT EXISTANT
nuke.addBeforeRender( createOutDirs, nodeClass='Write' )
nuke.load('environment.py')