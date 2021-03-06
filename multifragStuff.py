from math import *
import numpy as np

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

from simpleKinematics import *
from miscellaneous import *
import copy

from termcolor import colored


def makeTreeCompletion(binTreeDict):
    makeInitialTreeCompletion(binTreeDict)

    print("Trying to pull every line automatically")
    generalList=getDirectFreeRoute(binTreeDict)
    if generalList == []:
        print("Error!!! Are you sure you filled \
        the free part dict correctly?!")
        return False

    boolPull=pullEveryLine(binTreeDict,generalList)
    if boolPull == True:
        print("Success in pulling every line")
    else:
        print("Unsuccessful pull :'-(")
        return False

    fillBool=fillMajorSols(binTreeDict,generalList)
    print("The fillBool is ",fillBool)
    fillSecSolsAlongTree(binTreeDict)
    #Put here the special vLine for the initial dict


def makeInitialTreeCompletion(binTreeDict):
    """Solves the system on its local CM system"""
    fillInit(binTreeDict)
    myDesc=fillTreeDescriptorL(binTreeDict)
    # print("myDesc = ",myDesc)
    # printTree(binTreeDict)

    completeTree0(binTreeDict)
    completeTree1(binTreeDict)
    # completeTree2(binTreeDict)

def getInitSolsDict(binTreeDict):
    #This is our free CM solution, we at least know this one! ;-)
    vCM=binTreeDict["outRedVcm"]
    sCenter=np.array([0.0,0.0,0.0])
    centerStr=str(sCenter.tolist())
    sphereSols={centerStr:{}}
    vCMVect=np.array([0.0,0.0,vCM])
    sphereSols[centerStr]["vLabSols"]=[vCMVect]

    #The only case when lab and cm solutions are the same
    sphereSols[centerStr]["vCMSols"]=[vCMVect]
    sphereSols[centerStr]["vCMPair"]=[sCenter,vCMVect]

    #Implementing the npCenter for stopping error propagation
    sphereSols[centerStr]["npCenter"]=sCenter
    return sphereSols

def getCompletedSolTree(treeNode,solsDict):
    myMass=treeNode["fMass"]
    treeNode["structType"]="goType"

    for vCenterStr in solsDict:
        #Get the CM vel of the system
        # sysCMVel=str2NPArray(vCenterStr)

        #Here we can override the sysCMVel that is less accurate
        npCenter=solsDict[vCenterStr]["npCenter"] #More precise
        sysCMVel=npCenter

        print("npCenter = ",npCenter)
        print("vCenterStr = ",vCenterStr)

        myLabVelList=solsDict[vCenterStr]["vLabSols"]
        solsDict[vCenterStr]["labEnergy"]=[]
        solsDict[vCenterStr]["vCMSols"]=[]
        solsDict[vCenterStr]["vCMMags"]=[] #4 debugging
        solsDict[vCenterStr]["thetaPhi"]=[]

        for myLabVel in myLabVelList:
            vCentNorm=np.linalg.norm(myLabVel)
            ECentSol=1.0/2.0*myMass*(vCentNorm/100.0)**2
            solsDict[vCenterStr]["labEnergy"].append(ECentSol)

            #Now the vel @ the CM system
            myCMVel=myLabVel-sysCMVel
            solsDict[vCenterStr]["vCMSols"].append(myCMVel)

            #4 debugging
            myCMMag=np.linalg.norm(myCMVel)
            solsDict[vCenterStr]["vCMMags"].append(myCMMag)

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
    EcmList=getAllEcms(mPro,mTar,ELab)
    inEcmAvail=EcmList[2]
    binTreeDict["inEcmAvail"]=inEcmAvail
    inEcmSys=EcmList[3]
    binTreeDict["inEcmSys"]=inEcmSys
    binTreeDict["inESum"]=inEcmAvail+inEcmSys
    #Saving the beta
    binTreeDict["inBVcm"]=getVelcm(mPro,mTar,ELab)[2]/c
    inRedVcm=binTreeDict["inBVcm"]*100
    binTreeDict["inRedVcm"]=inRedVcm
    #This is only for setting a search range, the final vel won't be
    #this high. This criteria will be improved eventually.
    binTreeDict["inBVLabMax"]=binTreeDict["inRedVcm"]

