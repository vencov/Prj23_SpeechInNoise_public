#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:35:09 2023

Create a graph showing the crosscorrelation between model responses for 10 sets of sentences and model with higher gain
Figs. 3 and 4 in the paper


@author: vencov
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt


plt.close('all')
filename = 'Results/speechnoiseCalibB/W20mssada01g10.mat'
    
mat = scipy.io.loadmat(filename)

L1 = mat['Levels'].flatten()
xc1q = mat['XCq']
xc1m = mat['XCm']


filename = 'Results/speechnoiseCalibB/W20mssada02g10.mat'
mat = scipy.io.loadmat(filename)

L = mat['Levels'].flatten()
xc2q = mat['XCq']
xc2m = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada03g10.mat'
mat = scipy.io.loadmat(filename)

L = mat['Levels'].flatten()
xc3q = mat['XCq']
xc3m = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada04g10.mat'
mat = scipy.io.loadmat(filename)

L = mat['Levels'].flatten()
xc4q = mat['XCq']
xc4m = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada05g10.mat'
mat = scipy.io.loadmat(filename)

L = mat['Levels'].flatten()
xc5q = mat['XCq']
xc5m = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada06g10.mat'
mat = scipy.io.loadmat(filename)
L = mat['Levels'].flatten()
xc6q = mat['XCq']
xc6m = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada07g10.mat'
mat = scipy.io.loadmat(filename)

L = mat['Levels'].flatten()
xc7q = mat['XCq']
xc7m = mat['XCm']


filename = 'Results/speechnoiseCalibB/W20mssada08g10.mat'
mat = scipy.io.loadmat(filename)

L = mat['Levels'].flatten()
xc8q = mat['XCq']
xc8m = mat['XCm']

filename = 'Results/speechnoiseCalibB/W20mssada09g10.mat'
L = mat['Levels'].flatten()
xc9q = mat['XCq']
xc9m = mat['XCm']


filename = 'Results/speechnoiseCalibB/W20mssada10g10.mat'
mat = scipy.io.loadmat(filename)

L = mat['Levels'].flatten()
xc10q = mat['XCq']
xc10m = mat['XCm']

cm = 1/2.54  # centimeters in inches
fig,ax = plt.subplots(2,5,figsize=(20*cm,10*cm))

plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True

for i in range(10):

    ax[0,0].plot(L1,xc1q[:,i], label=str(i)), ax[0,0].set_ylim((0,0.35))
    ax[0,1].plot(L,xc2q[:,i], label=str(i)), ax[0,1].set_ylim((0,0.35))
    ax[0,2].plot(L,xc3q[:,i], label=str(i)), ax[0,2].set_ylim((0,0.35))
    ax[0,3].plot(L,xc4q[:,i], label=str(i)), ax[0,3].set_ylim((0,0.35))
    ax[0,4].plot(L,xc5q[:,i], label=str(i)), ax[0,4].set_ylim((0,0.35))
    ax[1,0].plot(L,xc6q[:,i], label=str(i)), ax[1,0].set_ylim((0,0.35))
    ax[1,1].plot(L,xc7q[:,i], label=str(i)), ax[1,1].set_ylim((0,0.35))
    ax[1,2].plot(L,xc8q[:,i], label=str(i)), ax[1,2].set_ylim((0,0.35))
    ax[1,3].plot(L,xc9q[:,i], label=str(i)), ax[1,3].set_ylim((0,0.35))
    ax[1,4].plot(L,xc10q[:,i], label=str(i)), ax[1,4].set_ylim((0,0.35))

plt.gcf().text(0.5, 0.9, 'Higher gain, 0.05 quantile', fontsize=8, fontweight='bold',ha='center')



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
fig.supylabel('$r$ (-)')
#plt.ylabel('ddd')

plt.savefig('Figures/rconvG10q.eps', format='eps')

# plot for mean value

cm = 1/2.54  # centimeters in inches
fig,ax = plt.subplots(2,5,figsize=(20*cm,10*cm))

plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True


for i in range(10):
    ax[0,0].plot(L1,xc1m[:,i], label=str(i)), ax[0,0].set_ylim((0,0.7))
    ax[0,1].plot(L,xc2m[:,i], label=str(i)), ax[0,1].set_ylim((0,0.7))
    ax[0,2].plot(L,xc3m[:,i], label=str(i)), ax[0,2].set_ylim((0,0.7))
    ax[0,3].plot(L,xc4m[:,i], label=str(i)), ax[0,3].set_ylim((0,0.7))
    ax[0,4].plot(L,xc5m[:,i], label=str(i)), ax[0,4].set_ylim((0,0.7))
    ax[1,0].plot(L,xc6m[:,i], label=str(i)), ax[1,0].set_ylim((0,0.7))
    ax[1,1].plot(L,xc7m[:,i], label=str(i)), ax[1,1].set_ylim((0,0.7))
    ax[1,2].plot(L,xc8m[:,i], label=str(i)), ax[1,2].set_ylim((0,0.7))
    ax[1,3].plot(L,xc9m[:,i], label=str(i)), ax[1,3].set_ylim((0,0.7))
    ax[1,4].plot(L,xc10m[:,i], label=str(i)), ax[1,4].set_ylim((0,0.7))

plt.gcf().text(0.5, 0.9, 'Higher gain, mean', fontsize=8, fontweight='bold',ha='center')

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
fig.supylabel('$r$ (-)')
#plt.ylabel('ddd')

plt.savefig('Figures/rconvG10m.eps', format='eps')

