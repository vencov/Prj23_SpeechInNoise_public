#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 15:32:27 2023

plot isointensity responses (BM displacement relative to the input) derived from the
numerical solution of the cochlear model

Figure in the appendix, Fig. 2A


@author: vencov


"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

plt.close('all')
filename = 'Results/isoint/isointg10Lv20dB1000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr1 = mat['fvect'].flatten()
bmresp20f1kHz = mat['bmresp'].flatten()
meresp20f1kHz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv20dB1000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr1kHzg9 = mat['fvect'].flatten()
bmresp20f1kHzg9 = mat['bmresp'].flatten()
meresp20f1kHzg9 = mat['meresp'].flatten()



filename = 'Results/isoint/isointg10Lv40dB1000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr1kHz = mat['fvect'].flatten()
bmresp40f1kHz = mat['bmresp'].flatten()
meresp40f1kHz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv40dB1000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr1kHzg9 = mat['fvect'].flatten()
bmresp40f1kHzg9 = mat['bmresp'].flatten()
meresp40f1kHzg9 = mat['meresp'].flatten()


filename = 'Results/isoint/isointg10Lv60dB1000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr1kHz = mat['fvect'].flatten()
bmresp60f1kHz = mat['bmresp'].flatten()
meresp60f1kHz = mat['meresp'].flatten()

filename = 'Results/isoint/isointg9Lv60dB1000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr1kHzg9 = mat['fvect'].flatten()
bmresp60f1kHzg9 = mat['bmresp'].flatten()
meresp60f1kHzg9 = mat['meresp'].flatten()

filename = 'Results/isoint/isointg10Lv80dB1000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr1kHz = mat['fvect'].flatten()
bmresp80f1kHz = mat['bmresp'].flatten()
meresp80f1kHz = mat['meresp'].flatten()

filename = 'Results/isoint/isointg9Lv80dB1000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr1kHzhg9 = mat['fvect'].flatten()
bmresp80f1kHzg9 = mat['bmresp'].flatten()
meresp80f1kHzg9 = mat['meresp'].flatten()


filename = 'Results/isoint/isointg10Lv20dB500Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr500Hz = mat['fvect'].flatten()
bmresp20f500Hz = mat['bmresp'].flatten()
meresp20f500Hz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv20dB500Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr500Hzg9 = mat['fvect'].flatten()
bmresp20f500Hzg9 = mat['bmresp'].flatten()
meresp20f500Hzg9 = mat['meresp'].flatten()


filename = 'Results/isoint/isointg10Lv40dB500Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr500Hz = mat['fvect'].flatten()
bmresp40f500Hz = mat['bmresp'].flatten()
meresp40f500Hz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv40dB500Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr500Hzg9 = mat['fvect'].flatten()
bmresp40f500Hzg9 = mat['bmresp'].flatten()
meresp40f500Hzg9 = mat['meresp'].flatten()

filename = 'Results/isoint/isointg10Lv60dB500Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr500Hz = mat['fvect'].flatten()
bmresp60f500Hz = mat['bmresp'].flatten()
meresp60f500Hz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv60dB500Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr500Hzg9 = mat['fvect'].flatten()
bmresp60f500Hzg9 = mat['bmresp'].flatten()
meresp60f500Hzg9 = mat['meresp'].flatten()


filename = 'Results/isoint/isointg10Lv80dB500Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr500Hz = mat['fvect'].flatten()
bmresp80f500Hz = mat['bmresp'].flatten()
meresp80f500Hz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv80dB500Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr500Hzg9 = mat['fvect'].flatten()
bmresp80f500Hzg9 = mat['bmresp'].flatten()
meresp80f500Hzg9 = mat['meresp'].flatten()


filename = 'Results/isoint/isointg10Lv20dB2000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr2kHz = mat['fvect'].flatten()
bmresp20f2kHz = mat['bmresp'].flatten()
meresp20f2kHz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv20dB2000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr2kHzg9 = mat['fvect'].flatten()
bmresp20f2kHzg9 = mat['bmresp'].flatten()
meresp20f2kHzg9 = mat['meresp'].flatten()

filename = 'Results/isoint/isointg10Lv40dB2000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr2kHz = mat['fvect'].flatten()
bmresp40f2kHz = mat['bmresp'].flatten()
meresp40f2kHz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv40dB2000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr2kHzg9 = mat['fvect'].flatten()
bmresp40f2kHzg9 = mat['bmresp'].flatten()
meresp40f2kHzg9 = mat['meresp'].flatten()

