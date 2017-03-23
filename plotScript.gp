#!/usr/bin/gnuplot --persist

degAng=28.5
radAng=pi/180*degAng
m=tan(radAng)

v1=7.49
v2=7.49

r=v1+v2
x0Max=sqrt((m**2+1)/m**2)*r
print x0Max

x0=5.0
detFun(x)=m*x
circFun(x)=sqrt(r**2-(x-x0)**2)

xSolF(x)=(x+sqrt(x**2-(m**2+1)*(x**2-r**2)))/(m**2+1)

xSolVal=xSolF(x0)
ySolValCirc=circFun(xSolVal)
ySolValLine=detFun(xSolVal)

mLine1=ySolValLine/(xSolVal-x0)
line1Eq(x)=(x <= x0 || x > xSolVal ? NaN: mLine1*(x-x0))

set object circle at first (xSolVal+x0)/2,ySolValLine/2 radius char 0.5 \
    fillstyle empty border lc rgb '#aa1100' lw 2

# segFunc(x)=(x < 20 || x > 30? NaN: 30)

solCM(x)=(x < 0 || x > x0Max ? NaN: detFun((xSolF(x)+x)/2)/2)

print xSolVal, ySolValCirc, ySolValLine

set xrange[0:45]
set yrange[0:30]
set sample 1500

plot detFun(x),circFun(x), line1Eq(x), solCM(x)
