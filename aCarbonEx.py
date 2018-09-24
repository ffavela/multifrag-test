from multifragStuff import *

print(colored(easyStr,"blue"))
#print all energies in MeV
beamE=120.0
m11B=10255.1029833
m12C=11177.9292
m16O=14899.168598161144
m6He=5606.55669604
m4He=3728.401315862896
m9Be=8394.79535317
m8Be=7456.894471212898
m14N=13043.780817
m24Mg=22341.924829
m23Na=21414.8344465
m21Ne=19555.6443234
m20Ne=18622.8400687

m3H=2809.43210768
m2H=1876.12392312
m1H=938.783071355
m1n=939.565417991

ex8Be=3.04

m3He=2809.41351708

m7Be=6536.227700006069
m8He=7483.562484072099

#Types of dictionaries
tP="particle"
tS="set" #particle set
tD="detector"
tI="initial"

##############################################
##########Particle dict tree definition#######
##############################################
beamE=64.0

initDict={"type":tI,"name":"a+12C","massP":m4He,
          "massT":m12C,"ELab":beamE}
alphaADict={"type":tP,"name":"4He_A","mass":m4He,"exE":0.0}

carbon12Dict={"type":tP,"name":"12C","mass":m12C,"exE":10.3}

alphaBDict={"type":tP,"name":"4He_B","mass":m4He,"exE":0.0}
alphaCDict={"type":tP,"name":"4He_C","mass":m4He,"exE":0.0}
alphaDDict={"type":tP,"name":"4He_D","mass":m4He,"exE":0.0}

be8Dict={"type":tP,"name":"8Be","mass":m8Be,"exE":0.0}

#Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(47.82),radians(180)]}
d1Dict={"type":tD,"name":"d1","angles":[radians(70.82),radians(180)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(35.2),radians(180)]}
d2Dict={"type":tD,"name":"d2","angles":[radians(34.9),radians(180)]}
d3Dict={"type":tD,"name":"d3","angles":[radians(35.4),radians(180)]}

#Completing the dictionaries
alphaADict["dictList"]=[{},{}]
carbon12Dict["dictList"]=[alphaBDict,be8Dict]

alphaBDict["dictList"]=[d1Dict,{}]
# be8Dict["dictList"]=[d2Dict,{}]
be8Dict["dictList"]=[alphaCDict,alphaDDict]

alphaCDict["dictList"]=[d2Dict,{}]
alphaDDict["dictList"]=[d3Dict,{}]

initDict["dictList"]=[alphaADict,carbon12Dict]

##############################################
#####Particle end dict tree definition########
##############################################


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

genSimpVCMD=getGeneralSimplifiedVCMD(initDict)
print(genSimpVCMD)
print(colored(easyStr,"red"))

# printTree(initDict)
# printTreeOnlyCleanSolsPart(initDict)

############################################
####The plotting part#######################
############################################

fig = plt.figure()
ax = fig.gca(projection='3d')


fig_size = plt.rcParams["figure.figsize"]
print("The figsize is = ",fig_size)
# Set figure width to 9 and height to 9, a square
fig_size[0] = 8
fig_size[1] = 4
plt.rcParams["figure.figsize"] = fig_size
print("The new figsize is = ",fig_size)

plt.xlim(-15, 15)
plt.ylim(-15, 15)

plotAllLines(initDict,ax)
ax.legend()

modifyAx4Arrows(ax,genSimpVCMD)

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)

ax.set_zlim3d(-15, 15)

plt.show()

############################################
####The plotting part finish################
############################################