filename = 'Results/isoint/isointg10Lv60dB2000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr2kHz = mat['fvect'].flatten()
bmresp60f2kHz = mat['bmresp'].flatten()
meresp60f2kHz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv60dB2000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr2kHzg9 = mat['fvect'].flatten()
bmresp60f2kHzg9 = mat['bmresp'].flatten()
meresp60f2kHzg9 = mat['meresp'].flatten()

filename = 'Results/isoint/isointg10Lv80dB2000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr2kHz = mat['fvect'].flatten()
bmresp80f2kHz = mat['bmresp'].flatten()
meresp80f2kHz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv80dB2000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr2kHzg9 = mat['fvect'].flatten()
bmresp80f2kHzg9 = mat['bmresp'].flatten()
meresp80f2kHzg9 = mat['meresp'].flatten()


filename = 'Results/isoint/isointg10Lv20dB4000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr4kHz = mat['fvect'].flatten()
bmresp20f4kHz = mat['bmresp'].flatten()
meresp20f4kHz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv20dB4000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr4kHzg9 = mat['fvect'].flatten()
bmresp20f4kHzg9 = mat['bmresp'].flatten()
meresp20f4kHzg9 = mat['meresp'].flatten()


filename = 'Results/isoint/isointg10Lv40dB4000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr4kHz = mat['fvect'].flatten()
bmresp40f4kHz = mat['bmresp'].flatten()
meresp40f4kHz = mat['meresp'].flatten()

filename = 'Results/isoint/isointg9Lv40dB4000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr4kHzg9 = mat['fvect'].flatten()
bmresp40f4kHzg9 = mat['bmresp'].flatten()
meresp40f4kHzg9 = mat['meresp'].flatten()

filename = 'Results/isoint/isointg10Lv60dB4000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr4kHz = mat['fvect'].flatten()
bmresp60f4kHz = mat['bmresp'].flatten()
meresp60f4kHz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv60dB4000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr4kHzg9 = mat['fvect'].flatten()
bmresp60f4kHzg9 = mat['bmresp'].flatten()
meresp60f4kHzg9 = mat['meresp'].flatten()


filename = 'Results/isoint/isointg10Lv80dB4000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr4kHz = mat['fvect'].flatten()
bmresp80f4kHz = mat['bmresp'].flatten()
meresp80f4kHz = mat['meresp'].flatten()


filename = 'Results/isoint/isointg9Lv80dB4000Hz.mat'
    
mat = scipy.io.loadmat(filename)
fr4kHzg9 = mat['fvect'].flatten()
bmresp80f4kHzg9 = mat['bmresp'].flatten()
meresp80f4kHzg9 = mat['meresp'].flatten()


cm = 1/2.54
fig, ax = plt.subplots(2,1,figsize=(20*cm,14*cm))


plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True


idx0 = 30
idx1 = 90
l1, = ax[0].plot(fr500Hz[1:idx1],20*np.log10(bmresp20f500Hz[1:idx1]/meresp20f500Hz[1:idx1]),color='#1f77b4',alpha=0.7)
l1g9, = ax[0].plot(fr500Hzg9[1:idx1],20*np.log10(bmresp20f500Hzg9[1:idx1]/meresp20f500Hzg9[1:idx1]),color='#1f77b4',linestyle='--')
l2, = ax[0].plot(fr500Hz[1:idx1],20*np.log10(bmresp40f500Hz[1:idx1]/meresp40f500Hz[1:idx1]),color='#ff7f0e',alpha=0.7)
l2g9, = ax[0].plot(fr500Hzg9[1:idx1],20*np.log10(bmresp40f500Hzg9[1:idx1]/meresp40f500Hzg9[1:idx1]),color='#ff7f0e',linestyle='--')
l3, = ax[0].plot(fr500Hz[1:idx1],20*np.log10(bmresp60f500Hz[1:idx1]/meresp60f500Hz[1:idx1]),color='#2ca02c',alpha=0.7)
l3g9, = ax[0].plot(fr500Hzg9[1:idx1],20*np.log10(bmresp60f500Hzg9[1:idx1]/meresp60f500Hzg9[1:idx1]),color='#2ca02c',linestyle='--')
l4, = ax[0].plot(fr500Hz[1:idx1],20*np.log10(bmresp80f500Hz[1:idx1]/meresp80f500Hz[1:idx1]),color='#d62728',alpha=0.7)
l4g9, = ax[0].plot(fr500Hzg9[1:idx1],20*np.log10(bmresp80f500Hzg9[1:idx1]/meresp80f500Hzg9[1:idx1]),color='#d62728',linestyle='--')



