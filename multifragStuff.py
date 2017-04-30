from math import *
import numpy as np

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

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
        if e != "name" and e != "dictList" and e != "sphereSols":
            print(e,binTreeDict[e])

    if  "sphereSols" in binTreeDict:
        print("sphereSols")
        for sphereString in binTreeDict["sphereSols"]:
            print("sphereString = ", sphereString)
            for subVal in binTreeDict["sphereSols"][sphereString]:
                print(subVal)
                print(binTreeDict["sphereSols"][sphereString][subVal])
    print("The child names are")
    printChildNames(binTreeDict["dictList"])

    for e in binTreeDict["dictList"]:
        printTree(e)

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


def initSphereSols(binTreeDict):
    #This is our free CM solution, we at least know this one! ;-)
    if binTreeDict["type"]=="initial":
        vCM=binTreeDict["redVcm"]
        sCenter=np.array([0.0,0.0,0.0])
        sphereString=str([sCenter.tolist(),vCM])
        binTreeDict["sphereSols"]={}
        binTreeDict["sphereSols"][sphereString]={}
        binTreeDict["sphereSols"][sphereString]["velSols"]=[[[np.array([0.0,0.0,-vCM])]]]#put []
        #The minus is there for the velocity part to preserve program
        #structure, the function will invert the velocity value and
        #use the correct initial velocity.

        #I think this is enough for the initial system
        return binTreeDict["sphereSols"]

def getInitSolsDict2(binTreeDict):
    #This is our free CM solution, we at least know this one! ;-)
    vCM=binTreeDict["redVcm"]
    sCenter=np.array([0.0,0.0,0.0])
    centerStr=str(sCenter.tolist())
    sphereSols={centerStr:{}}
    sphereSols[centerStr]["vLabSols"]=[np.array([0.0,0.0,vCM])]

    return sphereSols

def getCompletedSolTree(treeNode,solsDict):
    myMass=treeNode["fMass"]

    for vCenterStr in solsDict:
        #Get the CM vel of the system
        sysCMVel=str2NPArray(vCenterStr)

        myLabVelList=solsDict[vCenterStr]["vLabSols"]
        solsDict[vCenterStr]["labEnergy"]=[]
        solsDict[vCenterStr]["cmVel"]=[]
        for myLabVel in myLabVelList:
            vCentNorm=np.linalg.norm(myLabVel)
            ECentSol=1.0/2.0*myMass*(vCentNorm/100.0)**2
            solsDict[vCenterStr]["labEnergy"].append(ECentSol)

            #Now the vel @ the CM system
            myCMVel=myLabVel-sysCMVel
            solsDict[vCenterStr]["cmVel"].append(myCMVel)

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

    #Just forzing it to have a line so it doesn't mess with the rest
    #of the code, in the future use one point, edit getDictWithIdxs2
    #no epsilon needed...
    epsilon=0.000000000000001
    binTreeDict["vLines"]=[np.array([[0,0,redVcm-epsilon/2],\
                                 [0,0,redVcm+epsilon/2]])]

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
    lineParentsIdxList=[]
    offsetList=[]
    #Sweep from line 1 to line 2
    for vLine1 in vLines1:
        for vLine2 in vLines2:
            cmLine=getMidPointLine(vLine1,vLine2,vRad,myFrac)
            vLineList.append(cmLine)
            offsets=getMidPOffsets(vLine1,vLine2,vRad)
            offsetList.append(offsets)

            parentChildIdx1=vLines1.index(vLine1)
            parentChildIdx2=vLines2.index(vLine2)
            lineParentsIdxList.append([parentChildIdx1,parentChildIdx2])

    #Sweep from line 2 to line 1
    for vLine2 in vLines2:
        for vLine1 in vLines1:
            cmLine=getMidPointLine(vLine2,vLine1,vRad,1-myFrac)
            vLineList.append(cmLine)
            offsets=getMidPOffsets(vLine2,vLine1,vRad)
            parentChildIdx1=vLines1.index(vLine1)
            parentChildIdx2=vLines2.index(vLine2)
            #Inverting order so that when recalling this info the
            #convention remains no matter the index in the lists.
            if offsets != None:
                i,j=offsets
                offsets=j,i

            offsetList.append(offsets)
            lineParentsIdxList.append([parentChildIdx2,parentChildIdx1])


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