def completeTree0(binTreeDict):
    if binTreeDict == {}:
        return

    finalMass=getFinalMass(binTreeDict)
    if finalMass != None:
        binTreeDict["fMass"]=finalMass

    qVal=getNodeQVal(binTreeDict) #Always None
    if qVal != None:
        print("filling tree with", qVal)
        binTreeDict["Q"]=qVal

    if "dictList" not in binTreeDict:
        return

    for e in binTreeDict["dictList"]:
        completeTree0(e)

def completeTree1(binTreeDict):
    if binTreeDict == {} or "name" not in binTreeDict:
        return

    qVal=getNodeQVal(binTreeDict)
    if qVal != None:
        binTreeDict["Q"]=qVal

    print("0qVal was = ",qVal)
    print("Node name is "+binTreeDict["name"])

    inOutMass=getNodeInOutMass(binTreeDict)
    if inOutMass != None:
        print("filling tree with", inOutMass)
        inMass,outMass=inOutMass
        binTreeDict["inMass"]=inMass
        binTreeDict["outMass"]=outMass

        print("Also including the out energies")
        inEcmSys=binTreeDict["inEcmSys"]
        inEcmAvail=binTreeDict["inEcmAvail"]

        if "leaf" in binTreeDict["descriptors"]:
            return

        exE1,exE2=getChildEx(binTreeDict)
        locEx=0.0
        if "exE" in binTreeDict:
            locEx=binTreeDict["exE"]
        outEcmSys=1.0*(inMass/outMass)*inEcmSys
        binTreeDict["outEcmSys"]=outEcmSys
        outEcmAvail=inEcmSys*(1-1.0*(inMass/outMass))+inEcmAvail+qVal+locEx-(exE1+exE2)
        binTreeDict["outEcmAvail"]=outEcmAvail
        binTreeDict["outEcmSum"]=outEcmSys+outEcmAvail

        binTreeDict["outBVcm"]=getVelFromEAndM(outEcmSys,outMass)/c
        outRedVcm=binTreeDict["outBVcm"]*100
        binTreeDict["outRedVcm"]=outRedVcm
        print("in "+binTreeDict["name"]+"outRedVcm = "+str(outEcmSys))
        #This is only for setting a search range, the final vel won't be
        #this high. This criteria will be improved eventually.
        binTreeDict["outBVLabMax"]=binTreeDict["outRedVcm"]
        BVcm=sqrt(2.0*outEcmAvail/outMass)#Leaving out *c for now
        # dictNode["outBVcm"]=BVcm
        # dictNode["outRedVcm"]=BVcm*100
        # maxVel=binTreeDict["outBVLabMax"]
        binTreeDict["outBVLabMax"]+=BVcm*100

        childMasses=getChildMasses(binTreeDict)
        if childMasses != None:
            m1,m2=childMasses
            print("qVal was = ",qVal)
            print("locEx,outEcmAvail = ",locEx,outEcmAvail)
            E1cm,E2cm=getEcmsFromECM2(m1,m2,outEcmAvail)
            # maxVel=binTreeDict["outBVLabMax"]
            maxVel=65 #This needs to be changed!!!!!
            pushNewEcmAndVels2(E1cm,E2cm,binTreeDict["dictList"],maxVel)
            # specialPushNewEcmAndVels(E1cm,E2cm,outEcmSys,binTreeDict["dictList"],maxVel)
    # else:
    #     binTreeDict["outEcmSys"]=binTreeDict["inEcmSys"]
    #     binTreeDict["outEcmAvail"]=binTreeDict["inEcmAvail"]


    if "dictList" not in binTreeDict:
        return

    for e in binTreeDict["dictList"]:
        completeTree1(e)

