#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:53:41 2023

Create a graph showing the cross-correlation for each time frame for one sentence.

Fig. 10 in the paper

@author: vencov
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

filename = 'Results/speechnoiseCalibB/W20mssada01g9.mat'
    
mat = scipy.io.loadmat(filename)

L1g9 = mat['Levels'].flatten()
xc1q9 = mat['XCq']
xc1m9 = mat['XCm']
xctimeg9 = mat['rm_coeffAll']

filename = 'Results/speechnoiseCalibB/W20mssada01g10.mat'
    
mat = scipy.io.loadmat(filename)

L1g10 = mat['Levels'].flatten()
xc1q10 = mat['XCq']
xc1m10 = mat['XCm']
xctimeg10 = mat['rm_coeffAll']

filename = 'rec01.mat'
    
mat = scipy.io.loadmat(filename)
rec = mat['rec']


plt.close('all')  # close all previous figures

cm = 1/2.54  # centimeters in inches
y1 = -0.2
y2 = 0.3
#fig,ax = plt.subplots(figsize=(20*cm,10*cm))
fs = 44.1e3;
tx = np.linspace(0,20e-3*(len(xctimeg10[0,0])),len(xctimeg10[0,0]))


cm = 1/2.54  # centimeters in inches
y1 = -0.2
y2 = 0.3
wP = 0.4
hP = 0.8
xD = 0.05
xL = 0.1
yB = 0.14

fig,[ax1,ax2] = plt.subplots(1,2,figsize=(20*cm,8*cm))


plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True


qLine30g10 = xc1q10[0,0]*np.ones_like(tx)
mLine30g10 = xc1m10[0,0]*np.ones_like(tx)
qLine50g10 = xc1q10[4,0]*np.ones_like(tx)
mLine50g10 = xc1m10[4,0]*np.ones_like(tx)
qLine70g10 = xc1q10[8,0]*np.ones_like(tx)
mLine70g10 = xc1m10[8,0]*np.ones_like(tx)
qLine90g10 = xc1q10[12,0]*np.ones_like(tx)
mLine90g10 = xc1m10[12,0]*np.ones_like(tx)

qLine30g9 = xc1q9[0,0]*np.ones_like(tx)
mLine30g9 = xc1m9[0,0]*np.ones_like(tx)
qLine50g9 = xc1q9[4,0]*np.ones_like(tx)
mLine50g9 = xc1m9[4,0]*np.ones_like(tx)
qLine70g9 = xc1q9[8,0]*np.ones_like(tx)
mLine70g9 = xc1m9[8,0]*np.ones_like(tx)
qLine90g9 = xc1q9[12,0]*np.ones_like(tx)
mLine90g9 = xc1m9[12,0]*np.ones_like(tx)


l1 = ax1.plot(tx,xctimeg10[0,0])
l2 = ax1.plot(tx,xctimeg10[4,0])
l3 = ax1.plot(tx,xctimeg10[8,0])
l4 = ax1.plot(tx,xctimeg10[12,0])
ax1.plot(tx,qLine30g10,color=l1[0].get_color(),linestyle=':',alpha=0.3)
ax1.plot(tx,mLine30g10,color=l1[0].get_color(),linestyle='--',alpha=0.3)
ax1.plot(tx,qLine50g10,color=l2[0].get_color(),linestyle=':',alpha=0.3)
ax1.plot(tx,mLine50g10,color=l2[0].get_color(),linestyle='--',alpha=0.3)
ax1.plot(tx,qLine70g10,color=l3[0].get_color(),linestyle=':',alpha=0.3)
ax1.plot(tx,mLine70g10,color=l3[0].get_color(),linestyle='--',alpha=0.3)
ax1.plot(tx,qLine90g10,color=l4[0].get_color(),linestyle=':',alpha=0.3)
ax1.plot(tx,mLine90g10,color=l4[0].get_color(),linestyle='--',alpha=0.3)
txRec = np.arange(0,len(rec)*1/44100,1/44100)
ax1.plot(txRec,rec/max(rec),'k',alpha=0.2)

ax1.set_xlabel('Time (s)')
ax1.set_ylabel('$r(t)$')
ax1.set_xlim((0,2.5))
ax1.set_ylim((0,1))
ax1.set_position([xL,yB,wP,hP])
plt.gcf().text(0.15, 0.95, 'Higher gain', fontsize=8, fontweight='bold',ha='center')

plt.gcf().text(0.15, 0.85, 'Telefonoval', fontsize=8, fontweight='normal',ha='center')


ax2.plot(tx,xctimeg9[0,0])
ax2.plot(tx,xctimeg9[4,0])
ax2.plot(tx,xctimeg9[8,0])
ax2.plot(tx,xctimeg9[12,0])
ax2.plot(tx,qLine30g9,color=l1[0].get_color(),linestyle=':',alpha=0.3)
ax2.plot(tx,mLine30g9,color=l1[0].get_color(),linestyle='--',alpha=0.3)
ax2.plot(tx,qLine50g9,color=l2[0].get_color(),linestyle=':',alpha=0.3)
ax2.plot(tx,mLine50g9,color=l2[0].get_color(),linestyle='--',alpha=0.3)
ax2.plot(tx,qLine70g9,color=l3[0].get_color(),linestyle=':',alpha=0.3)
ax2.plot(tx,mLine70g9,color=l3[0].get_color(),linestyle='--',alpha=0.3)
ax2.plot(tx,qLine90g9,color=l4[0].get_color(),linestyle=':',alpha=0.3)
ax2.plot(tx,mLine90g9,color=l4[0].get_color(),linestyle='--',alpha=0.3)

txRec = np.arange(0,len(rec)*1/44100,1/44100)
ax2.plot(txRec,rec/max(rec),'k',alpha=0.2)

#ax2.plot(tx,qLine,color='k',linestyle=':')
#ax2.plot(tx,mLine,color='k',linestyle='--')
ax2.set_xlabel('Time (s)')
#ax2.set_ylabel('$r(t)$')
ax2.set_xlim((0,2.5))
ax2.set_ylim((0,1))
ax2.set_position([xL+wP+xD,yB,wP,hP])
ax2.set_yticklabels([])
#plt.legend()

plt.gcf().text(0.6, 0.85, 'Telefonoval', fontsize=8, fontweight='normal',ha='center')

plt.gcf().text(0.9, 0.95, 'Lower gain', fontsize=8, fontweight='bold',ha='center')

#plt.subplots_adjust(left=10,
#                    bottom=1,
#                    wpace=0.05
#                    )


ax2.legend(('30','50','70','90 dB SPL'),loc='upper center', bbox_to_anchor=(0,1.1),
          ncol=4,fancybox=True,shadow=True)

plt.savefig('Figures/xcorr.png', format='png')

