from math import *
import numpy as np

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

import copy

from termcolor import colored

easyStr="#"*50

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

#Not using relativistic case here, these are betas (v/c)
def getSimpleVels(m1,E1cm,m2,E2cm):
    v1cm=sqrt(2.0*E1cm/m1)
    v2cm=sqrt(2.0*E2cm/m2)
    return v1cm,v2cm

def printNode(nodeFromTree):
    if nodeFromTree == {}:
        return

    # print(binTreeDict)
    print("")
    print("name is ", nodeFromTree["name"])

    if "dictList" not in nodeFromTree:
        return

    for e in nodeFromTree:
        if e != "name" and e != "dictList":
            print(e,nodeFromTree[e])

    print("The child names are")
    printChildNames(nodeFromTree["dictList"])

def printTree(binTreeDict):
    if binTreeDict == {}:
        return

    # print(binTreeDict)
    print("")
    print("name is ", binTreeDict["name"])

    if "dictList" not in binTreeDict:
        return

    for e in binTreeDict:
        if e != "name" and e != "dictList" and e != "solsDict":
            print(e,binTreeDict[e])

    if  "solsDict" in binTreeDict:
        print("solsDict")
        for sphereCenterStr in binTreeDict["solsDict"]:
            print("sphereCenterStr = ", sphereCenterStr)
            for subVal in binTreeDict["solsDict"][sphereCenterStr]:
                if subVal == "vLabSols":
                    print(colored(subVal,"yellow"))
                else:
                    print(subVal)
                print(binTreeDict["solsDict"][sphereCenterStr][subVal])
    print("The child names are")
    printChildNames(binTreeDict["dictList"])

    for e in binTreeDict["dictList"]:
        printTree(e)

def printTreeOnlySolsPart(binTreeDict):
    if binTreeDict == {}:
        return

    # print(binTreeDict)
    if "dictList" not in binTreeDict:
        return

    if  "solsDict" in binTreeDict:
        print("")
        print(colored("name is "+ binTreeDict["name"],"magenta"))
        print(colored("structType = "+binTreeDict["structType"],"magenta"))

        print("solsDict")
        for sphereCenterStr in binTreeDict["solsDict"]:
            print("sphereCenterStr = ", sphereCenterStr)
            for subVal in binTreeDict["solsDict"][sphereCenterStr]:
                if subVal == "vLabSols":
                    print(colored(subVal,"red"))
                elif subVal == "vCMSols":
                    print(colored(subVal,"green"))
                else:
                    print(subVal)
                print(binTreeDict["solsDict"][sphereCenterStr][subVal])


    for e in binTreeDict["dictList"]:
        printTreeOnlySolsPart(e)


def printTreeOnlyCleanSolsPart(binTreeDict):
    if binTreeDict == {}:
        return

    # print(binTreeDict)
    if "dictList" not in binTreeDict:
        return

    if  "clnSD" in binTreeDict:
        print("")
        print(colored("name is "+ binTreeDict["name"],"magenta"))
        print(colored("structType = "+binTreeDict["structType"],"magenta"))

        print("clnSD")
        for sphereCenterStr in binTreeDict["clnSD"]:
            print("sphereCenterStr = ", sphereCenterStr)
            for subVal in binTreeDict["clnSD"][sphereCenterStr]:
                if subVal == "vLabSols":
                    print(colored(subVal,"red"))
                elif subVal == "vCMSols":
                    print(colored(subVal,"green"))
                else:
                    print(subVal)
                print(binTreeDict["clnSD"][sphereCenterStr][subVal])


    for e in binTreeDict["dictList"]:
        printTreeOnlyCleanSolsPart(e)

def printChildNames(dictList):
    for i in range(len(dictList)):
        if "name" not in dictList[i]:
            continue
        print(dictList[i]["name"])

def getFinalMass(dictNode):
    if "mass" not in dictNode:
        if dictNode["type"] == "set":
            leftDict=dictNode["dictList"][0]
            rightDict=dictNode["dictList"][1]
            mLeft=getFinalMass(leftDict)
            mRight=getFinalMass(leftDict)
            m=mLeft+mRight
            return m
        return None

    m=dictNode["mass"]
    if "exE" not in dictNode:
        myExE=0
    else:
        myExE=dictNode["exE"]

    m+=myExE
    return m

def globalCompleteTree(binTreeDict):
    fillInit(binTreeDict)
    completeTree0(binTreeDict)
    completeTree1(binTreeDict)
    completeTree2(binTreeDict)
    # print("Trying to pull every line automatically")
    # boolPull=pullEveryLine(binTreeDict,generalList)
    # if boolPull == True:
    #     print("Success in pulling every line")
    # else:
    #     print("Unsuccessful pull :'-(")

    #Put here the special vLine for the initial dict


def getInitSolsDict(binTreeDict):
    #This is our free CM solution, we at least know this one! ;-)
    vCM=binTreeDict["redVcm"]
    sCenter=np.array([0.0,0.0,0.0])
    centerStr=str(sCenter.tolist())
    sphereSols={centerStr:{}}
    vCMVect=np.array([0.0,0.0,vCM])
    sphereSols[centerStr]["vLabSols"]=[vCMVect]

    #The only case when lab and cm solutions are the same
    sphereSols[centerStr]["vCMSols"]=[vCMVect]
    sphereSols[centerStr]["vCMPair"]=[sCenter,vCMVect]

    return sphereSols

