# -*- coding: mbcs -*-
#
# Abaqus/CAE Release 2024 replay file
# Internal Version: 2023_09_21-08.55.25 RELr426 190762
# Run by SJR4 on Wed Jun  5 17:47:19 2024
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=340.256469726563, 
    height=219.555572509766)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from caeModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
openMdb('BridgeScript.cae')
#: The model database "C:\Users\SJR4\Desktop\Abaqus Files\BridgeScript\BridgeScript.cae" has been opened.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=ON)
execfile('C:/Users/SJR4/Desktop/Abaqus Files/BridgeScript/Script3.py', 
    __main__.__dict__)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
mdb.Job(name='Job-1', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, numThreadsPerMpiProcess=1, 
    multiprocessingMode=DEFAULT, numCpus=1, numGPUs=0)
mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
#: The job input file "Job-1.inp" has been submitted for analysis.
#: Job Job-1: Analysis Input File Processor completed successfully.
#: Job Job-1: Abaqus/Standard completed successfully.
#: Job Job-1 completed successfully. 
o3 = session.openOdb(
    name='C:/Users/SJR4/Desktop/Abaqus Files/BridgeScript/Job-1.odb')
#: Model: C:/Users/SJR4/Desktop/Abaqus Files/BridgeScript/Job-1.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             3
#: Number of Element Sets:       7
#: Number of Node Sets:          7
#: Number of Steps:              1
session.viewports['Viewport: 1'].setValues(displayedObject=o3)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6)
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.6463, 
    farPlane=25.7725, width=11.7598, height=5.01583, cameraPosition=(23.5862, 
    0.227139, 5.04996), cameraUpVector=(-0.364691, 0.867221, -0.339011), 
    cameraTarget=(-0.322957, -0.29923, 5.89466))
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.5298, 
    farPlane=25.8891, width=11.6965, height=4.98883, cameraPosition=(23.5862, 
    0.227139, 5.04996), cameraUpVector=(-0.357112, 0.930161, -0.0852744), 
    cameraTarget=(-0.322957, -0.29923, 5.89466))
session.viewports['Viewport: 1'].view.setValues(nearPlane=21.5353, 
    farPlane=25.8836, width=11.6995, height=4.9901, cameraPosition=(23.5862, 
    0.227139, 5.04996), cameraUpVector=(-0.354774, 0.934811, -0.0162123), 
    cameraTarget=(-0.322957, -0.29923, 5.89466))
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=5)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=6)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=3)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=4)
mdb.save()
#: The model database has been saved to "C:\Users\SJR4\Desktop\Abaqus Files\BridgeScript\BridgeScript.cae".
