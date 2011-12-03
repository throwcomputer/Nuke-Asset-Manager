import os

# retrieve directory plugin is running from and prepare env file to store ENV
plugin_directory = ''.join(nuke.plugins(0, 'manager.py'))
plugin_directory = os.path.normpath(plugin_directory)
plugin_directory = os.path.split(plugin_directory)[0]
environment_filename = os.path.join(plugin_directory, 'environment.py')
init_filename = os.path.join(plugin_directory, 'init.py')

# Check to see if ENV set already
env_check = os.environ.get('NKASSETS')

#Create Asset Management and Shot Selection Panel
myPanel = nuke.Panel("Asset Manager - Setup")
myPanel.setWidth(300)
if not env_check:
	myPanel.addFilenameSearch("Asset Directory: ", "")
	# print 'not set'
myPanel.addSingleLineInput("production company: ", "")
myPanel.addSingleLineInput("show: ", "")
myPanel.addSingleLineInput("scene: ", "")
myPanel.addSingleLineInput("shot: ", "")

# Open Panel
if myPanel.show():
    # Execute if panel completed.
	if not env_check:
		amd = myPanel.value("Asset Directory: ")
		os.environ['NKASSETS'] = amd
		# Saves ENV to file
		with open(environment_filename, 'a') as f:
			txt = "import os\n\nos.environ['NKASSETS'] = '" + amd + "'"
			write_env = f.write(txt)
		f.closed
		# Loads ENV file for Program startup
		with open(init_filename, 'a') as f:
			txt = "\nnuke.load('assetManagerEnv.py')"
			write_init = f.write(txt)
		f.closed
	if env_check:
		amd = os.environ['NKASSETS']
	os.environ['PROD'] = myPanel.value("production company: ")
	os.environ['SHOW'] = myPanel.value("show: ")
	os.environ['SCENE'] = myPanel.value("scene: ")
	os.environ['SHOT'] = myPanel.value("shot: ")
    
	myLabel = os.environ['SHOW'] + '-' + os.environ['SCENE'] + '-' + os.environ['SHOT']
	myPath = os.path.join(amd, os.environ['PROD'], os.environ['SHOW'], 'scene' + os.environ['SCENE'], 'shot' + os.environ['SHOT'])
	nuke.addFavoriteDir('Asset Management Dir', amd, nuke.SCRIPT | nuke.IMAGE, icon='E:/Video/Tools/Nuke/icons/tc_menu_icon.png')
	nuke.addFavoriteDir(myLabel, myPath, nuke.SCRIPT | nuke.IMAGE, icon='E:/Video/Tools/Nuke/icons/slate_icon.png')