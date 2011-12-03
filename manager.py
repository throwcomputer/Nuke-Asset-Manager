import nukescripts
import nuke
import re
import os
from glob import glob
  
# DEFINE SHOT'S NUKE DIR
def nukeDir():
    nkDir = os.path.join( os.getenv('NKASSETS'), os.getenv('PROD'), os.getenv('SHOW'), 'scene' + os.getenv('SCENE'), 'shot' + os.getenv('SHOT'), 'nuke' )
    if not os.path.isdir( nkDir ):
		os.makedirs( nkDir )
    return nkDir
	
# DEFINE EASY SAVE
def easySave():
    nkDir = nukeDir()
    # GET DESCRIPTION FROM USER BUT STRIP ALL WHITE SPACES - EASYSAVE
    description = nuke.getInput( 'script description: ', 'init comp' ).replace( ' ', '')
    
    fileSaved = False
    version = 1
    while not fileSaved:
		# CONSTRUCT FILENAME
		t = os.getenv('SHOW')
		t = str(t)
		t = t.replace(' ', '')
		nkName = '%s_%s_%s_%s_v%02d.nk' % ( t, 'scene' + os.getenv('SCENE'), 'shot' + os.getenv('SHOT'), description, version )
		# JOIN DIRECTORY AND NAME TO FORM FULL FILE PATH
		nkPath = os.path.join( nkDir, nkName )
		# IF FILE EXISTS VERSION UP
		if os.path.isfile( nkPath ):
		    version += 1
		    continue
		# SAVE NUKE SCRIPT
		nuke.scriptSaveAs( nkPath )
		fileSaved = True
    return nkPath

# ADD EASY SAVE TO SHOT MENU								    
shotMenu = '%s - %s' % ( os.getenv('SCENE'), os.getenv('SHOT') )
nuke.menu( 'Nuke' ).addCommand( shotMenu+'/Easy Save', easySave, 'Ctrl+S' )
nuke.menu('Nuke').addCommand( shotMenu+'/Write Assets', 'nuke.createNode("WriteAssets")', 'W', icon='Write.png')

# REQUIRE VERSIONING IN SCRIPT NAME
def checkScriptName():
    if not re.search( r'[vV]\d+', nuke.root().name() ):
		raise NameError, 'Please include a version number and save script again.'
nuke.addOnScriptSave( checkScriptName )

# GET ALL NUKE SCRIPTS FOR CURRENT SHOT
def getNukeScripts():
    nkFiles = glob( os.path.join( nukeDir(), '*.nk' ) )
    return nkFiles

# PANEL TO SHOW NUKE SCRIPTS FOR CURRENT SHOT
class NkPanel( nukescripts.PythonPanel ):
    def __init__( self, nkScripts ):
		nukescripts.PythonPanel.__init__( self, 'Open NUKE Script' )
		self.checkboxes = []
		self.nkScripts = nkScripts
		self.selectedScript = ''

		for i, n in enumerate( self.nkScripts ):
		    # PUT INDEX INTO KNOB NAMES SO WE CAN IDENTIFY THEM LATER
		    k = nuke.Boolean_Knob( 'nk_%s' % i, os.path.basename( n ) )
		    self.addKnob( k )
		    k.setFlag( nuke.STARTLINE )
		    self.checkboxes.append( k )

    def knobChanged( self, knob ):
		if knob in self.checkboxes:
		    # MAKE SURE ONLY ONE KNOB IS CHECKED
		    for cb in self.checkboxes:
				if knob == cb:
				    # EXTRACT THE INDEX FORM THE NAME AGAIN
				    index = int( knob.name().split('_')[-1] )
				    self.selectedScript = self.nkScripts[ index ]
				    continue
				cb.setValue( False )
		    
# HELPER FUNCTION FOR NUKE SCRIPT PANEL
def nkPanelHelper():
		# GET ALL NUKE SCRIPTS FOR CURRENT SHOT
		nkScripts = getNukeScripts()
		if not nkScripts:
				# IF THERE ARE NONE DON'T DO ANYTHING
				return
		# CREATE PANEL
		p = NkPanel( nkScripts )
		# ADJUST SIZE
		p.setMinimumSize( 200, 200 )

		# IF PANEL WAS CONFIRMED AND A NUKE SCRIPT WAS SELECTED, OPEN IT
		if p.showModalDialog():
				if p.selectedScript:
						nuke.scriptOpen( p.selectedScript )

# AUTO LOAD SCRIPT SELECTOR		    
nuke.addOnUserCreate( nkPanelHelper, nodeClass='Root')