c_20g10 = np.abs(bmresp20f500Hz[1:idx1]/meresp20f500Hz[1:idx1])
c_20g10 = c_20g10/np.max(c_20g10)
print(f"ERB 500 Hz, 20 dB, g = 1: ERB = {np.trapz(c_20g10**2,fr500Hz[1:idx1])} Hz")
c_40g10 = np.abs(bmresp40f500Hz[1:idx1]/meresp40f500Hz[1:idx1])
c_40g10 = c_40g10/np.max(c_40g10)
print(f"ERB 500 Hz, 40 dB, g = 1: ERB = {np.trapz(c_40g10**2,fr500Hz[1:idx1])} Hz")
c_60g10 = np.abs(bmresp60f500Hz[1:idx1]/meresp60f500Hz[1:idx1])
c_60g10 = c_60g10/np.max(c_60g10)
print(f"ERB 500 Hz, 60 dB, g = 1: ERB = {np.trapz(c_60g10**2,fr500Hz[1:idx1])} Hz")
c_80g10 = np.abs(bmresp80f500Hz[1:idx1]/meresp80f500Hz[1:idx1])
c_80g10 = c_80g10/np.max(c_80g10)
print(f"ERB 500 Hz, 80 dB, g = 1: ERB = {np.trapz(c_80g10**2,fr500Hz[1:idx1])} Hz")


c_20g10 = np.abs(bmresp20f500Hzg9[1:idx1]/meresp20f500Hzg9[1:idx1])
c_20g10 = c_20g10/np.max(c_20g10)
print(f"ERB 500 Hz, 20 dB, g = 0.9: ERB = {np.trapz(c_20g10**2,fr500Hz[1:idx1])} Hz")
c_40g10 = np.abs(bmresp40f500Hzg9[1:idx1]/meresp40f500Hzg9[1:idx1])
c_40g10 = c_40g10/np.max(c_40g10)
print(f"ERB 500 Hz, 40 dB, g = 0.9: ERB = {np.trapz(c_40g10**2,fr500Hz[1:idx1])} Hz")
c_60g10 = np.abs(bmresp60f500Hzg9[1:idx1]/meresp60f500Hzg9[1:idx1])
c_60g10 = c_60g10/np.max(c_60g10)
print(f"ERB 500 Hz, 60 dB, g = 0.9: ERB = {np.trapz(c_60g10**2,fr500Hz[1:idx1])} Hz")
c_80g10 = np.abs(bmresp80f500Hzg9[1:idx1]/meresp80f500Hzg9[1:idx1])
c_80g10 = c_80g10/np.max(c_80g10)
print(f"ERB 500 Hz, 80 dB, g = 0.9: ERB = {np.trapz(c_80g10**2,fr500Hz[1:idx1])} Hz")









idx1 = 90
ax[0].plot(fr1kHz[idx0:idx1],20*np.log10(bmresp20f1kHz[idx0:idx1]/meresp20f1kHz[idx0:idx1]),color='#1f77b4',alpha=0.7)
ax[0].plot(fr1kHzg9[idx0:idx1],20*np.log10(bmresp20f1kHzg9[idx0:idx1]/meresp20f1kHzg9[idx0:idx1]),color='#1f77b4',linestyle='--')
ax[0].plot(fr1kHz[idx0:idx1],20*np.log10(bmresp40f1kHz[idx0:idx1]/meresp40f1kHz[idx0:idx1]),color='#ff7f0e',alpha=0.7)
ax[0].plot(fr1kHzg9[idx0:idx1],20*np.log10(bmresp40f1kHzg9[idx0:idx1]/meresp40f1kHzg9[idx0:idx1]),color='#ff7f0e',linestyle='--')
ax[0].plot(fr1kHz[idx0:idx1],20*np.log10(bmresp60f1kHz[idx0:idx1]/meresp60f1kHz[idx0:idx1]),color='#2ca02c',alpha=0.7)
ax[0].plot(fr1kHzg9[idx0:idx1],20*np.log10(bmresp60f1kHzg9[idx0:idx1]/meresp60f1kHzg9[idx0:idx1]),color='#2ca02c',linestyle='--')
ax[0].plot(fr1kHz[idx0:idx1],20*np.log10(bmresp80f1kHz[idx0:idx1]/meresp80f1kHz[idx0:idx1]),color='#d62728',alpha=0.7)
ax[0].plot(fr1kHzg9[idx0:idx1],20*np.log10(bmresp80f1kHzg9[idx0:idx1]/meresp80f1kHzg9[idx0:idx1]),color='#d62728',linestyle='--')



