from multifragStuff import *

print(colored(easyStr,"blue"))
#print all energies in MeV
beamE=120.0

m12C=11177.9292
m16O=14899.168598161144
m4He=3728.401315862896
m8Be=7456.894471212898
m14N=13043.780817
m24Mg=22341.924829

m2H=1876.12392312
m1H=938.783071355
m1n=939.565417991

ex8Be=3.04

m3He=2809.41351708

#Types of dictionaries
tP="particle"
tS="set" #particle set
tD="detector"
tI="initial"

#################################################
##########Particle dict quaternary sequential####
#################################################

####Working with this one 4 now################
# initDict={"type":tI,"name":"12C+12C","massP":m12C,
#           "massT":m12C,"ELab":beamE}
# oxyDict={"type":tP,"name":"16O","mass":m16O,"exE":6.0494}
# beDict={"type":tP,"name":"8Be","mass":m8Be,"exE":3.04}
# carbonDict={"type":tP,"name":"12C","mass":m12C,"exE":7.65}

# # alphaSysDict={"type":tS,"name":"4He+4He"}
# alphaADict={"type":tP,"name":"4HeA","mass":m4He}
# alphaBDict={"type":tP,"name":"4HeB","mass":m4He}
# alphaCDict={"type":tP,"name":"4HeC","mass":m4He}
# # alphaDDict={"type":tP,"name":"4He","mass":m4He}
# # alphaEDict={"type":tP,"name":"4He","mass":m4He}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(3),radians(6)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(15),radians(20)]}
# d3Dict={"type":tD,"name":"d3","angles":[radians(140),radians(20)]}
# # d4Dict={"type":tD,"name":"d4"}

# #Completing the dictionaries
# alphaBDict["dictList"]=[d3Dict,{}]
# alphaADict["dictList"]=[{},{}]
# alphaCDict["dictList"]=[d1Dict,{}]

# oxyDict["dictList"]=[alphaCDict,carbonDict]

# beDict["dictList"]=[alphaADict,alphaBDict]
# # alphaSysDict["dictList"]=[alphaADict,alphaBDict]
# carbonDict["dictList"]=[d2Dict,{}]

# initDict["dictList"]=[oxyDict,beDict]

#################################################
####Particle dict end quaternary sequential######
#################################################

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
##########Particle dict ternary direct########
##############################################
# beamE=350 #Lucia's case
# initDict={"type":tI,"name":"12C+24Mg","massP":m12C,
#           "massT":m24Mg,"ELab":beamE}
# carbonADict={"type":tP,"name":"12C_A","mass":m12C,"exE":7.60}

# carbonSysDict={"type":tS,"name":"12C+12C"}
# carbonCDict={"type":tP,"name":"12C_C","mass":m12C}
# carbonBDict={"type":tP,"name":"12C_B","mass":m12C}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(17),radians(15.0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(130),radians(50)]}

# #Completing the dictionaries
# carbonADict["dictList"]=[d1Dict,{}]
# carbonBDict["dictList"]=[d2Dict,{}]
# carbonCDict["dictList"]=[{},{}]

# carbonSysDict["dictList"]=[carbonBDict,carbonCDict]

# initDict["dictList"]=[carbonADict,carbonSysDict]

##############################################
##########Particle end dict ternary direct####
##############################################


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


##################################################
##########Particle dict ternary seq dpn###########
##################################################
beamE=100

initDict={"type":tI,"name":"d+d","massP":m2H,
          "massT":m2H,"ELab":beamE}
helium3Dict={"type":tP,"name":"3He","mass":m3He,"exE":18.5}

protonDict={"type":tP,"name":"p","mass":m1H}
deuteronDict={"type":tP,"name":"d","mass":m2H}
neutronDict={"type":tP,"name":"n","mass":m1n}

#Defining the detectors
d1Dict={"type":tD,"name":"d1","angles":[radians(17),radians(20)]}
d2Dict={"type":tD,"name":"d2","angles":[radians(10),radians(45)]}

#Completing the dictionaries
protonDict["dictList"]=[{},{}]
deuteronDict["dictList"]=[d1Dict,{}]
neutronDict["dictList"]=[d2Dict,{}]

