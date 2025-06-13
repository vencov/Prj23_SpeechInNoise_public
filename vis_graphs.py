#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:35:09 2023

Create a graph showing the crosscorrelation between model responses for 10 sets of sentences and model with higher gain
Figs. 4 and 5 in the paper

The script includes statistical tests


@author: Vaclav Vencovsky, vaclav.vencovsky@gmail.com
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


#%% plot 5% quantile simulated results for model with higher gain

cm = 1/2.54  # centimeters in inches
fig,ax = plt.subplots(2,5,figsize=(20*cm,10*cm))

plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True

import seaborn as sns
import pandas as pd

def to_long_df(data, x_values, label):
    """
    Converts 2D data array (levels x subjects) into long-form dataframe.
    """
    n_levels, n_subjects = data.shape
    return pd.DataFrame({
        'Level': np.tile(x_values, n_subjects),
        'Value': data.flatten(order='F'),
        'Sentence': np.repeat(np.arange(n_subjects), n_levels),
        'Panel': label
    })

df_all = pd.concat([
    to_long_df(xc1q, L, 'xc1'),
    to_long_df(xc2q, L,  'xc2'),
    to_long_df(xc3q, L,  'xc3'),
    to_long_df(xc4q, L,  'xc4'),
    to_long_df(xc5q, L,  'xc5'),
    to_long_df(xc6q, L,  'xc6'),
    to_long_df(xc7q, L,  'xc7'),
    to_long_df(xc8q, L,  'xc8'),
    to_long_df(xc9q, L,  'xc9'),
    to_long_df(xc10q, L, 'xc10'),
])

df_all_q = df_all

for i in range(10):

    ax[0,0].plot(L,xc1q[:,i], label=str(i),alpha=0.6), ax[0,0].set_ylim((0,0.35))
    ax[0,1].plot(L,xc2q[:,i], label=str(i),alpha=0.6), ax[0,1].set_ylim((0,0.35))
    ax[0,2].plot(L,xc3q[:,i], label=str(i),alpha=0.6), ax[0,2].set_ylim((0,0.35))
    ax[0,3].plot(L,xc4q[:,i], label=str(i),alpha=0.6), ax[0,3].set_ylim((0,0.35))
    ax[0,4].plot(L,xc5q[:,i], label=str(i),alpha=0.6), ax[0,4].set_ylim((0,0.35))
    ax[1,0].plot(L,xc6q[:,i], label=str(i),alpha=0.6), ax[1,0].set_ylim((0,0.35))
    ax[1,1].plot(L,xc7q[:,i], label=str(i),alpha=0.6), ax[1,1].set_ylim((0,0.35))
    ax[1,2].plot(L,xc8q[:,i], label=str(i),alpha=0.6), ax[1,2].set_ylim((0,0.35))
    ax[1,3].plot(L,xc9q[:,i], label=str(i),alpha=0.6), ax[1,3].set_ylim((0,0.35))
    ax[1,4].plot(L,xc10q[:,i], label=str(i),alpha=0.6), ax[1,4].set_ylim((0,0.35))

plt.gcf().text(0.5, 0.9, 'Higher gain, 0.05 quantile', fontsize=8, fontweight='bold',ha='center')
panel_names = [f'xc{i}' for i in range(1, 11)]

for idx, panel in enumerate(panel_names):
    row = idx // 5
    col = idx % 5
    ax_panel = ax[row, col]

    df_subset = df_all[df_all['Panel'] == panel].copy()
    df_subset['Level'] = pd.Categorical(df_subset['Level'], categories=sorted(df_subset['Level'].unique()), ordered=True)

    sns.lineplot(
        data=df_subset, x='Level', y='Value',
        ax=ax_panel,
        estimator='median', errorbar=('ci',95),
        color='black', linewidth=2,
        err_style='band', err_kws={'alpha': 0.2},
        legend=False
    )

    ax_panel.set_ylabel('')  # remove default y-axis label
    ax_panel.set_xlabel('')  # remove default y-axis label



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