c_20g10 = np.abs(bmresp20f1kHz[1:idx1]/meresp20f1kHz[1:idx1])
c_20g10 = c_20g10/np.max(c_20g10)
print(f"ERB 1 kHz, 20 dB, g = 1: ERB = {np.trapz(c_20g10**2,fr1kHz[1:idx1])} Hz")
c_40g10 = np.abs(bmresp40f1kHz[1:idx1]/meresp40f1kHz[1:idx1])
c_40g10 = c_40g10/np.max(c_40g10)
print(f"ERB 1 kHz, 40 dB, g = 1: ERB = {np.trapz(c_40g10**2,fr1kHz[1:idx1])} Hz")
c_60g10 = np.abs(bmresp60f1kHz[1:idx1]/meresp60f1kHz[1:idx1])
c_60g10 = c_60g10/np.max(c_60g10)
print(f"ERB 1 kHz, 60 dB, g = 1: ERB = {np.trapz(c_60g10**2,fr1kHz[1:idx1])} Hz")
c_80g10 = np.abs(bmresp80f1kHz[1:idx1]/meresp80f1kHz[1:idx1])
c_80g10 = c_80g10/np.max(c_80g10)
print(f"ERB 1 kHz, 80 dB, g = 1: ERB = {np.trapz(c_80g10**2,fr1kHz[1:idx1])} Hz")


c_20g10 = np.abs(bmresp20f1kHzg9[1:idx1]/meresp20f1kHzg9[1:idx1])
c_20g10 = c_20g10/np.max(c_20g10)
print(f"ERB 1 kHz, 20 dB, g = 0.9: ERB = {np.trapz(c_20g10**2,fr1kHz[1:idx1])} Hz")
c_40g10 = np.abs(bmresp40f1kHzg9[1:idx1]/meresp40f1kHzg9[1:idx1])
c_40g10 = c_40g10/np.max(c_40g10)
print(f"ERB 1 kHz, 40 dB, g = 0.9: ERB = {np.trapz(c_40g10**2,fr1kHz[1:idx1])} Hz")
c_60g10 = np.abs(bmresp60f1kHzg9[1:idx1]/meresp60f1kHzg9[1:idx1])
c_60g10 = c_60g10/np.max(c_60g10)
print(f"ERB 1 kHz, 60 dB, g = 0.9: ERB = {np.trapz(c_60g10**2,fr1kHz[1:idx1])} Hz")
c_80g10 = np.abs(bmresp80f1kHzg9[1:idx1]/meresp80f1kHzg9[1:idx1])
c_80g10 = c_80g10/np.max(c_80g10)
print(f"ERB 1 kHz, 80 dB, g = 0.9: ERB = {np.trapz(c_80g10**2,fr1kHz[1:idx1])} Hz")