def getSphereLineIdxSols(vSCent,vSRad,vLine):
    i=getTrainSolIdx(vSCent,vSRad,vLine,i=0)
    idxSols=[]
    while i != None:
        idxSols.append(i)
        i=getTrainSolIdx(vSCent,vSRad,vLine,i+1)

    return idxSols

def fillMajorSols(binTreeDict,freePartRoute,sphereSolsD={}):
    #Do more error checking... please
    if binTreeDict["type"]=="initial":
        sphereSolsD=initSphereSols(binTreeDict)

    vRad=binTreeDict["redVcm"]
    vCenterList=getVCenterList(sphereSolsD)
    fillBoolList=[]
    newCentList=[]
    for lastVCent in vCenterList:
        normInvVelSol=-lastVCent/np.linalg.norm(lastVCent)
        newCent=vRad*normInvVelSol
        newCentList.append(newCent)

    #Fill the current node
    noIdxBool=noIdxFillSolVelsEnergiesEtcInNode(binTreeDict,newCentList)
    if noIdxBool==False:
        return False

    if len(freePartRoute)==0:
        return True
    freePartIndex=freePartRoute[0]
    branchIndex=getOtherVal(freePartIndex)

    if branchIndex==None:
        return False
    branch2Solve=binTreeDict["dictList"][branchIndex]
    branch2Go=binTreeDict["dictList"][freePartIndex]

    #Maybe these 2 are reduntant
    b2SolveRad=branch2Solve["redVcm"]
    b2GoRad=branch2Go["redVcm"]

    nSphereSolsDList=[]

    for newCent in newCentList:
        fillBool=fillSphereLineIdxSolsInNode(branch2Solve,newCent,b2SolveRad)
        fillBoolList.append(fillBool)

    if True in fillBoolList:
        newSphereSolsD=fillSolVelsEnergiesEtcInNode(branch2Solve)
        nSphereSolsDList.append(newSphereSolsD)

    binTreeDict["dictList"][branchIndex]=branch2Solve

    boolList=[]
    falseList=[False for e in nSphereSolsDList]

    for newSphereSolsD in nSphereSolsDList:
        if newSphereSolsD == {}:
            #The corresponding bool value was False
            boolList.append(False)
            continue

        #Call the fill major sols here!!
        newBool=fillMajorSols(branch2Go,freePartRoute[1:],newSphereSolsD)
        #If that value was true then make a dictionary entry in the
        #current tree the with the corresponding radius. But what
        #about the indices?...
        boolList.append(newBool)

    binTreeDict["dictList"][freePartIndex]=branch2Go
    # print("boolList = ", boolList)
    if boolList == falseList:
        print("Returning a false value somewhere")
        return False

    print("Made it to the last part")
    return True

