from multifragStuff import *

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

beamE=60.0 #MeV
#Masses are in MeV/c^2
mC=11177.9292

mOxy=14899.168598161144
mAlpha=3728.401315862896

mBe=7456.894471212898

exEnergy=3.04
mBeEx=mBe+exEnergy

myVLine1=getStraightLinePoints(radians(25),radians(15),15.0)
myVLine2=getStraightLinePoints(radians(45),radians(35),15.0)

vRad=3.5
frac=0.1
midPLine1=getMidPointLine(myVLine1,myVLine2,vRad,frac)
midPLine2=getMidPointLine(myVLine2,myVLine1,vRad,1-frac)

x1=myVLine1[ : ,0]
y1=myVLine1[ : ,1]
z1=myVLine1[ : ,2]

x2=myVLine2[ : ,0]
y2=myVLine2[ : ,1]
z2=myVLine2[ : ,2]

midX1=midPLine1[ : ,0]
midY1=midPLine1[ : ,1]
midZ1=midPLine1[ : ,2]

midX2=midPLine2[ : ,0]
midY2=midPLine2[ : ,1]
midZ2=midPLine2[ : ,2]

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, y1, z1, label='my curve')
ax.plot(x2, y2, z2, label='my sec curve')
ax.plot(midX1, midY1, midZ1, label='my mid curve 1')
ax.plot(midX2, midY2, midZ2, label='my mid curve 2')
ax.legend()

plt.show()
