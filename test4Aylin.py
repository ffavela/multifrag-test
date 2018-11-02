from multifragStuff import *

print(colored(easyStr,"blue"))
#print all energies in MeV
beamE=53.0

m4He=3728.401315862896
mt=2809.4321076824253
m1n=939.565417991
m1H=938.7830713545549

#Types of dictionaries
tP="particle"
tS="set" #particle set
tD="detector"
tI="initial"


##################################################
########## Example 4 Aylin 1 #####################
##################################################
initDict={"type":tI,"name":"a+a","massP":m4He,
          "massT":m4He,"ELab":beamE}
alpha1Dict={"type":tP,"name":"4He_1","mass":m4He,"exE":0.0}
alpha2Dict={"type":tP,"name":"4He_2","mass":m4He,"exE":20.3}

# neutron1Dict={"type":tP,"name":"n1","mass":m1n,"exE":0.0}
protonDict={"type":tP,"name":"p1","mass":m1H,"exE":0.0}
tritonDict={"type":tP,"name":"t1","mass":mt,"exE":0.0}

#Defining the detectors
d1Dict={"type":tD,"name":"d1","angles":[radians(0.0),radians(0)]}
d2Dict={"type":tD,"name":"d2","angles":[radians(30.0),radians(180)]}

#Completing the dictionaries
alpha1Dict["dictList"]=[d1Dict,{}]
protonDict["dictList"]=[d2Dict,{}]
alpha2Dict["dictList"]=[protonDict,tritonDict]
tritonDict["dictList"]=[{},{}]
# neutron1Dict["dictList"]=[{},{}]

initDict["dictList"]=[alpha1Dict,alpha2Dict]

######################################################
########## Example 4 Aylin 1 #########################
######################################################

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
