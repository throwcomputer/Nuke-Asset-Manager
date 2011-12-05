nuke.load("manager")
nuke.load("setup")
nuke.load('panel')

def addManagementPanel():
    return assetManagerPanel().addToPane()

menu = nuke.menu('Pane')
menu.addCommand('Project Management Settings', addManagementPanel)
nukescripts.registerPanel( 'assetpanel', addManagementPanel)