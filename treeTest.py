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

#Types of dictionaries
tP="particle"
tS="set" #particle set
tD="detector"
tI="initial"

#################################################
##########Particle dict quaternary sequential####
#################################################

###############Working with this one 4 now################
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
# d2Dict={"type":tD,"name":"d2","angles":[radians(35),radians(20)]}
# d3Dict={"type":tD,"name":"d3","angles":[radians(80),radians(140)]}
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

#################################################
##########Particle dict five part sequential#####
#################################################

# initDict={"type":tI,"name":"12C+12C","massP":m12C,
#           "massT":m12C,"ELab":beamE}
# oxyDict={"type":tP,"name":"16O","mass":m16O,"exE":6.0494}
# be8ADict={"type":tP,"name":"8BeA","mass":m8Be,"exE":0.0}
# be8BDict={"type":tP,"name":"8BeB","mass":m8Be,"exE":0.0}
# carbonDict={"type":tP,"name":"12C","mass":m12C,"exE":7.65}

# # alphaSysDict={"type":tS,"name":"4He+4He"}
# alphaADict={"type":tP,"name":"4HeA","mass":m4He}
# alphaBDict={"type":tP,"name":"4HeB","mass":m4He}
# alphaCDict={"type":tP,"name":"4HeC","mass":m4He}
# alphaDDict={"type":tP,"name":"4HeD","mass":m4He}
# # alphaDDict={"type":tP,"name":"4He","mass":m4He}
# # alphaEDict={"type":tP,"name":"4He","mass":m4He}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(4),radians(6)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(35),radians(30)]}
# d3Dict={"type":tD,"name":"d3","angles":[radians(90),radians(220)]}
# d4Dict={"type":tD,"name":"d4","angles":[radians(40),radians(19)]}
# # d4Dict={"type":tD,"name":"d4"}

# #Completing the dictionaries
# alphaBDict["dictList"]=[d3Dict,{}]
# alphaADict["dictList"]=[{},{}]
# alphaCDict["dictList"]=[d1Dict,{}]
# alphaDDict["dictList"]=[d2Dict,{}]
# be8BDict["dictList"]=[d4Dict,{}]

# oxyDict["dictList"]=[carbonDict,alphaCDict]

# be8ADict["dictList"]=[alphaADict,alphaBDict]
# # alphaSysDict["dictList"]=[alphaADict,alphaBDict]
# carbonDict["dictList"]=[alphaDDict,be8BDict]

# initDict["dictList"]=[oxyDict,be8ADict]

#################################################
####Particle dict end five part sequential#######
#################################################

#################################################
##########Particle dict six part sequential#####
#################################################

initDict={"type":tI,"name":"12C+12C","massP":m12C,
          "massT":m12C,"ELab":beamE}

oxyDict={"type":tP,"name":"16O","mass":m16O,"exE":6.0494}
be8ADict={"type":tP,"name":"8BeA","mass":m8Be,"exE":0.0}
be8BDict={"type":tP,"name":"8BeB","mass":m8Be,"exE":0.0}
carbonDict={"type":tP,"name":"12C","mass":m12C,"exE":7.65}

# alphaSysDict={"type":tS,"name":"4He+4He"}
alphaADict={"type":tP,"name":"4HeA","mass":m4He}
alphaBDict={"type":tP,"name":"4HeB","mass":m4He}
alphaCDict={"type":tP,"name":"4HeC","mass":m4He}
alphaDDict={"type":tP,"name":"4HeD","mass":m4He}
alphaEDict={"type":tP,"name":"4HeE","mass":m4He}
alphaFDict={"type":tP,"name":"4HeF","mass":m4He}
# alphaDDict={"type":tP,"name":"4He","mass":m4He}
# alphaEDict={"type":tP,"name":"4He","mass":m4He}

#Defining the detectors
d1Dict={"type":tD,"name":"d1","angles":[radians(4),radians(6)]}
d2Dict={"type":tD,"name":"d2","angles":[radians(35),radians(30)]}
d3Dict={"type":tD,"name":"d3","angles":[radians(90),radians(220)]}
d4Dict={"type":tD,"name":"d4","angles":[radians(40),radians(19)]}
d5Dict={"type":tD,"name":"d5","angles":[radians(57),radians(13)]}
# d4Dict={"type":tD,"name":"d4"}

