from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

# Create ranges for materials.
concreteSect = 1
steelSect = 18

concreteArr = range(1, concreteSect + 1, 1)
steelArr = range(2, steelSect + 1, 1)

# Create Materials
mdb.models['Model-1'].Material(name='Concrete')
mdb.models['Model-1'].materials['Concrete'].Density(table=((0.000224571909, ),
    ))
mdb.models['Model-1'].materials['Concrete'].Elastic(table=((5221356.0, 0.15),
    ))
mdb.models['Model-1'].Material(name='Steel')
mdb.models['Model-1'].materials['Steel'].Density(table=((0.000739215869, ), ))
mdb.models['Model-1'].materials['Steel'].Elastic(table=((29007536.0, 0.29), ))

# Create Material Sections
mdb.models['Model-1'].HomogeneousSolidSection(material='Concrete', name=
    'Concrete', thickness=None)
mdb.models['Model-1'].HomogeneousSolidSection(material='Steel', name='Steel',
    thickness=None)

# Assign Material Sections
assignMaterials = True

if assignMaterials:
    for i in concreteArr:
        mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].Set(cells=
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].cells.getSequenceFromMask(
            ('[#1 ]', ), ), name='Set-1')
        mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].SectionAssignment(
            offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].sets['Set-1']
            , sectionName='Concrete', thicknessAssignment=FROM_SECTION)
    for i in steelArr:
        mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].Set(cells=
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].cells.getSequenceFromMask(
            ('[#1 ]', ), ), name='Set-1')
        mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].SectionAssignment(
            offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].sets['Set-1']
            , sectionName='Steel', thicknessAssignment=FROM_SECTION)

# Assign Meshes. Know what meshes need a different meshing control and use tetMeshRange for those.
assignMeshes = True
meshRange = range(1, 20, 1)
tetMeshRange = range(18, 20, 1)

if assignMeshes:
    for i in meshRange:
        if i in tetMeshRange:
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].setMeshControls(
                elemShape=TET, regions=
                mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].cells.getSequenceFromMask(
                    ('[#1 ]',), ), technique=FREE)
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].setElementType(
                elemTypes=(ElemType(elemCode=C3D20R, elemLibrary=STANDARD), ElemType(
                    elemCode=C3D15, elemLibrary=STANDARD), ElemType(elemCode=C3D10,
                                                                    elemLibrary=STANDARD)), regions=(
                    mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].cells.getSequenceFromMask(
                        ('[#1 ]',), ),))
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].seedPart(
                deviationFactor=0.1, minSizeFactor=0.1, size=3.9)
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].generateMesh()

        else:
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].seedPart(
                deviationFactor=0.1, minSizeFactor=0.1, size=2.0)
            mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-'+str(i)].generateMesh()