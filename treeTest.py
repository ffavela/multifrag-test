from multifragStuff import *

print(colored(easyStr,"blue"))
#print all energies in MeV
beamE=120.0

m12C=11177.9292
m16O=14899.168598161144
m4He=3728.401315862896
m8Be=7456.894471212898
m14N=13043.780817

m2H=1876.12392312

ex8Be=3.04

#Types of dictionaries
tP="particle"
tS="set" #particle set
tD="detector"
tI="initial"

##############################################
##########Particle dict quaternary sequential####
##############################################

initDict={"type":tI,"name":"12C+12C","massP":m12C,
          "massT":m12C,"ELab":beamE}
oxyDict={"type":tP,"name":"16O","mass":m16O,"exE":6.0494}
beDict={"type":tP,"name":"8Be","mass":m8Be,"exE":3.04}
carbonDict={"type":tP,"name":"12C","mass":m12C,"exE":7.65}

# alphaSysDict={"type":tS,"name":"4He+4He"}
alphaADict={"type":tP,"name":"4HeA","mass":m4He}
alphaBDict={"type":tP,"name":"4HeB","mass":m4He}
alphaCDict={"type":tP,"name":"4HeC","mass":m4He}
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
# alphaSysDict["dictList"]=[alphaADict,alphaBDict]
carbonDict["dictList"]=[d2Dict,{}]

initDict["dictList"]=[oxyDict,beDict]

##############################################
####Particle dict end quaternary sequential######
##############################################

##############################################
##########Particle dict ternary direct########
##############################################

# initDict={"type":tI,"name":"12C+12C","massP":m12C,
#           "massT":m12C,"ELab":beamE}
# oxyDict={"type":tP,"name":"16O","mass":m16O,"exE":0.0}

# alphaSysDict={"type":tS,"name":"4He+4He"}
# alphaADict={"type":tP,"name":"4HeA","mass":m4He}
# alphaBDict={"type":tP,"name":"4HeB","mass":m4He}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(17),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(130),radians(0)]}

# #Completing the dictionaries
# oxyDict["dictList"]=[d1Dict,{}]
# alphaADict["dictList"]=[d2Dict,{}]
# alphaBDict["dictList"]=[{},{}]

# alphaSysDict["dictList"]=[alphaADict,alphaBDict]

# initDict["dictList"]=[oxyDict,alphaSysDict]

##############################################
##########Particle end dict ternary direct####
##############################################

##################################################
##########Particle dict ternary sequential########
##################################################

# initDict={"type":tI,"name":"12C+12C","massP":m12C,
#           "massT":m12C,"ELab":beamE}
# oxyDict={"type":tP,"name":"16O","mass":m16O,"exE":0.0}

# beDict={"type":tP,"name":"8Be","mass":m8Be,"exE":0.0}
# alphaSysDict={"type":tS,"name":"4He+4He"}
# alphaADict={"type":tP,"name":"4HeA","mass":m4He}
# alphaBDict={"type":tP,"name":"4HeB","mass":m4He}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(17),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(130),radians(0)]}

# #Completing the dictionaries
# oxyDict["dictList"]=[d1Dict,{}]
# alphaADict["dictList"]=[d2Dict,{}]
# alphaBDict["dictList"]=[{},{}]
# beDict["dictList"]=[alphaADict,alphaBDict]
# # # alphaSysDict["dictList"]=[alphaADict,alphaBDict]

# initDict["dictList"]=[oxyDict,beDict]

##################################################
##########Particle end dict ternary sequential####
##################################################



##############################################
##########Particle dict binary################
##############################################
# beamE=60.0
# initDict={"type":tI,"name":"d+14N","massP":m2H,
#           "massT":m14N,"ELab":beamE}

# carbonDict={"type":tP,"name":"12C","mass":m12C,"exE":7.65}

# alphaDict={"type":tP,"name":"4He","mass":m4He}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(35),radians(0)]}

# #Completing the dictionaries
# carbonDict["dictList"]=[{},{}]
# alphaDict["dictList"]=[d1Dict,{}]

# initDict["dictList"]=[carbonDict,alphaDict]

##############################################
##########Particle dict end binary############
##############################################


# printTree(initDict)
print("")

# print("The final mass of 8Be is")
# print(getFinalMass(beDict))
print("")
print("Now completing the tree")
globalCompleteTree(initDict)

# printTree(initDict)

print("\n\nNow testing the free part route stuff\n")
generalList=getDirectFreeRoute(initDict)
print(colored(generalList,'red'))
if generalList == []:
    print("Error!!! Are you sure you filled \
    the free part dict correctly?!")


print("Trying to pull every line automatically")
boolPull=pullEveryLine(initDict,generalList)

# print("Printing the entire tree, without major sols")
# printTree(initDict)

fillBool=fillMajorSols(initDict,generalList)

print(colored("Now printing only the tree sols part","red"))
printTreeOnlySolsPart(initDict)


# print("Now the entire filled tree")
# printTree(initDict)

# print("")
# print("Now printing a node")
# printNode(alphaSysDict)

print("Now the new cleanDict function")
myBool=cleanDict(initDict,generalList)
print("The bool val is ", myBool)
print(colored(easyStr,"red"))

print("Printing the entire tree, after cleaning")
printTree(initDict)

# printTreeOnlyCleanSolsPart(initDict)
############################################
####The plotting part#######################
############################################

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


# fig = plt.figure()
# ax = fig.gca(projection='3d')

# plt.xlim(-15, 15)
# plt.ylim(-15, 15)

# plotAllLines(initDict,ax)
# ax.legend()

# firstVelMag=initDict["redVcm"]
# a = Arrow3D([0, 0], [0, 0], [0, firstVelMag], mutation_scale=20,
#             lw=1, arrowstyle="-|>", color="k")

# ax.add_artist(a)

# u = np.linspace(0, 2 * np.pi, 100)
# v = np.linspace(0, np.pi, 100)

# ax.set_zlim3d(-5, 20)

# plt.show()

############################################
####The plotting part finish################
############################################