def completeTree2(binTreeDict):
    if binTreeDict == {}:
        return

    outEcmAvail=getAvailE(binTreeDict)
    # outEcmAvail=binTreeDict["outEcmAvail"]
    print("outEcmAvail = ",outEcmAvail)
        # eAvail=21.4147 #for ground
    # eAvail=40.0147 #for 18.6
    # Q = -7.506343852104692
    if "inMass" in binTreeDict:
        print("#####################")
        print("###inMass is present####")
        print("#####################")
        print("eAvail and inEcmAvail = %0.4f,%0.4f" % (outEcmAvail,binTreeDict["inEcmAvail"]))
    if outEcmAvail != None:
        print("the local name is = "+binTreeDict["name"])
        print("outEcmAvail=%0.4f" %(outEcmAvail))

        binTreeDict["EAvail"]=outEcmAvail
        childMasses=getChildMasses(binTreeDict)
        if childMasses != None:
            m1,m2=childMasses
            E1cm,E2cm=getEcmsFromECM2(m1,m2,outEcmAvail)
            inEcmSys=binTreeDict["inEcmSys"]
            maxVel=binTreeDict["outBVLabMax"]
            pushNewEcmAndVels(E1cm,E2cm,binTreeDict["dictList"],maxVel)

    if "dictList" not in binTreeDict:
        return

    for e in binTreeDict["dictList"]:
        completeTree2(e)

def pushNewEcmAndVels(inE1cmAvail,inE2cmAvail,dictNode,maxVel):
    m1=dictNode[0]["fMass"]
    Q1,locEx1=0.0, 0.0
    if "exE" in dictNode[0]:
        locEx1=dictNode[0]["exE"]
    if "Q" in dictNode[0]:
        Q1=dictNode[0]["Q"]
    dictNode[0]["inEcmSys"]=inE1cmAvail# +locEx1
    BVcm1=sqrt(2.0*inE1cmAvail/m1)#Leaving out *c for now
    dictNode[0]["inBVcm"]=BVcm1
    dictNode[0]["inRedVcm"]=BVcm1*100
    dictNode[0]["inBVLabMax"]=maxVel+BVcm1*100

    m2=dictNode[1]["fMass"]
    Q2,locEx2=0.0, 0.0
    if "exE" in dictNode[1]:
        locEx1=dictNode[1]["exE"]
    if "Q" in dictNode[1]:
        Q1=dictNode[1]["Q"]
    dictNode[1]["inEcmSys"]=inE2cmAvail# +locEx2
    BVcm2=sqrt(2.0*inE2cmAvail/m2)#Leaving out *c for now
    dictNode[1]["inBVcm"]=BVcm2
    dictNode[1]["inRedVcm"]=BVcm2*100
    dictNode[1]["inBVLabMax"]=maxVel+BVcm2*100

def pushNewEcmAndVels2(inE1cmSys,inE2cmSys,dictNode,maxVel):
    m1=dictNode[0]["fMass"]
    Q1,locEx1=0.0, 0.0
    if "exE" in dictNode[0]:
        locEx1=dictNode[0]["exE"]
    if "Q" in dictNode[0]:
        Q1=dictNode[0]["Q"]
    dictNode[0]["inEcmSys"]=inE1cmSys
    dictNode[0]["inEcmAvail"]=0.0
    BVcm1=sqrt(2.0*inE1cmSys/m1)#Leaving out *c for now
    dictNode[0]["inBVcm"]=BVcm1
    dictNode[0]["inRedVcm"]=BVcm1*100
    dictNode[0]["inBVLabMax"]=maxVel+BVcm1*100
    if "leaf" in dictNode[0]["descriptors"]:
        dictNode[0]["outEcmSys"]=inE1cmSys
        dictNode[0]["outEcmAvail"]=inE1cmSys

        dictNode[0]["outBVcm"]=BVcm1
        dictNode[0]["outRedVcm"]=BVcm1*100
        dictNode[0]["outBVLabMax"]=maxVel+BVcm1*100

    m2=dictNode[1]["fMass"]
    Q2,locEx2=0.0, 0.0
    if "exE" in dictNode[1]:
        locEx1=dictNode[1]["exE"]
    if "Q" in dictNode[1]:
        Q1=dictNode[1]["Q"]
    dictNode[1]["inEcmSys"]=inE2cmSys
    dictNode[1]["inEcmAvail"]=0.0
    BVcm2=sqrt(2.0*inE2cmSys/m2)#Leaving out *c for now
    dictNode[1]["inBVcm"]=BVcm2
    dictNode[1]["inRedVcm"]=BVcm2*100
    dictNode[1]["inBVLabMax"]=maxVel+BVcm2*100
    if "leaf" in dictNode[1]["descriptors"]:
        dictNode[1]["outEcmSys"]=inE2cmSys
        dictNode[1]["outEcmAvail"]=inE2cmSys
        dictNode[1]["outBVcm"]=BVcm2
        dictNode[1]["outRedVcm"]=BVcm2*100
        dictNode[1]["outBVLabMax"]=maxVel+BVcm2*100

