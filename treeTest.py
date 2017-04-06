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
d1Dict={"type":tD,"name":"d1","angles":[radians(35),radians(24)]}
d2Dict={"type":tD,"name":"d2","angles":[radians(16),radians(56)]}
d3Dict={"type":tD,"name":"d3","angles":[radians(130),radians(24)]}
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

printTree(initDict)
print("")

# print("The final mass of 8Be is")
# print(getFinalMass(beDict))
print("")
print("Now completing the tree")
globalCompleteTree(initDict)

printTree(initDict)

print("\n\nNow testing the free part route stuff\n")
getDirectFreeRoute(initDict)
print(generalList)

print("trying to fill the oxyDict tree")
boolPull=pullLinesFromNode(oxyDict)
print(boolPull)
printTree(initDict)

# print("Testing the Q val function")
# print(getQVal(initDict))
