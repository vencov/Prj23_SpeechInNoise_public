#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 16:21:49 2023

create a graph with measured speech understanding in babble noise for young subjects
Fig.8 in the paper


@author: Vaclav Vencovsky, vaclav.vencovsky@gmail.com
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
    
    ax.plot(Lvect,100*ProbVal,'x-',color='b',alpha=0.2)


#import seaborn as sns

#sns.set(style="whitegrid", context="talk", font_scale=1.0)  # Improved visuals




# Sort and aggregate
myKeys = sorted(ProbValD.keys())
ProbValDS = {k: ProbValD[k] for k in myKeys}
DataY = [np.array(xi) for xi in ProbValDS.values()]
DataYM = [np.mean(100 * xi) for xi in DataY]
DataYSE = [np.std(100 * xi) / np.sqrt(len(xi)) for xi in DataY]

'''
myKeys = list(ProbValD.keys())
myKeys.sort()
ProbValDS = {i: ProbValD[i] for i in myKeys}
 



DataY=[np.array(xi) for xi in list(ProbValDS.values())]
DataYM = [np.mean(100*xi) for xi in DataY]
DataYSTD = [np.std(100*xi) for xi in DataY]
DataYSE = [np.std(100*xi)/np.sqrt(len(xi)) for xi in DataY]
'''
ax.errorbar(ProbValDS.keys(), DataYM, yerr=DataYSE, color='k', capsize=4, label='Mean ± SE')


xlim = [30, 75]
ax.set_xlim(xlim)
ylim = [0, 100]
ax.set_ylim(ylim)

ax.set_xlabel('Level (dB SPL)',fontsize=12)
ax.set_ylabel('Recognition (%)',fontsize=12)
plt.gcf().subplots_adjust(bottom=0.15)
plt.gcf().subplots_adjust(left=0.15)
#plt.savefig('Figures/recog30.eps', format='eps')
ax.grid(True, linestyle='--', alpha=0.6)

#ax[1].errorbar(ProbValDS.keys(),DataYM,DataYSTD)
plt.savefig('Figures/recogSPINYoung.eps', format='eps')


#%% Figure with seaborn, 95 % confidence intervals, this figure is shown in the paper

cm = 1/2.54

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

import pandas as pd

# Prepare long-format dataframe
levels = []
scores = []
for level, vals in ProbValDS.items():
    levels.extend([level] * len(vals))
    scores.extend([100 * val for val in vals])
df = pd.DataFrame({'Level': levels, 'Score': scores})

plt.figure(figsize=(12*cm, 9*cm))

# Individual points exactly on the levels (no jitter)
sns.stripplot(data=df, x='Level', y='Score', color='blue', alpha=0.4, jitter=False)

# Mean ± 95% CI with thinner line (e.g., linewidth=0.8)



sns.pointplot(data=df, x='Level', y='Score', estimator='median', errorbar=('ci',95), capsize=0.2, markersize=5, color='k', linewidth=1.5)

plt.xlabel('Level (dB SPL)', fontsize=13)
plt.ylabel('Recognition (%)', fontsize=13)
plt.style.use('default')  # reset style to default
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_edgecolor('black')   # change spine color to black
    spine.set_linewidth(1.0)       # optionally make them thicker
levels = sorted(df['Level'].unique())
plt.xticks(ticks=range(len(levels)), labels=levels, fontsize=12)
plt.yticks(range(0, 101, 20), fontsize=12)
plt.ylim(0, 100)

dot_legend = mlines.Line2D([], [], color='blue', marker='o', linestyle='None',
                           markersize=4, label='Individual data')
line_legend = mlines.Line2D([], [], color='k', linestyle='-', linewidth=0.8,
                           label='Median ± 95% CI')

plt.legend(handles=[dot_legend, line_legend], loc='lower right', fontsize=12)

plt.minorticks_on()
plt.grid(True, which='major', linestyle='-', linewidth=0.7, alpha=0.8)
plt.grid(True, which='minor', linestyle='--', linewidth=0.3, alpha=0.4)
# Major ticks — bigger length, thicker
ax.tick_params(axis='both', which='major', direction='in', length=4, width=1, color='black')

# Minor ticks — smaller but still visible
ax.tick_params(axis='both', which='minor', direction='in', length=2, width=0.5, color='black')

plt.tight_layout()
plt.savefig('Figures/recogSPINYoung_wLegend.png', format='png', dpi=600)
plt.show()

#%% LMM to test statisctical significance

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

# Prepare DataFrame from OverallRes dictionary
rows = []
for subj, res in OverallRes.items():
    levels = res['level']          # list of levels for this subject
    scores = res['sin']            # corresponding scores
    for lvl, score in zip(levels, scores):
        rows.append({'subject': subj, 'level': lvl, 'score': score})

df = pd.DataFrame(rows)
df['subject'] = df['subject'].astype('category')

# Fit the mixed linear model
model = smf.mixedlm("score ~ level", df, groups=df["subject"])
result = model.fit(method='powell',maxiter=1000)


print(result.summary())

#%%
import pandas as pd

# Calculate variance of scores by subject
subject_var = df.groupby('subject')['score'].var()
print("Variance of scores within each subject:")
print(subject_var)

# Calculate overall variance of scores
print("Overall variance of scores:", df['score'].var())

# Mean score per subject
subject_means = df.groupby('subject')['score'].mean()

# Variance of subject means (between-subject variance proxy)
between_subject_var = subject_means.var()
print("Variance between subject means:", between_subject_var)



#%%
# Fit OLS model: score predicted by level
ols_model = smf.ols("score ~ level", data=df)
ols_result = ols_model.fit()

# Print summary of the OLS fit
print(ols_result.summary())


#%% N=21, is this enough? Power a
# Extract parameters from fitted model
beta_level = result.params['level']
intercept = result.params['Intercept']
sigma_resid = np.sqrt(result.scale)        # residual std dev
# Variance of random intercept, if available:
if 'Group Var' in result.cov_re:
    var_group = result.cov_re.iloc[0,0]
else:
    var_group = 0.0
std_group = np.sqrt(var_group)



n_subjects = df['subject'].nunique()
mean_group_size = df.groupby('subject').size().mean()

np.random.seed(42)
n_simulations = 1000
alpha = 0.05
significant_results = 0

for _ in range(n_simulations):
    simulated_data = []
    for subj in range(n_subjects):
        n_obs = int(np.round(mean_group_size))
        levels_sim = np.linspace(df['level'].min(), df['level'].max(), n_obs)
        b_subj = np.random.normal(0, std_group)  # random intercept per subject
        scores_sim = intercept + b_subj + beta_level * levels_sim + np.random.normal(0, sigma_resid, n_obs)
        subject_ids = [subj] * n_obs
        for lvl, sc, sid in zip(levels_sim, scores_sim, subject_ids):
            simulated_data.append({'level': lvl, 'score': sc, 'subject': sid})

    sim_df = pd.DataFrame(simulated_data)
    md = smf.mixedlm("score ~ level", sim_df, groups=sim_df["subject"])
    mdf = md.fit(method='powell',maxiter=1000,reml=True)
    pval = mdf.pvalues.get('level', 1)
    if pval < alpha:
        significant_results += 1

power_estimate = significant_results / n_simulations
print(f"Estimated power to detect effect of level: {power_estimate:.2f}")