#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 22:17:32 2025

@author: vencov
"""
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.text(
    .5, .5, "There are 几个汉字 in between!",
    family=['DejaVu Sans', 'Noto Sans CJK JP', 'Noto Sans TC'],
    ha='center'
)