def fillMajorSols2(binTreeDic,freePartRoute,solsDict={}):
    if binTreeDic["type"] == "initial":
        #Maybe put this outside at the initialization stage..
        solsDict=getInitSolsDict2(binTreeDic)

    #Filling the local node
    binTreeDic["solsDict"]=solsDict

    #now given the dictionary is partially pre-filled we now fill it
    #with the corresponding solutions

    solsDict=getCompletedSolTree(binTreeDic,solsDict)

    newCentList=getVCenterList2(solsDict)

    # newSphereSolsD=getSolVelsEnergiesEtcInNode2(binTreeDic,\
    #                                             newSphSolsD)
    # binTreeDic["majorSols"]=newSphereSolsD#Maybe redundant

    if len(freePartRoute)==0:
        return True

    #Now figure out the branches to fill and 2 go, first we get the
    #indices
    freePartIndex=freePartRoute[0]
    branchIndex=getOtherVal(freePartIndex)

    if branchIndex==None:
        return False

    #The branches to fill (solve) and to go
    branch2Solve=binTreeDic["dictList"][branchIndex]
    branch2Go=binTreeDic["dictList"][freePartIndex]

    vCenterList=getVCenterList2(solsDict)
    print("vCenterList = ", vCenterList)

    solsD4B2Solve={}
    for newerCent in vCenterList:
        print("newerCent = ", newerCent)
        newerCentStr=npArray2Str(newerCent)
        print("Inside newerCentLoop, newerCentStr = ", newerCentStr)
        solsD4B2Solve=getDictWithIdxs2(branch2Solve,\
                                       newerCent,solsD4B2Solve)

    print("solsD4B2Solve = ")
    print(solsD4B2Solve)
    #Put conditional here in case solsD4B2Solve is not properly
    #filled... make a function for this?... then fill up the
    #solsDictetc then attach it to the binTreeDict...
    if solsD4B2Solve == {}:
        return False

    solsD4B2Solve=getSolVelsEnergiesEtcInNode2(branch2Solve,\
                                                   solsD4B2Solve)
    print("solsD4B2Solve = ",solsD4B2Solve)

    # branch2Solve["majorSols"]=solsD4B2Solve

    # # print("Printing branch2Solve")
    # # printNode(binTreeDic["dictList"][branchIndex])

    #Do a function to get the newestCenters
    vMagnitude=branch2Go["redVcm"]
    # newestCenterList=getVCenterListNewest(solsD4B2Solve,vMagnitude)
    dict4Branch2Go=getCompSolsDict(solsD4B2Solve,vMagnitude)

    print("########Now printing dict4Branch2Go ########")
    print(dict4Branch2Go)


    fillBool=fillMajorSols2(branch2Go,freePartRoute[1:],dict4Branch2Go)

    return fillBool

def getVCenterList2(solsDict):
    vCenterListofLists=[]
    for sphCentStr in solsDict:
        for newVCenter in solsDict[sphCentStr]["vLabSols"]:
            vCenterListofLists.append(newVCenter)

    return vCenterListofLists

def getVCenterListBetter(solsDict):
    vCenterList=[]
    for sphCentStr in solsDict:
        for newVCenterList in solsDict[sphCentStr]["vLabSols"]:
            for newVCenter in newVCenterList:
                vCenterList.append(newVCenter)

    return vCenterList

def getVCenterListNewest(solsDict,vMagnitude):
    vCenterList=[]
    for sphCentStr in solsDict:
        #Convert this string to an np array
        vCenter=str2NPArray(sphCentStr)

        myNormalizedVCMList=solsDict[sphCentStr]["vCMSolsNL"]
        for vNormCMSubL in myNormalizedVCMList:
            for vNormCM in vNormCMSubL:
                # print("vNormCM = ", vNormCM)
                newestCentCM=-vNormCM*vMagnitude
                newestCentLab=vCenter+newestCentCM
                vCenterList.append(newestCentLab)

    return vCenterList

def getCompSolsDict(solsDict,vMagnitude):
    compSolsDict={}
    for sphCentStr in solsDict:
        #Convert this string to an np array
        vCenter=str2NPArray(sphCentStr)
        compSolsDict[sphCentStr]={"vLabSols":[]}
        myNormalizedVCMList=solsDict[sphCentStr]["vCMSolsNL"]
        for vNormCMSubL in myNormalizedVCMList:
            for vNormCM in vNormCMSubL:
                newestCentCM=-vNormCM*vMagnitude
                newestCentLab=vCenter+newestCentCM
                compSolsDict[sphCentStr]["vLabSols"]\
                    .append(newestCentLab)

    return compSolsDict

def getVCenterList(sphereSolsD):
    vCenterList=[]
    for sphereString in sphereSolsD:
        for velLists in sphereSolsD[sphereString]["velSols"]:
            print("Inside getVCenterList the second nested for")
            print("velLists = ", velLists)
            print("")
            for velSolSet in velLists:
                # print("velSolSet = ", velSolSet)
                for velocitySol in velSolSet:
                    vCenterList.append(velocitySol)
    return vCenterList