idx1 = 90
ax[0].plot(fr2kHz[idx0:idx1],20*np.log10(bmresp20f2kHz[idx0:idx1]/meresp20f2kHz[idx0:idx1]),color='#1f77b4',alpha=0.7)
ax[0].plot(fr2kHzg9[idx0:idx1],20*np.log10(bmresp20f2kHzg9[idx0:idx1]/meresp20f2kHzg9[idx0:idx1]),color='#1f77b4',linestyle='--')
ax[0].plot(fr2kHz[idx0:idx1],20*np.log10(bmresp40f2kHz[idx0:idx1]/meresp40f2kHz[idx0:idx1]),color='#ff7f0e',alpha=0.7)
ax[0].plot(fr2kHzg9[idx0:idx1],20*np.log10(bmresp40f2kHzg9[idx0:idx1]/meresp40f2kHzg9[idx0:idx1]),color='#ff7f0e',linestyle='--')
ax[0].plot(fr2kHz[idx0:idx1],20*np.log10(bmresp60f2kHz[idx0:idx1]/meresp60f2kHz[idx0:idx1]),color='#2ca02c',alpha=0.7)
ax[0].plot(fr2kHzg9[idx0:idx1],20*np.log10(bmresp60f2kHzg9[idx0:idx1]/meresp60f2kHzg9[idx0:idx1]),color='#2ca02c',linestyle='--')
ax[0].plot(fr2kHz[idx0:idx1],20*np.log10(bmresp80f2kHz[idx0:idx1]/meresp80f2kHz[idx0:idx1]),color='#d62728',alpha=0.7)
ax[0].plot(fr2kHzg9[idx0:idx1],20*np.log10(bmresp80f2kHzg9[idx0:idx1]/meresp80f2kHzg9[idx0:idx1]),color='#d62728',linestyle='--')




c_20g10 = np.abs(bmresp20f2kHz[1:idx1]/meresp20f2kHz[1:idx1])
c_20g10 = c_20g10/np.max(c_20g10)
print(f"ERB 2 kHz, 20 dB, g = 1: ERB = {np.trapz(c_20g10**2,fr2kHz[1:idx1])} Hz")
c_40g10 = np.abs(bmresp40f2kHz[1:idx1]/meresp40f2kHz[1:idx1])
c_40g10 = c_40g10/np.max(c_40g10)
print(f"ERB 2 kHz, 40 dB, g = 1: ERB = {np.trapz(c_40g10**2,fr2kHz[1:idx1])} Hz")
c_60g10 = np.abs(bmresp60f2kHz[1:idx1]/meresp60f2kHz[1:idx1])
c_60g10 = c_60g10/np.max(c_60g10)
print(f"ERB 2 kHz, 60 dB, g = 1: ERB = {np.trapz(c_60g10**2,fr2kHz[1:idx1])} Hz")
c_80g10 = np.abs(bmresp80f2kHz[1:idx1]/meresp80f2kHz[1:idx1])
c_80g10 = c_80g10/np.max(c_80g10)
print(f"ERB 2 kHz, 80 dB, g = 1: ERB = {np.trapz(c_80g10**2,fr2kHz[1:idx1])} Hz")


c_20g10 = np.abs(bmresp20f2kHzg9[1:idx1]/meresp20f2kHzg9[1:idx1])
c_20g10 = c_20g10/np.max(c_20g10)
print(f"ERB 2 kHz, 20 dB, g = 0.9: ERB = {np.trapz(c_20g10**2,fr2kHz[1:idx1])} Hz")
c_40g10 = np.abs(bmresp40f2kHzg9[1:idx1]/meresp40f2kHzg9[1:idx1])
c_40g10 = c_40g10/np.max(c_40g10)
print(f"ERB 2 kHz, 40 dB, g = 0.9: ERB = {np.trapz(c_40g10**2,fr2kHz[1:idx1])} Hz")
c_60g10 = np.abs(bmresp60f2kHzg9[1:idx1]/meresp60f2kHzg9[1:idx1])
c_60g10 = c_60g10/np.max(c_60g10)
print(f"ERB 2 kHz, 60 dB, g = 0.9: ERB = {np.trapz(c_60g10**2,fr2kHz[1:idx1])} Hz")
c_80g10 = np.abs(bmresp80f2kHzg9[1:idx1]/meresp80f2kHzg9[1:idx1])
c_80g10 = c_80g10/np.max(c_80g10)
print(f"ERB 2 kHz, 80 dB, g = 0.9: ERB = {np.trapz(c_80g10**2,fr2kHz[1:idx1])} Hz")


