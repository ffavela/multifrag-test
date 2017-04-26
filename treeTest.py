from multifragStuff import *

#print all energies in MeV
beamE=120

m12C=11177.9292
m16O=14899.168598161144
m4He=3728.401315862896
m8Be=7456.894471212898

ex8Be=3.04

#Types of dictionaries
tP="particle"
tS="set" #particle set
tD="detector"
tI="initial"

#Particle dict
initDict={"type":tI,"name":"12C+12C","massP":m12C,
          "massT":m12C,"ELab":beamE}
oxyDict={"type":tP,"name":"16O","mass":m16O,"exE":6.0494}
beDict={"type":tP,"name":"8Be","mass":m8Be,"exE":3.04}
carbonDict={"type":tP,"name":"12C","mass":m12C,"exE":7.65}

alphaSysDict={"type":tS,"name":"4He+4He"}
alphaADict={"type":tP,"name":"4He","mass":m4He}
alphaBDict={"type":tP,"name":"4He","mass":m4He}
alphaCDict={"type":tP,"name":"4He","mass":m4He}
# alphaDDict={"type":tP,"name":"4He","mass":m4He}
# alphaEDict={"type":tP,"name":"4He","mass":m4He}

#Defining the detectors
d1Dict={"type":tD,"name":"d1","angles":[radians(3),radians(6)]}
d2Dict={"type":tD,"name":"d2","angles":[radians(15),radians(20)]}
d3Dict={"type":tD,"name":"d3","angles":[radians(140),radians(20)]}
# d4Dict={"type":tD,"name":"d4"}

#Completing the dictionaries
alphaBDict["dictList"]=[d3Dict,{}]
alphaADict["dictList"]=[{},{}]
alphaCDict["dictList"]=[d1Dict,{}]

oxyDict["dictList"]=[alphaCDict,carbonDict]

beDict["dictList"]=[alphaADict,alphaBDict]
alphaSysDict["dictList"]=[alphaADict,alphaBDict]
carbonDict["dictList"]=[d2Dict,{}]

initDict["dictList"]=[oxyDict,beDict]
# initDict["dictList"]=[oxyDict,alphaSysDict]

# treeStruct=[alphaADict,[d1Dict,{}]]

# printTree(initDict)
print("")

# print("The final mass of 8Be is")
# print(getFinalMass(beDict))
print("")
print("Now completing the tree")
globalCompleteTree(initDict)

# printTree(initDict)

print("\n\nNow testing the free part route stuff\n")
getDirectFreeRoute(initDict)
print(generalList)

# print("trying to fill the oxyDict tree")
# boolPull=pullLinesFromNode(oxyDict)
# print(boolPull)
# printTree(initDict)

# print("Testing the Q val function")
# print(getQVal(initDict))
print("Trying to pull every line automatically")

boolPull=pullEveryLine(initDict,generalList)

# printTree(initDict)

fig = plt.figure()
ax = fig.gca(projection='3d')

plt.xlim(-15, 15)
plt.ylim(-15, 15)
# plt.zlim(-15, 15)

plotAllLines(initDict,ax)
ax.legend()

from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
class Arrow3D(FancyArrowPatch):

    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)


firstVelMag=initDict["redVcm"]
a = Arrow3D([0, 0], [0, 0], [0, firstVelMag], mutation_scale=20,
            lw=1, arrowstyle="-|>", color="k")
# a = Arrow3D([0,1],[0,1],[0,1], mutation_scale=20, lw=1, arrowstyle="-|>", color="k", linestyle="dashed")

ax.add_artist(a)

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

# oxyVel=initDict["dictList"][0]["redVcm"]
oxyVelRad=initDict["dictList"][0]["redVcm"]

x = oxyVelRad * np.outer(np.cos(u), np.sin(v))
y = oxyVelRad * np.outer(np.sin(u), np.sin(v))
z = oxyVelRad * np.outer(np.ones(np.size(u)), np.cos(v))+firstVelMag
ax.plot_surface(x, y, z,  rstride=4, cstride=4, color='#668800')


oxyLine1=initDict["dictList"][0]["vLines"][0]
oxyLine2=initDict["dictList"][0]["vLines"][1]

oxyVelRad=initDict["dictList"][0]["redVcm"]
# print("oxyVelRad = ",oxyVelRad)
# oxyVelRad=1.3
oxyCenter=np.array([0,0,firstVelMag])
# print(oxyLine1)
# print(oxyLine2)

normVelSols1=getSphereLineSols(oxyCenter,oxyVelRad,oxyLine1)
normVelSols2=getSphereLineSols(oxyCenter,oxyVelRad,oxyLine2)

# print("normalized solutions 1",normVelSols1)
# print("normalized solutions 2",normVelSols2)


indexSols1=getSphereLineIdxSols(oxyCenter,oxyVelRad,oxyLine1)
indexSols2=getSphereLineIdxSols(oxyCenter,oxyVelRad,oxyLine2)

# print("idx sols 1", indexSols1)
# print("idx sols 2", indexSols2)

totIndexSols=indexSols1+indexSols2
# print("tot idx Sols", totIndexSols)
myVar=len(initDict["dictList"][0]["vLines"])
# print("num of lines",myVar)

print("Now doing the new function")
solListInParents=getSolListInParents(oxyDict,totIndexSols)
print(solListInParents)

# print("Filling the oxygenNode with solutions")
# print("oxyVelRad = ",oxyVelRad)
# fillSphereLineIdxSolsInNode(oxyDict,oxyCenter,oxyVelRad)
# sphereSols=fillSolVelsEnergiesEtcInNode(oxyDict)
# print("sphereSols = ",sphereSols)

ax.set_zlim3d(-5, 20)
# mayorSolBool=fillMayorSols(initDict,generalList)
# if mayorSolBool == False:
#     print("Couldn't fill the tree :'-(")
# else:
#     print("Success in filling the tree!! :-)")
# printTree(initDict)


fillMajorSols2(initDict,generalList)
# fillMajorSols2(oxyDict,generalList)

vPoint=np.array([0,0,0])
vRad=7.326472906898222
vLine=np.array([[ 0.,0., 6.82647291],[ 0.,0.,7.82647291]])
# vLine=np.array([[ 0.,0., 5.82647291],[ 0.,0., 6.82647291],[ 0.,0.,7.82647291],[ 0.,0.,8.82647291]])
myTrainSolIdx=getTrainSolIdx(vPoint,vRad,vLine,)

print("myTrainSolIdx = ", myTrainSolIdx)

i=0

train=vLine[i:i+2]
print("train = ",train)
trainStatus=getTrainStatus(vPoint,vRad,train)
print("trainStatus = ",trainStatus)

plt.show()
