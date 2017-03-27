#!/usr/bin/gnuplot --persist

degAng=22
radAng=pi/180*degAng
m=tan(radAng)

v1=7.49
v2=7.49

r=v1+v2
x0Max=sqrt((m**2+1)/m**2)*r
print x0Max

x0=27.01
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

# print xSolVal, ySolValCirc, ySolValLine

print mLine1

set xrange[0:45]
set yrange[-5:30]
set sample 1500

###Configuring the plot environment so it accepts normal & parametric
###plots on the same canvas

set title "legends test"

set multiplot

# make a box around the legend
set key box

set border 15 lw 1

# fix the margins, this is important to ensure alignment of the plots.
set lmargin at screen 0.15
set rmargin at screen 0.98
set tmargin at screen 0.90
set bmargin at screen 0.15

plot detFun(x),circFun(x), line1Eq(x)

# turn everything off
set format x ""   #numbers off
set format y ""
set xlabel ""     #label off
set ylabel ""
set border 0      #border off
unset xtics       #tics off
unset ytics
unset grid        #grid off
unset title       #title off

#Now doing the parametric stuff
set parametric

y0=detFun(xSolF(0))

# set trange[0:x0Max]
# plot (xSolF(t)+t)/2,detFun(xSolF(t))/2
set trange[x0:x0Max]
plot (xSolF(t)+t),detFun(xSolF(t))

# plot sin(t) title "sinus",NaN w l ls 2 lt 2 title "parametric line"
# set trange[0:pi]
# plot 5*sin(t)+5,5*cos(t)+5
unset parametric

unset multiplot