ax[0].plot(fr4kHz[idx0:idx1],20*np.log10(bmresp20f4kHz[idx0:idx1]/meresp20f4kHz[idx0:idx1]),color='#1f77b4',alpha=0.7)
ax[0].plot(fr4kHzg9[idx0:idx1],20*np.log10(bmresp20f4kHzg9[idx0:idx1]/meresp20f4kHzg9[idx0:idx1]),color='#1f77b4',linestyle='--')
ax[0].plot(fr4kHz[idx0:idx1],20*np.log10(bmresp40f4kHz[idx0:idx1]/meresp40f4kHz[idx0:idx1]),color='#ff7f0e',alpha=0.7)
ax[0].plot(fr4kHzg9[idx0:idx1],20*np.log10(bmresp40f4kHzg9[idx0:idx1]/meresp40f4kHzg9[idx0:idx1]),color='#ff7f0e',linestyle='--')
ax[0].plot(fr4kHz[idx0:idx1],20*np.log10(bmresp60f4kHz[idx0:idx1]/meresp60f4kHz[idx0:idx1]),color='#2ca02c',alpha=0.7)
ax[0].plot(fr4kHzg9[idx0:idx1],20*np.log10(bmresp60f4kHzg9[idx0:idx1]/meresp60f4kHzg9[idx0:idx1]),color='#2ca02c',linestyle='--')
ax[0].plot(fr4kHz[idx0:idx1],20*np.log10(bmresp80f4kHz[idx0:idx1]/meresp80f4kHz[idx0:idx1]),color='#d62728',alpha=0.7)
ax[0].plot(fr4kHzg9[idx0:idx1],20*np.log10(bmresp80f4kHzg9[idx0:idx1]/meresp80f4kHzg9[idx0:idx1]),color='#d62728',linestyle='--')




c_20g10 = np.abs(bmresp20f4kHz[1:idx1]/meresp20f4kHz[1:idx1])
c_20g10 = c_20g10/np.max(c_20g10)
print(f"ERB 4 kHz, 20 dB, g = 1: ERB = {np.trapz(c_20g10**2,fr4kHz[1:idx1])} Hz")
c_40g10 = np.abs(bmresp40f4kHz[1:idx1]/meresp40f4kHz[1:idx1])
c_40g10 = c_40g10/np.max(c_40g10)
print(f"ERB 4 kHz, 40 dB, g = 1: ERB = {np.trapz(c_40g10**2,fr4kHz[1:idx1])} Hz")
c_60g10 = np.abs(bmresp60f4kHz[1:idx1]/meresp60f4kHz[1:idx1])
c_60g10 = c_60g10/np.max(c_60g10)
print(f"ERB 4 kHz, 60 dB, g = 1: ERB = {np.trapz(c_60g10**2,fr4kHz[1:idx1])} Hz")
c_80g10 = np.abs(bmresp80f4kHz[1:idx1]/meresp80f4kHz[1:idx1])
c_80g10 = c_80g10/np.max(c_80g10)
print(f"ERB 4 kHz, 80 dB, g = 1: ERB = {np.trapz(c_80g10**2,fr4kHz[1:idx1])} Hz")


c_20g10 = np.abs(bmresp20f4kHzg9[1:idx1]/meresp20f4kHzg9[1:idx1])
c_20g10 = c_20g10/np.max(c_20g10)
print(f"ERB 4 kHz, 20 dB, g = 0.9: ERB = {np.trapz(c_20g10**2,fr4kHz[1:idx1])} Hz")
c_40g10 = np.abs(bmresp40f4kHzg9[1:idx1]/meresp40f4kHzg9[1:idx1])
c_40g10 = c_40g10/np.max(c_40g10)
print(f"ERB 4 kHz, 40 dB, g = 0.9: ERB = {np.trapz(c_40g10**2,fr4kHz[1:idx1])} Hz")
c_60g10 = np.abs(bmresp60f4kHzg9[1:idx1]/meresp60f4kHzg9[1:idx1])
c_60g10 = c_60g10/np.max(c_60g10)
print(f"ERB 4 kHz, 60 dB, g = 0.9: ERB = {np.trapz(c_60g10**2,fr4kHz[1:idx1])} Hz")
c_80g10 = np.abs(bmresp80f4kHzg9[1:idx1]/meresp80f4kHzg9[1:idx1])
c_80g10 = c_80g10/np.max(c_80g10)
print(f"ERB 4 kHz, 80 dB, g = 0.9: ERB = {np.trapz(c_80g10**2,fr4kHz[1:idx1])} Hz")

CF = np.array([500,1000,2000,4000])
ERB = 0.108*CF + 24.7


