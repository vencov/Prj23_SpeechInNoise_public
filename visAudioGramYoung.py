#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:30:59 2024

Shows auditory thresholds in dB SPL for young group of listeners used in the study
Fig. 1 in the paper

@author: vencov
"""


import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import codecs
    
plt.close('all')


# find all files with results from babble experiment

import os, fnmatch
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

myfilelist = find('audiogram*', 'Results/AZVresults22_leveldep/do30let')

cm = 1/2.54
fig, ax = plt.subplots(figsize=(11*cm,8*cm))

ProbValM = np.array
ProbValD = {}
AudTL = []
AudTR = []

for i in range(len(myfilelist)):
    filename = myfilelist[i]
    print(filename)
    leve = True    

    with codecs.open(filename, 'r', encoding='utf-8',errors='ignore') as fdata:
        all_text = fdata.readlines()
        
        for i in range(len(all_text[:29])):
            if all_text[i].find('500')==0:
                TH = []
                for k in range(5):
                    TH.append(float(all_text[i+k].split()[1]))
                if leve == True:
                    AudTL.append(TH)
                    leve = False
                else:
                    AudTR.append(TH)

AudTLM  = []
AudTRM  = []

for j in range(len(AudTL[0])):
    soucetL = 0
    soucetR = 0
    for i in range(len(AudTL)):
        soucetL += AudTL[i][j]
        soucetR += AudTR[i][j]
    AudTLM.append(soucetL/len(AudTL))
    AudTRM.append(soucetR/len(AudTR))
    
fvect = [500,1000,2000,4000,8000]
ax.plot(fvect,AudTLM,'x',color=(0,0,0))
ax.plot(fvect,AudTRM,'.',color=(0,0,0))    
ylim = [-10,95]
ax.set_ylim(ylim)
ax.set_xscale('log')

ax.set_xticks((500,1000,2000,4000,8000))
ax.set_xticklabels((0.500,1,2,4,8))


myfilelist = find('audiogram*', 'Results/AZVresults22_leveldep/od60let')

ax.legend(('Left ear','Right ear'),fontsize=12)

ax.set_xlabel('Frequency (kHz)',fontsize=12)

ax.set_ylabel('Threshold (dB SPL)',fontsize=12)
plt.gcf().subplots_adjust(bottom=0.15)
plt.savefig('Figures/AudThresholdYoung.eps', format='eps')