def fillSphereLineIdxSolsInNode(treeNode,vSCent,vSRad):
    nodeVLines=treeNode["vLines"]
    solIdxList=[]
    for vLine in nodeVLines:
        lineInterIdxList=getSphereLineIdxSols(vSCent,vSRad,vLine)
        solIdxList.append(lineInterIdxList)
    if solIdxList == []:
        return False
    if "sphereSols" not in treeNode:
        treeNode["sphereSols"]={}
    #Getting rid of the -0. It messes with the string convertion
    print("vSCent = ", vSCent)
    vSCent[vSCent==0.] = 0.
    sphereString=str([vSCent.tolist(),vSRad])
    treeNode["sphereSols"][sphereString]={"indexSols":solIdxList}
    return True

def getDictWithIdxs(treeNode,vSCent):
    nodeVLines=treeNode["vLines"]
    vSRad=treeNode["redVcm"]
    solIdxList=[]
    for vLine in nodeVLines:
        lineInterIdxList=getSphereLineIdxSols(vSCent,vSRad,vLine)
        solIdxList.append(lineInterIdxList)
    #Getting rid of the -0. It messes with the string convertion
    vSCent[vSCent==0.] = 0.
    centerStr=str(vSCent.tolist())
    sphereSols={centerStr:{}}
    sphereSols[centerStr]["solIdxList"]=solIdxList

    return sphereSols

def getDictWithIdxs2(treeNode,vSCent,sphSolsDict):
    #Getting rid of the -0. It messes with the string convertion
    vSCent[vSCent==0.] = 0.
    centerStr=str(vSCent.tolist())

    nodeVLines=treeNode["vLines"]
    vSRad=treeNode["redVcm"]
    solIdxList=[]
    for vLine in nodeVLines:
        lineInterIdxList=getSphereLineIdxSols(vSCent,vSRad,vLine)
        if lineInterIdxList == []:
            continue
        solIdxList.append(lineInterIdxList)

    if solIdxList != []:
        sphSolsDict[centerStr]={}
        sphSolsDict[centerStr]["solIdxList"]=solIdxList

    return sphSolsDict

def getSolVelsEnergiesEtcInNode2(treeNode,sphereSolsDict):
    myMass=treeNode["fMass"]

    for sphereCenterStr in sphereSolsDict:
        print("\n\n sphereCenterStr = ", sphereCenterStr)
        myNpCenter=str2NPArray(sphereCenterStr)
        print("myNpCenter = ",myNpCenter)

        print("\n\n")
        indexSolLists=sphereSolsDict[sphereCenterStr]["solIdxList"]
        for i in range(len(indexSolLists)):
            solIdxSubList=indexSolLists[i]
            #Here the "i" index corresponds to an intersection with a
            #line with the same index.
            myVLine=treeNode["vLines"][i]
            solVelList=[]
            solEList=[]
            vCMSolList=[]
            vCMNormList=[]
            for vSolIndex in solIdxSubList:
                velSol=myVLine[vSolIndex]
                solVelList.append(velSol)

                vNorm=np.linalg.norm(velSol)
                ESol=1.0/2.0*myMass*(vNorm/100.0)**2
                solEList.append(ESol)

                vCMSol=velSol-myNpCenter
                vCMSolList.append(vCMSol)

                vCMNorm=vCMSol/np.linalg.norm(vCMSol)
                vCMNormList.append(vCMNorm)
                #ECM energies should be the same as in the first
                #calculation... I'll corroborate later

            if "vLabSols" not in sphereSolsDict[sphereCenterStr]:
                sphereSolsDict[sphereCenterStr]["vLabSols"]=[]
            sphereSolsDict[sphereCenterStr]["vLabSols"].append(solVelList)

            if "energyLabSols" not in sphereSolsDict[sphereCenterStr]:
                sphereSolsDict[sphereCenterStr]["energyLabSols"]=[]
            sphereSolsDict[sphereCenterStr]["energyLabSols"].append(solEList)

            if "vCMSols" not in sphereSolsDict[sphereCenterStr]:
                sphereSolsDict[sphereCenterStr]["vCMSols"]=[]
            sphereSolsDict[sphereCenterStr]["vCMSols"].append(vCMSolList)

            if "vCMSolsNL" not in sphereSolsDict[sphereCenterStr]:
                sphereSolsDict[sphereCenterStr]["vCMSolsNL"]=[]
            sphereSolsDict[sphereCenterStr]["vCMSolsNL"].append(vCMNormList)

    return sphereSolsDict