def getCompletedSolTree(treeNode,solsDict):
    myMass=treeNode["fMass"]
    treeNode["structType"]="goType"

    for vCenterStr in solsDict:
        #Get the CM vel of the system
        sysCMVel=str2NPArray(vCenterStr)

        myLabVelList=solsDict[vCenterStr]["vLabSols"]
        solsDict[vCenterStr]["labEnergy"]=[]
        solsDict[vCenterStr]["vCMSols"]=[]
        solsDict[vCenterStr]["thetaPhi"]=[]
        for myLabVel in myLabVelList:
            vCentNorm=np.linalg.norm(myLabVel)
            ECentSol=1.0/2.0*myMass*(vCentNorm/100.0)**2
            solsDict[vCenterStr]["labEnergy"].append(ECentSol)

            #Now the vel @ the CM system
            myCMVel=myLabVel-sysCMVel
            solsDict[vCenterStr]["vCMSols"].append(myCMVel)

            #Getting the lab angles
            thetaPhi=getThetaPhi(myLabVel)
            solsDict[vCenterStr]["thetaPhi"].append(thetaPhi)

    return solsDict

def fillInit(binTreeDict):
    if binTreeDict == {}:
        return
    if "ELab" not in binTreeDict:#Do more error cheching...
        return
    mPro=binTreeDict["massP"]
    mTar=binTreeDict["massT"]
    binTreeDict["mass"]=mPro+mTar

    ELab=binTreeDict["ELab"]
    initEcm=getEcm(mPro,mTar,ELab)[2]
    binTreeDict["Ecm"]=initEcm
    #Saving the beta
    binTreeDict["BVcm"]=getVelcm(mPro,mTar,ELab)[2]/c
    redVcm=binTreeDict["BVcm"]*100
    binTreeDict["redVcm"]=redVcm
    #This is only for setting a search range, the final vel won't be
    #this high. This criteria will be improved eventually.
    binTreeDict["BVLabMax"]=binTreeDict["redVcm"]

def completeTree0(binTreeDict):
    if binTreeDict == {}:
        return

    finalMass=getFinalMass(binTreeDict)
    if finalMass != None:
        binTreeDict["fMass"]=finalMass

    qVal=getNodeQVal(binTreeDict)
    if qVal != None:
        print("filling tree with", qVal)
        binTreeDict["Q"]=qVal

    if "dictList" not in binTreeDict:
        return

    for e in binTreeDict["dictList"]:
        completeTree0(e)

def completeTree1(binTreeDict):
    if binTreeDict == {}:
        return

    qVal=getNodeQVal(binTreeDict)
    if qVal != None:
        binTreeDict["Q"]=qVal

    if "dictList" not in binTreeDict:
        return

    for e in binTreeDict["dictList"]:
        completeTree1(e)


def completeTree2(binTreeDict):
    if binTreeDict == {}:
        return

    eAvail=getAvailE(binTreeDict)
    if eAvail != None:
        binTreeDict["EAvail"]=eAvail
        childMasses=getChildMasses(binTreeDict)
        if childMasses != None:
            m1,m2=childMasses
            E1cm,E2cm=getEcmsFromECM2(m1,m2,eAvail)
            maxVel=binTreeDict["BVLabMax"]
            pushNewEcmAndVels(E1cm,E2cm,binTreeDict["dictList"],maxVel)

    if "dictList" not in binTreeDict:
        return

    for e in binTreeDict["dictList"]:
        completeTree2(e)

def pushNewEcmAndVels(E1cm,E2cm,dictNode,maxVel):
    dictNode[0]["Ecm"]=E1cm
    m1=dictNode[0]["fMass"]
    BVcm1=sqrt(2.0*E1cm/m1)#Leaving out *c for now
    dictNode[0]["BVcm"]=BVcm1
    dictNode[0]["redVcm"]=BVcm1*100
    dictNode[0]["BVLabMax"]=maxVel+BVcm1*100

    dictNode[1]["Ecm"]=E2cm
    m2=dictNode[1]["fMass"]
    BVcm2=sqrt(2.0*E2cm/m2)#Leaving out *c for now
    dictNode[1]["BVcm"]=BVcm2
    dictNode[1]["redVcm"]=BVcm2*100
    dictNode[1]["BVLabMax"]=maxVel+BVcm2*100

def getAvailE(dictNode):
    if "Ecm" not in dictNode:
        return None
    eCm=dictNode["Ecm"]
    if "Q" not in dictNode:
        qVal=0
    else:
        qVal=dictNode["Q"]
    eAvail=eCm+qVal
    return eAvail

def getChildMasses(dictNode):
    if "dictList" not in dictNode:
        return None
    leftDict=dictNode["dictList"][0]
    rightDict=dictNode["dictList"][1]

    if "fMass" not in leftDict or "fMass" not in rightDict:
        return None
    leftMass=leftDict["fMass"]
    rightMass=rightDict["fMass"]
    return leftMass,rightMass

def getNodeQVal(dictNode):
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

def checkIfNodeIsFreePart(dictNode):
    if dictNode == {}:
        return None
    if "type" not in dictNode:
        return None
    if "dictList" not in dictNode:
        return None
    dList=dictNode["dictList"]
    if dList[0]=={} and dList[1]=={}:
        return True
    return None

generalList=[]
def getFreePartRoute(binTreeDict):
    if binTreeDict == {}:
        return None
    if "dictList" not in binTreeDict:
        return None

    myDict=binTreeDict["dictList"]
    for i in range(len(myDict)):
        myVal=checkIfNodeIsFreePart(myDict[i])
        if myVal != None:
            generalList.append(i)
            return True

    for i in range(len(myDict)):
        myVal=getFreePartRoute(myDict[i])
        if myVal != None:
            generalList.append(i)
            return True

def getDirectFreeRoute(binTreeDict):
    getFreePartRoute(binTreeDict)
    generalList.reverse()
    directFreeRoute=generalList
    return generalList

def spherToCart(r,theta,phi):
    x=r*sin(theta)*cos(phi)
    y=r*sin(theta)*sin(phi)
    z=r*cos(theta)
    return x,y,z