#handles, labels = ax[1,4].get_legend_handles_labels()
#labels = ('1','2','3','4','5','6','7','8','9','10')
#fig.legend(handles, labels, loc='right')


import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# 1. Get individual lines handles and labels (from the last subplot, e.g. ax[1,4])
handles, labels = ax[1, 4].get_legend_handles_labels()

# 2. Create a custom handle for the mean + CI band:
mean_line = mlines.Line2D([], [], color='black', linewidth=2, label='Median')
ci_band = mpatches.Patch(color='black', alpha=0.2, label='95% CI')

# 3. Combine handles and labels
handles.append(mean_line)
handles.append(ci_band)
labels = [str(i+1) for i in range(10)]  # individual lines labeled 1 to 10
labels.append('Median')
labels.append('95% CI')

# 4. Add figure legend on the right
fig.legend(handles, labels, loc='right', fontsize=10)


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
plt.subplots_adjust(right=0.85)
#ax[1,4].legend(('1','2','3','4','5','6','7','8','9'))

fig.supxlabel('Level (dB SPL)')
fig.supylabel('$r$ (-)')
#plt.ylabel('ddd')

for axs in ax.flatten():
    axs.tick_params(axis='both', which='major', width=0.5, length=2)
    axs.tick_params(axis='both', which='minor', width=0.5, length=1)
for axs in ax.flatten():
    axs.grid(True, which='major', linestyle='-', linewidth=0.3, alpha=0.7)
    axs.grid(True, which='minor', linestyle=':', linewidth=0.2, alpha=0.5)
    axs.minorticks_on()

plt.savefig('Figures/rconvG10q.png', format='png',dpi=600)



#%%  plot the mean values, model with higher gain

cm = 1/2.54  # centimeters in inches
fig,ax = plt.subplots(2,5,figsize=(20*cm,10*cm))


df_all = pd.concat([
    to_long_df(xc1m, L, 'xc1'),
    to_long_df(xc2m, L, 'xc2'),
    to_long_df(xc3m, L, 'xc3'),
    to_long_df(xc4m, L, 'xc4'),
    to_long_df(xc5m, L, 'xc5'),
    to_long_df(xc6m, L, 'xc6'),
    to_long_df(xc7m, L, 'xc7'),
    to_long_df(xc8m, L, 'xc8'),
    to_long_df(xc9m, L, 'xc9'),
    to_long_df(xc10m, L, 'xc10'),
])

df_all_m = df_all
for i in range(10):
    ax[0,0].plot(L, xc1m[:,i], label=str(i), alpha=0.6), ax[0,0].set_ylim((0,0.7))
    ax[0,1].plot(L, xc2m[:,i], label=str(i), alpha=0.6), ax[0,1].set_ylim((0,0.7))
    ax[0,2].plot(L, xc3m[:,i], label=str(i), alpha=0.6), ax[0,2].set_ylim((0,0.7))
    ax[0,3].plot(L, xc4m[:,i], label=str(i), alpha=0.6), ax[0,3].set_ylim((0,0.7))
    ax[0,4].plot(L, xc5m[:,i], label=str(i), alpha=0.6), ax[0,4].set_ylim((0,0.7))
    ax[1,0].plot(L, xc6m[:,i], label=str(i), alpha=0.6), ax[1,0].set_ylim((0,0.7))
    ax[1,1].plot(L, xc7m[:,i], label=str(i), alpha=0.6), ax[1,1].set_ylim((0,0.7))
    ax[1,2].plot(L, xc8m[:,i], label=str(i), alpha=0.6), ax[1,2].set_ylim((0,0.7))
    ax[1,3].plot(L, xc9m[:,i], label=str(i), alpha=0.6), ax[1,3].set_ylim((0,0.7))
    ax[1,4].plot(L, xc10m[:,i], label=str(i), alpha=0.6), ax[1,4].set_ylim((0,0.7))

