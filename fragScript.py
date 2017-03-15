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

print(getAvailEnergy(mC,mC,mOxy,mBeEx,beamE))

print(getAvailEnergy(mC,mC,mOxy,2*mAlpha,beamE))