def getStraightLinePoints(theta,phi,vLabMax,part=2000):
    vArray=np.linspace(0,vLabMax,part)
    myVectArray=np.zeros( (part,3) )
    for i in range(part):
        v=vArray[i]
        x,y,z=spherToCart(v,theta,phi)
        myVectArray[i]=np.array([x,y,z])
    return myVectArray

def getTrainStatus(aPoint,aVRad,train):
    trueList=[True for e in train]
    falseList=[False for e in train]
    boolList=[np.linalg.norm(t-aPoint)<aVRad\
              for t in train]
    if boolList == trueList:
        return -1
    if boolList == falseList:
        return 1
    return 0

def getTrainSolIdx(vPoint,vRad,vLine,i=0,\
                   direction="forward",tolerance=None,\
                   trainLen=2):
    if direction == "forward":
        dIncr=1
    else:
        dIncr=-1
    lineMax=len(vLine)

    if tolerance == None:
        tolerance=lineMax

    #Train derail
    if i < 0 or i+trainLen > lineMax:
        return None
    train=vLine[i:i+trainLen]
    trainStatus=getTrainStatus(vPoint,vRad,train)
    while trainStatus != 0:
        #Train derail
        i+=dIncr
        if i < 0 or i+trainLen >= lineMax:
            return None
        if tolerance <= 0:
            return None
        tolerance-=1
        train=vLine[i:i+trainLen]
        trainStatus=getTrainStatus(vPoint,vRad,train)

    return i

def getMidPointLine(vLine1,vLine2,vRad,frac=0.5):
    fD="forward"
    bD="backward"
    forTol=4
    backTol=4
    oldI=0
    foundAny=False
    midPLine=[]
    for vP1 in vLine1:
        if not foundAny:
            i=getTrainSolIdx(vP1,vRad,vLine2,oldI,fD)
            if i == None:
                continue
            else:
                foundAny=True
                oldI=i
                continue

        i=getTrainSolIdx(vP1,vRad,vLine2,oldI,fD,forTol)
        if i == None:
            # print("Trying backward sol")
            i=getTrainSolIdx(vP1,vRad,vLine2,oldI,bD,backTol)
            if i == None:
                # print("No back sol found")
                break

        oldI=i
        train=vLine2[i:i+2]
        myP=getLinSolPoint(vP1,vRad,train)
        midPoint=vP1*(1-frac)+myP*frac
        midPLine.append(midPoint)

    midPLine=np.array(midPLine)
    return midPLine

def getLinSol(vP,vRad,train):
    #Here we expect to use only 2 points
    p0=train[0]
    p1=train[-1] #expecting len(train)==2 so this works properly
    A=np.linalg.norm(p0-vP)-vRad**2
    C=np.linalg.norm(p1-p0)
    B=np.linalg.norm(p1-vP)-A-C-vRad**2
    tPlus=(-B+sqrt(B**2-4*A*C))/(2*A)
    tMinus=(-B-sqrt(B**2-4*A*C))/(2*A)
    return [tPlus,tMinus]

def getLinSolPoint(vP,vRad,train):
    p0=train[0]
    p1=train[-1]
    linSol=getLinSol(vP,vRad,train)
    t=None
    for tValue in linSol:
        if 0 <= tValue <= 1:
            t=tValue
    if t == None:
        return None
    myP=p0*(1-t)+t*p1
    return myP

def pullEveryLine(binTreeDict,freePartListRoute):
    if len(freePartListRoute)==0:
        return True
    freePartIndex=freePartListRoute[0]
    branchIndex=getOtherVal(freePartIndex)
    if branchIndex==None:
        return False
    tree2Fill=binTreeDict["dictList"][branchIndex]
    pullBool=pullLinesFromNode(tree2Fill)
    if pullBool==False:
        return False
    newBinTree=binTreeDict["dictList"][freePartIndex]
    return pullEveryLine(newBinTree,freePartListRoute[1:])

def pullLinesFromNode(binTreeDict):
    emptyNpA=np.array([])
    if binTreeDict == {}:
        return emptyNpA
    if checkIfLastPartNode(binTreeDict) == True:
        idx=findDetectIndex(binTreeDict["dictList"])
        if idx == None:
            return False
        vLabMax=binTreeDict["BVLabMax"]
        theta,phi=binTreeDict["dictList"][idx]["angles"]
        vLine=getStraightLinePoints(theta,phi,vLabMax)
        binTreeDict["vLines"]=[vLine]
        return True

    dList=binTreeDict["dictList"]
    boolVal1=pullLinesFromNode(dList[0])
    if boolVal1 == False:
        return False
    boolVal2=pullLinesFromNode(dList[1])
    if boolVal2 == False:
        return False

    vLines1=dList[0]["vLines"]
    l1EmptyBoolVal=checkIfAllAreEmpty(vLines1)
    vLines2=dList[1]["vLines"]
    l2EmptyBoolVal=checkIfAllAreEmpty(vLines2)

    if l1EmptyBoolVal or l2EmptyBoolVal:
        return False

    #Preparing to do line sweeps
    childVels=getChildVels(binTreeDict)
    if childVels == None:
        return False
    vLeft,vRight=childVels
    vRad=vLeft+vRight
    myFrac=vLeft/vRad
    vLineList=[]
    lineParentsIdxList=[[],[]]
    offsetList=[[],[]]
    #Sweep from line 1 to line 2
    for vLine1 in vLines1:
        for vLine2 in vLines2:
            cmLine=getMidPointLine(vLine1,vLine2,vRad,myFrac)
            vLineList.append(cmLine)
            vLLIdx=vLineList.index(cmLine)
            offsets=getMidPOffsets(vLine1,vLine2,vRad)
            offsetList[0].append([vLLIdx,offsets])

            parentChildIdx1=vLines1.index(vLine1)
            parentChildIdx2=vLines2.index(vLine2)
            lineParentsIdxList[0].append([vLLIdx,[parentChildIdx1,parentChildIdx2]])

    #Sweep from line 2 to line 1
    for vLine2 in vLines2:
        for vLine1 in vLines1:
            cmLine=getMidPointLine(vLine2,vLine1,vRad,1-myFrac)
            vLineList.append(cmLine)
            vLLIdx=vLineList.index(cmLine)
            offsets=getMidPOffsets(vLine2,vLine1,vRad)
            parentChildIdx1=vLines1.index(vLine1)
            parentChildIdx2=vLines2.index(vLine2)

            offsetList[1].append([vLLIdx,offsets])
            lineParentsIdxList[1].append([vLLIdx,[parentChildIdx1,parentChildIdx2]])


    binTreeDict["vLines"]=vLineList
    binTreeDict["offsets"]=offsetList
    binTreeDict["lParentsIdxs"]=lineParentsIdxList
    return True