#Completing the dictionaries
alphaBDict["dictList"]=[d3Dict,{}]
alphaADict["dictList"]=[{},{}]
alphaCDict["dictList"]=[d1Dict,{}]
alphaDDict["dictList"]=[d2Dict,{}]
alphaEDict["dictList"]=[d4Dict,{}]
alphaFDict["dictList"]=[d5Dict,{}]

be8BDict["dictList"]=[alphaEDict,alphaFDict]

oxyDict["dictList"]=[carbonDict,alphaCDict]

be8ADict["dictList"]=[alphaADict,alphaBDict]
# alphaSysDict["dictList"]=[alphaADict,alphaBDict]
carbonDict["dictList"]=[alphaDDict,be8BDict]

initDict["dictList"]=[oxyDict,be8ADict]

#################################################
####Particle dict end six part sequential########
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


# ##############################################
# ##########Particle dict binary################
# ##############################################
# beamE=50.0
# initDict={"type":tI,"name":"d+14N","massP":m2H,
#           "massT":m14N,"ELab":beamE}

# carbonDict={"type":tP,"name":"12C","mass":m12C,"exE":10.84}

# alphaDict={"type":tP,"name":"4He","mass":m4He}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(51.31),radians(152.68)]}

# #Completing the dictionaries
# carbonDict["dictList"]=[{},{}]
# alphaDict["dictList"]=[d1Dict,{}]

# initDict["dictList"]=[carbonDict,alphaDict]

# ##############################################
# ##########Particle dict end binary############
# ##############################################

##############################################
##########Particle dict alphas################
##############################################
# beamE=50.0
# initDict={"type":tI,"name":"d+14N","massP":m2H,
#           "massT":m14N,"ELab":beamE}

# carbonDict={"type":tP,"name":"12C","mass":m12C,"exE":7.65}
# be8Dict={"type":tP,"name":"8Be","mass":m8Be,"exE":0.0}

# alphaADict={"type":tP,"name":"4HeA","mass":m4He}
# alphaBDict={"type":tP,"name":"4HeB","mass":m4He}
# alphaCDict={"type":tP,"name":"4HeC","mass":m4He}
# alphaDDict={"type":tP,"name":"4HeD","mass":m4He}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(51.31),radians(152.68)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(51.31),radians(2.6)]}
# d3Dict={"type":tD,"name":"d3","angles":[radians(31.46),radians(340.2)]}

# #Completing the dictionaries
# alphaADict["dictList"]=[d1Dict,{}]
# alphaBDict["dictList"]=[{},{}]
# alphaCDict["dictList"]=[d3Dict,{}]
# alphaDDict["dictList"]=[{},{}]
# be8Dict["dictList"]=[{},d2Dict]

# carbonDict["dictList"]=[alphaBDict,be8Dict]
# initDict["dictList"]=[carbonDict,alphaADict]

##############################################
##########Particle dict end alphas############
##############################################


##################################################
##########Particle dict ternary seq dpn###########
##################################################
# beamE=100

# initDict={"type":tI,"name":"d+d","massP":m2H,
#           "massT":m2H,"ELab":beamE}
# helium3Dict={"type":tP,"name":"3He","mass":m3He,"exE":18.5}

# protonDict={"type":tP,"name":"p","mass":m1H}
# deuteronDict={"type":tP,"name":"d","mass":m2H}
# neutronDict={"type":tP,"name":"n","mass":m1n}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(17),radians(20)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(12),radians(49)]}

# #Completing the dictionaries
# protonDict["dictList"]=[{},{}]
# deuteronDict["dictList"]=[d1Dict,{}]
# neutronDict["dictList"]=[d2Dict,{}]

# helium3Dict["dictList"]=[deuteronDict,protonDict]
# # # alphaSysDict["dictList"]=[alphaADict,alphaBDict]

# initDict["dictList"]=[helium3Dict,neutronDict]

##################################################
##########Particle end dict ternary seq dpn#######
##################################################

##################################################
##########Particle dict ternary 6He case protons detect##########
##################################################
# beamE=67.2

