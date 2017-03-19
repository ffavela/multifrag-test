from math import *
c=299792458 #in m/s
#Masses in MeV/c^2
def getEcm(mE1,mE2,E1L):
    vels=getVelcm(mE1,mE2,E1L)
    # mE1=getEMass(iso1)
    # mE2=getEMass(iso2)
    #Alternative way
    # mu=mE1*mE2/(mE1+mE2)
    # rVel=vels[0]-vels[1]
    # print 1.0/2.0*mu*rVel**2
    E1cm=0.5*(vels[0]/c)**2*mE1
    E2cm=0.5*(vels[1]/c)**2*mE2
    Ecm=E1cm+E2cm
    return E1cm,E2cm,Ecm

def getEcmsFromECM2(m1,m2,ECM):
    #For example, in a decay ECM=Q
    # m1=getEMass(iso1)
    # m2=getEMass(iso2)
    mu=1.0*m1*m2/(m1+m2)
    P=sqrt(2.0*mu*ECM)/c
    E1=0.5*(P*c)**2/m1
    E2=0.5*(P*c)**2/m2
    return E1,E2

def getAvailEnergy(m1,m2,m3,m4,E1L,E2L=0):
    E1cm,E2cm,Ecm=getEcm(m1,m2,E1L)
    Q=getQVal(m1,m2,m3,m4)
    return Ecm+Q

def getAvailEnergy0(m1,me1,me2,Ecm):
    Q=getQVal(m1,0,me2,me2)
    return Ecm+Q

def getAllVs(iso1,iso2,isoE,isoR,E1L):
    v1cm,v2cm,Vcm=getVelcm(iso1,iso2,E1L)
    EcmAvail=getAvailEnergy(iso1,iso2,isoE,isoR,E1L)
    ejectE,resE=getEcmsFromECM(isoE,isoR,EcmAvail)
    print(ejectE,resE)
    vE=sqrt(2.0*ejectE/getEMass(isoE))*c
    vR=sqrt(2.0*resE/getEMass(isoR))*c

def getVelcm(m1,m2,E1):
    # m1=getEMass(iso1)
    # m2=getEMass(iso2)
    v1=sqrt(2.0*E1/m1)*c
    v2=0 #assuming it is still
    Vcm=(1.0*v1*m1+1.0*v2*m2)/(m1+m2)
    v1p=v1-Vcm
    v2p=v2-Vcm
    return v1p,v2p,Vcm

def getQVal(m1,m2,m3,m4):
    Q=(m1+m2-m3-m4)
    return Q

#Not using relativistic case here
def getSimpleVels(m1,E1cm,m2,E2cm):
    v1cm=sqrt(2.0*E1cm/m1)
    v2cm=sqrt(2.0*E2cm/m2)
    return v1cm,v2cm

def printTree(treeDict):
    if treeDict == {}:
        return

    # print(treeDict)
    print("")
    print("name is ", treeDict["name"])

    if "dictList" not in treeDict:
        return

    for e in treeDict:
        if e != "name" and e != "dictList":
            print(e,treeDict[e])

    print("The child names are")
    printChildNames(treeDict["dictList"])

    for e in treeDict["dictList"]:
        printTree(e)

def printChildNames(dictList):
    for i in range(len(dictList)):
        if "name" not in dictList[i]:
            continue
        print(dictList[i]["name"])


def getFinalMass(dictNode):
    if "mass" not in dictNode:
        return None

    m=dictNode["mass"]
    if "exE" not in dictNode:
        myExE=0
    else:
        myExE=dictNode["exE"]

    m+=myExE
    return m

def globalCompleteTree(treeDict):
    treeDict["mass"]=treeDict["massP"]+treeDict["massT"]
    mPro=treeDict["massP"]
    mTar=treeDict["massT"]
    ELab=treeDict["ELab"]
    initEcm=getEcm(mPro,mTar,ELab)[2]
    treeDict["Ecm"]=initEcm
    completeTree0(treeDict)
    completeTree1(treeDict)

def completeTree0(treeDict):
    if treeDict == {}:
        return

    finalMass=getFinalMass(treeDict)
    if finalMass != None:
        treeDict["fMass"]=finalMass

    qVal=getQVal(treeDict)
    if qVal != None:
        print("filling tree with", qVal)
        treeDict["Q"]=qVal

    if "dictList" not in treeDict:
        return

    for e in treeDict["dictList"]:
        completeTree0(e)

def completeTree1(treeDict):
    if treeDict == {}:
        return

    qVal=getQVal(treeDict)
    if qVal != None:
        treeDict["Q"]=qVal

    if "dictList" not in treeDict:
        return

    for e in treeDict["dictList"]:
        completeTree1(e)


def getQVal(dictNode):
    if "fMass" not in dictNode:
        return None

    if "dictList" not in dictNode:
        return None

    for e in dictNode["dictList"]:
        if "fMass" not in e:
            return None

    finalMass=dictNode["fMass"]
    daugthersMass=0
    for e in dictNode["dictList"]:
        daugthersMass+=e["fMass"]

    Q=finalMass-daugthersMass
    return Q

# def getEcmFromNode(dictNode):
