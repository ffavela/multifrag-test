from multifragStuff import *

beamE=60.0 #MeV
#Masses are in MeV/c^2
mC=11177.9292

mOxy=14899.168598161144
mAlpha=3728.401315862896

mBe=7456.894471212898

exEnergy=3.04
mBeEx=mBe+exEnergy

print(getEcm(mC,mC,beamE))

print("Q values")
berReactQ=getQVal(mC,mC,mOxy,mBeEx)
alphasReactQ=getQVal(mC,mC,mOxy,2*mAlpha)

print(berReactQ)
print(alphasReactQ)

print("Available energies")
berEnergy=getAvailEnergy(mC,mC,mOxy,mBeEx,beamE)
print(berEnergy)

alphasE=getAvailEnergy(mC,mC,mOxy,2*mAlpha,beamE)
print(alphasE)

print("Energies for each system")

print("Case berEx")
EOxyBer,EBerEx=getEcmsFromECM2(mOxy,mBeEx,berEnergy)
print(EOxyBer,EBerEx)

EOxy,EAlphas=getEcmsFromECM2(mOxy,2*mAlpha,alphasE)

print("Case alphas")
print(EOxy,EAlphas)

print("getting cm velocities")

print("Berillium case")
vOxyBer,vBerEx=getSimpleVels(mOxy,EOxyBer,mBeEx,EBerEx)
print("vOxyBer, vBerEx")
print(vOxyBer,vBerEx)

print("Alphas case")
vOxy,vAlphas=getSimpleVels(mOxy,EOxy,2*mAlpha,EAlphas)
print("vOxy, vAlphas")
print(vOxy,vAlphas)

print("\n\nThe oxygen velocity in the center of mass frame\n\
 is finally defined, now is the alphas turn\n\n")
