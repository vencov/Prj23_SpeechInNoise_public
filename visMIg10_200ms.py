#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:30:57 2024

Create a graph showing the modulation index showing the amplitude fluctuations in the model outputs and how it changes across levels.
The graphs shows fluctuations calculated in 200-ms long time frames

Fig. 12 in the paper


@author: vencov
"""


import scipy.io
import numpy as np
import matplotlib.pyplot as plt


plt.close('all')

cf = scipy.io.loadmat('NobiliModel/cf_nobiliEXP_R3107_10dBOME.mat')
cf = cf['cf_new'].flatten()/1000

filename = 'Results/speechnoiseCalibB/MIw200ms_sada01g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI01 = mat['mDW'][0]

filename = 'Results/speechnoiseCalibB/MIw200ms_sada02g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI02 = mat['mDW'][0]

filename = 'Results/speechnoiseCalibB/MIw200ms_sada03g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI03 = mat['mDW'][0]

filename = 'Results/speechnoiseCalibB/MIw200ms_sada04g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI04 = mat['mDW'][0]


filename = 'Results/speechnoiseCalibB/MIw200ms_sada05g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI05 = mat['mDW'][0]


filename = 'Results/speechnoiseCalibB/MIw200ms_sada06g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI06 = mat['mDW'][0]


filename = 'Results/speechnoiseCalibB/MIw200ms_sada07g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI07 = mat['mDW'][0]

filename = 'Results/speechnoiseCalibB/MIw200ms_sada08g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI08 = mat['mDW'][0]

filename = 'Results/speechnoiseCalibB/MIw200ms_sada09g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI09 = mat['mDW'][0]


filename = 'Results/speechnoiseCalibB/MIw200ms_sada10g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
MI10 = mat['mDW'][0]


# set values of the modulation index larger than one to 1 (Daniel and Weber equation 7)
def set_values_above_1_to_1(arr):
    return np.clip(arr, a_min=None, a_max=1)


for i in range(len(MI01)):
    MI01[i] = set_values_above_1_to_1(MI01[i])
    MI02[i] = set_values_above_1_to_1(MI02[i])
    MI03[i] = set_values_above_1_to_1(MI03[i])
    MI04[i] = set_values_above_1_to_1(MI04[i])
    MI05[i] = set_values_above_1_to_1(MI05[i])
    MI06[i] = set_values_above_1_to_1(MI06[i])
    MI07[i] = set_values_above_1_to_1(MI07[i])
    MI08[i] = set_values_above_1_to_1(MI08[i])
    MI09[i] = set_values_above_1_to_1(MI09[i])
    MI10[i] = set_values_above_1_to_1(MI10[i])





cm = 1/2.54  # centimeters in inches
fig,ax = plt.subplots()

colorcycle = (plt.rcParams['axes.prop_cycle'].by_key()['color'])

ax.semilogx(cf,np.mean(MI01[2]/MI01[0],0),color=colorcycle[0])
ax.semilogx(cf,np.mean(MI01[4]/MI01[0],0),color=colorcycle[1])
ax.semilogx(cf,np.mean(MI01[6]/MI01[0],0),color=colorcycle[2])
ax.semilogx(cf,np.mean(MI01[8]/MI01[0],0),color=colorcycle[3])
ax.semilogx(cf,np.mean(MI01[10]/MI01[0],0),color=colorcycle[4])
ax.semilogx(cf,np.mean(MI01[12]/MI01[0],0),color=colorcycle[5])


fig,ax = plt.subplots(2,5,figsize=(20*cm,10*cm))

plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True

yLimity = (0.55,1.2)
xLimity = (0.1,10)

ax[0,0].semilogx(cf,np.mean(MI01[12]/MI01[0],0),color=colorcycle[5])
ax[0,0].semilogx(cf,np.mean(MI01[12]/MI01[0],0),color=colorcycle[5])
ax[0,0].semilogx(cf,np.mean(MI01[10]/MI01[0],0),color=colorcycle[4])
ax[0,0].semilogx(cf,np.mean(MI01[8]/MI01[0],0),color=colorcycle[3])
ax[0,0].semilogx(cf,np.mean(MI01[6]/MI01[0],0),color=colorcycle[2])
ax[0,0].semilogx(cf,np.mean(MI01[4]/MI01[0],0),color=colorcycle[1])
ax[0,0].semilogx(cf,np.mean(MI01[2]/MI01[0],0),color=colorcycle[0])


ax[0,0].set_xlim(xLimity)
ax[0,0].set_ylim(yLimity)


ax[0,1].semilogx(cf,np.mean(MI02[12]/MI02[0],0),color=colorcycle[5])
ax[0,1].semilogx(cf,np.mean(MI02[10]/MI02[0],0),color=colorcycle[4])
ax[0,1].semilogx(cf,np.mean(MI02[8]/MI02[0],0),color=colorcycle[3])
ax[0,1].semilogx(cf,np.mean(MI02[6]/MI02[0],0),color=colorcycle[2])
ax[0,1].semilogx(cf,np.mean(MI02[4]/MI02[0],0),color=colorcycle[1])
ax[0,1].semilogx(cf,np.mean(MI02[2]/MI02[0],0),color=colorcycle[0])

ax[0,1].set_xlim(xLimity)
ax[0,1].set_ylim(yLimity)


ax[0,2].semilogx(cf,np.mean(MI03[12]/MI03[0],0),color=colorcycle[5])
ax[0,2].semilogx(cf,np.mean(MI03[10]/MI03[0],0),color=colorcycle[4])
ax[0,2].semilogx(cf,np.mean(MI03[6]/MI03[0],0),color=colorcycle[2])
ax[0,2].semilogx(cf,np.mean(MI03[8]/MI03[0],0),color=colorcycle[3])
ax[0,2].semilogx(cf,np.mean(MI03[4]/MI03[0],0),color=colorcycle[1])
ax[0,2].semilogx(cf,np.mean(MI03[2]/MI03[0],0),color=colorcycle[0])






ax[0,2].set_xlim(xLimity)
ax[0,2].set_ylim(yLimity)

ax[0,3].semilogx(cf,np.mean(MI04[12]/MI04[0],0),color=colorcycle[5])
ax[0,3].semilogx(cf,np.mean(MI04[10]/MI04[0],0),color=colorcycle[4])
ax[0,3].semilogx(cf,np.mean(MI04[8]/MI04[0],0),color=colorcycle[3])
ax[0,3].semilogx(cf,np.mean(MI04[6]/MI04[0],0),color=colorcycle[2])
ax[0,3].semilogx(cf,np.mean(MI04[4]/MI04[0],0),color=colorcycle[1])
ax[0,3].semilogx(cf,np.mean(MI04[2]/MI04[0],0),color=colorcycle[0])





ax[0,3].set_xlim(xLimity)
ax[0,3].set_ylim(yLimity)

ax[0,4].semilogx(cf,np.mean(MI05[12]/MI05[0],0),color=colorcycle[5])
ax[0,4].semilogx(cf,np.mean(MI05[10]/MI05[0],0),color=colorcycle[4])
ax[0,4].semilogx(cf,np.mean(MI05[8]/MI05[0],0),color=colorcycle[3])
ax[0,4].semilogx(cf,np.mean(MI05[6]/MI05[0],0),color=colorcycle[2])
ax[0,4].semilogx(cf,np.mean(MI05[4]/MI05[0],0),color=colorcycle[1])
ax[0,4].semilogx(cf,np.mean(MI05[2]/MI05[0],0),color=colorcycle[0])





ax[0,4].set_xlim(xLimity)
ax[0,4].set_ylim(yLimity)


ax[1,0].semilogx(cf,np.mean(MI06[12]/MI06[0],0),color=colorcycle[5])
ax[1,0].semilogx(cf,np.mean(MI06[10]/MI06[0],0),color=colorcycle[4])
ax[1,0].semilogx(cf,np.mean(MI06[8]/MI06[0],0),color=colorcycle[3])
ax[1,0].semilogx(cf,np.mean(MI06[6]/MI06[0],0),color=colorcycle[2])
ax[1,0].semilogx(cf,np.mean(MI06[4]/MI06[0],0),color=colorcycle[1])
ax[1,0].semilogx(cf,np.mean(MI06[2]/MI06[0],0),color=colorcycle[0])



ax[1,0].set_xlim(xLimity)
ax[1,0].set_ylim(yLimity)

ax[1,1].semilogx(cf,np.mean(MI07[12]/MI07[0],0),color=colorcycle[5])
ax[1,1].semilogx(cf,np.mean(MI07[10]/MI07[0],0),color=colorcycle[4])
ax[1,1].semilogx(cf,np.mean(MI07[8]/MI07[0],0),color=colorcycle[3])
ax[1,1].semilogx(cf,np.mean(MI07[6]/MI07[0],0),color=colorcycle[2])
ax[1,1].semilogx(cf,np.mean(MI07[4]/MI07[0],0),color=colorcycle[1])
ax[1,1].semilogx(cf,np.mean(MI07[2]/MI07[0],0),color=colorcycle[0])





ax[1,1].set_xlim(xLimity)
ax[1,1].set_ylim(yLimity)

ax[1,2].semilogx(cf,np.mean(MI08[12]/MI08[0],0),color=colorcycle[5])
ax[1,2].semilogx(cf,np.mean(MI08[10]/MI08[0],0),color=colorcycle[4])
ax[1,2].semilogx(cf,np.mean(MI08[8]/MI08[0],0),color=colorcycle[3])
ax[1,2].semilogx(cf,np.mean(MI08[6]/MI08[0],0),color=colorcycle[2])
ax[1,2].semilogx(cf,np.mean(MI08[4]/MI08[0],0),color=colorcycle[1])
ax[1,2].semilogx(cf,np.mean(MI08[2]/MI08[0],0),color=colorcycle[0])





ax[1,2].set_xlim(xLimity)
ax[1,2].set_ylim(yLimity)


ax[1,3].semilogx(cf,np.mean(MI04[12]/MI04[0],0),color=colorcycle[5])
ax[1,3].semilogx(cf,np.mean(MI04[10]/MI04[0],0),color=colorcycle[4])
ax[1,3].semilogx(cf,np.mean(MI04[8]/MI04[0],0),color=colorcycle[3])
ax[1,3].semilogx(cf,np.mean(MI04[6]/MI04[0],0),color=colorcycle[2])
ax[1,3].semilogx(cf,np.mean(MI04[4]/MI04[0],0),color=colorcycle[1])
ax[1,3].semilogx(cf,np.mean(MI04[2]/MI04[0],0),color=colorcycle[0])





ax[1,3].set_xlim(xLimity)
ax[1,3].set_ylim(yLimity)

ax[1,4].semilogx(cf,np.mean(MI05[12]/MI05[0],0),label='90',color=colorcycle[5])
ax[1,4].semilogx(cf,np.mean(MI05[10]/MI05[0],0),label='80',color=colorcycle[4])
ax[1,4].semilogx(cf,np.mean(MI05[8]/MI05[0],0),label='70',color=colorcycle[3])
ax[1,4].semilogx(cf,np.mean(MI05[6]/MI05[0],0),label='60',color=colorcycle[2])
ax[1,4].semilogx(cf,np.mean(MI05[4]/MI05[0],0),label='50',color=colorcycle[1])
ax[1,4].semilogx(cf,np.mean(MI05[2]/MI05[0],0),label='40 dB',color=colorcycle[0])



ax[0,0].text(0.55, 0.95, 'set 01', transform=ax[0,0].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,1].text(0.55, 0.95, 'set 02', transform=ax[0,1].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,2].text(0.55, 0.95, 'set 03', transform=ax[0,2].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,3].text(0.55, 0.95, 'set 04', transform=ax[0,3].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,4].text(0.05, 0.95, 'set 05', transform=ax[0,4].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,0].text(0.55, 0.95, 'set 06', transform=ax[1,0].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,1].text(0.55, 0.95, 'set 07', transform=ax[1,1].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,2].text(0.55, 0.95, 'set 08', transform=ax[1,2].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,3].text(0.55, 0.95, 'set 09', transform=ax[1,3].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,4].text(0.55, 0.95, 'set 10', transform=ax[1,4].transAxes, fontsize=8, fontweight='bold', va='top')



ax[1,4].set_xlim(xLimity)
ax[1,4].set_ylim(yLimity)


Xtickss = (1)
ax[0,1].set_yticklabels('') 
ax[0,2].set_yticklabels('') 
ax[0,3].set_yticklabels('') 
ax[0,4].set_yticklabels('')

XticksV = (0.1,1,10)
#YticksV = (0.75,1,1.25,1.5,1.75)
XticksLab = ['0.1','1','10']

for j in range(2):
    for i in range(5):
        ax[j,i].set_xticks(XticksV) 
        ax[j,i].set_xticklabels(XticksLab)
       # ax[j,i].set_yticks(YticksV)
        if i>0:
            ax[j,i].set_yticklabels('')



fig.supxlabel('Frequency (kHz)')
fig.supylabel('$m/m_{30}$ (-)')
#plt.ylabel('ddd')

handles, labels = ax[1,4].get_legend_handles_labels()
#labels = ('40','50','60','70','80','90',)
fig.legend(handles, labels, loc='upper right', ncol= 1,fontsize=8)
plt.gcf().text(0.5, 0.9, 'Higher gain, 200-ms window', fontsize=8, fontweight='bold',ha='center')


plt.savefig('Figures/MIg10w200ms.eps', format='eps')
