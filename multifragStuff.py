from math import *

def getEcmsFromECM2(m1,m2,ECM):
    #For example, in a decay ECM=Q
    # m1=getEMass(iso1)
    # m2=getEMass(iso2)
    mu=1.0*m1*m2/(m1+m2)
    P=sqrt(2.0*mu*ECM)/c
    E1=0.5*(P*c)**2/m1
    E2=0.5*(P*c)**2/m2
    return E1,E2

def getAvailEnergy(iso1,iso2,isoEject,isoRes,E1L,E2L=0):
    E1cm,E2cm,Ecm=getEcm(iso1,iso2,E1L)
    Q=getIsoQVal(iso1,iso2,isoEject,isoRes)
    return Ecm+Q

def getAllVs(iso1,iso2,isoE,isoR,E1L):
    v1cm,v2cm,Vcm=getVelcm(iso1,iso2,E1L)
    EcmAvail=getAvailEnergy(iso1,iso2,isoE,isoR,E1L)
    ejectE,resE=getEcmsFromECM(isoE,isoR,EcmAvail)
    print(ejectE,resE)
    vE=sqrt(2.0*ejectE/getEMass(isoE))*c
    vR=sqrt(2.0*resE/getEMass(isoR))*c

def getVelcm(iso1,iso2,E1):
    m1=getEMass(iso1)
    m2=getEMass(iso2)
    v1=sqrt(2.0*E1/m1)*c
    v2=0 #assuming it is still
    Vcm=(1.0*v1*m1+1.0*v2*m2)/(m1+m2)
    v1p=v1-Vcm
    v2p=v2-Vcm
    return v1p,v2p,Vcm

def getQVal(m1,m2,m3,m4):
    Q=(m1+m2-m3-m4)
    return Q
