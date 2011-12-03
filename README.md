Nuke Asset Manager README

# Overview
Nuke Asset manager is a tool for organizing project assets within a rigid file structure.  Original source taken from [The Foundry's Nuke Python Dev Guide - Asset Manager Tutorial](http://docs.thefoundry.co.uk/nuke/63/pythondevguide/asset.html).

# Goals
To progress the basic asset manager code into a fully functional front-end control panel for managing projects and their assets.
	Features:
		- set/reset asset directory as NKASSETS environment variable
		- permanently store asset directory variable in file for launch
		- Define the production company (PROD), show name (SHOW), scene (SCENE) and shot (SHOT) numbers
		- create bookmarks for Asset directory as well as shot directory for file you are working on.
		- open existing .nk files for show/scene/shot
		- store all project files in directory structure:
			NKASSETS/PROD/SHOW/SCENE/SHOT
		- Using WriteAssets.gizmo: render all exports into folders based on export types
			(anim, cg, comp, concept, grade, matte, plates, roto, pass)
			and render version (_v01, etc.)
			as such:
				NKASSETS/PROD/SHOW/SCENE/SHOT/type/type_description_vVERSION/type_description_vVERSION.filetype
					
	Planned Features:
		- panel optimization:
			-dropdown to select all "production companies" based on existing folders within NKASSETS dir
			-dropdown to select all "shows" based on existing folders within NKASSETS/PROD dir
			-dropdown to select all "scenes" based on existing dirs
			-dropdwon to select all "shots" based on existing dirs
			-create new (prod/show/scene/shot) buttons to compliment each dropdown for creation of new entities
		-WriteAssets optimization:
			-only include _%04d in filenames when render is an image sequence
		-Automatic Read Nodes
		-Automatic Slate gizmo (in works..)
	
	Future Features:
		- Database linking (mysql, sql)
		- Cloud storage (Amazon E3, Google Storage, etc..)
		
# How to install
Put Nuke-Asset-Manager in your .nuke directory (or somewhere else in your Nuke path if you're fancy), then add this line to the init.py of that parent directory:

nuke.pluginAddPath('./asset-manager')

Importing the module adds a "scene-shot" item to the Nuke menu.
The "scene-shot" menu provides easy save button for auto saving of .nk scripts into the correct directory as well as a button for the WriteAssets gizmo. 

# How to use
Run Nuke.
use the folder icon to navigate to and select your desired asset directory.
Enter Production Company Name
Enter Show Name
Enter scene number
Enter shot number

once done, if you enter an existing prod/show/scene/shot and there are .nk scripts in the corresponding ../nuke directory, a new window will pop up asking you to select which script to open.

Select script to open or cancel to ignore.
if you open existing script, the first menu will open again.. just cancel. (to be fixed)


# Details
Built on windows.. compatibility probably not available on function that creates directories if they dont exist.

# Thank you
The Foundry python dev guide.

# LICENSE

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.