

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:21:49 2023

create a graph with measured speech understanding in babble noise for young subjects
Fig.7 in the paper


@author: vencov
"""

import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import re

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

myfilelist = find('*babble.mer', 'Results/AZVresults22_leveldep/do30let')

cm = 1/2.54
fig, ax = plt.subplots(figsize=(11*cm,8*cm))

ProbValM = np.array
ProbValD = {}
OverallRes = {}

for i in range(len(myfilelist)):
    filename = myfilelist[i]
    mat = scipy.io.loadmat(filename)

    s = myfilelist[i] 
    match = re.search(r"/(s0\d{2})", s)
        
    data_subj = mat['odpovedi']

    if len(data_subj[0])==4:
        Lvect = [data_subj[0][0][5][0][0], data_subj[0][1][5][0][0], data_subj[0][2][5][0][0], data_subj[0][3][5][0][0]]
    
        ProbVal = np.array([np.mean(data_subj[0][0][13][0]), np.mean(data_subj[0][1][13][0]), np.mean(data_subj[0][2][13][0]), np.mean(data_subj[0][3][13][0])])
        if data_subj[0][0][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][0][5][0][0]] += [np.mean(data_subj[0][0][13][0])]
        else:
            ProbValD[data_subj[0][0][5][0][0]] = [np.mean(data_subj[0][0][13][0])]
        if data_subj[0][1][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][1][5][0][0]] += [np.mean(data_subj[0][1][13][0])]
        else:
            ProbValD[data_subj[0][1][5][0][0]] = [np.mean(data_subj[0][1][13][0])]
        if data_subj[0][2][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][2][5][0][0]] += [np.mean(data_subj[0][2][13][0])]
        else:
            ProbValD[data_subj[0][2][5][0][0]] = [np.mean(data_subj[0][2][13][0])]
        if data_subj[0][3][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][3][5][0][0]] += [np.mean(data_subj[0][3][13][0])]
        else:
            ProbValD[data_subj[0][3][5][0][0]] = [np.mean(data_subj[0][3][13][0])]
    elif len(data_subj[0])==3:
        Lvect = [data_subj[0][0][5][0][0], data_subj[0][1][5][0][0], data_subj[0][2][5][0][0]]
    
        ProbVal = np.array([np.mean(data_subj[0][0][13][0]), np.mean(data_subj[0][1][13][0]), np.mean(data_subj[0][2][13][0])])
        if data_subj[0][0][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][0][5][0][0]] += [np.mean(data_subj[0][0][13][0])]
        else:
            ProbValD[data_subj[0][0][5][0][0]] = [np.mean(data_subj[0][0][13][0])]
        if data_subj[0][1][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][1][5][0][0]] += [np.mean(data_subj[0][1][13][0])]
        else:
            ProbValD[data_subj[0][1][5][0][0]] = [np.mean(data_subj[0][1][13][0])]
        if data_subj[0][2][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][2][5][0][0]] += [np.mean(data_subj[0][2][13][0])]
        else:
            ProbValD[data_subj[0][2][5][0][0]] = [np.mean(data_subj[0][2][13][0])]
    elif len(data_subj[0])==2:
        Lvect = [data_subj[0][0][5][0][0], data_subj[0][1][5][0][0]]
    
        ProbVal = np.array([np.mean(data_subj[0][0][13][0]), np.mean(data_subj[0][1][13][0])])
        if data_subj[0][0][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][0][5][0][0]] += [np.mean(data_subj[0][0][13][0])]
        else:
            ProbValD[data_subj[0][0][5][0][0]] = [np.mean(data_subj[0][0][13][0])]
        if data_subj[0][1][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][1][5][0][0]] += [np.mean(data_subj[0][1][13][0])]
        else:
            ProbValD[data_subj[0][1][5][0][0]] = [np.mean(data_subj[0][1][13][0])]
        
    elif len(data_subj[0])==1:
        Lvect = [data_subj[0][0][5][0][0]]
    
        ProbVal = np.array([np.mean(data_subj[0][0][13][0])])
        if data_subj[0][0][5][0][0] in ProbValD.keys():
            ProbValD[data_subj[0][0][5][0][0]] += [np.mean(data_subj[0][0][13][0])]
        else:
            ProbValD[data_subj[0][0][5][0][0]] = [np.mean(data_subj[0][0][13][0])]
            
    subj_n = match[0][1:]
    OverallRes[subj_n] = {}  # dictionary with individual results        
    OverallRes[subj_n]['level'] = Lvect
    OverallRes[subj_n]['sin'] = ProbVal
    
    ax.plot(Lvect,100*ProbVal,'x-',color='b',alpha=0.5)



myKeys = list(ProbValD.keys())
myKeys.sort()
ProbValDS = {i: ProbValD[i] for i in myKeys}
 

DataY=[np.array(xi) for xi in list(ProbValDS.values())]
DataYM = [np.mean(100*xi) for xi in DataY]
DataYSTD = [np.std(100*xi) for xi in DataY]

ax.errorbar(ProbValDS.keys(),DataYM,DataYSTD,color='k')

xlim = [30, 75]
ax.set_xlim(xlim)
ylim = [0, 100]
ax.set_ylim(ylim)

ax.set_xlabel('Level (dB SPL)',fontsize=12)
ax.set_ylabel('Recognition (%)',fontsize=12)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
#plt.savefig('Figures/recog30.eps', format='eps')


#ax[1].errorbar(ProbValDS.keys(),DataYM,DataYSTD)
plt.savefig('Figures/recogSPINYoung.eps', format='eps')



#%% Mixed Linear Model (MixedLM)


import pandas as pd
import statsmodels.formula.api as smf

data = OverallRes
# Convert dictionary to a flat DataFrame
records = []
for subj_id, subj_data in data.items():
    for level, score in zip(subj_data['level'], subj_data['sin']):
        records.append({'subject': subj_id, 'level': level, 'score': score})

df = pd.DataFrame(records)

# Fit linear mixed-effects model: score ~ level + (1|subject)
model = smf.mixedlm("score ~ level", df, groups=df["subject"])
result = model.fit()

# Print model summary
print(result.summary())


