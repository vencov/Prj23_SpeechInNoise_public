#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:15:25 2023

Create graphs showing the effect of feedback gain in the model. It shows a difference between the cross-correlations
for the model with higher gain and for the model with lower gain
Figs. 8 and 9 in the paper


@author: vencov
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt

filename = 'Results/speechnoiseCalibB/W20mssada01g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc1q9 = mat['XCq']
xc1m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada01g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc1q10 = mat['XCq']
xc1m10 = mat['XCm']


filename = 'Results/speechnoiseCalibB/W20mssada02g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc2q9 = mat['XCq']
xc2m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada02g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc2q10 = mat['XCq']
xc2m10 = mat['XCm']


filename = 'Results/speechnoiseCalibB/W20mssada03g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc3q9 = mat['XCq']
xc3m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada03g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc3q10 = mat['XCq']
xc3m10 = mat['XCm']


filename = 'Results/speechnoiseCalibB/W20mssada04g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc4q9 = mat['XCq']
xc4m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada04g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc4q10 = mat['XCq']
xc4m10 = mat['XCm']



filename = 'Results/speechnoiseCalibB/W20mssada05g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc5q9 = mat['XCq']
xc5m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada05g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc5q10 = mat['XCq']
xc5m10 = mat['XCm']


filename = 'Results/speechnoiseCalibB/W20mssada06g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc6q9 = mat['XCq']
xc6m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada06g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc6q10 = mat['XCq']
xc6m10 = mat['XCm']


filename = 'Results/speechnoiseCalibB/W20mssada07g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc7q9 = mat['XCq']
xc7m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada07g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc7q10 = mat['XCq']
xc7m10 = mat['XCm']


filename = 'Results/speechnoiseCalibB/W20mssada08g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc8q9 = mat['XCq']
xc8m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada08g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc8q10 = mat['XCq']
xc8m10 = mat['XCm']



filename = 'Results/speechnoiseCalibB/W20mssada09g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc9q9 = mat['XCq']
xc9m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada09g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
    

xc9q10 = mat['XCq']
xc9m10 = mat['XCm']




filename = 'Results/speechnoiseCalibB/W20mssada10g9.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc10q9 = mat['XCq']
xc10m9 = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada10g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc10q10 = mat['XCq']
xc10m10 = mat['XCm']

dxc1q = xc1q10 - xc1q9
dxc2q = xc2q10 - xc2q9
dxc3q = xc3q10 - xc3q9
dxc4q = xc4q10 - xc4q9
dxc5q = xc5q10 - xc5q9
dxc6q = xc6q10 - xc6q9
dxc7q = xc7q10 - xc7q9
dxc8q = xc8q10 - xc8q9
dxc9q = xc9q10 - xc9q9
dxc10q = xc10q10 - xc10q9

dxc1m = xc1m10 - xc1m9
dxc2m = xc2m10 - xc2m9
dxc3m = xc3m10 - xc3m9
dxc4m = xc4m10 - xc4m9
dxc5m = xc5m10 - xc5m9
dxc6m = xc6m10 - xc6m9
dxc7m = xc7m10 - xc7m9
dxc8m = xc8m10 - xc8m9
dxc9m = xc9m10 - xc9m9
dxc10m = xc10m10 - xc10m9


# draw graphs
plt.close('all')  # close all previous figures