ax[0].set_xscale('log')
ax[0].set_xticks((200,500,1000,2000,5000))
ax[0].set_xticklabels((0.2,0.5,1,2,5))
ax[0].set_ylim((-180,-120))

from matplotlib.legend_handler import HandlerTuple
#ax[0].legend((l1,l2),('a','bdddd'))
ax[0].legend([(l1, l1g9), (l2, l2g9),(l3, l3g9),(l4, l4g9)], ['20 dB', '40 dB','60 dB','80 dB'],
             handler_map={tuple: HandlerTuple(ndivide=None)})

idx0 = 30
idx1 = 90
cycle = 2*np.pi
ax[1].plot(fr500Hz[1:idx1],np.unwrap(np.angle(bmresp20f500Hz[1:idx1]/meresp20f500Hz[1:idx1]))/cycle,color='#1f77b4',alpha=0.7)
ax[1].plot(fr500Hzg9[1:idx1],np.unwrap(np.angle(bmresp20f500Hzg9[1:idx1]/meresp20f500Hzg9[1:idx1]))/cycle,color='#1f77b4',linestyle='--')
ax[1].plot(fr500Hz[1:idx1],np.unwrap(np.angle(bmresp40f500Hz[1:idx1]/meresp40f500Hz[1:idx1]))/cycle,color='#ff7f0e',alpha=0.7)
ax[1].plot(fr500Hzg9[1:idx1],np.unwrap(np.angle(bmresp40f500Hzg9[1:idx1]/meresp40f500Hzg9[1:idx1]))/cycle,color='#ff7f0e',linestyle=':')
ax[1].plot(fr500Hz[1:idx1],np.unwrap(np.angle(bmresp60f500Hz[1:idx1]/meresp60f500Hz[1:idx1]))/cycle,color='#2ca02c',alpha=0.7)
ax[1].plot(fr500Hzg9[1:idx1],np.unwrap(np.angle(bmresp60f500Hzg9[1:idx1]/meresp60f500Hzg9[1:idx1]))/cycle,color='#2ca02c',linestyle='--')
ax[1].plot(fr500Hz[1:idx1],np.unwrap(np.angle(bmresp80f500Hz[1:idx1]/meresp80f500Hz[1:idx1]))/cycle+1,color='#d62728',linestyle='-',alpha=0.7)
ax[1].plot(fr500Hzg9[1:idx1],np.unwrap(np.angle(bmresp80f500Hzg9[1:idx1]/meresp80f500Hzg9[1:idx1]))/cycle+1,color='#d62728',linestyle='--')

idx1 = 90
ax[1].plot(fr1kHz[idx0:idx1],np.unwrap(np.angle(bmresp20f1kHz[idx0:idx1]/meresp20f1kHz[idx0:idx1]))/cycle,color='#1f77b4',alpha=0.7)
ax[1].plot(fr1kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp20f1kHzg9[idx0:idx1]/meresp20f1kHzg9[idx0:idx1]))/cycle,color='#1f77b4',linestyle='--')
ax[1].plot(fr1kHz[idx0:idx1],np.unwrap(np.angle(bmresp40f1kHz[idx0:idx1]/meresp40f1kHz[idx0:idx1]))/cycle,color='#ff7f0e',alpha=0.7)
ax[1].plot(fr1kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp40f1kHzg9[idx0:idx1]/meresp40f1kHzg9[idx0:idx1]))/cycle,color='#ff7f0e',linestyle='--')
ax[1].plot(fr1kHz[idx0:idx1],np.unwrap(np.angle(bmresp60f1kHz[idx0:idx1]/meresp60f1kHz[idx0:idx1]))/cycle,color='#2ca02c',alpha=0.7)
ax[1].plot(fr1kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp60f1kHzg9[idx0:idx1]/meresp60f1kHzg9[idx0:idx1]))/cycle,color='#2ca02c',linestyle='--')
ax[1].plot(fr1kHz[idx0:idx1],np.unwrap(np.angle(bmresp80f1kHz[idx0:idx1]/meresp80f1kHz[idx0:idx1]))/cycle,color='#d62728',alpha=0.7)
ax[1].plot(fr1kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp80f1kHzg9[idx0:idx1]/meresp80f1kHzg9[idx0:idx1]))/cycle,color='#d62728',linestyle='--')

