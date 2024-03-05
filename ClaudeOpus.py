##
## Written by Claude Opus  
##
from abaqus import *
from abaqusConstants import *
import __main__

# Create a new model
model = mdb.Model(name='3D_Solid_Part')

# Create a new sketch
sketch = model.ConstrainedSketch(name='Sketch', sheetSize=200.0)

# Create a rectangle
sketch.rectangle(point1=(0.0, 0.0), point2=(5.0, 5.0))

# Create a 3D part by extruding the sketch
part = model.Part(name='Part-1', dimensionality=THREE_D, type=DEFORMABLE_BODY)
part.BaseSolidExtrude(sketch=sketch, depth=50.0)

# Create a viewport to visualize the part
viewport = session.Viewport(name='Viewport for 3D Solid Part')
viewport.setValues(displayedObject=part)