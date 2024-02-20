##
## Written by ChatGPT GPT-4  
##
# Import Abaqus modules
from abaqus import *
from abaqusConstants import *
import part

# Start a new model
Mdb()
mdb.models.changeKey(fromName='Model-1', toName='SolidPartModel')

# Create a new part in the model
# Define the dimensions of the part
width = 5.0
depth = 5.0
height = 50.0

# Access the model
model = mdb.models['SolidPartModel']

# Create the part
# The part is a 3D deformable solid.
# Sketch for the base profile
s = model.ConstrainedSketch(name='baseSketch', sheetSize=200.0)
# Draw the rectangle for the base
s.rectangle(point1=(0, 0), point2=(width, depth))

# Create the solid extrusion
model.Part(name='SolidBlock', dimensionality=THREE_D, type=DEFORMABLE_BODY)
model.parts['SolidBlock'].BaseSolidExtrude(sketch=s, depth=height)

# Optional: Generate mesh for the part if required for simulation
# This step is optional and depends on your specific needs for simulation
part = model.parts['SolidBlock']
part.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
part.generateMesh()

# Save the model
mdb.saveAs(pathName='3D_Solid_Part_Model.cae')
