#!/usr/bin/gnuplot

reset
set terminal pngcairo size 350,262 enhanced font 'Verdana,10'
set output "cmLine000.png"

system('[ -e animation ] && rm -rf animation')
system('[ ! -e animation ] && mkdir -p animation')

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

degAng=22
radAng=pi/180*degAng
m=tan(radAng)

v1=7.49
v2=7.49

r=v1+v2
x0Max=sqrt((m**2+1)/m**2)*r
print x0Max

x0=30.01
detFun(x)=m*x
circFun(x)=sqrt(r**2-(x-x0)**2)

xSolF(x)=(x+sqrt(x**2-(m**2+1)*(x**2-r**2)))/(m**2+1)

xSolFSec(x)=(x-sqrt(x**2-(m**2+1)*(x**2-r**2)))/(m**2+1)


# segFunc(x)=(x < 20 || x > 30? NaN: 30)

# solCM(x)=(x < 0 || x > x0Max ? NaN: detFun((xSolF(x)+x)/2)/2)

# print xSolVal, ySolValCirc, ySolValLine

# print mLine1


unset multiplot

set xrange[0:65]
set yrange[-5:30]
set sample 1500

###Configuring the plot environment so it accepts normal & parametric
###plots on the same canvas

set title "legends test"

# set multiplot

# # make a box around the legend
# set key box

set border 15 lw 1

# fix the margins, this is important to ensure alignment of the plots.
set lmargin at screen 0.15
set rmargin at screen 0.98
set tmargin at screen 0.90
set bmargin at screen 0.15

xSolVal=xSolF(x0)
ySolValCirc=circFun(xSolVal)
ySolValLine=detFun(xSolVal)

mLine1=ySolValLine/(xSolVal-x0)
line1Eq(x)=(x <= 0 || x > xSolVal ? NaN: mLine1*(x-x0))
line1Sec(x)=(line1Eq(x) < 0 ? NaN: line1Eq(x))

line2Eq(x)=(x <= 0 || x < xSolVal ? NaN: mLine1*(x-x0))
line2Sec(x)=(line2Eq(x) < 0 ? NaN: line2Eq(x))

myLineEq(x)=(mLine1 > 0? line1Sec(x): line2Sec(x))

detFunSec(x)=(detFun(x) > 0 ? detFun(x): NaN )

cF=0.5

frac=0.1
myCount=0
myIncFunc(aValue)=(aValue < 0 ? 1: 0)

do for [x00=0:int(x0Max/frac)] {
    x0=frac*x00
    outfile = sprintf('animation/cmLine%03.0f.png',x00)
    xSolVal=xSolF(x0)
    ySolValCirc=circFun(xSolVal)
    ySolValLine=detFun(xSolVal)

    mLine1=ySolValLine/(xSolVal-x0)

    set output outfile
    set object 1 circle at first (xSolVal+x0)*cF,\
    ySolValLine*cF radius\
    char 0.1 fillstyle empty border lc rgb '#00cc66' lw 2

     set object circle at first (xSolVal+x0)*cF,\
     ySolValLine*cF radius\
     char 0.01 fillstyle empty border lc rgb '#aa0099' lw 2

    set object 2 circle at first x0,0 radius char 0.2 \
    fillstyle empty border lc rgb '#aabbaa' lw 2

    set object 3 circle at first xSolVal,\
    ySolValLine radius char 0.2 \
    fillstyle empty border lc rgb '#aabbaa' lw 2

    plot detFun(x),circFun(x), myLineEq(x), 0
}

do for [x00=0:int(x0Max/frac)-152] {
    x0=x0Max-frac*x00
    outfile = sprintf('animation/cmLineSec%03.0f.png',x00)
    xSolVal=xSolFSec(x0)
    ySolValCirc=circFun(xSolVal)
    ySolValLine=detFun(xSolVal)

    mLine1=ySolValLine/(xSolVal-x0)

    set output outfile
    set object 1 circle at first (xSolVal+x0)*cF,\
    ySolValLine*cF radius\
    char 0.1 fillstyle empty border lc rgb '#00cc66' lw 2

    set object circle at first (xSolVal+x0)*cF,\
    ySolValLine/2 radius\
    char 0.01 fillstyle empty border lc rgb '#666699' lw 2

    set object 2 circle at first x0,0 radius char 0.2 \
    fillstyle empty border lc rgb '#aabbaa' lw 2

    set object 3 circle at first xSolVal,\
    ySolValLine radius char 0.2 \
    fillstyle empty border lc rgb '#aabbaa' lw 2

    plot detFun(x),circFun(x), myLineEq(x), 0
}


# #Now doing the parametric stuff
# set parametric

# y0=detFun(xSolF(0))

# # set trange[0:x0Max]
# set trange[0:x0Max]
# plot (xSolF(t)+t)/2,detFun(xSolF(t))/2 lt 5
# set trange[x0Max:0]
# plot (xSolFSec(t)+t)/2,detFunSec(xSolFSec(t))/2 lt 7
# # set trange[x0:x0Max]
# # plot (xSolF(t)+t),detFun(xSolF(t))

# # plot sin(t) title "sinus",NaN w l ls 2 lt 2 title "parametric line"
# # set trange[0:pi]
# # plot 5*sin(t)+5,5*cos(t)+5
# unset parametric

# # plot detFun(x),circFun(x), line1Eq(x), 0


system('convert -delay 1 -loop 0 animation/*.png animation/ani.gif')