def checkIfAllAreEmpty(lines):
    emptyNpA=np.array([])
    myEmptyArrays=[emptyNpA for e in lines]
    if lines == myEmptyArrays:
        return True
    return False

def checkIfLastPartNode(dictNode):
    childTypes=getChildTypes(dictNode)
    if childTypes == None:
        return None
    #Important if there is a connection to a detector
    if "detector" in childTypes:
        return True
    return False

def getChildTypes(dictNode):
    if "dictList" not in dictNode:
        return None
    leftDict=dictNode["dictList"][0]
    rightDict=dictNode["dictList"][1]

    if "type" not in leftDict:
        leftType=None
    else:
        leftType=leftDict["type"]
    if "type" not in rightDict:
        rightType=None
    else:
        rightType=rightDict["type"]

    return [rightType,leftType]


def getChildVels(dictNode):
    if "dictList" not in dictNode:
        return None
    leftDict=dictNode["dictList"][0]
    rightDict=dictNode["dictList"][1]

    if "redVcm" not in leftDict or "redVcm" not in rightDict:
        return None
    leftVel=leftDict["redVcm"]
    rightVel=rightDict["redVcm"]
    return [leftVel,rightVel]

def findDetectIndex(aList):
    for i in range(len(aList)):
        if "type" not in aList[i]:
            continue
        if aList[i]["type"] == "detector":
            return i
    return None

def getOtherVal(j):
    if j not in [0,1]:
        return None
    if j==0:
        return 1
    return 0

def plotAllLines(binTreeDict,ax):
    if binTreeDict == {}:
        return

    if "dictList" not in binTreeDict:
        return

    if "vLines" in binTreeDict:
        myVLines=binTreeDict["vLines"]
    else:
        myVLines=[]
    for line in myVLines:
        plotNoDisplay(ax,line,name=binTreeDict["name"])

    for e in binTreeDict["dictList"]:
        plotAllLines(e,ax)

def plotNoDisplay(ax,lineArray,name="defaultName"):
    x=lineArray[ : ,0]
    y=lineArray[ : ,1]
    z=lineArray[ : ,2]
    ax.plot(x,y,z,label=name)

def getSphereLineSols(vSCent,vSRad,vLine):
    i=getTrainSolIdx(vSCent,vSRad,vLine,i=0)
    cmNormVects=[]
    while i != None:
        train=vLine[i:i+2]
        myP=getLinSolPoint(vSCent,vSRad,train)
        myPInCM=myP-vSCent
        norm=np.linalg.norm(myPInCM)
        cmNormVects.append(myPInCM/norm)
        i=getTrainSolIdx(vSCent,vSRad,vLine,i+1)
    return np.array(cmNormVects)

def getSphereLineIdxSolsList(vSCent,vSRad,vLine):
    """Gets a list of all the solution indices in the line with the given
sphere

    """
    i=getTrainSolIdx(vSCent,vSRad,vLine,i=0)
    idxSols=[]
    while i != None:
        idxSols.append(i)
        i=getTrainSolIdx(vSCent,vSRad,vLine,i+1)

    return idxSols

def fillMajorSols(binTreeDic,freePartRoute,solsDict={}):
    if binTreeDic["type"] == "initial":
        solsDict=getInitSolsDict(binTreeDic)

    #Filling the local node
    binTreeDic["solsDict"]=solsDict

    #now given the dictionary is partially pre-filled we now fill it
    #with the corresponding solutions
    solsDict=getCompletedSolTree(binTreeDic,solsDict)

    if len(freePartRoute)==0:
        return True

    #Now figure out the branches to fill and to go, first we get the
    #indices
    freePartIndex=freePartRoute[0]
    branchIndex=getOtherVal(freePartIndex)

    if branchIndex==None:
        return False

    #The branches to fill (solve) and to go
    branch2Solve=binTreeDic["dictList"][branchIndex]
    branch2Go=binTreeDic["dictList"][freePartIndex]

    vInfoList=getVInfoList(solsDict)

    solsD4B2Solve={}
    for importantL in vInfoList:
        newCent=importantL[0]
        pairCM=importantL[1]
        newCentStr=npArray2Str(newCent)
        solsD4B2Solve=getDictWithIdxs(branch2Solve,\
                                      newCent,solsD4B2Solve)

    if solsD4B2Solve == {}:
        return False

    solsD4B2Solve=getSolVelsEnergiesEtcInNode(branch2Solve,\
                                                   solsD4B2Solve)
    branch2Solve["solsDict"]=solsD4B2Solve

    vMagL=[branch2Solve["redVcm"],branch2Go["redVcm"]]

    dict4Branch2Go=getComplementarySolsDict(solsD4B2Solve,vMagL)

    fillBool=fillMajorSols(branch2Go,freePartRoute[1:],dict4Branch2Go)

    return fillBool

