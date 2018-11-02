from multifragStuff import *

print(colored(easyStr,"blue"))
#print all energies in MeV
beamE=1904.0

m12C=11177.9292
m68Ni=63278.13497892765
m67Ni=62346.36201288145
m1n=939.565417991

#Types of dictionaries
tP="particle"
tS="set" #particle set
tD="detector"
tI="initial"


##################################################
########## Example 4 Nancy 1 #####################
##################################################
initDict={"type":tI,"name":"68Ni+12C","massP":m68Ni,
          "massT":m12C,"ELab":beamE}
nickel68Dict={"type":tP,"name":"68Ni","mass":m68Ni,"exE":10.0}
nickel67Dict={"type":tP,"name":"67Ni","mass":m67Ni,"exE":0.0}

carbon12Dict={"type":tP,"name":"12C","mass":m12C,"exE":0.0}
neutron1Dict={"type":tP,"name":"n1","mass":m1n,"exE":0.0}

#Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(6.6),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(65.6),radians(180)]}

d1Dict={"type":tD,"name":"d1","angles":[radians(2.2),radians(0)]}
d2Dict={"type":tD,"name":"d2","angles":[radians(78.8),radians(180)]}

#Completing the dictionaries
nickel68Dict["dictList"]=[nickel67Dict,neutron1Dict]
nickel67Dict["dictList"]=[d1Dict,{}]
carbon12Dict["dictList"]=[d2Dict,{}]
neutron1Dict["dictList"]=[{},{}]

initDict["dictList"]=[carbon12Dict,nickel68Dict]

######################################################
########## Example 4 Nancy 1 #########################
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
