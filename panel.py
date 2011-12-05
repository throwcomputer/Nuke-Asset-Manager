class AssetManagerPanel( nukescripts.PythonPanel ):
    
    # Create Asset Manager Panel
    def __init__( self ):
        nukescripts.PythonPanel.__init__( self, 'Project Management' )
        self.prodcoKnob = nuke.Enumeration_Knob( 'prodcoknob', 'Production Company', [] )
        showlist = os.listdir( os.environ['NKASSETS'] )
        self.showKnob = nuke.Enumeration_Knob( 'showknob', 'Show', [] )
        for k in ( self.prodcoKnob, self.showKnob ):
            self.addKnob( k )
        self.prodDict = {}
        self.getData()

    def getData(self):
        self.prodDict = os.listdir( os.environ['NKASSETS'] )
        rootLayer = self.elementKnob.rootLayer

    # Show Dialog
    p = AssetManagerPanel()
    p.showModalDialog()
