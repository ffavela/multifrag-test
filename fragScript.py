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
print("Getting the Vcm of the initial system")
initVelsCM=getVelcm(mC,mC,beamE)
print(initVelsCM[2]/c)

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

print("Q values")
print("For the Be case")
berSysQ=getQVal(mBeEx,0,mAlpha,mAlpha)
print(berSysQ)

print("For the alphas, 0 obviously")
alphasSysQ=getQVal(mAlpha,mAlpha,mAlpha,mAlpha)
print(alphasSysQ)

print("Now getting their available energies @ cm")

print("4 the excited 8Be breakup")
ExBeBreakE=getAvailEnergy0(mBeEx,mAlpha,mAlpha,berEnergy)
print(ExBeBreakE)

print("4 the 2 alpha system")
print("Q=0 in this case")
alphasAvailE=getAvailEnergy0(2*mAlpha,mAlpha,mAlpha,EAlphas)
print(alphasAvailE)

print("Getting the Ecms")

print("alphas from 8BeEx")
alphasBeECM=getEcmsFromECM2(mAlpha,mAlpha,ExBeBreakE)
print(alphasBeECM)

print("direct breakup alphas")
dBAlphas=getEcmsFromECM2(mAlpha,mAlpha,alphasAvailE)
print(dBAlphas)

print("\nNow getting the alpha's velocity for each final case\n")

print("the ones from Berillium")
print(getSimpleVels(mAlpha,alphasBeECM[0],mAlpha,alphasBeECM[1]))

print("the ones from direct")
print(getSimpleVels(mAlpha,dBAlphas[0],mAlpha,dBAlphas[1]))
