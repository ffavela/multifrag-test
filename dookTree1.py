from multifragStuff import *

print(colored(easyStr,"blue"))
#print all energies in MeV
beamE=50.0

m4He=3728.401315862896
m3He=2809.41351708

m3H=2809.43210768
m2H=1876.12392312
m1H=938.783071355

m9B=8395.86338939857
m9Be=8394.795353167417
m8Be=7456.894471212898
m5Li=4669.14938672698

#Types of dictionaries
tP="particle"
tS="set" #particle set
tD="detector"
tI="initial"


##################################################
##########Particle dict ternary 6He case tritons##########
##################################################
initDict={"type":tI,"name":"3He+9Be","massP":m3He,
          "massT":m9Be,"ELab":beamE}

protonDict={"type":tP,"name":"p","mass":m1H}

alpha1Dict={"type":tP,"name":"a1","mass":m4He,"exE":0.0}
alpha2Dict={"type":tP,"name":"a2","mass":m4He,"exE":0.0}

tritiumDict={"type":tP,"name":"t","mass":m3H,"exE":0.0}

boron9Dict={"type":tP,"name":"9B","mass":m9B,"exE":11.7}

berillium8Dict={"type":tP,"name":"8Be","mass":m8Be,"exE":3.04}
#Defining the detectors
d1Dict={"type":tD,"name":"d1","angles":[radians(0),radians(0)]}
d2Dict={"type":tD,"name":"d2","angles":[radians(140),radians(180)]}
d3Dict={"type":tD,"name":"d3","angles":[radians(23),radians(0)]}

#Completing the dictionaries
protonDict["dictList"]=[d3Dict,{}]
tritiumDict["dictList"]=[d1Dict,{}]

alpha1Dict["dictList"]=[{},{}]
alpha2Dict["dictList"]=[d2Dict,{}]

berillium8Dict["dictList"]=[alpha1Dict,alpha2Dict]
# berillium8Dict["dictList"]=[{},{}]
boron9Dict["dictList"]=[berillium8Dict,protonDict]

initDict["dictList"]=[tritiumDict,boron9Dict]

######################################################
##########Particle end dict ternary 6He case tritons######
##################################################

makeTreeCompletion(initDict)
# makeInitialTreeCompletion(initDict)
printTree(initDict)

print("")
print(colored("The energy print out function","yellow"))
printLastNodes(initDict)

genSimpVCMD=getGeneralSimplifiedVCMD(initDict)
print(genSimpVCMD)
print(colored(easyStr,"red"))

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