cm = 1/2.54  # centimeters in inches
y1 = -0.2
y2 = 0.3
fig,ax = plt.subplots(2,5,figsize=(20*cm,10*cm))
for i in range(10):
    ax[0,0].plot(L1,dxc1q[:,i], label=str(i)), ax[0,0].set_ylim((y1,y2))
    ax[0,1].plot(L1,dxc2q[:,i], label=str(i)), ax[0,1].set_ylim((y1,y2))
    ax[0,2].plot(L1,dxc3q[:,i], label=str(i)), ax[0,2].set_ylim((y1,y2))
    ax[0,3].plot(L1,dxc4q[:,i], label=str(i)), ax[0,3].set_ylim((y1,y2))
    ax[0,4].plot(L1,dxc5q[:,i], label=str(i)), ax[0,4].set_ylim((y1,y2))
    ax[1,0].plot(L1,dxc6q[:,i], label=str(i)), ax[1,0].set_ylim((y1,y2))
    ax[1,1].plot(L1,dxc7q[:,i], label=str(i)), ax[1,1].set_ylim((y1,y2))
    ax[1,2].plot(L1,dxc8q[:,i], label=str(i)), ax[1,2].set_ylim((y1,y2))
    ax[1,3].plot(L1,dxc9q[:,i], label=str(i)), ax[1,3].set_ylim((y1,y2))
    ax[1,4].plot(L1,dxc10q[:,i], label=str(i)), ax[1,4].set_ylim((y1,y2))
    
#ax[0,0].grid(True)
plt.gcf().text(0.5, 0.9, '0.05 quantile', fontsize=9, fontweight='bold',ha='center')

ax[0,0].set_xticks((30,50,70,90))
ax[0,1].set_yticklabels(''), ax[0,1].set_xticks((30,50,70,90))
ax[0,2].set_yticklabels(''), ax[0,2].set_xticks((30,50,70,90))
ax[0,3].set_yticklabels(''), ax[0,3].set_xticks((30,50,70,90))
ax[0,4].set_yticklabels(''), ax[0,4].set_xticks((30,50,70,90))


ax[1,0].set_xticks((30,50,70,90))
ax[1,1].set_yticklabels(''), ax[1,1].set_xticks((30,50,70,90))
ax[1,2].set_yticklabels(''), ax[1,2].set_xticks((30,50,70,90))
ax[1,3].set_yticklabels(''), ax[1,3].set_xticks((30,50,70,90))
ax[1,4].set_yticklabels(''), ax[1,4].set_xticks((30,50,70,90))

handles, labels = ax[1,4].get_legend_handles_labels()
labels = ('1','2','3','4','5','6','7','8','9','10')
fig.legend(handles, labels, loc='right')

ax[0,0].text(0.05, 0.95, 'set 01', transform=ax[0,0].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,1].text(0.05, 0.95, 'set 02', transform=ax[0,1].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,2].text(0.05, 0.95, 'set 03', transform=ax[0,2].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,3].text(0.05, 0.95, 'set 04', transform=ax[0,3].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,4].text(0.05, 0.95, 'set 05', transform=ax[0,4].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,0].text(0.05, 0.95, 'set 06', transform=ax[1,0].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,1].text(0.05, 0.95, 'set 07', transform=ax[1,1].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,2].text(0.05, 0.95, 'set 08', transform=ax[1,2].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,3].text(0.05, 0.95, 'set 09', transform=ax[1,3].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,4].text(0.05, 0.95, 'set 10', transform=ax[1,4].transAxes, fontsize=8, fontweight='bold', va='top')

#fig.add_subplot(111, frameon=False)
#plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False

#ax[1,4].legend(('1','2','3','4','5','6','7','8','9'))

fig.supxlabel('Level (dB SPL)')
fig.supylabel('$\Delta r$ (-)')
#plt.ylabel('ddd')

plt.savefig('Figures/drconvG9q.eps', format='eps')


cm = 1/2.54  # centimeters in inches
y1 = -0.05
y2 = 0.15
fig,ax = plt.subplots(2,5,figsize=(20*cm,10*cm))
for i in range(10):
    ax[0,0].plot(L1,dxc1m[:,i], label=str(i)), ax[0,0].set_ylim((y1,y2))
    ax[0,1].plot(L1,dxc2m[:,i], label=str(i)), ax[0,1].set_ylim((y1,y2))
    ax[0,2].plot(L1,dxc3m[:,i], label=str(i)), ax[0,2].set_ylim((y1,y2))
    ax[0,3].plot(L1,dxc4m[:,i], label=str(i)), ax[0,3].set_ylim((y1,y2))
    ax[0,4].plot(L1,dxc5m[:,i], label=str(i)), ax[0,4].set_ylim((y1,y2))
    ax[1,0].plot(L1,dxc6m[:,i], label=str(i)), ax[1,0].set_ylim((y1,y2))
    ax[1,1].plot(L1,dxc7m[:,i], label=str(i)), ax[1,1].set_ylim((y1,y2))
    ax[1,2].plot(L1,dxc8m[:,i], label=str(i)), ax[1,2].set_ylim((y1,y2))
    ax[1,3].plot(L1,dxc9m[:,i], label=str(i)), ax[1,3].set_ylim((y1,y2))
    ax[1,4].plot(L1,dxc10m[:,i], label=str(i)), ax[1,4].set_ylim((y1,y2))