# initDict={"type":tI,"name":"a+t","massP":m4He,
#           "massT":m3H,"ELab":beamE}
# helium6Dict={"type":tP,"name":"6He","mass":m6He,"exE":18.60}

# protonDict={"type":tP,"name":"p","mass":m1H}
# tritium1Dict={"type":tP,"name":"t1","mass":m3H}
# tritium2Dict={"type":tP,"name":"t2","mass":m3H}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(21),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(15),radians(180)]}

# #Completing the dictionaries
# protonDict["dictList"]=[d1Dict,{}]
# tritium1Dict["dictList"]=[d2Dict,{}]
# tritium2Dict["dictList"]=[{},{}]

# helium6Dict["dictList"]=[tritium1Dict,tritium2Dict]

# initDict["dictList"]=[protonDict,helium6Dict]

##################################################
##########Particle end dict ternary 6He case protons detect######
##################################################

##################################################
##########Particle dict ternary direct (no 6He) case##########
##################################################

# ##There appears to be no solutions, not even with proton conf

# beamE=67.2

# initDict={"type":tI,"name":"a+t","massP":m4He,
#           "massT":m3H,"ELab":beamE}
# # helium6Dict={"type":tP,"name":"6He","mass":m6He,"exE":15.80}
# pTSysDict={"type":tP,"name":"(p+t)"}

# protonDict={"type":tP,"name":"p","mass":m1H}
# tritium1Dict={"type":tP,"name":"t1","mass":m3H}
# tritium2Dict={"type":tP,"name":"t2","mass":m3H}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(20),radians(180)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(21),radians(0)]}

# #Completing the dictionaries
# protonDict["dictList"]=[{},{}]
# tritium1Dict["dictList"]=[d1Dict,{}]
# tritium2Dict["dictList"]=[d2Dict,{}]

# pTSysDict["dictList"]=[tritium1Dict,tritium2Dict]
# # # alphaSysDict["dictList"]=[alphaADict,alphaBDict]

# initDict["dictList"]=[protonDict,pTSysDict]

##################################################
##########Particle end dict ternary direct (no 6He) case######
##################################################

##################################################
##########Particle dict ternary 6He case tritons##########
##################################################
# beamE=67.2

# initDict={"type":tI,"name":"a+t","massP":m4He,
#           "massT":m3H,"ELab":beamE}
# helium6Dict={"type":tP,"name":"6He","mass":m6He,"exE":18.6}

# #The actual state seems to be 15.8 for iii, with a contribution in
# #18.67 and 9.4 in the spectra fig4(b).

# #Same fig the peaks at 13.73,28.11,9.5 and 30.8 seem to come from the
# #18.6 *6He excitation level.

# #Notice the overlap of peaks below the 10MeV part.

# #Was not able to reproduce any *4He decay fragmentation.

# protonDict={"type":tP,"name":"p","mass":m1H}
# tritium1Dict={"type":tP,"name":"t1","mass":m3H,"exE":0.0}
# tritium2Dict={"type":tP,"name":"t2","mass":m3H,"exE":0.0}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(20),radians(180)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(21),radians(0)]}

# #Completing the dictionaries
# protonDict["dictList"]=[{},{}]
# tritium1Dict["dictList"]=[d1Dict,{}]
# tritium2Dict["dictList"]=[d2Dict,{}]

# helium6Dict["dictList"]=[tritium1Dict,tritium2Dict]


# initDict["dictList"]=[protonDict,helium6Dict]

##################################################
##########Particle end dict ternary 6He case tritons######
##################################################

##################################################
##Particle dict ternary 6He case protons alphas##########
##################################################

##There appears to be no solutions, not even with proton conf

# beamE=67.2

# initDict={"type":tI,"name":"a+t","massP":m4He,
#           "massT":m3H,"ELab":beamE}
# # helium6Dict={"type":tP,"name":"6He","mass":m6He,"exE":15.5}
# helium4Dict={"type":tP,"name":"4He","mass":m4He,"exE":20.20}
# #The actual state seems 2 be

# tritium1Dict={"type":tP,"name":"t1","mass":m3H}
# tritium2Dict={"type":tP,"name":"t2","mass":m3H}
# protonDict={"type":tP,"name":"p","mass":m1H}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(21),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(15),radians(180)]}

