##
## Written by HuggingChat model: mistralai/Mixtral-8x7B-Instruct-v0.1
##
import abaqus
from abaqus import *
from abaqusConstants import *

# Create the model database and the part
modelName = 'solid_part'
mdb = mdb.Model(name=modelName)
sketch1 = mdb.ConstrainedSketch(name='__profile__', sheetSize=200.0)
part1 = mdb.Part(name='solid_part', dimensionality=THREE_D, type=DEFORMABLE_BODY)

# Define the sketch profile
w = 5.0 # width
h = 5.0 # height
d = 50.0 # depth
sketch1.rectangle(point1=(0.0, 0.0), point2=(w, h))

# Extrude the sketch into a 3D solid
extrude = part1.ExtrudedCut(sketch=sketch1, direction=(0.0, 0.0, d))
del mdb.models[modelName].sketches['__profile__']

# Set up the material properties for the part
materialProperties = {
    "name": "Material-1",
    "elasticModulus": 70e9, # Young's modulus (Pa)
    "poissonRatio": 0.3, # Poisson's ratio
    "density": 8000.0 # Density (kg/m^3)
}

# Add the material to the model
mdb.models[modelName].Material(name=materialProperties["name"])
mdb.models[modelName].materials[materialProperties["name"]].Elastic(table=((materialProperties["elasticModulus"], ), ))
mdb.models[modelName].materials[materialProperties["name"]].PoissonRatio(ratio=materialProperties["poissonRatio"])
mdb.models[modelName].materials[materialProperties["name"]].Density(table=((materialProperties["density"], ), ))

# Assign the material to the part
part1.setMaterial(name=materialProperties["name"])

# Save the model
mdb.saveAs('solid_part.cae')