def specialPushNewEcmAndVels(inE1cmAvail,inE2cmAvail,inEcmSys,dictNode,maxVel):
    print("pushing vals into "+dictNode[0]["name"]+" and "+dictNode[1]["name"])
    m1=dictNode[0]["fMass"]
    Q1,locEx1=0.0, 0.0
    if "exE" in dictNode[0]:
        locEx1=dictNode[0]["exE"]
    if "Q" in dictNode[0]:
        Q1=dictNode[0]["Q"]
    myEcm=inE1cmAvail
    # if "leaf" in dictNode[0]["descriptors"]:
    #     myEcm=inE1cmAvail+inEcmSys
    dictNode[0]["inEcmSys"]=inEcmSys
    dictNode[0]["inEcmAvail"]=myEcm
    BVcm1=sqrt(2.0*myEcm/m1)#Leaving out *c for now
    dictNode[0]["inBVcm"]=BVcm1
    dictNode[0]["inRedVcm"]=BVcm1*100
    dictNode[0]["inBVLabMax"]=maxVel+BVcm1*100
    if "leaf" in dictNode[0]["descriptors"]:
        dictNode[0]["outEcmSys"]=myEcm # +locEx1
        dictNode[0]["outEcmAvail"]=myEcm # +locEx1

        dictNode[0]["outBVcm"]=BVcm1
        dictNode[0]["outRedVcm"]=BVcm1*100
        dictNode[0]["outBVLabMax"]=maxVel+BVcm1*100

    m2=dictNode[1]["fMass"]
    Q2,locEx2=0.0, 0.0
    if "exE" in dictNode[1]:
        locEx1=dictNode[1]["exE"]
    if "Q" in dictNode[1]:
        Q1=dictNode[1]["Q"]
    myEcm=inE2cmAvail
    # if "leaf" in dictNode[1]["descriptors"]:
    #     myEcm=inE2cmAvail+inEcmSys
    dictNode[1]["inEcmSys"]=inEcmSys# +locEx2
    dictNode[1]["inEcmAvail"]=myEcm
    BVcm2=sqrt(2.0*myEcm/m2)#Leaving out *c for now
    dictNode[1]["inBVcm"]=BVcm2
    dictNode[1]["inRedVcm"]=BVcm2*100
    dictNode[1]["inBVLabMax"]=maxVel+BVcm2*100

    if "leaf" in dictNode[1]["descriptors"]:
        dictNode[1]["outEcmSys"]=myEcm # +locEx1
        dictNode[1]["outEcmAvail"]=myEcm # +locEx1
        dictNode[1]["outBVcm"]=BVcm2
        dictNode[1]["outRedVcm"]=BVcm2*100
        dictNode[1]["outBVLabMax"]=maxVel+BVcm2*100