# #Completing the dictionaries
# protonDict["dictList"]=[d1Dict,{}]
# tritium1Dict["dictList"]=[{},{}]
# tritium2Dict["dictList"]=[d2Dict,{}]

# helium4Dict["dictList"]=[protonDict,tritium1Dict]
# # # alphaSysDict["dictList"]=[alphaADict,alphaBDict]

# initDict["dictList"]=[tritium1Dict,helium4Dict]

##################################################
##Particle end dict ternary 6He case protons alphas######
##################################################

# ##############################################
# ##########Particle dict giuseppe nancy ternary direct########
# ##############################################
# beamE=56.0 #Originally 58 but beam lost approx 2MeV in target

# initDict={"type":tI,"name":"23Na+d","massP":m23Na,
#           "massT":m2H,"ELab":beamE}
# neon20Dict={"type":tP,"name":"20Ne","mass":m20Ne,"exE":0.0}
# #1.1 not reported...

# neutNeonSysDict={"type":tS,"name":"n+20Ne"}
# # neutNeonSysDict={"type":tS,"name":"n+20Ne","mass":(m1n+m20Ne)}
# # neon21Dict={"type":tS,"name":"21Ne","mass":m21Ne,"exE":7.35}

# alphaADict={"type":tP,"name":"4HeA","mass":m4He}
# neutronDict={"type":tP,"name":"n","mass":m1n}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(7),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(22),radians(180)]}

# #Completing the dictionaries
# neon20Dict["dictList"]=[d1Dict,{}]
# alphaADict["dictList"]=[d2Dict,{}]
# neutronDict["dictList"]=[{},{}]

# neutNeonSysDict["dictList"]=[neutronDict,neon20Dict]
# # neon21Dict["dictList"]=[neutronDict,neon20Dict]

# initDict["dictList"]=[alphaADict,neutNeonSysDict]
# # initDict["dictList"]=[alphaADict,neon21Dict]

# ##############################################
# ##########Particle end dict giuseppe nancy ternary direct####
# ##############################################

##############################################
##########Particle dict giuseppe nancy ternary seq########
##############################################
# beamE=56.0

# initDict={"type":tI,"name":"23Na+d","massP":m23Na,
#           "massT":m2H,"ELab":beamE}
# neon20Dict={"type":tP,"name":"20Ne","mass":m20Ne,"exE":0.0}
# #1.1 not reported...

# # neutNeonSysDict={"type":tS,"name":"n+20Ne"}
# mag24Dict={"type":tS,"name":"24Mg","mass":m24Mg,"exE":11.0}

# alphaADict={"type":tP,"name":"4HeA","mass":m4He}
# neutronDict={"type":tP,"name":"n","mass":m1n}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(7),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(22),radians(180)]}

# #Completing the dictionaries
# neon20Dict["dictList"]=[d1Dict,{}]
# alphaADict["dictList"]=[d2Dict,{}]
# neutronDict["dictList"]=[{},{}]

# # neutNeonSysDict["dictList"]=[neutronDict,neon20Dict]
# mag24Dict["dictList"]=[alphaADict,neon20Dict]

# # initDict["dictList"]=[alphaADict,neutNeonSysDict]
# initDict["dictList"]=[neutronDict,mag24Dict]

##############################################
##########Particle end dict giuseppe nancy ternary seq####
##############################################

##############################################
##########Particle dict  ternary direct THM###
##############################################
# beamE=35.5

# initDict={"type":tI,"name":"d+t","massP":m2H,
#           "massT":m3H,"ELab":beamE}
# neutronDict={"type":tP,"name":"1n","mass":m1n,"exE":0.0}

# deuteron1Dict={"type":tP,"name":"deut1","mass":m2H}
# deuteron2Dict={"type":tP,"name":"deut2","mass":m2H}
# # dSysDict={"type":tP,"name":"dSys","mass":2*m2H}
# alphaDict={"type":tP,"name":"alpha","mass":m4He,"exE":23.10}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(20),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(40),radians(180)]}

# #alpha ex=24.1 angle 20...

# #Completing the dictionaries
# neutronDict["dictList"]=[{},{}]
# deuteron1Dict["dictList"]=[d1Dict,{}]
# deuteron2Dict["dictList"]=[d2Dict,{}]

