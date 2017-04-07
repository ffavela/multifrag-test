from multifragStuff import *

beamE=60.0 #MeV
#Masses are in MeV/c^2
mC=11177.9292

mOxy=14899.168598161144
mAlpha=3728.401315862896

mBe=7456.894471212898

exEnergy=3.04
mBeEx=mBe+exEnergy

myVLine1=getStraightLinePoints(radians(25),radians(5),15.0)
myVLine2=getStraightLinePoints(radians(45),radians(35),15.0)
myVLine3=getStraightLinePoints(radians(55),radians(77),15.0)
myVLine4=getStraightLinePoints(radians(75),radians(47),15.0)

vRad=3.5
vRad2=4.5
vRad1=6.0
frac=0.3
frac3=0.45
frac4=0.63
midPLine1=getMidPointLine(myVLine1,myVLine2,vRad,frac)
midPLine2=getMidPointLine(myVLine2,myVLine1,vRad,1-frac)
midPLine3=getMidPointLine(myVLine3,midPLine1,vRad,frac3)
midPLine3_4=getMidPointLine(myVLine3,myVLine4,vRad2,frac4)
midPLine4_3=getMidPointLine(myVLine4,myVLine3,vRad2,1-frac4)
midPLine3P=getMidPointLine(midPLine1,myVLine3,vRad,frac3)
midPLineSec3=getMidPointLine(myVLine3,midPLine2,vRad1,1-frac3)
midPLineSec3P=getMidPointLine(midPLine2,myVLine3,vRad1,1-frac3)

x1=myVLine1[ : ,0]
y1=myVLine1[ : ,1]
z1=myVLine1[ : ,2]

x2=myVLine2[ : ,0]
y2=myVLine2[ : ,1]
z2=myVLine2[ : ,2]

x3=myVLine3[ : ,0]
y3=myVLine3[ : ,1]
z3=myVLine3[ : ,2]

x4=myVLine4[ : ,0]
y4=myVLine4[ : ,1]
z4=myVLine4[ : ,2]

midX1=midPLine1[ : ,0]
midY1=midPLine1[ : ,1]
midZ1=midPLine1[ : ,2]

midX2=midPLine2[ : ,0]
midY2=midPLine2[ : ,1]
midZ2=midPLine2[ : ,2]

midX3=midPLine3[ : ,0]
midY3=midPLine3[ : ,1]
midZ3=midPLine3[ : ,2]

midX3_4=midPLine3_4[ : ,0]
midY3_4=midPLine3_4[ : ,1]
midZ3_4=midPLine3_4[ : ,2]

midX4_3=midPLine4_3[ : ,0]
midY4_3=midPLine4_3[ : ,1]
midZ4_3=midPLine4_3[ : ,2]

midX3P=midPLine3P[ : ,0]
midY3P=midPLine3P[ : ,1]
midZ3P=midPLine3P[ : ,2]

midXSec3=midPLineSec3[ : ,0]
midYSec3=midPLineSec3[ : ,1]
midZSec3=midPLineSec3[ : ,2]

midXSec3P=midPLineSec3P[ : ,0]
midYSec3P=midPLineSec3P[ : ,1]
midZSec3P=midPLineSec3P[ : ,2]

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x1, y1, z1, label='my curve')
plotNoDisplay(ax,myVLine1,"aName")
plotNoDisplay(ax,myVLine2,"aName")

# ax.plot(x2, y2, z2, label='my sec curve')
# ax.plot(x3, y3, z3, label='my third curve')
# ax.plot(x4, y4, z4, label='my fourth curve')
# ax.plot(midX1, midY1, midZ1, label='my mid curve 1')
# ax.plot(midX2, midY2, midZ2, label='my mid curve 2')
# ax.plot(midX3, midY3, midZ3, label='my mid curve 3')
# ax.plot(midX3_4, midY3_4, midZ3_4, label='my mid curve 3_4')
# ax.plot(midX4_3, midY4_3, midZ4_3, label='my mid curve 4_3')
# ax.plot(midX3P, midY3P, midZ3P, label='my mid curve 3 P')
# ax.plot(midXSec3, midYSec3, midZSec3, label='my mid curve sec 3')
# ax.plot(midXSec3P, midYSec3P, midZSec3P, label='my mid curve sec 3 P')
# ax.legend()

plt.show()
