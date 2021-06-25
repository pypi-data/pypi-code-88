#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 12:48:26 2020

@author: jacob
"""
import seaborn as sns
import matplotlib.pyplot as plt
        
def heatmap_gr(plat, data_path):
    plate_name = plat.get_plate_name()
    # List for making heatmaps
    row_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    w, h = 3, 96
    heatmap_df = [[0 for x in range(w)] for y in range(h)]
    
    index = 0
    for i in range(8):
        for j in range(12):
            heatmap_df[index][0] = row_letters[i]
            heatmap_df[index][1] = cols[j]
            index += 1
            
    heatmap_df.columns = ["Rows", "Columns", "GR"]
    
    hm_data_gr[(col + row * 12) - 1][2] = gr

    # Tranposes data
    heatmap_df = heatmap_df.pivot(index="Rows", columns="Columns", values="GR")
    
    # Formatting heatmap to align with 96 well plate
    sns.set(font_scale=3)
    f, ax = plt.subplots(figsize=(42,28))
    sns.heatmap(heatmap_df, ax=ax, linewidth=0.5, cmap="magma", annot=True, vmin=0.5, vmax=1.5)
    ax.set_title(plate_name + ": Growth Rate Stress Ratio\n\n")
    plt.yticks(rotation=0)
    ax.xaxis.tick_top()  
    ax.set_xlabel('')
    ax.set_ylabel('')

    plt.savefig(data_path + "Heatmaps/GR/" + plate_name) 
    plt.close()
    
def heatmap_ymax(plat, data_path):
    # List for making heatmaps  
    row_letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
    cols = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    w, h = 3, 96
    heatmap_df = [[0 for x in range(w)] for y in range(h)]
    
    index = 0
    for i in range(8):
        for j in range(12):    
            heatmap_df[index][0] = row_letters[i]
            heatmap_df[index][1] = cols[j]
            index += 1
        
    heatmap_df.columns = ["Rows", "Columns", "GR"]
        
    # Tranposes data
    heatmap_df = heatmap_df.pivot(index="Rows", columns="Columns", values="Ymax")
    
    # Formatting heatmap to align with 96 well plate
    sns.set(font_scale=3)
    f, ax = plt.subplots(figsize=(42,28))
    sns.heatmap(heatmap_df, ax=ax, linewidth=0.5, cmap="magma", annot=True, vmin=0.5, vmax=1.5)
    ax.set_title(file_n + ": Ymax Stress Ratio\n\n")
    plt.yticks(rotation=0)
    ax.xaxis.tick_top()  
    ax.set_xlabel('')
    ax.set_ylabel('')
    
    plt.savefig(data_path + "Heatmaps/Ymax/" + file_n) 
    plt.close()