def getStraightLinePoints(theta,phi,vLabMax,part=4000):
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
        vLabMax=binTreeDict["outBVLabMax"]
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
    vLLIdx=0#keeping track of the indices
    for i in range(len(vLines1)):
        vLine1=vLines1[i]
        for j in range(len(vLines2)):
            vLine2=vLines2[j]
            cmLine=getMidPointLine(vLine1,vLine2,vRad,myFrac)
            vLineList.append(cmLine)
            # vLLIdx=vLineList.index(cmLine)
            offsets=getMidPOffsets(vLine1,vLine2,vRad)
            offsetList[0].append([vLLIdx,offsets])

            parentChildIdx1=i #vLines1.index(vLine1)
            parentChildIdx2=j #vLines2.index(vLine2)
            lineParentsIdxList[0].append([vLLIdx,[parentChildIdx1,parentChildIdx2]])
            vLLIdx+=1

    #Sweep from line 2 to line 1
    for i in range(len(vLines2)):
        vLine2=vLines2[i]
        for j in range(len(vLines1)):
            vLine1=vLines1[j]
            cmLine=getMidPointLine(vLine2,vLine1,vRad,1-myFrac)
            vLineList.append(cmLine)
            # print("cmLine = ",cmLine)
            # vLLIdx=vLineList.index(cmLine)
            print("Line idx = ",vLLIdx)
            offsets=getMidPOffsets(vLine2,vLine1,vRad)
            parentChildIdx1=j #vLines1.index(vLine1)
            parentChildIdx2=i #vLines2.index(vLine2)

            offsetList[1].append([vLLIdx,offsets])
            lineParentsIdxList[1].append([vLLIdx,[parentChildIdx1,parentChildIdx2]])
            vLLIdx+=1

    binTreeDict["vLines"]=vLineList
    binTreeDict["offsets"]=offsetList
    binTreeDict["lParentsIdxs"]=lineParentsIdxList
    return True

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
    vMagL=[branch2Solve["outRedVcm"],branch2Go["outRedVcm"]]
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
    print("Inside getComplementarySolsDict entering the for")
    for sphCentStr in solsDict:
        #Convert this string to an np array
        # vCenter=str2NPArray(sphCentStr)
        vCenter=solsDict[sphCentStr]["npCenter"]#More precise

        print("npCenter val is = ",solsDict[sphCentStr]["npCenter"])

        myVCMList=solsDict[sphCentStr]["vCMSols"]

        compSolsDict[sphCentStr]={"vLabSols":[],\
                                  "vCMPair":[],\
                                  "npCenter":solsDict[sphCentStr]["npCenter"]}

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
    vSRad=treeNode["outRedVcm"]
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
        sphSolsDict[centerStr]["npCenter"]=vSCent

    return sphSolsDict

def getSolVelsEnergiesEtcInNode(treeNode,sphereSolsDict):
    myMass=treeNode["fMass"]
    treeNode["structType"]="solveType"


    print("Inside getSolVelsEnergiesEtcInNode entering the for")
    for sphereCenterStr in sphereSolsDict:
        #Surely some numerical errors lying around but I'll live with
        #it for now
        # myNpCenter=str2NPArray(sphereCenterStr)
        myNpCenter=sphereSolsDict[sphereCenterStr]["npCenter"]#More precise

        print("npCenter present in for ",sphereCenterStr)
        print("sphere..npCenter = ", sphereSolsDict[sphereCenterStr]["npCenter"])

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
            debugECMList=[]
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
                debugVCMNorm=np.linalg.norm(vCMSol)
                debugECM=1.0/2.0*myMass*(debugVCMNorm/100.0)**2
                debugECMList.append(debugECM)

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

            if "debugECMs" not in sphereSolsDict[sphereCenterStr]:
                sphereSolsDict[sphereCenterStr]["debugECMs"]=[]
            sphereSolsDict[sphereCenterStr]["debugECMs"].append(debugECMList)

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
        initRedVcm=treeNode["outRedVcm"]
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
    vCMSols=b2SSolsD["vCMSols"]
    for i in range(len(vCMSols)):
        print(colored("Inside getB2SolClnSolsIdxs","magenta"))
        lineSolCML=vCMSols[i]
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

def getSimpleSecSolIdxL(centerStr,solsDict):
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

def getSecSolParentIdxWithNonesL(centerStr,treeNode):
    localSolsD=treeNode["solsDict"][centerStr]
    solIdxList=localSolsD["solIdxList"]
    #For relating the inner indices to the outer real line indices
    idxLineList=localSolsD["idxLineList"]

    secSolParentIdxL=[]
    for i in range(len(solIdxList)):
        lineIdx=idxLineList[i]
        lineParAndOffsets=getLineParIdxsAndOffsets(lineIdx,treeNode)
        sweepStr,parIdx1,parIdx2,offIdxVal=lineParAndOffsets
        solIdxSubL=solIdxList[i]

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

            print(colored("theEntry = "+str(theEntry),"red"))
            secSolParentIdxL.append(theEntry)

    return secSolParentIdxL

