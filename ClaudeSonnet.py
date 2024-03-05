#
# Written by Claude Sonnet
#
from abaqus import *
from abaqusConstants import *
import regionToolset

# Create a new model database
modelDB = mdb.models.add("Part3D")

# Create a sketch for the base
sketcher = modelDB.ConstrainedSketch(name="baseSketch", sheetSize=20.0)
sketcher.rectangle(point1=(0.0, 0.0), point2=(5.0, 5.0))
sketcher.unsetPrimaryObject()

# Create a 3D part by extruding the sketch
modelDB.Part(name="Part3D", dimensionality=THREE_D, type=DEFORMABLE_BODY)
modelDB.parts["Part3D"].BaseSolidExtrude(sketch=modelDB.sketches["baseSketch"], depth=50.0)

# Save the model
modelDB.saveAs("Part3D.cae")