def cleanDict(binTreeDict,freePartRoute):
    #Figure out the branches to fill and to go, first we get the
    #indices
    freePartIndex=freePartRoute[0]
    branchIndex=getOtherVal(freePartIndex)
    if branchIndex==None:
        return False

    #The branches to fill (solve) and to go
    branch2Solve=binTreeDict["dictList"][branchIndex]
    branch2Go=binTreeDict["dictList"][freePartIndex]

    #Reached the node b4 the free part
    if len(freePartRoute)==1:
        #Pushing the clnDict in branch2Go, this is the only case it is
        #done. Also, it happens to be an exact copy of the branch2Go
        #solsDict.
        childClnSDict=copy.copy(branch2Go["solsDict"])
        #The pushing...
        branch2Go["clnSD"]=childClnSDict

        #The cleanded solutions dictionary reference
        clnSDR=getVCent4IdxSearchD(binTreeDict,freePartRoute)
        print(colored("clnSDR = ","red"))
        print(colored(clnSDR,"red"))
        #Incorporating it in the current node.
        binTreeDict["clnSDR"]=clnSDR


        #Now, the childClnSDict should be used to clean the current
        #node and also the branch2Solve solutions node.
        clnSD=getClnSD(binTreeDict,clnSDR)
        binTreeDict["clnSD"]=clnSD

        print(colored("clnSD = ","blue"))
        print(colored(clnSD,"blue"))

        getIdxL4B2Solve(branch2Go,branch2Solve)
        cleanRestB2Solve(branch2Solve)
        return True

    aBool=cleanDict(branch2Go,freePartRoute[1:])
    clnSDR=getVCent4IdxSearchD(binTreeDict,freePartRoute)
    print(colored("After a recursive call","magenta"))
    print(colored("clnSDR = ","blue"))
    print(colored(clnSDR,"blue"))
    #Incorporating it in the current node.
    binTreeDict["clnSDR"]=clnSDR

    #Now, the childClnSDict should be used to clean the current
    #node and also the branch2Solve solutions node.
    clnSD=getClnSD(binTreeDict,clnSDR)
    binTreeDict["clnSD"]=clnSD

    getIdxL4B2Solve(branch2Go,branch2Solve)
    cleanRestB2Solve(branch2Solve)
    return True

    # clnSD=getClnSD(binTreeDict,clnSDR)
    # print(colored(clnSD,"blue"))


def getLocalCleanDict(b2SolD,b2GD,referenceDict):
    #All of the dicts need a solsDict entry, the b2GD needs a vCMPairL sub entry
    pass

def getCleanB2Sol1(initB2Sol,refDict):
    cleanB2Sol={}
    for b2SolEStr in initB2Sol:
        print("Current element is ",b2SolEStr)
        if b2SolEStr in refDict:
            cleanB2Sol[b2SolEStr]=initB2Sol[b2SolEStr]

    return cleanB2Sol

def getVInfoList(solsDict):
    vInfoList=[]
    for sphCentStr in solsDict:
        centList=solsDict[sphCentStr]["vLabSols"]
        vCMPairL=solsDict[sphCentStr]["vCMPair"]
        for newVCenter,newPair in zip(centList,vCMPairL):
            #Please note that the vLabSols are the new centers.
            vInfoList.append([newVCenter,newPair])

    return vInfoList

def getComplementarySolsDict(solsDict,vMagL):
    compSolsDict={}
    vMag2Sol,vMag2Go=vMagL
    for sphCentStr in solsDict:
        #Convert this string to an np array
        vCenter=str2NPArray(sphCentStr)

        myVCMList=solsDict[sphCentStr]["vCMSols"]

        compSolsDict[sphCentStr]={"vLabSols":[],\
                                  "vCMPair":[]}

        for vCMSub in myVCMList:
            for vCM in vCMSub:
                vNormCM=vCM/np.linalg.norm(vCM)
                newestCentCM=-vNormCM*vMag2Go
                newestCentLab=vCenter+newestCentCM

                compSolsDict[sphCentStr]["vLabSols"]\
                    .append(newestCentLab)

                compSolsDict[sphCentStr]["vCMPair"]\
                    .append([vCM,newestCentCM])

    return compSolsDict

def getDictWithIdxs(treeNode,vSCent,sphSolsDict):
    #Getting rid of the -0. It messes with the string convertion
    vSCent[vSCent==0.] = 0.
    centerStr=str(vSCent.tolist())

    nodeVLines=treeNode["vLines"]
    vSRad=treeNode["redVcm"]
    solIdxList=[]
    #To properly connect the solIdxList to its corresponding vLine
    idxLineList=[]
    for i in range(len(nodeVLines)):
        vLine=nodeVLines[i]
        lineInterIdxList=getSphereLineIdxSolsList(vSCent,vSRad,vLine)
        if lineInterIdxList == []:
            continue
        solIdxList.append(lineInterIdxList)
        idxLineList.append(i)
        #this ensures the j var gets the correct index in the
        #solIdxList

    if solIdxList != []:
        sphSolsDict[centerStr]={}
        sphSolsDict[centerStr]["solIdxList"]=solIdxList
        sphSolsDict[centerStr]["idxLineList"]=idxLineList

    return sphSolsDict