def getSecSolParentIdxWithNonesL2(centerStr,treeNode):
    #Make sure the treeNode already has the secSolsD
    print(treeNode["secSolsDict"])
    localSecSolsD=treeNode["secSolsDict"][centerStr]
    simpleSecSolIdxL=localSecSolsD["simpleSecSolIdxL"]

    secSolParentIdxL=[]
    # print(colored("inside getSecSolParentIdxWithNonesL2","red"))
    # print(solIdxList)
    for secSolL in simpleSecSolIdxL:
        lineIdx,pIdx=secSolL
        lineParAndOffsets=getLineParIdxsAndOffsets(lineIdx,treeNode)
        sweepStr,parIdx1,parIdx2,offIdxVal=lineParAndOffsets
        print(colored("Inside the infamous for ","red"))
        if sweepStr == "left":
            theEntry=[sweepStr,
                      [parIdx1,pIdx+offIdxVal],
                      [lineIdx,pIdx],
                      [parIdx2,None]]
        else:
            theEntry=[sweepStr,
                      [parIdx1,None],
                      [lineIdx,pIdx],
                      [parIdx2,pIdx+offIdxVal]]

        secSolParentIdxL.append(theEntry)

    return secSolParentIdxL

def fillInitSecSols(treeNode):
    if treeNode["structType"] != "solveType":
        print("Error fillInitSecSols should only be called on solveType")
        return

    secSolsDict={}
    solsDict=treeNode["solsDict"]
    for centStr in solsDict:
        simpleSecSolIdxL,threeSecSolIdxL=getRawSecSolsLEntry(centStr,treeNode)
        secSolsDict[centStr]={}
        secSolsDict[centStr]["simpleSecSolIdxL"]=simpleSecSolIdxL

        if threeSecSolIdxL != None:
            secSolsDict[centStr]["threeSecSolIdxL"]=threeSecSolIdxL

        secSolsDict[centStr]["npCenter"]=solsDict[centStr]["npCenter"]
    treeNode["secSolsDict"]=secSolsDict

def getRawSecSolsLEntry(centerStr,treeNode):
    solsDict=treeNode["solsDict"]
    simpleSecSolIdxL=getSimpleSecSolIdxL(centerStr,solsDict)
    print(colored("HERE "*5,"red"))

    if checkIfLastPartNode(treeNode):
        print(colored("HERE "*5,"blue"))
        return [simpleSecSolIdxL,None]

    secSolParentIdxWithNonesL=getSecSolParentIdxWithNonesL(centerStr,treeNode)
    print(colored("HERE "*10,"yellow"))
    threeSecSolIdxL=getThreeSecSolsIdxL(secSolParentIdxWithNonesL,treeNode)

    return [simpleSecSolIdxL,threeSecSolIdxL]

def getThreeSecSolsIdxL(secSolParentIdxL,treeNode):

    print(colored("Inside getThreeSecSolsIdxL","magenta"))
    print("secSolParentIdxL = ",secSolParentIdxL)
    leftN,rightN=treeNode["dictList"]

    lVLines,rVLines=leftN["vLines"],rightN["vLines"]
    nVLines=treeNode["vLines"]

    lVMag,rVMag=leftN["outRedVcm"],rightN["outRedVcm"]

    secSolsL=[]

    for e in secSolParentIdxL:
        sweepStr,lInfo,nInfo,rInfo=e
        print(colored("e = ","magenta"))
        print(colored(e,"magenta"))
        nLineIdx,nPointIdx=nInfo
        nVel=nVLines[nLineIdx][nPointIdx]
        nVInfo=[nLineIdx,nPointIdx]

        lLineIdx,lPointIdx=lInfo
        rLineIdx,rPointIdx=rInfo

        if sweepStr == "left":
            lVel=lVLines[lLineIdx][lPointIdx]
            lVcm=lVel-nVel
            lVInfo=[lLineIdx,lPointIdx]

            vNormCM=lVcm/np.linalg.norm(lVcm)
            rVcm=-vNormCM*rVMag

            rVel=nVel+rVcm

            rPointIdx=getClosestIdx(rVel,rVLines[rLineIdx])

            rVInfo=[rLineIdx,rPointIdx]
        else:
            rVel=rVLines[rLineIdx][rPointIdx]
            rVcm=rVel-nVel
            rVInfo=[rLineIdx,rPointIdx]

            vNormCM=rVcm/np.linalg.norm(rVcm)
            lVcm=-vNormCM*lVMag

            lVel=nVel+lVcm
            lPointIdx=getClosestIdx(lVel,lVLines[lLineIdx])

            lVInfo=[lLineIdx,lPointIdx]

        secSolsE=[sweepStr,lVInfo,nVInfo,rVInfo]
        print(colored("secSolsE = "+str(secSolsE),"yellow"))
        secSolsL.append(secSolsE)

    return secSolsL