plt.gcf().text(0.5, 0.9, 'Higher gain, mean', fontsize=8, fontweight='bold', ha='center')

for idx, panel in enumerate(panel_names):
    row = idx // 5
    col = idx % 5
    ax_panel = ax[row, col]

    df_subset = df_all[df_all['Panel'] == panel].copy()
    df_subset['Level'] = pd.Categorical(df_subset['Level'], categories=sorted(df_subset['Level'].unique()), ordered=True)

    sns.lineplot(
        data=df_subset, x='Level', y='Value',
        ax=ax_panel,
        estimator='median', errorbar=('ci',95),
        color='black', linewidth=2,
        err_style='band', err_kws={'alpha': 0.2},
        legend=False
    )

    ax_panel.set_ylabel('')  # remove default y-axis label
    ax_panel.set_xlabel('')  # remove default y-axis label



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
#fig.legend(handles, labels, loc='right')

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

# 1. Get individual lines handles and labels (from the last subplot, e.g. ax[1,4])
handles, labels = ax[1, 4].get_legend_handles_labels()

# 2. Create a custom handle for the mean + CI band:
mean_line = mlines.Line2D([], [], color='black', linewidth=2, label='Median')
ci_band = mpatches.Patch(color='black', alpha=0.2, label='95% CI')

# 3. Combine handles and labels
handles.append(mean_line)
handles.append(ci_band)
labels = [str(i+1) for i in range(10)]  # individual lines labeled 1 to 10
labels.append('Median')
labels.append('95% CI')

# 4. Add figure legend on the right
fig.legend(handles, labels, loc='right', fontsize=10)


plt.subplots_adjust(right=0.85)
#ax[1,4].legend(('1','2','3','4','5','6','7','8','9'))

fig.supxlabel('Level (dB SPL)')
fig.supylabel('$r$ (-)')
#plt.ylabel('ddd')

for axs in ax.flatten():
    axs.tick_params(axis='both', which='major', width=0.5, length=2)
    axs.tick_params(axis='both', which='minor', width=0.5, length=1)
for axs in ax.flatten():
    axs.grid(True, which='major', linestyle='-', linewidth=0.3, alpha=0.7)
    axs.grid(True, which='minor', linestyle=':', linewidth=0.2, alpha=0.5)
    axs.minorticks_on()

plt.rcParams["xtick.direction"]="in"
plt.rcParams["ytick.direction"]="in"
plt.rcParams["xtick.top"]=True
plt.rcParams["ytick.right"]=True


plt.savefig('Figures/rconvG10m.png', format='png')


#%% Statistical tests: random effect model

import pandas as pd
import statsmodels.formula.api as smf

# Make sure Panel is categorical
df_all['Panel'] = df_all['Panel'].astype('category')

# Fit LMM: Value ~ Level * Panel + (1 | Sentence)
model = smf.mixedlm(
    "Value ~ Level * Panel",
    df_all,
    groups=df_all["Sentence"]  # random intercept per sentence
)
result = model.fit()

# Print summary
print(result.summary())




#%% OLS model quantile


import statsmodels.formula.api as smf
import pandas as pd

# Add quadratic term to test inverted U-shape (i.e. increase and then decrease in correlation)


df_all_q['Level_c'] = df_all_q['Level'] - df_all_q['Level'].mean()
df_all_q['Level_sq'] = df_all_q['Level_c'] ** 2


# Fit OLS regression with linear and quadratic Level terms
model = smf.ols("Value ~ Level + Level_sq", data=df_all_q)
result = model.fit()

print(result.summary())

#%% OLS model mean

df_all_m['Level_c'] = df_all_m['Level'] - df_all_m['Level'].mean()
df_all_m['Level_sq'] = df_all_m['Level_c'] ** 2


# Fit OLS regression with linear and quadratic Level terms
model = smf.ols("Value ~ Level + Level_sq", data=df_all_m)
result = model.fit()

print(result.summary())
