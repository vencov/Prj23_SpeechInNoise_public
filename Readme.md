# Speech in Noise Project: Level Dependence of Speech in Multitalker Masking Noise

This repository contains Python and MATLAB scripts used for analyzing speech in noise, specifically studying the level dependence of speech in multitalker masking noise. The scripts generate various figures and results presented in the associated research paper.

## Python Scripts

- **visIsoIntResp.py** - Shows iso-intensity responses in the cochlear model (Figure A2 in the paper).
- **visIOfce.py** - Displays input/output functions of the cochlear model (Figure A1 in the paper).
- **visAudioGramYoung.py** - Shows auditory thresholds in dB SPL for the young group of listeners used in the study (Figure 1 in the paper).
- **vis_graphs.py** - Creates a graph showing the cross-correlation between model responses for 10 sets of sentences and the model with higher gain (Figures 3 and 4 in the paper).
- **vis_graphsG9.py** - Creates a graph showing the cross-correlation between model responses for 10 sets of sentences and the model with lower gain (Figures 5 and 6 in the paper).
- **vis_SubjDataSpeechInNoiseYoungOnly.py** - Creates a graph with measured speech understanding in babble noise for young subjects (Figure 7 in the paper).
- **visRdiff.py** - Creates graphs showing the effect of feedback gain in the model by illustrating the difference between the cross-correlations for the model with higher gain and for the model with lower gain (Figures 8 and 9 in the paper).
- **visXCORR.py** - Creates a graph showing the cross-correlation for each time frame for one sentence (Figure 10 in the paper).
- **visMIg10.py** - Creates a graph showing the modulation index, indicating the amplitude fluctuations in the model outputs and how it changes across levels (Figure 11 in the paper).
- **visMIg10_200ms.py** - Creates a graph showing the modulation index, indicating the amplitude fluctuations in the model outputs and how it changes across levels. The graphs show fluctuations calculated in 200-ms long time frames (Figure 12 in the paper).

## MATLAB Scripts

These scripts are used for running simulations:

- **runDRNLModel_speechinbabblenoiseSet01.m** - The main code that runs the simulations calculating cross-correlations. It has a parameter `Gcontrol`, which sets the higher (1) or lower (0.9) gain of the cochlear model.
- **runNobiliModel_IOfce_calib.m** - Script for I/O function calculation for the model.
- **runNobiliModel_isointfce.m** - Script that calculates iso-intensity responses of the model.
- **runNobiliModel_spinRDW.m** - Script that calculates the modulation index for the sentences (at the output of the cochlear model).

## About

This repository supports research on speech perception in noise, specifically examining how speech intelligibility and auditory responses change with sound level in multitalker masking noise. The simulations and analyses contribute to understanding cochlear processing and speech intelligibility under complex listening conditions.