def getSolVelsEnergiesEtcInNode(treeNode,sphereSolsDict):
    myMass=treeNode["fMass"]
    treeNode["structType"]="solveType"

    for sphereCenterStr in sphereSolsDict:
        #Surely some numerical errors lying around but I'll live with
        #it for now
        myNpCenter=str2NPArray(sphereCenterStr)

        indexSolLists=sphereSolsDict[sphereCenterStr]["solIdxList"]
        #The proper indices on the outside list
        idxLineList=sphereSolsDict[sphereCenterStr]["idxLineList"]
        for i in range(len(indexSolLists)):
            solIdxSubList=indexSolLists[i]
            #Here the "j" index corresponds to an intersection with a
            #line (that is outside this sub dict) with the same index.
            j=idxLineList[i]
            myVLine=treeNode["vLines"][j]
            solVelList=[]
            solEList=[]
            vCMSolList=[]
            thetaPhiList=[]
            for vSolIndex in solIdxSubList:
                velSol=myVLine[vSolIndex]
                solVelList.append(velSol)

                vNorm=np.linalg.norm(velSol)
                ESol=1.0/2.0*myMass*(vNorm/100.0)**2
                solEList.append(ESol)

                vCMSol=velSol-myNpCenter
                vCMSolList.append(vCMSol)

                #ECM energies should be the same as in the first
                #calculation... I'll corroborate later

                thetaPhi=getThetaPhi(velSol)
                thetaPhiList.append(thetaPhi)

            if "vLabSols" not in sphereSolsDict[sphereCenterStr]:
                sphereSolsDict[sphereCenterStr]["vLabSols"]=[]
            sphereSolsDict[sphereCenterStr]["vLabSols"].append(solVelList)

            if "energyLabSols" not in sphereSolsDict[sphereCenterStr]:
                sphereSolsDict[sphereCenterStr]["energyLabSols"]=[]
            sphereSolsDict[sphereCenterStr]["energyLabSols"].append(solEList)

            if "vCMSols" not in sphereSolsDict[sphereCenterStr]:
                sphereSolsDict[sphereCenterStr]["vCMSols"]=[]
            sphereSolsDict[sphereCenterStr]["vCMSols"].append(vCMSolList)

            if "thetaPhi" not in sphereSolsDict[sphereCenterStr]:
                sphereSolsDict[sphereCenterStr]["thetaPhi"]=[]
            sphereSolsDict[sphereCenterStr]["thetaPhi"].append(thetaPhiList)


    return sphereSolsDict

def getMidPOffsets(vLine1,vLine2,vRad):
    """Returns the i,j indices in line 1 and 2 where the first
intersection is found using the CM values.

    """
    j=0
    foundAny=False
    for i in range(len(vLine1)):
        vP1=vLine1[i]
        j=getTrainSolIdx(vP1,vRad,vLine2,j)
        if j == None:
            continue
        return [i,j]
    return None

def getVelSolutions(treeNode):
    if "type" not in treeNode:
        return False
    if treeNode["type"]==detector:
            return False
    if treeNode["type"]=="initial":
        initRedVcm=treeNode["redVcm"]
        centerPos=np.array([0.0,0.0,initRedVcm])
        treeNode["velSolutions"]=[centerPos]
        return True

    #More is missing, check it later

def findLineParentSolsInChildNodes(branchDict):
    if branchDict == {}:
        return False
    if "type" not in branchDict:
        return False
    if treeNode["type"] == "detector":
        return True

    boolVelStatus=getVelSolutions(branchDict)
    if checkIfLastPartNode(binTreeDict) == True:
        return True

#Still need to implement some functions
def solveEveryRoute(binTreeDict,freePartListRoute):
    if len(freePartListRoute)==0:
        return True
    freePartIndex=freePartListRoute[0]
    branchIndex=getOtherVal(freePartIndex)
    if branchIndex==None:
        return False
    tree2Fill=binTreeDict["dictList"][branchIndex]
    #Here, find the solutions of the velCirc with the lines. This func
    #also fills all the indeces and velocities and energies etc. of the
    #corresponding points.
    boolSolStatus=findIntersectionsAndSolveBranch(tree2Fill)
    if pullBool==False:
        return False
    newBinTree=binTreeDict["dictList"][freePartIndex]
    return solveEveryRoute(newBinTree,freePartListRoute[1:])

def getSolListInParents(treeNode,solIdxList):
    checkRes=checkIfNodeIsFreePart(treeNode)
    if checkRes == True:
        #First generation line return the index (or true?) no need to
        #recall the function
        return None
    if "dictList" not in treeNode:
        return None
    if "offsets" not in treeNode:
        return None
    if "lParentsIdxs" not in treeNode:
        return None
    offS=treeNode["offsets"]
    parIdx=treeNode["lParentsIdxs"]
    sols4LeftNode=[]
    sols4RightNode=[]
    # print("solIdxList",solIdxList)
    for pIdx,oSet,solIdx in zip(parIdx,offS,solIdxList):
        # print("pIdx,oSet,solIdx = ",pIdx,oSet,solIdx)
        leftIdxStuff=[pIdx[0],oSet[0]+solIdx]
        sols4LeftNode.append(leftIdxStuff)
        rightIdxStuff=[pIdx[1],oSet[1]+solIdx]
        sols4RightNode.append(sols4RightNode)
    return [leftIdxStuff,rightIdxStuff]

def str2NPArray(myString):
    #In principle, all the strings were numpy arrays that where pre
    #converted to lists b4 the string convertion.
    myNPArray=np.array([float(t) for t in myString[1:-1].split(",")])
    return myNPArray

def npArray2Str(myNpArray):
    #Getting rid of the -0. It messes with the string convertion
    myNpArray[myNpArray==0.] = 0.
    myString=str(myNpArray.tolist())
    return myString

def getVLabCIdxP(vCentStr,solsDict):
    for centStr in solsDict:
        vList=solsDict[centStr]["vLabSols"]
        for i in range(len(vList)):
            v=vList[i]
            #I think is better to change all the vals to str rather than
            #converting back a single string to a np.array.
            vStr=npArray2Str(v)
            if vStr == vCentStr:
                return [centStr,i]

    print("This should not be printed")
    return None

