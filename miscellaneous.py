from termcolor import colored
import numpy as np
from math import *
import random

easyStr="#"*50

#####################################
######printing stuff part############
#####################################

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

def printFreePartProp(initDict):
    #First get the free part route.

    # freePartRoute=getDirectFreeRoute(initDict)
    freePartRoute=generalList #This should be improved
    print("The freePartRoute is",freePartRoute)
    #Now get the dictionary that is at the end of the route
    freePartDict=getFreePartDict(initDict,freePartRoute)
    print("The name is "+freePartDict["name"])
    solsDict=freePartDict["solsDict"]
    for centStr in solsDict:
        print("center = "+centStr)
        centSol=solsDict[centStr]
        for energySol in centSol["labEnergy"]:
            print(colored(energySol,"magenta"))

def getFreePartDict(treeNode,freePartRoute):
    if len(freePartRoute) == 1:
        return treeNode["dictList"][freePartRoute[0]]
    newNode=treeNode["dictList"][freePartRoute[0]]
    freePartDict=getFreePartDict(newNode,freePartRoute[1:])
    return freePartDict

def printLastNodes(binTreeDict):
    print("Properties at last particle")
    printFreePartProp(binTreeDict)
    print("")
    print("Properties at detectors")
    printPropAtDetector(binTreeDict)
#####################################
######printing stuff part end########
#####################################

#############################################
#########plotting part#######################
#############################################
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

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


def modifyAx4Arrows(ax,genSimpVCMD):
    for centStr in genSimpVCMD:
        vVal=str2NPArray(centStr)
        vXVal,vYVal,vZVal=vVal
        myRandColor=getRandomColor()
        for vCMVal in genSimpVCMD[centStr]:
            newVLab=vCMVal+vVal
            vCMX,vCMY,vCMZ=newVLab
            vCMArrow=Arrow3D([vXVal, vCMX], [vYVal, vCMY],
                             [vZVal, vCMZ],
                             mutation_scale=20,
                             lw=1,
                             arrowstyle="-|>", color=myRandColor)
            ax.add_artist(vCMArrow)

def getRandomColor():
    r = lambda: random.randint(0,255)
    randColor=('#%02X%02X%02X' % (r(),r(),r()))
    return randColor

#############################################
#########plotting part end###################
#############################################

#############################################
#########some string operarions##############
#############################################

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

#############################################
#########some string operarions end##########
#############################################

#############################################
#########simple tree operarions##############
#############################################
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

#This is dangerous, bad idea to use global variables, I'll leave it
#for now.
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

def checkIfLastFragment(treeNode):
    freePartBool=checkIfNodeIsFreePart(treeNode)
    lastPartBool=checkIfLastPartNode(treeNode)

    if freePartBool == True or lastPartBool == True:
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

def fillDetectorRouteD(treeNode,detectorRouteD,currentRoute=[]):
    #To be useful call it on a binary dict tree
    if checkIfLastPartNode(treeNode):
        #If here then it was connected to a detector
        dName=getDName(treeNode)
        detectorRouteD[dName]=currentRoute
        return
    if checkIfNodeIsFreePart(treeNode):
        #Not interested here
        return

    dictList=treeNode["dictList"]
    for i in range(len(dictList)):
        newNode=dictList[i]
        newRoute=currentRoute+[i]
        fillDetectorRouteD(newNode,detectorRouteD,newRoute)
    return

def getDName(treeNode):
    #Only to be called on a fragment node that has a detector as a
    #child!!!
    dictList=treeNode["dictList"]
    for e in range(len(dictList)):
        childD=dictList[e]
        if "type" in childD and childD["type"]=="detector":
            return childD["name"]
    print("Error, should not have arrived here!!")

def printPropAtDetector(binTreeDict):
    dRouteD={}
    fillDetectorRouteD(binTreeDict,dRouteD)

    for dName in dRouteD:
        print("detector "+dName)
        routeL=dRouteD[dName]
        myNode=getMyNode(binTreeDict,routeL)
        print(colored("particle Name "+myNode["name"],"red"))
        mySolsStr="solsDict"
        if "secSolsDict" in myNode:
            mySolsStr="secSolsDict"
        mySolsD=myNode[mySolsStr]
        for centStr in mySolsD:
            print("center = "+centStr)
            energyList=mySolsD[centStr]["labEnergy"]
            print(colored(energyList,"magenta"))

def getMyNode(treeNode,routeL):
    if routeL == []:
        return treeNode
    i=routeL[0]
    newTNode=treeNode["dictList"][i]
    myNode=getMyNode(newTNode,routeL[1:])
    return myNode

def fillGeneralSimplifiedVCMD(binTreeDict,genSimpVCMD):
    #The binTreeDict needs to be solved at this point
    solsStr="solsDict"
    if "secSolsDict" in binTreeDict:
        solsStr="secSolsDict"
    mySolsD=binTreeDict[solsStr]
    for centStr in mySolsD:
        myVCML=mySolsD[centStr]["vCMSols"]
        if centStr not in genSimpVCMD:
            genSimpVCMD[centStr]=[]
        genSimpVCMD[centStr]+=myVCML

    lastFragCheckBool=checkIfLastFragment(binTreeDict)
    if lastFragCheckBool == True:
        return

    leftNode=binTreeDict["dictList"][0]
    rightNode=binTreeDict["dictList"][1]

    fillGeneralSimplifiedVCMD(leftNode,genSimpVCMD)
    fillGeneralSimplifiedVCMD(rightNode,genSimpVCMD)

def getGeneralSimplifiedVCMD(binTreeDict):
    genSimpVCMD={}
    fillGeneralSimplifiedVCMD(binTreeDict,genSimpVCMD)
    return genSimpVCMD

#############################################
#########simple tree operarions end##########
#############################################

#############################################
#########simple coord transformations########
#############################################

def spherToCart(r,theta,phi):
    x=r*sin(theta)*cos(phi)
    y=r*sin(theta)*sin(phi)
    z=r*cos(theta)
    return x,y,z

#############################################
#########simple coord transformations end####
#############################################