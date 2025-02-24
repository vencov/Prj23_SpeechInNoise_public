#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  7 22:54:36 2023

script which plots IO functions derived from the numerical solution of the cochlear model
IO functions show the level dependence of BM displacement at a given place on the BM
four frequencies: 0.5, 1, 2, 4 kHz
two variants of the model gain: g10, g9

Fig. A1 in the paper

@author: vencov
"""


import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

plt.close('all')
filename = 'Results/io/iog10_1000Hz.mat'
    
mat = scipy.io.loadmat(filename)

Levels = mat['Levels'].flatten()

io1kHz_g10 = mat['out'].flatten()

filename = 'Results/io/iog10_2000Hz.mat'
    
mat = scipy.io.loadmat(filename)

Levels = mat['Levels'].flatten()

io2kHz_g10 = mat['out'].flatten()

filename = 'Results/io/iog10_4000Hz.mat'

mat = scipy.io.loadmat(filename)

Levels = mat['Levels'].flatten()

io4kHz_g10 = mat['out'].flatten()

filename = 'Results/io/iog10_500Hz.mat'

mat = scipy.io.loadmat(filename)

Levels = mat['Levels'].flatten()

io500Hz_g10 = mat['out'].flatten()



filename = 'Results/io/iog9_1000Hz.mat'
    
mat = scipy.io.loadmat(filename)

Levels = mat['Levels'].flatten()

io1kHz_g9 = mat['out'].flatten()

filename = 'Results/io/iog9_2000Hz.mat'
    
mat = scipy.io.loadmat(filename)

Levels = mat['Levels'].flatten()

io2kHz_g9 = mat['out'].flatten()

filename = 'Results/io/iog9_4000Hz.mat'

mat = scipy.io.loadmat(filename)

Levels = mat['Levels'].flatten()

io4kHz_g9 = mat['out'].flatten()

filename = 'Results/io/iog9_500Hz.mat'

mat = scipy.io.loadmat(filename)

Levels = mat['Levels'].flatten()

io500Hz_g9 = mat['out'].flatten()



cm = 1/2.54  # centimeters in inches
fig,ax = plt.subplots(1,4,figsize=(20*cm,6*cm))


plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True


#fig.tight_layout(pad=10.0)

# extrapolate on io data for passive response
p1 = 20*np.log10(io500Hz_g10[-2:])
l1 = Levels[-2:]

f = interpolate.interp1d(l1, p1, fill_value = "extrapolate")
l1Int = f(Levels)

p2 = 20*np.log10(io1kHz_g10[-2:])
l2 = Levels[-2:]
f = interpolate.interp1d(l2, p2, fill_value = "extrapolate")
l2Int = f(Levels)


p3 = 20*np.log10(io2kHz_g10[-2:])
l3 = Levels[-2:]
f = interpolate.interp1d(l3, p3, fill_value = "extrapolate")
l3Int = f(Levels)


p4 = 20*np.log10(io4kHz_g10[-2:])
l4 = Levels[-2:]
f = interpolate.interp1d(l4, p4, fill_value = "extrapolate")
l4Int = f(Levels)

p1g9 = 20*np.log10(io500Hz_g9[-2:])
l1g9 = Levels[-2:]

f = interpolate.interp1d(l1g9, p1g9, fill_value = "extrapolate")
l1Intg9 = f(Levels)

p2g9 = 20*np.log10(io1kHz_g9[-2:])
l2g9 = Levels[-2:]
f = interpolate.interp1d(l2g9, p2g9, fill_value = "extrapolate")
l2Intg9 = f(Levels)


p3g9 = 20*np.log10(io2kHz_g9[-2:])
l3g9 = Levels[-2:]
f = interpolate.interp1d(l3g9, p3g9, fill_value = "extrapolate")
l3Intg9 = f(Levels)


p4g9 = 20*np.log10(io4kHz_g9[-2:])
l4g9 = Levels[-2:]
f = interpolate.interp1d(l4g9, p4g9, fill_value = "extrapolate")
l4Intg9 = f(Levels)


ax[0].plot(Levels,20*np.log10(io500Hz_g10))
ax[0].plot(Levels,l1Int,linewidth=0.4,color=[0,0,0])
#ax[0].plot(Levels,l1Intg9,linewidth=0.4,color=[0,0,0])
ax[1].plot(Levels,20*np.log10(io1kHz_g10))
ax[1].plot(Levels,l2Int,linewidth=0.4,color=[0,0,0])
ax[2].plot(Levels,20*np.log10(io2kHz_g10))
ax[2].plot(Levels,l3Int,linewidth=0.4,color=[0,0,0])
ax[3].plot(Levels,20*np.log10(io4kHz_g10))
ax[3].plot(Levels,l4Int,linewidth=0.4,color=[0,0,0])

ax[0].plot(Levels,20*np.log10(io500Hz_g9))
ax[1].plot(Levels,20*np.log10(io1kHz_g9))
ax[2].plot(Levels,20*np.log10(io2kHz_g9))
ax[3].plot(Levels,20*np.log10(io4kHz_g9))

# calculate gains from the io curves
# higher gain
gain500Hzg10 = Levels[np.where(l1Int>20*np.log10(io500Hz_g10[0]))[0][0]]
gain1kHzg10 = Levels[np.where(l2Int>20*np.log10(io1kHz_g10[0]))[0][0]]
gain2kHzg10 = Levels[np.where(l3Int>20*np.log10(io2kHz_g10[0]))[0][0]]
gain4kHzg10 = Levels[np.where(l4Int>20*np.log10(io4kHz_g10[0]))[0][0]]
# lower gain
gain500Hzg9 = Levels[np.where(l1Intg9>20*np.log10(io500Hz_g9[0]))[0][0]]
gain1kHzg9 = Levels[np.where(l2Intg9>20*np.log10(io1kHz_g9[0]))[0][0]]
gain2kHzg9 = Levels[np.where(l3Intg9>20*np.log10(io2kHz_g9[0]))[0][0]]
gain4kHzg9 = Levels[np.where(l4Intg9>20*np.log10(io4kHz_g9[0]))[0][0]]

# draw arrows to show the gain in the IO functions
ax[0].annotate("", xy=(10, -50), xytext=(55, -50),
            arrowprops=dict(arrowstyle="<->"))
ax[0].text(60,-50,str(gain500Hzg10)+' dB',fontsize=8)

ax[0].annotate("", xy=(13, -60), xytext=(45, -60),
            arrowprops=dict(arrowstyle="<->"))
ax[0].text(50,-62,str(gain1kHzg9)+' dB',fontsize=8)

ax[1].annotate("", xy=(3, -50), xytext=(51, -50),
            arrowprops=dict(arrowstyle="<->"))
ax[1].text(60,-50,str(gain1kHzg10)+' dB',fontsize=8)

ax[1].annotate("", xy=(7, -60), xytext=(41, -60),
            arrowprops=dict(arrowstyle="<->"))
ax[1].text(50,-62,str(gain1kHzg9)+' dB',fontsize=8)

ax[2].annotate("", xy=(2, -50), xytext=(51, -50),
            arrowprops=dict(arrowstyle="<->"))
ax[2].text(60,-50,str(gain2kHzg10)+' dB',fontsize=8)

ax[2].annotate("", xy=(7, -60), xytext=(41, -60),
            arrowprops=dict(arrowstyle="<->"))
ax[2].text(50,-62,str(gain2kHzg9)+' dB',fontsize=8)

ax[3].annotate("", xy=(8, -50), xytext=(52, -50),
            arrowprops=dict(arrowstyle="<->"))
ax[3].text(60,-50,str(gain4kHzg10)+' dB',fontsize=8)

ax[3].annotate("", xy=(11, -60), xytext=(43, -60),
            arrowprops=dict(arrowstyle="<->"))
ax[3].text(50,-62,str(gain4kHzg9)+' dB',fontsize=8)



ax[1].set_yticklabels(''), ax[2].set_yticklabels(''), ax[3].set_yticklabels('')
ylim = (-80,0)
xlim = (0,100)
ax[0].set_ylim(ylim), ax[1].set_ylim(ylim), ax[2].set_ylim(ylim), ax[3].set_ylim(ylim)
ax[0].set_xlim(xlim), ax[1].set_xlim(xlim), ax[2].set_xlim(xlim), ax[3].set_xlim(xlim)
ax[0].set_xticks((0,20,40,60,80,100)), ax[1].set_xticks((0,20,40,60,80,100))
ax[2].set_xticks((0,20,40,60,80,100)), ax[3].set_xticks((0,20,40,60,80,100))

plt.subplots_adjust(left=0.1,
                    bottom=0.18,
                    )

ax[0].text(0.05, 7, '0.5 kHz', fontsize=8, fontweight='bold', va='top')
ax[1].text(0.05, 7, '1 kHz', fontsize=8, fontweight='bold', va='top')
ax[2].text(0.05, 7, '2 kHz', fontsize=8, fontweight='bold', va='top')
ax[3].text(0.05, 7, '4 kHz', fontsize=8, fontweight='bold', va='top')

fig.supxlabel('Level (dB SPL)')
fig.supylabel('BM displ. (dB re 1 a.u.)')


plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True

plt.savefig('Figures/io.eps', format='eps')