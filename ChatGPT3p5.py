##
## Wrtten by ChatGPT3.5
##
from abaqus import *
from abaqusConstants import *

# Create a new model
myModel = mdb.Model(name='MyModel')

# Create a new part
myPart = myModel.Part(name='MyPart', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Define vertices
vertices = [
    (0.0, 0.0, 0.0),    # Node 1
    (5.0, 0.0, 0.0),    # Node 2
    (5.0, 5.0, 0.0),    # Node 3
    (0.0, 5.0, 0.0),    # Node 4
    (0.0, 0.0, 50.0),   # Node 5
    (5.0, 0.0, 50.0),   # Node 6
    (5.0, 5.0, 50.0),   # Node 7
    (0.0, 5.0, 50.0)    # Node 8
]

# Create vertices
for vertexIndex, vertexCoords in enumerate(vertices):
    myPart.Node(coordinates=vertexCoords, 
                label=vertexIndex+1)

# Define cells (hexahedral)
cells = [
    (1, 2, 3, 4, 5, 6, 7, 8),
    (1, 2, 6, 5),
    (2, 3, 7, 6),
    (3, 4, 8, 7),
    (1, 4, 8, 5)
]

# Create cells
for cellIndex, cellNodes in enumerate(cells):
    myPart.Element(nodes=cellNodes, 
                   elemShape=HEX8, 
                   elemType='C3D8R', 
                   label=cellIndex+1)

# Generate part
myPart.generateMesh()

# Save the model
myModelName = 'MyModel'
mdb.saveAs(pathName=myModelName + '.cae')