def getClosestIdx(vPoint,vLine):
    dist_2=np.sum((vPoint-vLine)**2,axis=1)
    return np.argmin(dist_2)

def fillSecSolsAlongTree(treeNode):
    print("Entering the fillSecSolsAlongTree")
    #Check if it has children
    if "dictList" not in treeNode:
        return

    lNode,rNode=treeNode["dictList"]

    if "structType" in lNode and lNode["structType"]=="solveType":
        print("fillSecSolsAlongTree left node")
        fillSecSols(lNode)
        fillSecSolsAlongTree(rNode)
        return
    elif "structType" in rNode and rNode["structType"]=="solveType":
        print("fillSecSolsAlongTree right node")
        fillSecSols(rNode)
        fillSecSolsAlongTree(lNode)
        return

    print(colored("In fillSecSolsAlongTree this should be printed once at the end!!","magenta"))

    return

def completeSecSolNode(treeNode):
    #make sure the tree node was "properly" prefilled
    if "secSolsDict" not in treeNode:
        print(colored("Something went really wrong, secSolsDict was not found","magenta"))
        return

    secSolsDict=treeNode["secSolsDict"]

    fMass=treeNode["fMass"]
    vLines=treeNode["vLines"]
    for centerStr in secSolsDict:
        secSolsDict[centerStr]["labVSols"]=[]
        secSolsDict[centerStr]["vCMSols"]=[]
        secSolsDict[centerStr]["vCMMag"]=[]
        secSolsDict[centerStr]["labEnergy"]=[]
        secSolsDict[centerStr]["thetaPhi"]=[]
        simpleSecSolL=secSolsDict[centerStr]["simpleSecSolIdxL"]
        # centerVcm=str2NPArray(centerStr)
        print("Right b4 assigning npCenter on secSolsDict")
        print("centerStr = ",centerStr)
        print("treeNode[\"name\"] = ", treeNode["name"])
        centerVcm=secSolsDict[centerStr]["npCenter"]
        for sSecSol in simpleSecSolL:
            lineIdx,pointIdx=sSecSol
            vLabVal=vLines[lineIdx][pointIdx]
            secSolsDict[centerStr]["labVSols"].append(vLabVal)

            vLabValNorm=np.linalg.norm(vLabVal)
            labEnergy=1.0/2.0*fMass*(vLabValNorm/100.0)**2
            secSolsDict[centerStr]["labEnergy"].append(labEnergy)

            vCM=vLabVal-centerVcm
            secSolsDict[centerStr]["vCMSols"].append(vCM)

            vCMMag=np.linalg.norm(vCM)
            secSolsDict[centerStr]["vCMMag"].append(vCMMag)

            #Getting the lab angles
            thetaPhi=getThetaPhi(vLabVal)
            secSolsDict[centerStr]["thetaPhi"].append(thetaPhi)