helium3Dict["dictList"]=[deuteronDict,protonDict]
# # alphaSysDict["dictList"]=[alphaADict,alphaBDict]

initDict["dictList"]=[helium3Dict,neutronDict]

##################################################
##########Particle end dict ternary seq dpn#######
##################################################

#####################################################################
# # printTree(initDict)
# print("")

# # print("The final mass of 8Be is")
# # print(getFinalMass(beDict))
# print("")
# print("Now completing the tree")
# makeInitialTreeCompletion(initDict)

# # printTree(initDict)

# print("\n\nNow testing the free part route stuff\n")
# generalList=getDirectFreeRoute(initDict)
# print(colored(generalList,'red'))
# if generalList == []:
#     print("Error!!! Are you sure you filled \
#     the free part dict correctly?!")


# print("Trying to pull every line automatically")
# boolPull=pullEveryLine(initDict,generalList)

# # print("Printing the entire tree, without major sols")
# # printTree(initDict)

# fillBool=fillMajorSols(initDict,generalList)

# print(colored("Now printing only the tree sols part","red"))
# printTreeOnlySolsPart(initDict)


# print("Now the entire filled tree")
# printTree(initDict)

# print("")
# print("Now printing the oxygen node")
# printNode(oxyDict)

# print("")
# print("Now printing the alpha B node")
# printNode(alphaBDict)

# print("Testing the getLineParIdxsAndOffsets function for 0 and 1")
# myVal=getLineParIdxsAndOffsets(0,oxyDict)
# print(colored(myVal,"blue"))
# myVal=getLineParIdxsAndOffsets(1,oxyDict)
# print(colored(myVal,"blue"))
########################################################################


# print("Now the new cleanDict function")
# myBool=cleanDict(initDict,generalList)
# print("The bool val is ", myBool)

###################################################################
# print("Testing the getLineIdxFromSol function")
# myLocalLineIdx=getLineIdxFromSolIdx(1,'[0.0, 0.0, 7.326472906898222]',oxyDict)
# print("myLocalLineIdx = ", myLocalLineIdx)

# print("")
# print("Testing the getSimpleSecSolIdxL function")
# solsDict=oxyDict["solsDict"]
# simpleSecSolL=getSimpleSecSolIdxL('[0.0, 0.0, 7.326472906898222]',solsDict)
# print(simpleSecSolL)

# print("")
# print("Testing the getSimpleSecSolIdxWithNonesL function")
# secSolParentList=getSecSolParentIdxWithNonesL('[0.0, 0.0, 7.326472906898222]',oxyDict)
# print(secSolParentList)
#######################################################################

# print("")
# print("Testing the getThreeSecSolsIdxL function")
# secSolList=getThreeSecSolsIdxL(secSolParentList,oxyDict)
# for e in secSolList:
#     print(e)


# print("")
# print("Now testing the fillInitSecSols function on the oxyDict")
# fillInitSecSols(oxyDict)
# printNode(oxyDict)

# print("")
# print("Now testing the fillInitSecSols function on the alphaB")
# fillInitSecSols(alphaBDict)
# printNode(alphaBDict)

# print("")
# print(colored("Now testing the fillSecSols function on the alphaB","red"))
# fillSecSols(alphaBDict)
# printNode(alphaBDict)

# print("")
# print(colored("Now testing the fillSecSols function on the oxyDict","red"))
# fillSecSols(oxyDict)
# printNode(oxyDict)

# print("")
# print("Testing the getClosestIdx function")
# vLines=oxyDict["vLines"][0]
# print(getClosestIdx(np.array([2.63729793,0.93756194,11.78698489]),vLines))

##############################################################################
# print("")
# print("Calling the fillSecSolsAlongTree ")
# fillSecSolsAlongTree(initDict)
# #Printing the entire tree
# print("Printing the entire tree")
# printTree(initDict)

##############################################################################

makeTreeCompletion(initDict)
printTree(initDict)

print("")
print(colored("The energy print out function","yellow"))
printLastNodes(initDict)

print(colored(easyStr,"red"))


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


fig = plt.figure()
ax = fig.gca(projection='3d')

plt.xlim(-15, 15)
plt.ylim(-15, 15)

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
