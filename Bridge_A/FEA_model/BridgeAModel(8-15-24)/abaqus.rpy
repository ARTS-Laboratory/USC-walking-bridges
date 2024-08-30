# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2020 replay file
# Internal Version: 2019_09_13-13.49.31 163176
# Run by SJR4 on Fri Aug 30 15:50:43 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=243.599990844727, 
    height=105.534255981445)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('BridgeA4.cae')
#: The model database "C:\Users\SJR4\Desktop\ABAQUS\BridgeA4-GitHub\BridgeA4.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
p = mdb.models['Model-1'].parts['AnalyticalRigidLine']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
o3 = session.openOdb(
    name='C:/Users/SJR4/Desktop/ABAQUS/BridgeA4-GitHub/Spring3D1S.odb')
#: Model: C:/Users/SJR4/Desktop/ABAQUS/BridgeA4-GitHub/Spring3D1S.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     15
#: Number of Meshes:             16
#: Number of Element Sets:       23
#: Number of Node Sets:          29
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/SJR4/Desktop/ABAQUS/BridgeA4-GitHub/Spring3D1S.odb'])
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.jobs['Job2-NoCrossNoRail']
del mdb.jobs['LoadTest']
del mdb.jobs['NonPinMidFreq']
del mdb.jobs['Job-6']
del mdb.jobs['Job-1']
del mdb.jobs['GravPressureTest']
del mdb.jobs['ElasticOrigSupp']
del mdb.jobs['ElasticBothSupports']
del mdb.jobs['Elastic80-20']
mdb.Job(name='Job-2', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Standard completed successfully.
#: Job Job-2 completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/SJR4/Desktop/ABAQUS/BridgeA4-GitHub/Spring3D1S.odb'])
o3 = session.openOdb(
    name='C:/Users/SJR4/Desktop/ABAQUS/BridgeA4-GitHub/Job-2.odb')
#: Model: C:/Users/SJR4/Desktop/ABAQUS/BridgeA4-GitHub/Job-2.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     15
#: Number of Meshes:             16
#: Number of Element Sets:       23
#: Number of Node Sets:          29
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.jobs['Job-2']
mdb.Job(name='SpringOriginalSupportOnly', model='Model-1', description='', 
    type=ANALYSIS, atTime=None, waitMinutes=0, waitHours=0, queue=None, 
    memory=90, memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['SpringOriginalSupportOnly'].submit(consistencyChecking=OFF)
#: The job input file "SpringOriginalSupportOnly.inp" has been submitted for analysis.
#: Job SpringOriginalSupportOnly: Analysis Input File Processor completed successfully.
#: Job SpringOriginalSupportOnly: Abaqus/Standard completed successfully.
#: Job SpringOriginalSupportOnly completed successfully. 
session.viewports['Viewport: 1'].setValues(
    displayedObject=session.odbs['C:/Users/SJR4/Desktop/ABAQUS/BridgeA4-GitHub/Job-2.odb'])
o3 = session.openOdb(
    name='C:/Users/SJR4/Desktop/ABAQUS/BridgeA4-GitHub/SpringOriginalSupportOnly.odb')
#: Model: C:/Users/SJR4/Desktop/ABAQUS/BridgeA4-GitHub/SpringOriginalSupportOnly.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     15
#: Number of Meshes:             16
#: Number of Element Sets:       23
#: Number of Node Sets:          29
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=7)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=10)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=9)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
del mdb.jobs['Spring3D1S']
mdb.save()
#: The model database has been saved to "C:\Users\SJR4\Desktop\ABAQUS\BridgeA4-GitHub\BridgeA4.cae".
