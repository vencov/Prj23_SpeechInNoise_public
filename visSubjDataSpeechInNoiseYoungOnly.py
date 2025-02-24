

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
for i in range(len(myfilelist)):
    filename = myfilelist[i]
    mat = scipy.io.loadmat(filename)


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
    else:
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
plt.savefig('Figures/recogSPINYoung.pdf', format='pdf')