# # dSysDict["dictList"]=[deuteron1Dict,deuteron2Dict]
# alphaDict["dictList"]=[deuteron1Dict,deuteron2Dict]


# # initDict["dictList"]=[neutronDict,dSysDict]
# initDict["dictList"]=[neutronDict,alphaDict]

##############################################
#####Particle end dict  ternary direct THM####
##############################################


# ##############################################
# ##########Particle dict lamia ternary direct########
# ##############################################
# #Apparently no sols
# beamE=27.0

# initDict={"type":tI,"name":"d+11B","massP":m2H,
#           "massT":m11B,"ELab":beamE}

# alphaDict={"type":tP,"name":"alpha","mass":m4He,"exE":0.0}

# neutBe8SysDict={"type":tS,"name":"n+8Be"}
# be8Dict={"type":tP,"name":"8Be","mass":m8Be,"exE":0.0}

# neutronDict={"type":tP,"name":"1n","mass":m1n}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(52),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(16),radians(180)]}

# #Completing the dictionaries
# be8Dict["dictList"]=[d2Dict,{}]
# alphaDict["dictList"]=[d1Dict,{}]
# neutronDict["dictList"]=[{},{}]

# # neutNeonSysDict["dictList"]=[neutronDict,neon20Dict]
# neutBe8SysDict["dictList"]=[be8Dict,neutronDict]

# # initDict["dictList"]=[alphaADict,neutNeonSysDict]
# initDict["dictList"]=[alphaDict,neutBe8SysDict]

# ##############################################
# ##########Particle end dict lamia ternary direct####
# ##############################################


##############################################
##########Particle dict lamia ternary seq########
##############################################
# beamE=27.0

# initDict={"type":tI,"name":"d+11B","massP":m2H,
#           "massT":m11B,"ELab":beamE}

# alphaDict={"type":tP,"name":"alpha","mass":m4He,"exE":0.0}

# be9Dict={"type":tP,"name":"9Be","mass":m9Be,"exE":3.04}
# be8Dict={"type":tP,"name":"8Be","mass":m8Be,"exE":0.0}

# neutronDict={"type":tP,"name":"1n","mass":m1n}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(132),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(16),radians(180)]}

# #Completing the dictionaries
# be8Dict["dictList"]=[d2Dict,{}]
# alphaDict["dictList"]=[d1Dict,{}]
# neutronDict["dictList"]=[{},{}]

# # neutNeonSysDict["dictList"]=[neutronDict,neon20Dict]
# be9Dict["dictList"]=[be8Dict,neutronDict]
# # be9Dict["dictList"]=[{},{}]

# # initDict["dictList"]=[alphaADict,neutNeonSysDict]
# initDict["dictList"]=[alphaDict,be9Dict]

##############################################
##########Particle end dict lamia ternary seq####
##############################################


##############################################
##########Particle dict  BUG HERE#############
##############################################
# beamE=35.5

# initDict={"type":tI,"name":"d+t","massP":m2H,
#           "massT":m3H,"ELab":beamE}
# neutronDict={"type":tP,"name":"1n","mass":m1n,"exE":0.0}

# deuteron1Dict={"type":tP,"name":"deut1","mass":m2H}
# deuteron2Dict={"type":tP,"name":"deut2","mass":m2H}
# # dSysDict={"type":tP,"name":"dSys","mass":2*m2H}
# alphaDict={"type":tP,"name":"alpha","mass":m4He,"exE":32.0}

# #Defining the detectors
# d1Dict={"type":tD,"name":"d1","angles":[radians(20),radians(0)]}
# d2Dict={"type":tD,"name":"d2","angles":[radians(40),radians(180)]}

# #Completing the dictionaries
# neutronDict["dictList"]=[{},{}]
# deuteron1Dict["dictList"]=[d1Dict,{}]
# deuteron2Dict["dictList"]=[d2Dict,{}]

# # dSysDict["dictList"]=[deuteron1Dict,deuteron2Dict]
# alphaDict["dictList"]=[deuteron1Dict,deuteron2Dict]


# # initDict["dictList"]=[neutronDict,dSysDict]
# initDict["dictList"]=[neutronDict,alphaDict]

##############################################
#####Particle end dict BUG HERE###############
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