def fillSecSols(treeNode):
    if "structType" in treeNode and treeNode["structType"] == "solveType":
        fillInitSecSols(treeNode)

    completeSecSolNode(treeNode)

    if checkIfLastPartNode(treeNode):
        return

    secSolsDict=treeNode["secSolsDict"]
    lTreeNode,rTreeNode=treeNode["dictList"]
    lSecSolsD,rSecSolsD={},{}
    vLines=treeNode["vLines"]
    lParentBool=checkIfLastPartNode(lTreeNode)
    rParentBool=checkIfLastPartNode(rTreeNode)

    print(colored("Danger part!!!","red"))
    print(colored("name = "+treeNode["name"],"yellow"))
    for centerStr in secSolsDict:
        threeSecSolIdxL=secSolsDict[centerStr]["threeSecSolIdxL"]
        print("threeSecSolIdxL = ")
        print(threeSecSolIdxL)
        for threeSecSolIdx in threeSecSolIdxL:
            print("threeSecSolIdx = ")
            print(threeSecSolIdx)
            sweepStr,lInfo,nInfo,rInfo=threeSecSolIdx
            nLineIdx,nPointIdx=nInfo
            newVel=vLines[nLineIdx][nPointIdx]
            newCentStr=npArray2Str(newVel)

            if newCentStr not in lSecSolsD:
                if lParentBool:
                    lSecSolsD[newCentStr]={"simpleSecSolIdxL":[],
                                           "npCenter":newVel}
                else:
                    lSecSolsD[newCentStr]={"simpleSecSolIdxL":[],
                                           "threeSecSolIdxL":[],
                                           "npCenter":newVel}

                if rParentBool:
                    rSecSolsD[newCentStr]={"simpleSecSolIdxL":[],
                                           "npCenter":newVel}
                else:
                    rSecSolsD[newCentStr]={"simpleSecSolIdxL":[],
                                           "threeSecSolIdxL":[],
                                           "npCenter":newVel}

            lSecSolsD[newCentStr]["simpleSecSolIdxL"].append(lInfo)
            rSecSolsD[newCentStr]["simpleSecSolIdxL"].append(rInfo)

    print(colored("THE PUSHING PART!!!","yellow"))
    #Pushing the values on the child nodes, prepopulating the the
    #dictionary.
    print(colored(lTreeNode["name"],"magenta"))
    lTreeNode["secSolsDict"]=lSecSolsD
    print(colored(rTreeNode["name"],"magenta"))
    rTreeNode["secSolsDict"]=rSecSolsD

    #Here somehow the threesecsols need to be defined b4 already b4 I
    #look through them!...?..!
    for centerStr in secSolsDict:
        threeSecSolIdxL=secSolsDict[centerStr]["threeSecSolIdxL"]
        for threeSecSolIdx in threeSecSolIdxL:
            sweepStr,lInfo,nInfo,rInfo=threeSecSolIdx
            nLineIdx,nPointIdx=nInfo
            newVel=vLines[nLineIdx][nPointIdx]
            newCentStr=npArray2Str(newVel)

            print(colored("MAJOR LOOOK HEEEEEERE","cyan"))
            if not lParentBool:
                print(colored("YEAH "+lTreeNode["name"],"blue"))
                lSecSolParentIdxWithNonesL=getSecSolParentIdxWithNonesL2(newCentStr,lTreeNode)
                print(colored(lSecSolParentIdxWithNonesL,"red"))
                lThreeSecSolIdxL=getThreeSecSolsIdxL(lSecSolParentIdxWithNonesL,lTreeNode)
                print(colored("The new element is "+str(lThreeSecSolIdxL),"green"))

                lSecSolsD[newCentStr]["threeSecSolIdxL"]+=lThreeSecSolIdxL

            if not rParentBool:
                print(colored(rTreeNode["name"],"green"))
                rSecSolParentIdxWithNonesL=getSecSolParentIdxWithNonesL2(newCentStr,rTreeNode)
                print(colored(rSecSolParentIdxWithNonesL,"red"))
                rThreeSecSolIdxL=getThreeSecSolsIdxL(rSecSolParentIdxWithNonesL,rTreeNode)
                print(colored("The new element is "+str(rThreeSecSolIdxL),"green"))
                if rThreeSecSolIdxL == []:
                    print(colored("AN EMPTY RIGHT LIST!!","red"))

                rSecSolsD[newCentStr]["threeSecSolIdxL"]+=rThreeSecSolIdxL

    #Pushing the values on the child nodes again
    lTreeNode["secSolsDict"]=lSecSolsD
    print(colored(lTreeNode["name"],"magenta"))
    print(colored(lSecSolsD,"blue"))

    print(colored(rTreeNode["name"],"magenta"))
    print(colored(rSecSolsD,"blue"))
    rTreeNode["secSolsDict"]=rSecSolsD


    #Doing the recursive call on both child nodes
    fillSecSols(lTreeNode)
    fillSecSols(rTreeNode)
