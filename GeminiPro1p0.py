##
## Written by Gemini Pro 1.0
##
import abaqus
from abaqus import mdb, session

# Set up the model
mdb.Model(name='MyModel')
session.viewports['Viewport:1'].setValues(displayedObject=None)

# Create a block
block_name = 'Block-1'
mdb.models['MyModel'].Part(name=block_name, objectName=block_name, type=
   mdb.models['MyModel'].parts.SOLID)

# Create a sketch on the XY plane
mdb.models['MyModel'].parts[block_name].BaseShell(side1=mdb.models['MyModel'].parts[block_name].faces[0])
sketch_name = 'Sketch-1'
mdb.models['MyModel'].parts[block_name].sketches.add(name=sketch_name, plane=mdb.models['MyModel'].parts[block_name].planes[0])

# Draw a rectangle in the sketch
sketch = mdb.models['MyModel'].parts[block_name].sketches[sketch_name]
sketch.geometry.Rectangle(point1=(0.0, 0.0), point2=(5.0, 5.0))

# Extrude the sketch to create the block
mdb.models['MyModel'].parts[block_name].features.extrude(sketch=sketch_name,
   depth=50.0)

# Save the model
mdb.saveAs(pathName='MyPart.cae')

print('3D solid part generated successfully in Abaqus/CAE!')
