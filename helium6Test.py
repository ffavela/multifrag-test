from multifragStuff import *

print(colored(easyStr,"blue"))
#print all energies in MeV
beamE=67.2
m6He=5606.55669604
m4He=3728.401315862896
m3He=2809.41351708

m3H=2809.43210768
m2H=1876.12392312
m1H=938.783071355
m1n=939.565417991

#Types of dictionaries
tP="particle"
tS="set" #particle set
tD="detector"
tI="initial"


##################################################
##########Particle dict ternary 6He case tritons##########
##################################################
initDict={"type":tI,"name":"a+t","massP":m4He,
          "massT":m3H,"ELab":beamE}
# helium6Dict={"type":tP,"name":"6He","mass":m6He,"exE":18.6}
helium6Dict={"type":tP,"name":"6He","mass":m6He,"exE":15.5}
#The actual state seems to be 15.8 for iii, with a contribution in
#18.67 and 9.4 in the spectra fig4(b).

#Same fig the peaks at 13.73,28.11,9.5 and 30.8 seem to come from the
#18.6 *6He excitation level.

#Notice the overlap of peaks below the 10MeV part.

#Was not able to reproduce any *4He decay fragmentation.

protonDict={"type":tP,"name":"p","mass":m1H}

#Defining the detectors
d1Dict={"type":tD,"name":"d1","angles":[radians(3.2424),radians(0)]}


#Completing the dictionaries
protonDict["dictList"]=[{},{}]

helium6Dict["dictList"]=[d1Dict,{}]


initDict["dictList"]=[protonDict,helium6Dict]

######################################################
##########Particle end dict ternary 6He case tritons######
##################################################

makeTreeCompletion(initDict)
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