idx1 = 90
ax[1].plot(fr2kHz[idx0:idx1],np.unwrap(np.angle(bmresp20f2kHz[idx0:idx1]/meresp20f2kHz[idx0:idx1]))/cycle,color='#1f77b4',alpha=0.7)
ax[1].plot(fr2kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp20f2kHzg9[idx0:idx1]/meresp20f2kHzg9[idx0:idx1]))/cycle,color='#1f77b4',linestyle='--')
ax[1].plot(fr2kHz[idx0:idx1],np.unwrap(np.angle(bmresp40f2kHz[idx0:idx1]/meresp40f2kHz[idx0:idx1]))/cycle,color='#ff7f0e',alpha=0.7)
ax[1].plot(fr2kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp40f2kHzg9[idx0:idx1]/meresp40f2kHzg9[idx0:idx1]))/cycle,color='#ff7f0e',linestyle='--')
ax[1].plot(fr2kHz[idx0:idx1],np.unwrap(np.angle(bmresp60f2kHz[idx0:idx1]/meresp60f2kHz[idx0:idx1]))/cycle,color='#2ca02c',alpha=0.7)
ax[1].plot(fr2kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp60f2kHzg9[idx0:idx1]/meresp60f2kHzg9[idx0:idx1]))/cycle,color='#2ca02c',linestyle='--')
ax[1].plot(fr2kHz[idx0:idx1],np.unwrap(np.angle(bmresp80f2kHz[idx0:idx1]/meresp80f2kHz[idx0:idx1]))/cycle,color='#d62728',alpha=0.7)
ax[1].plot(fr2kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp80f2kHzg9[idx0:idx1]/meresp80f2kHzg9[idx0:idx1]))/cycle,color='#d62728',linestyle='--')


ax[1].plot(fr4kHz[idx0:idx1],np.unwrap(np.angle(bmresp20f4kHz[idx0:idx1]/meresp20f4kHz[idx0:idx1]))/cycle,color='#1f77b4',alpha=0.7)
ax[1].plot(fr4kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp20f4kHzg9[idx0:idx1]/meresp20f4kHzg9[idx0:idx1]))/cycle,color='#1f77b4',linestyle='--')
ax[1].plot(fr4kHz[idx0:idx1],np.unwrap(np.angle(bmresp40f4kHz[idx0:idx1]/meresp40f4kHz[idx0:idx1]))/cycle,color='#ff7f0e',alpha=0.7)
ax[1].plot(fr4kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp40f4kHzg9[idx0:idx1]/meresp40f4kHzg9[idx0:idx1]))/cycle,color='#ff7f0e',linestyle='--')
ax[1].plot(fr4kHz[idx0:idx1],np.unwrap(np.angle(bmresp60f4kHz[idx0:idx1]/meresp60f4kHz[idx0:idx1]))/cycle,color='#2ca02c',alpha=0.7)
ax[1].plot(fr4kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp60f4kHzg9[idx0:idx1]/meresp60f4kHzg9[idx0:idx1]))/cycle,color='#2ca02c',linestyle='--')
ax[1].plot(fr4kHz[idx0:idx1],np.unwrap(np.angle(bmresp80f4kHz[idx0:idx1]/meresp80f4kHz[idx0:idx1]))/cycle,color='#d62728',alpha=0.7)
ax[1].plot(fr4kHzg9[idx0:idx1],np.unwrap(np.angle(bmresp80f4kHzg9[idx0:idx1]/meresp80f4kHzg9[idx0:idx1]))/cycle,color='#d62728',linestyle='--')

ax[1].set_xscale('log')
ax[1].set_xticks((200,500,1000,2000,5000))
ax[1].set_xticklabels((0.2,0.5,1,2,5))
#ax[0].set_ylim((-180,-120))
ax[1].set_xlabel('Frequency (kHz)')
ax[1].set_ylabel('Phase (cycles)')
ax[0].set_ylabel('Magnitude (dB re 1 a.u.)')

fig.align_ylabels(ax)


plt.show()




plt.savefig('Figures/isoint.eps', format='eps')
plt.savefig('Figures/isoint.pdf', format='pdf')


#%% calcualte ERB values:
    
c1 = np.abs(bmresp20f500Hz[1:idx1]/meresp20f500Hz[1:idx1])

fig,ax = plt.subplots()
ax.plot(c1/np.max(c1))