def getVCent4IdxSearchD(binTreeDict,freePartRoute):
    #Get the solsDict of branch2Go
    mySolsDict=binTreeDict["solsDict"]
    branch2Go=binTreeDict["dictList"][freePartRoute[0]]
    goClnSolsDict=branch2Go["clnSD"]
    clnDictRef={}
    for centerStr in goClnSolsDict:
        print("My looping centerStr = "+centerStr)

        cIdxP=getVLabCIdxP(centerStr,mySolsDict)
        if cIdxP != None:
            upperCStr,i=cIdxP
            if upperCStr not in clnDictRef:
                clnDictRef[upperCStr]=[]
            clnDictRef[upperCStr].append([i,centerStr])
    return clnDictRef

def getClnSD(nodeDict,clnSDR):
    clnSD={}

    #clnSDR={strC:[[idx,childCmStr],...],...}
    for centStr in clnSDR:
        myListOfPairs=clnSDR[centStr]

        clnSD[centStr]={}

        specificSolsD=nodeDict["solsDict"][centStr]

        for e in specificSolsD:
            clnSD[centStr][e]=[]
            for pairL in myListOfPairs:
                i=pairL[0]
                clnSD[centStr][e].append(specificSolsD[e][i])

    return clnSD

def getB2SolClnSolsIdxs(b2SSolsD,vCM2Search):
    vCML=b2SSolsD["vCMSols"]
    for i in range(len(vCML)):
        print(colored("Inside getB2SolClnSolsIdxs","magenta"))
        lineSolCML=vCML[i]
        print(colored(lineSolCML,"magenta"))
        for j in range(len(lineSolCML)):
            vCM=lineSolCML[j]
            print("vCM = ",vCM)
            if np.array_equal(vCM2Search,vCM):
                return [i,j]

    print("In getB2SolClnSolsIdxs this should not be printed")

def getIdxL4B2Solve(branch2Go,branch2Solve):
    #Need to loop through the centers of the child go node
    childClnSDict=branch2Go["clnSD"]
    clnSD={}
    for centStr in childClnSDict:
        clnSD[centStr]={"pairIdx4Cleaning":[]}
        print(colored("The centerStr inside the cleanDict is: "+centStr,"yellow"))
        print("childClnSDict = ",childClnSDict)
        #Need to loop through the pair values in branch2go
        for vCMSolPair in childClnSDict[centStr]["vCMPair"]:
            print("The current vCMSolPair is",vCMSolPair)
            print("The vCM to search in the branch2Go is")
            vCMSol=vCMSolPair[0]
            print(colored(vCMSol,"red"))
            print(colored("The vCMSol is: ","yellow"))
            print(colored(vCMSol,"yellow"))
            b2SSolsD=branch2Solve["solsDict"][centStr]
            print(b2SSolsD)
            print("Printing the value to search",vCMSol)
            print("Now calling the function")
            indexPair=getB2SolClnSolsIdxs(b2SSolsD,vCMSol)
            print(colored(indexPair,"red"))
            clnSD[centStr]["pairIdx4Cleaning"].append(indexPair)

    branch2Solve["clnSD"]=clnSD
    print(colored("The local clnSD is","blue"))
    print(colored(clnSD,"blue"))

def cleanRestB2Solve(branch2Solve):
    clnSD=branch2Solve["clnSD"]
    allSols=branch2Solve["solsDict"]
    print(colored("Starting printing in cleanRestB2Solve","yellow"))
    print(colored("clnSD = ","blue"))
    print(colored(clnSD,"blue"))

    #Imprortant to run the loop through the clnSD indices and not the
    #allSols. Since the former has the valid centers. These are always
    #present in the allSols dict by construction.
    for e in clnSD:
        print(colored(e,"yellow"))
        for idxPair in clnSD[e]["pairIdx4Cleaning"]:
            print(colored("idxPair stuff","magenta"))
            print(colored(idxPair,"magenta"))
            i,j=idxPair
            iListD={}
            for ee in allSols[e]:
                print(colored(ee,"magenta"))
                if ee not in clnSD[e]:
                    clnSD[e][ee]=[]

                if ee not in iListD:
                    iListD[ee]=[]

                if i not in iListD[ee]:
                    iListD[ee].append(i)
                    print(colored(easyStr,"magenta"))
                    clnSD[e][ee].append([])
                    print(colored(clnSD,"magenta"))

                print(colored(ee,"green"))
                print(colored(allSols[e][ee],"green"))
                print(colored("Using the index pair part!","red"))
                print(colored(allSols[e][ee][i][j],"green"))
                ii=iListD[ee].index(i)
                print(colored("iListD","blue"))
                print(colored(iListD,"blue"))
                print(colored(easyStr,"yellow"))
                print(colored(clnSD[e][ee][ii],"yellow"))
                clnSD[e][ee][ii].append(allSols[e][ee][i][j])

    print(colored("clnSD","red"))
    print(colored(clnSD,"red"))
    print(colored("Ending printing in cleanRestB2Solve","yellow"))

def getThetaPhi(vLab):
    x,y,z=vLab
    vMag=np.linalg.norm(vLab)
    theta=acos(z/vMag)
    phi=atan2(y,x)
    #Using degrees for now
    return [degrees(theta),degrees(phi)]

###############################
#The secondary solutions part##
###############################

