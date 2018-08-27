from math import *
import numpy as np

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

def getAllEcms(mE1,mE2,E1L):
    vels=getVelcm(mE1,mE2,E1L)
    # mE1=getEMass(iso1)
    # mE2=getEMass(iso2)
    #Alternative way
    # mu=mE1*mE2/(mE1+mE2)
    # rVel=vels[0]-vels[1]
    # print 1.0/2.0*mu*rVel**2
    E1cm=0.5*(vels[0]/c)**2*mE1
    E2cm=0.5*(vels[1]/c)**2*mE2
    EcmAvail0=E1cm+E2cm
    EcmSys=0.5*(vels[2]/c)**2*(mE1+mE2)
    return E1cm,E2cm,EcmAvail0,EcmSys


#ECM is really the available energy in the center of mass system.
def getEcmsFromECM2(m1,m2,ECM):
    #For example, in a decay ECM=Q
    # m1=getEMass(iso1)
    # m2=getEMass(iso2)
    mu=1.0*m1*m2/(m1+m2)
    P=sqrt(2.0*mu*ECM)/c
    E1=0.5*(P*c)**2/m1
    E2=0.5*(P*c)**2/m2
    return E1,E2

def getEcmAvailOutFromInVals0(ECMIn,ECMAvailIn,mIn,mOut,Q):
    ECMAvailOut=ECMIn*(1-(mIn/mOut))+ECMAvailIn+Q
    return ECMAvailOut

# def getEcmAvailOutFromInVals1(ECMIn,ECMAvailIn,mIn,mOut,Q):
#     ECMOut=getECMOutFromIn(ECMIn,mIn,mOut)
#     EcmAvailOut=

def getECMOutFromIn(ECMIn,mIn,mOut):
    ECMOut=1.0*(mIn/mOut)*ECMIn
    return ECMOut

def getVelFromEAndM(E,m):
    v=sqrt(2.0*E/m)*c
    return v

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
    #Don't forget they are magnitudes!!
    v1p=abs(v1-Vcm)
    v2p=abs(v2-Vcm)
    return v1p,v2p,Vcm

def getQVal(m1,m2,m3,m4):
    Q=(m1+m2-m3-m4)
    return Q

def getVoutCM(vInCM,mIn,mOut):
    vOutCM=1.0*mIn/mOut*vInCM
#Not using relativistic case here, these are betas (v/c)
def getSimpleVels(m1,E1cm,m2,E2cm):
    v1cm=sqrt(2.0*E1cm/m1)
    v2cm=sqrt(2.0*E2cm/m2)
    return v1cm,v2cm

def getThetaPhi(vLab):
    x,y,z=vLab
    vMag=np.linalg.norm(vLab)
    theta=acos(z/vMag)
    phi=atan2(y,x)
    #Using degrees for now
    return [degrees(theta),degrees(phi)]
