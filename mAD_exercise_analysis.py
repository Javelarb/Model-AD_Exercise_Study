#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 13:30:34 2023

@author: julio
"""

import os
import pandas as pd
#import skbio as bio

os.chdir("/media/julio/Storage/mAD_exercise")

#Import data as data frame and filter.
mp3_data = pd.read_csv('/media/julio/Storage/mAD_exercise/mAD_exercise_taxonomy_table.txt', sep='\t', comment='#')
mp3_data = mp3_data.drop(labels = 'NCBI_tax_id', axis = 1) #Drops the second column by name.
mp3_data.columns = mp3_data.columns.str.replace('_relab', '') #Modifies the column names.
mp3_data = mp3_data[mp3_data['clade_name'].str.contains('s__')] #Filters rows to those which only contain species calls.

mp3_data = mp3_data.transpose() #Transpose the data
mp3_data.columns = mp3_data.iloc[0] #Set new column names base on the first row 
mp3_data = mp3_data.drop(labels = 'clade_name', axis = 0) #Drop the clade names row since its already in the column names
mp3_data = mp3_data.apply(pd.to_numeric)

#Import read counts to convert relative abundance to counts
QF_read_counts = pd.read_csv('/media/julio/Storage/mAD_exercise/QF_read_counts.txt', sep='\t', comment='#', index_col= 'SampleID')
QF_read_counts = QF_read_counts.sort_values(by = 'SampleID', ascending = False)
QF_read_counts = QF_read_counts.squeeze()

#Convert to counts
mp3_data = mp3_data.mul(QF_read_counts, axis = 0)
mp3_data = round(mp3_data)

#Import metadata
metadata = pd.read_csv('/media/julio/Storage/mAD_exercise/mAD_exercise_metadata.txt', sep='\t')
merged_species_table = metadata.merge(mp3_data, how = 'left', left_on = 'SampleID', right_index = True)

#Write table
merged_species_table.to_csv('/media/julio/Storage/mAD_exercise/merged_species_table.tsv', sep="\t", index=False)

#Alpha diversity
#shannon_div = mp3_data.apply(bio.diversity.alpha.shannon, axis = 1)