def getLineParIdxsAndOffsets(lineIdx,treeNode):
    if "lParentsIdxs" not in treeNode:
        print(colored("getLineParIdxsAndOffsets called on wrong node!!","red"))
        return None

    lParIdxs=treeNode["lParentsIdxs"]
    offsetList=treeNode["offsets"]
    sweepStr=""
    for val,offVal in zip(lParIdxs[0],offsetList[0]):
        if lineIdx == val[0]:
            sweepStr="left"
            parIdx1,parIdx2=val[1]
            offIdxVal=offVal[1][0]
            return [sweepStr,parIdx1,parIdx2,offIdxVal]

    for val,offVal in zip(lParIdxs[1],offsetList[1]):
        if lineIdx == val[0]:
            sweepStr="right"
            parIdx1,parIdx2=val[1]
            offIdxVal=offVal[1][0]
            return [sweepStr,parIdx1,parIdx2,offIdxVal]

    print(colored("getLineParIdxsAndOffsets this should never be printed!!","red"))
    return None

def getLineIdxFromSolIdx(i,centerStr,treeNode):
    if 'solsDict' not in treeNode:
        print("Error in getLineIdxFromSolIdx")
        print("'solsDict' not found in node")
        return None

    if centerStr not in treeNode["solsDict"]:
        print("Error in getLineIdxFromSolIdx")
        print("a center string was not found in node")
        return None

    if "solIdxList" not in treeNode["solsDict"][centerStr]:
        print("Error in getLineIdxFromSolIdx")
        print("solIdxList not found in node")
        return None

    if 'idxLineList' not in treeNode["solsDict"][centerStr]:
        print("Error in getLineIdxFromSolIdx")
        print("idxLineList not found in node")
        return None

    if i not in range(len(treeNode["solsDict"][centerStr]['idxLineList'])):
        print("Error in getLineIdxFromSolIdx")
        print("Index i out of range")
        return None

    myLineIdx=treeNode["solsDict"][centerStr]['idxLineList'][i]
    return myLineIdx

def getSecSolL(centerStr,solsDict):
    solsEntry=solsDict[centerStr]
    solIdxList=solsEntry["solIdxList"]
    idxLineList=solsEntry["idxLineList"]

    secSolL=[]

    for i in range(len(solIdxList)):
        solIdxSubL=solIdxList[i]
        lineIdx=idxLineList[i]

        for solIdx in solIdxSubL:
            secSolL.append([i,solIdx])

    return secSolL

def getSecSolParList(centerStr,treeNode):
    localSolsD=treeNode["solsDict"][centerStr]
    solIdxList=localSolsD["solIdxList"]
    #For relating the inner indices to the outer real line indices
    idxLineList=localSolsD["idxLineList"]

    secSolParL=[]
    for i in range(len(solIdxList)):
        lineParAndOffsets=getLineParIdxsAndOffsets(i,treeNode)
        sweepStr,parIdx1,parIdx2,offIdxVal=lineParAndOffsets
        solIdxSubL=solIdxList[i]

        lineIdx=idxLineList[i]
        for solIdx in solIdxSubL:
            if sweepStr == "left":
                theEntry=[sweepStr,
                          [parIdx1,solIdx+offIdxVal],
                          [lineIdx,solIdx],
                          [parIdx2,None]]
            else:
                theEntry=[sweepStr,
                          [parIdx1,None],
                          [lineIdx,solIdx],
                          [parIdx2,solIdx+offIdxVal]]

            secSolParL.append(theEntry)

    return secSolParL

def fillInitSecSols(treeNode):
    if treeNode["structType"] != "solveType":
        print("Error fillInitSecSols should only be called on solveType")
        return

    secSolsDict={}
    solsDict=treeNode["solsDict"]
    for centStr in solsDict:
        #The next function has yet to be written
        secSolsDict[centerStr]=getRawSolsEntry(centerStr,solsDict)

    treeNode["secSolsDict"]=secSolsDict


def getVSecSolsList(secSolParL,treeNode):
    leftN,rightN=treeNode["dictList"]

    lVLines,rVLines=leftN["vLines"],rightN["vLines"]
    nVLines=treeNode["vLines"]

    lVMag,rVMag=leftN["redVcm"],rightN["redVcm"]

    secSolsL=[]

    for e in secSolParL:
        sweepStr,lInfo,nInfo,rInfo=e

        nLineIdx,nPointIdx=nInfo
        nVel=nVLines[nLineIdx][nPointIdx]
        nVInfo=[nLineIdx,nVel]

        lLineIdx,lPointIdx=lInfo
        rLineIdx,rPointIdx=rInfo

        if sweepStr == "left":
            lVel=lVLines[lLineIdx][lPointIdx]
            lVcm=lVel-nVel
            lVInfo=[lLineIdx,lVel]

            vNormCM=lVcm/np.linalg.norm(lVcm)
            rVcm=-vNormCM*rVMag

            rVel=nVel+rVcm

            rPointIdx=getClosestIdx(rVel,rVLines[rLineIdx])

            print(colored("Exact vs aprox","red"))
            print(rVel,rVLines[rLineIdx][rPointIdx])

            rVInfo=[rLineIdx,rVel]
        else:
            rVel=rVLines[rLineIdx][rPointIdx]
            rVcm=rVel-nVel
            rVInfo=[rLineIdx,rVel]

            vNormCM=rVcm/np.linalg.norm(rVcm)
            lVcm=-vNormCM*lVMag

            lVel=nVel+lVcm
            lPointIdx=getClosestIdx(lVel,lVLines[lLineIdx])

            print(colored("Exact vs aprox","red"))
            print(lVel,lVLines[lLineIdx][lPointIdx])

            lVInfo=[lLineIdx,lVel]

        secSolsE=[sweepStr,lVInfo,nVInfo,rVInfo]
        secSolsL.append(secSolsE)

    return secSolsL


def getClosestIdx(vPoint,vLine):
    dist_2=np.sum((vPoint-vLine)**2,axis=1)
    return np.argmin(dist_2)
