class assetManagerPanel( nukescripts.PythonPanel ):
    def __init__(self):
        nukescripts.PythonPanel.__init__(self, 'Project Management Panel', 'assetpanel')

        # Create all fields
        self.prod = nuke.Enumeration_Knob('prod', 'Production Company', [])
        self.prodNew = nuke.String_Knob('prodnew', 'Create New Company')
        self.prodCreate = nuke.PyScript_Knob('prodcreate', 'Create')
        self.show = nuke.Enumeration_Knob('show', 'Show', [])
        self.showNew = nuke.String_Knob('shownew', 'Create New Show')
        self.showCreate = nuke.PyScript_Knob('showcreate', 'Create')
        self.scene = nuke.Enumeration_Knob('scene', 'Scene', [])
        self.sceneNew = nuke.String_Knob('scenenew', 'Create New Scene')
        self.sceneCreate = nuke.PyScript_Knob('scenecreate', 'Create')
        self.shot = nuke.Enumeration_Knob('shot', 'Shot', [])
        self.shotNew = nuke.String_Knob('shotnew', 'Create New Shot')
        self.shotCreate = nuke.PyScript_Knob('shotcreate', 'Create')
        
        # Blank Array of dictionary names for all Enumeration Knobs
        dictionaries = []

        for k in ( self.prod, self.prodNew, self.prodCreate, self.show, self.showNew, self.showCreate, self.scene, self.sceneNew, self.sceneCreate, self.shot, self.shotNew, self.shotCreate ):
            # Create all knobs
            self.addKnob( k )
            if k.Class() == 'Enumeration_Knob':
                # generate dictionary names only for enumeration knobs
                dictionaries.append( k.name() + 'Dict' )
            elif k.Class() in ('String_Knob', 'PyScript_Knob'):
                # hide everything but enumeration knobs
                k.setVisible(False)

        for d in dictionaries:
            # create blank lists for each dictionary
            self.d = []
        
        self.getData()

    def getData( self ):
        self.prodDict = os.listdir( os.environ['NKASSETS'] )
        self.prodDict.sort()
        self.prodDict.append('Create New...')
        self.prod.setValues( self.prodDict )
    
    def knobChanged( self, knob ):
        new_parent = ''
        
        # Dropdown Change
        if knob.Class() is 'Enumeration_Knob':
            new_parent = knob.name()
        # Create New - toggle visibility
        if knob.value() == 'Create New...':
            self.prodNew.setVisible(True)
            self.prodCreate.setVisible(True)
        if knob.value() != 'Create New...':
            self.prodNew.setVisible(False)
            self.prodCreate.setVisible(False)
        # Create New - process
        if knob.Class() in  ('PyScript_Knob', 'String_Knob'):
            numvals = self.prod.numValues()
            txt = self.prodNew.value()
            self.prodDict.append( txt )
            self.prodDict.remove('Create New...')
            self.prodDict.sort()
            self.prodDict.append('Create New...')
            self.prod.setValues( self.prodDict )
            self.prod.setValue( txt )
        print knob.name()
        print new_parent
        