# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-13.49.31 163176
# Run by SJR4 on Thu Jul 11 02:50:51 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=267.524993896484, 
    height=123.168518066406)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('BridgeA2-NoRail.cae')
#: The model database "C:\Users\SJR4\Desktop\ABAQUS\BridgeA2-NoRail\BridgeA2-NoRail.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-2']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-2']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-2']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-2']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-1']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-1']
p.seedPart(size=10.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-1']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-15']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-15']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-15']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-15']
p.generateMesh()
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='Job-8', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Job-8'].submit(consistencyChecking=OFF)
#: The job input file "Job-8.inp" has been submitted for analysis.
#: Job Job-8: Analysis Input File Processor completed successfully.
#: Job Job-8: Abaqus/Standard completed successfully.
#: Job Job-8 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/SJR4/Desktop/ABAQUS/BridgeA2-NoRail/Job-8.odb')
#: Model: C:/Users/SJR4/Desktop/ABAQUS/BridgeA2-NoRail/Job-8.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     15
#: Number of Meshes:             15
#: Number of Element Sets:       22
#: Number of Node Sets:          24
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=8)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, ))
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-1']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-1']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-1']
p.seedPart(size=5.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-1']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-4']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-4']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-4']
p.seedPart(size=3.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-4']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-5']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-5']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-5']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-5']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-6']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-6']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-6']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-6']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-7']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-7']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-7']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-7']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-8']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-8']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-8']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-8']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-9']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-9']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-9']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-9']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-10']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-10']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-10']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-10']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-11']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-11']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-11']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-11']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-12']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-12']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-12']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-12']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-13']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-13']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-13']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-13']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-14']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-14']
p.deleteMesh()
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-14']
p.seedPart(size=2.0, deviationFactor=0.1, minSizeFactor=0.1)
p = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-14']
p.generateMesh()
p1 = mdb.models['Model-1'].parts['CAD Model of Bridge Assembly-15']
session.viewports['Viewport: 1'].setValues(displayedObject=p1)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
session.viewports['Viewport: 1'].setValues(displayedObject=a)
mdb.Job(name='Job-9', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Job-9'].submit(consistencyChecking=OFF)
#: The job input file "Job-9.inp" has been submitted for analysis.
#: Job Job-9: Analysis Input File Processor completed successfully.
#: Job Job-9: Abaqus/Standard completed successfully.
#: Job Job-9 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/SJR4/Desktop/ABAQUS/BridgeA2-NoRail/Job-8.odb'])
o3 = session.openOdb(
    name='C:/Users/SJR4/Desktop/ABAQUS/BridgeA2-NoRail/Job-9.odb')
#: Model: C:/Users/SJR4/Desktop/ABAQUS/BridgeA2-NoRail/Job-9.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     15
#: Number of Meshes:             15
#: Number of Element Sets:       22
#: Number of Node Sets:          24
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].view.setValues(nearPlane=744.633, 
    farPlane=1182.96, width=130.422, height=57.8328, viewOffsetX=-1.28587, 
    viewOffsetY=25.1062)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
mdb.save()
#: The model database has been saved to "C:\Users\SJR4\Desktop\ABAQUS\BridgeA2-NoRail\BridgeA2-NoRail.cae".