def fillSolVelsEnergiesEtcInNode(treeNode):
    #fillSphereLineIdxSolsInNode has to be called b4 this one
    if "sphereSols" not in treeNode:
        return None
    sphereSolsDict=treeNode["sphereSols"]
    # print("inside fillSolVelsEnergiesEtcInNode about to go in a loop")
    # print("the index sols here are ")
    myMass=treeNode["fMass"]
    for sphereStr in sphereSolsDict:
        velSolListOfLists=[]
        energySolListOfLists=[]
        indexSolLists=sphereSolsDict[sphereStr]["indexSols"]
        for i in range(len(indexSolLists)):
            solIdxSubList=indexSolLists[i]
            #Here the "i" index corresponds to an intersection with a
            #line with the same index.
            myVLine=treeNode["vLines"][i]
            solVelList=[]
            solEList=[]
            for vSolIndex in solIdxSubList:
                velSol=myVLine[vSolIndex]
                solVelList.append(velSol)

                vNorm=np.linalg.norm(velSol)
                ESol=1.0/2.0*myMass*(vNorm/100.0)**2
                solEList.append(ESol)

            velSolListOfLists.append(solVelList)
            energySolListOfLists.append(solEList)
        if "velSols" not in sphereSolsDict[sphereStr]:
            sphereSolsDict[sphereStr]["velSols"]=[]
        sphereSolsDict[sphereStr]["velSols"].append(velSolListOfLists)

        if "energySols" not in sphereSolsDict[sphereStr]:
            sphereSolsDict[sphereStr]["energySols"]=[]

        sphereSolsDict[sphereStr]["energySols"].append(energySolListOfLists)
    return sphereSolsDict

def noIdxFillSolVelsEnergiesEtcInNode(treeNode,velLists):
    solEList=[]
    myMass=treeNode["fMass"]
    if velLists == []:
        return False

    for velVal in velLists:
        vNorm=np.linalg.norm(velVal)
        print("velVal,vNorm = ", velVal,vNorm)
        ESol=1.0/2.0*myMass*(vNorm/100.0)**2
        solEList.append(ESol)

    if "solutions" not in treeNode:
        treeNode["solutions"]={}

    treeNode["solutions"]["velocities"]=velLists
    treeNode["solutions"]["energies"]=solEList

    return True

def getMidPOffsets(vLine1,vLine2,vRad):
    j=0
    foundAny=False
    for i in range(len(vLine1)):
        vP1=vLine1[i]
        j=getTrainSolIdx(vP1,vRad,vLine2,j)
        if j == None:
            continue
        return [i,j]
    return None

def getAllIdxSFromNode(treeNode):
    pass #For now
    if "type" not in treeNode:
        return None
    if treeNode["type"] != "particle":
        return None
    #By the time this function is called a lot of error checks have
    #been done.
    circleCenters=treeNode["velSolutions"]#If type is initial its the
                                         #reaction center
    partVelRad=treeNode["redVcm"]
    myVLines=treeNode["vLines"]
    indexSols=[]
    for solCenter in circleCenters:
        for vLine in myVLines:
            myIdx=getSphereLineIdxSols(solCenter,partVelRad,vLine)
            indexSols+=myIdx

    return idxSols

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
