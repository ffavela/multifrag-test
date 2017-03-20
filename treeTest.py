from multifragStuff import *

#print all energies in MeV
beamE=60

m12C=11177.9292
m16O=14899.168598161144
m4He=3728.401315862896
m8Be=7456.894471212898

ex8Be=3.04

#Types of dictionaries
tP="particle"
tD="detector"
tI="initial"

#Particle dict
initDict={"type":tI,"name":"12C+12C","massP":m12C,
          "massT":m12C,"ELab":60.0}
oxyDict={"type":tP,"name":"16O","mass":m16O}
beDict={"type":tP,"name":"8Be","mass":m8Be,"exE":3.04}
alphaSysDict={"type":tP,"name":"4He+4He","mass":2*m4He}
alphaADict={"type":tP,"name":"4He","mass":m4He}
alphaBDict={"type":tP,"name":"4He","mass":m4He}

#Defining the detectors
d1Dict={"type":tD,"name":"d1"}
d2Dict={"type":tD,"name":"d2"}

#Completing the dictionaries
alphaBDict["dictList"]=[{},{}]
alphaADict["dictList"]=[d2Dict,{}]

oxyDict["dictList"]=[d1Dict,{}]
beDict["dictList"]=[alphaADict,alphaBDict]
alphaSysDict["dictList"]=[alphaADict,alphaBDict]

initDict["dictList"]=[oxyDict,beDict]
# initDict["dictList"]=[oxyDict,alphaSysDict]

# treeStruct=[alphaADict,[d1Dict,{}]]

# printTree(initDict)
print("")

# print("The final mass of 8Be is")
# print(getFinalMass(beDict))
print("")
# print("Now completing the tree")
globalCompleteTree(initDict)

printTree(initDict)

# print("Testing the Q val function")
# print(getQVal(initDict))