ax[0,0].text(0.05, 0.95, 'set 01', transform=ax[0,0].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,1].text(0.05, 0.95, 'set 02', transform=ax[0,1].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,2].text(0.05, 0.95, 'set 03', transform=ax[0,2].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,3].text(0.05, 0.95, 'set 04', transform=ax[0,3].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,4].text(0.05, 0.95, 'set 05', transform=ax[0,4].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,0].text(0.05, 0.95, 'set 06', transform=ax[1,0].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,1].text(0.05, 0.95, 'set 07', transform=ax[1,1].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,2].text(0.05, 0.95, 'set 08', transform=ax[1,2].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,3].text(0.05, 0.95, 'set 09', transform=ax[1,3].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,4].text(0.05, 0.95, 'set 10', transform=ax[1,4].transAxes, fontsize=8, fontweight='bold', va='top')
plt.gcf().text(0.5, 0.9, 'mean', fontsize=8, fontweight='bold',ha='center')

ax[0,0].set_xticks((30,50,70,90))
ax[0,1].set_yticklabels(''), ax[0,1].set_xticks((30,50,70,90))
ax[0,2].set_yticklabels(''), ax[0,2].set_xticks((30,50,70,90))
ax[0,3].set_yticklabels(''), ax[0,3].set_xticks((30,50,70,90))
ax[0,4].set_yticklabels(''), ax[0,4].set_xticks((30,50,70,90))


ax[1,0].set_xticks((30,50,70,90))
ax[1,1].set_yticklabels(''), ax[1,1].set_xticks((30,50,70,90))
ax[1,2].set_yticklabels(''), ax[1,2].set_xticks((30,50,70,90))
ax[1,3].set_yticklabels(''), ax[1,3].set_xticks((30,50,70,90))
ax[1,4].set_yticklabels(''), ax[1,4].set_xticks((30,50,70,90))

handles, labels = ax[1,4].get_legend_handles_labels()
labels = ('1','2','3','4','5','6','7','8','9','10')
fig.legend(handles, labels, loc='right')

ax[0,0].text(0.05, 0.95, 'set 01', transform=ax[0,0].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,1].text(0.05, 0.95, 'set 02', transform=ax[0,1].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,2].text(0.05, 0.95, 'set 03', transform=ax[0,2].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,3].text(0.05, 0.95, 'set 04', transform=ax[0,3].transAxes, fontsize=8, fontweight='bold', va='top')
ax[0,4].text(0.05, 0.95, 'set 05', transform=ax[0,4].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,0].text(0.05, 0.95, 'set 06', transform=ax[1,0].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,1].text(0.05, 0.95, 'set 07', transform=ax[1,1].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,2].text(0.05, 0.95, 'set 08', transform=ax[1,2].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,3].text(0.05, 0.95, 'set 09', transform=ax[1,3].transAxes, fontsize=8, fontweight='bold', va='top')
ax[1,4].text(0.05, 0.95, 'set 10', transform=ax[1,4].transAxes, fontsize=8, fontweight='bold', va='top')

#fig.add_subplot(111, frameon=False)
#plt.tick_params(labelcolor='none', which='both', top=False, bottom=False, left=False, right=False

#ax[1,4].legend(('1','2','3','4','5','6','7','8','9'))

fig.supxlabel('Level (dB SPL)')
fig.supylabel('$\Delta r$ (-)')
#plt.ylabel('ddd')

plt.savefig('Figures/drconvG9m.eps', format='eps')
