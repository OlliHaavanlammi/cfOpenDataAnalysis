# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:30:11 2018

@author: ollih
"""

import pandas as pd
import numpy as np

#%% Importing data on men and joining to one dataframe
data_Men_Rx_2018_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Men_Rx_2018\\Men_Rx_2018_1')
data_Men_Rx_2018_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Men_Rx_2018\\Men_Rx_2018_2')
data_Men_Rx_2018_3 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Men_Rx_2018\\Men_Rx_2018_3')
data_Men_Rx_2018_4 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Men_Rx_2018\\Men_Rx_2018_4')
data_Men_Rx_2018_5 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Men_Rx_2018\\Men_Rx_2018_5')
data_Men_Rx_2018_6 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Men_Rx_2018\\Men_Rx_2018_6')
data_Men_Rx_2018_7 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Men_Rx_2018\\Men_Rx_2018_7')

data_Men_Rx_2018 = data_Men_Rx_2018_1
data_Men_Rx_2018 = data_Men_Rx_2018.append(data_Men_Rx_2018_2)
data_Men_Rx_2018 = data_Men_Rx_2018.append(data_Men_Rx_2018_3)
data_Men_Rx_2018 = data_Men_Rx_2018.append(data_Men_Rx_2018_4)
data_Men_Rx_2018 = data_Men_Rx_2018.append(data_Men_Rx_2018_5)
data_Men_Rx_2018 = data_Men_Rx_2018.append(data_Men_Rx_2018_6)
data_Men_Rx_2018 = data_Men_Rx_2018.append(data_Men_Rx_2018_7)

del data_Men_Rx_2018_1
del data_Men_Rx_2018_2
del data_Men_Rx_2018_3
del data_Men_Rx_2018_4
del data_Men_Rx_2018_5
del data_Men_Rx_2018_6
del data_Men_Rx_2018_7

data_Men_Rx_2018['Division'] = 'Men, Rx'

#%% Importing data on women and joining to one dataframe
data_Women_Rx_2018_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Women_Rx_2018\\Women_Rx_2018_1')
data_Women_Rx_2018_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Women_Rx_2018\\Women_Rx_2018_2')
data_Women_Rx_2018_3 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Women_Rx_2018\\Women_Rx_2018_3')
data_Women_Rx_2018_4 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Women_Rx_2018\\Women_Rx_2018_4')
data_Women_Rx_2018_5 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Women_Rx_2018\\Women_Rx_2018_5')
data_Women_Rx_2018_6 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Women_Rx_2018\\Women_Rx_2018_6')
data_Women_Rx_2018_7 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\Women_Rx_2018\\Women_Rx_2018_7')

data_Women_Rx_2018 = data_Women_Rx_2018_1
data_Women_Rx_2018 = data_Women_Rx_2018.append(data_Women_Rx_2018_2)
data_Women_Rx_2018 = data_Women_Rx_2018.append(data_Women_Rx_2018_3)
data_Women_Rx_2018 = data_Women_Rx_2018.append(data_Women_Rx_2018_4)
data_Women_Rx_2018 = data_Women_Rx_2018.append(data_Women_Rx_2018_5)
data_Women_Rx_2018 = data_Women_Rx_2018.append(data_Women_Rx_2018_6)
data_Women_Rx_2018 = data_Women_Rx_2018.append(data_Women_Rx_2018_7)

del data_Women_Rx_2018_1
del data_Women_Rx_2018_2
del data_Women_Rx_2018_3
del data_Women_Rx_2018_4
del data_Women_Rx_2018_5
del data_Women_Rx_2018_6
del data_Women_Rx_2018_7

data_Women_Rx_2018['Division'] = 'Women, Rx'

#%% Importing data on other dividions
data_Men_45_49_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Men_45-49_Rx_2018')
data_Men_45_49_Rx_2018['Division'] = 'Men 45-49, Rx'
data_Women_45_49_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Women_45-49_Rx_2018')
data_Women_45_49_Rx_2018['Division'] = 'Women 45-49, Rx'

data_Men_50_54_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Men_50-54_Rx_2018')
data_Men_50_54_Rx_2018['Division'] = 'Men 50-54, Rx'
data_Women_50_54_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Women_50-54_Rx_2018')
data_Women_50_54_Rx_2018['Division'] = 'Women 50-54, Rx'

data_Men_55_59_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Men_55-59_Rx_2018')
data_Men_55_59_Rx_2018['Division'] = 'Men 55-59, Rx'
data_Women_55_59_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Women_55-59_Rx_2018')
data_Women_55_59_Rx_2018['Division'] = 'Women 55-59, Rx'

data_Men_60_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Men_60+_Rx_2018')
data_Men_60_Rx_2018['Division'] = 'Men 60+, Rx'
data_Women_60_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Women_60+_Rx_2018')
data_Women_60_Rx_2018['Division'] = 'Women 60+, Rx'

data_Men_40_44_Rx_2018_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Men_40-44_Rx_2018_1')
data_Men_40_44_Rx_2018_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Men_40-44_Rx_2018_2')
data_Men_40_44_Rx_2018 = data_Men_40_44_Rx_2018_1
data_Men_40_44_Rx_2018 = data_Men_40_44_Rx_2018.append(data_Men_40_44_Rx_2018_2)
del data_Men_40_44_Rx_2018_1
del data_Men_40_44_Rx_2018_2
data_Men_40_44_Rx_2018['Division'] = 'Men 40-44, Rx'

data_Women_40_44_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Women_40-44_Rx_2018')
data_Women_40_44_Rx_2018['Division'] = 'Women 40-44, Rx'

data_Boys_14_15_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Boys_14-15_Rx_2018')
data_Boys_14_15_Rx_2018['Division'] = 'Boys 14-15, Rx'
data_Girls_14_15_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Girls_14-15_Rx_2018')
data_Girls_14_15_Rx_2018['Division'] = 'Girls 14-15, Rx'

data_Boys_16_17_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Boys_16-17_Rx_2018')
data_Boys_16_17_Rx_2018['Division'] = 'Boys 16-17, Rx'
data_Girls_16_17_Rx_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Girls_16-17_Rx_2018')
data_Girls_16_17_Rx_2018['Division'] = 'Girls 16-17, Rx'

data_Men_35_39_Rx_2018_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Men_35-39_Rx_2018_1')
data_Men_35_39_Rx_2018_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Men_35-39_Rx_2018_2')
data_Men_35_39_Rx_2018 = data_Men_35_39_Rx_2018_1
data_Men_35_39_Rx_2018 = data_Men_35_39_Rx_2018.append(data_Men_35_39_Rx_2018_2)
del data_Men_35_39_Rx_2018_1
del data_Men_35_39_Rx_2018_2
data_Men_35_39_Rx_2018['Division'] = 'Men 35-39, Rx'

data_Women_35_39_Rx_2018_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Women_35-39_Rx_2018_1')
data_Women_35_39_Rx_2018_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_other\\Women_35-39_Rx_2018_2')
data_Women_35_39_Rx_2018 = data_Women_35_39_Rx_2018_1
data_Women_35_39_Rx_2018 = data_Women_35_39_Rx_2018.append(data_Women_35_39_Rx_2018_2)
del data_Women_35_39_Rx_2018_1
del data_Women_35_39_Rx_2018_2
data_Women_35_39_Rx_2018['Division'] = 'Women 35-39, Rx'

#%% Importing data on scaled divisions

data_Men_Sc_2018_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_scaled\\Men_Sc_2018_1')
data_Men_Sc_2018_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_scaled\\Men_Sc_2018_2')
data_Men_Sc_2018 = data_Men_Sc_2018_1
data_Men_Sc_2018 = data_Men_Sc_2018.append(data_Men_Sc_2018_2)
del data_Men_Sc_2018_1
del data_Men_Sc_2018_2
data_Men_Sc_2018['Division'] = 'Men, Scaled'

data_Women_Sc_2018_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_scaled\\Women_Sc_2018_1')
data_Women_Sc_2018_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_scaled\\Women_Sc_2018_2')
data_Women_Sc_2018_3 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_scaled\\Women_Sc_2018_3')
data_Women_Sc_2018 = data_Women_Sc_2018_1
data_Women_Sc_2018 = data_Women_Sc_2018.append(data_Women_Sc_2018_2)
data_Women_Sc_2018 = data_Women_Sc_2018.append(data_Women_Sc_2018_3)
del data_Women_Sc_2018_1
del data_Women_Sc_2018_2
del data_Women_Sc_2018_3
data_Women_Sc_2018['Division'] = 'Women, Scaled'

data_Men_45_49_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Men_45-49_Sc_2018')
data_Men_45_49_Sc_2018['Division'] = 'Men 45-49, Scaled'
data_Women_45_49_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Women_45-49_Sc_2018')
data_Women_45_49_Sc_2018['Division'] = 'Women 45-49, Scaled'

data_Men_50_54_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_scaled\\Men_50-54_Sc_2018')
data_Men_50_54_Sc_2018['Division'] = 'Men 50-54, Scaled'
data_Women_50_54_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_scaled\\Women_50-54_Sc_2018')
data_Women_50_54_Sc_2018['Division'] = 'Women 50-54, Scaled'

data_Men_55_59_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Men_55-59_Sc_2018')
data_Men_55_59_Sc_2018['Division'] = 'Men 55-59, Scaled'
data_Women_55_59_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Women_55-59_Sc_2018')
data_Women_55_59_Sc_2018['Division'] = 'Women 55-59, Scaled'

data_Men_60_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Men_60+_Sc_2018')
data_Men_60_Sc_2018['Division'] = 'Men 60+, Scaled'
data_Women_60_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Women_60+_Sc_2018')
data_Women_60_Sc_2018['Division'] = 'Women 60+, Scaled'

data_Men_40_44_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Men_40-44_Sc_2018')
data_Men_40_44_Sc_2018['Division'] = 'Men 40-44, Scaled'
data_Women_40_44_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Women_40-44_Sc_2018')
data_Women_40_44_Sc_2018['Division'] = 'Women 40-44, Scaled'

data_Boys_14_15_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Boys_14-15_Sc_2018')
data_Boys_14_15_Sc_2018['Division'] = 'Boys 14-15, Scaled'
data_Girls_14_15_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Girls_14-15_Sc_2018')
data_Girls_14_15_Sc_2018['Division'] = 'Girls 14-15, Scaled'

data_Boys_16_17_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Boys_16-17_Sc_2018')
data_Boys_16_17_Sc_2018['Division'] = 'Boys 16-17, Scaled'
data_Girls_16_17_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Girls_16-17_Sc_2018')
data_Girls_16_17_Sc_2018['Division'] = 'Girls 16-17, Scaled'

data_Men_35_39_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Men_35-39_Sc_2018')
data_Men_35_39_Sc_2018['Division'] = 'Men 35-39, Scaled'
data_Women_35_39_Sc_2018 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2018_Scaled\\Women_35-39_Sc_2018')
data_Women_35_39_Sc_2018['Division'] = 'Women 35-39, Scaled'

#%% Joining all data to one DataFrame (Rx divisions last for the purppse on marking duplicates)
data = data_Men_45_49_Rx_2018
data = data.append(data_Women_45_49_Rx_2018)
data = data.append(data_Men_50_54_Rx_2018)
data = data.append(data_Women_50_54_Rx_2018)
data = data.append(data_Men_55_59_Rx_2018)
data = data.append(data_Women_55_59_Rx_2018)
data = data.append(data_Men_60_Rx_2018)
data = data.append(data_Women_60_Rx_2018)
data = data.append(data_Men_40_44_Rx_2018)
data = data.append(data_Women_40_44_Rx_2018)
data = data.append(data_Boys_14_15_Rx_2018)
data = data.append(data_Girls_14_15_Rx_2018)
data = data.append(data_Boys_16_17_Rx_2018)
data = data.append(data_Girls_16_17_Rx_2018)
data = data.append(data_Men_35_39_Rx_2018)
data = data.append(data_Women_35_39_Rx_2018)

data = data.append(data_Men_Sc_2018)
data = data.append(data_Women_Sc_2018)
data = data.append(data_Men_45_49_Sc_2018)
data = data.append(data_Women_45_49_Sc_2018)
data = data.append(data_Men_50_54_Sc_2018)
data = data.append(data_Women_50_54_Sc_2018)
data = data.append(data_Men_55_59_Sc_2018)
data = data.append(data_Women_55_59_Sc_2018)
data = data.append(data_Men_60_Sc_2018)
data = data.append(data_Women_60_Sc_2018)
data = data.append(data_Men_40_44_Sc_2018)
data = data.append(data_Women_40_44_Sc_2018)
data = data.append(data_Boys_14_15_Sc_2018)
data = data.append(data_Girls_14_15_Sc_2018)
data = data.append(data_Boys_16_17_Sc_2018)
data = data.append(data_Girls_16_17_Sc_2018)
data = data.append(data_Men_35_39_Sc_2018)
data = data.append(data_Women_35_39_Sc_2018)

data = data.append(data_Men_Rx_2018)
data = data.append(data_Women_Rx_2018)

del data_Men_Rx_2018
del data_Women_Rx_2018
del data_Men_45_49_Rx_2018
del data_Women_45_49_Rx_2018
del data_Men_50_54_Rx_2018
del data_Women_50_54_Rx_2018 
del data_Men_55_59_Rx_2018
del data_Women_55_59_Rx_2018
del data_Men_60_Rx_2018
del data_Women_60_Rx_2018
del data_Men_40_44_Rx_2018
del data_Women_40_44_Rx_2018
del data_Boys_14_15_Rx_2018
del data_Girls_14_15_Rx_2018
del data_Boys_16_17_Rx_2018
del data_Girls_16_17_Rx_2018
del data_Men_35_39_Rx_2018
del data_Women_35_39_Rx_2018

del data_Men_Sc_2018
del data_Women_Sc_2018
del data_Men_45_49_Sc_2018
del data_Women_45_49_Sc_2018
del data_Men_50_54_Sc_2018
del data_Women_50_54_Sc_2018 
del data_Men_55_59_Sc_2018
del data_Women_55_59_Sc_2018
del data_Men_60_Sc_2018
del data_Women_60_Sc_2018
del data_Men_40_44_Sc_2018
del data_Women_40_44_Sc_2018
del data_Boys_14_15_Sc_2018
del data_Girls_14_15_Sc_2018
del data_Boys_16_17_Sc_2018
del data_Girls_16_17_Sc_2018
del data_Men_35_39_Sc_2018
del data_Women_35_39_Sc_2018

#%% Marking duplicate rows
duplicates = data["Userid"].duplicated(keep='first')
data["duplicate"] = duplicates

#%% Importing data on CF Boxes in Finland
file = 'C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\cfBoxes.xlsx'
cfBoxes = pd.read_excel(file, sheet_name='cfBoxes')

#%% Classifying boxes to groups

"""
AffiliateGroup: Boxes in Finland = Affiliatename. Other. "All excl. Finland"
RegionnameMod: Region "Northern Europe" is divided to two group: "Europe North, excl. Finland" and "Finland"  
"""
    
# Mapping Finnish Affiliate names to Affiliateid (older than 2018 data has no name, only id)
cfBoxesTable = pd.merge(cfBoxes,
                     data[['Affiliatename', 'Affiliateid']],
                     on='Affiliatename',
                     how='left')
cfBoxesTable = cfBoxesTable.drop_duplicates(keep='first')
cfBoxesTable = cfBoxesTable.reset_index(drop=True)

# Adding "AffiliateGroup" -column to data for furher analysis
data = pd.merge(data,
                cfBoxesTable,
                on='Affiliateid',
                how='left')

data.rename(columns={'Affiliatename_x': 'Affiliatename'}, inplace=True)
data.rename(columns={'Affiliatename_y': 'AffiliateGroup'}, inplace=True)

data['AffiliateGroup'] = data['AffiliateGroup'].replace(np.nan, 'All excl. Finland', regex=True)
data['City'] = data['City'].replace(np.nan, 'Non-Finnish', regex=True)
data['Country'] = data['Country'].replace(np.nan, 'Non-Finnish', regex=True)

# Creating new column 'RegionnameMod'. Separating region "Northern Europe" to tow classes
data['RegionnameMod'] = data['Regionname']

EN_rows = data['Regionname'].isin(['Europe North'])
data.loc[EN_rows,('RegionnameMod')] = 'Europe North, excl. Finland'

FI_ids = cfBoxesTable['Affiliateid']
FI_rows = data['Affiliateid'].isin(FI_ids)
data.loc[FI_rows,('RegionnameMod')] = 'Finland'

#%% Separating 18.3 score to to different columns
"""
18.3_score_rep: If athlete has time, this column is 925 (=max reps in the event), otherwise this is 18.4_score column
18.3_score_time: If athlete has reps, this column in 'Nan', otherwise this is 18.3_score column
"""
data['18.3_score_rep'] = data['18.3_score']
data['18.3_score_time'] = data['18.3_score']

rep_rows = data.applymap(lambda x: isinstance(x, (int)))['18.3_score']
empty_rows = data.applymap(lambda x: isinstance(x, (float)))['18.3_score']
time_rows = ~(rep_rows | empty_rows)

data.loc[rep_rows,('18.3_score_rep')] = data.loc[rep_rows,('18.3_score')]
data.loc[empty_rows,('18.3_score_rep')] = None
data.loc[time_rows,('18.3_score_rep')] = 928

data.loc[rep_rows,('18.3_score_time')] = None
data.loc[empty_rows,('18.3_score_time')] = None
data.loc[time_rows,('18.3_score_time')] = data.loc[time_rows,('18.3_score')]

# Let's change columns containing time to seconds for the Tableau analysis
data.loc[time_rows,('18.3_score_time')] = data.loc[time_rows,('18.3_score_time')].map(lambda x: pd.to_timedelta(x).seconds)

#%% Separating 18.4 score to to different columns
"""
18.4_score_rep: If athlete has time, this column is 165 (=max reps in the event), otherwise this is 18.4_score column
18.4_score_time: If athlete has reps, this column in 'None', otherwise this is 18.4_score column
"""
data['18.4_score_rep'] = data['18.4_score']
data['18.4_score_time'] = data['18.4_score']

rep_rows = data.applymap(lambda x: isinstance(x, (int)))['18.4_score']
empty_rows = data.applymap(lambda x: isinstance(x, (float)))['18.4_score']
time_rows = ~(rep_rows | empty_rows)

data.loc[rep_rows,('18.4_score_rep')] = data.loc[rep_rows,('18.4_score')]
data.loc[empty_rows,('18.4_score_rep')] = None
data.loc[time_rows,('18.4_score_rep')] = 165

data.loc[rep_rows,('18.4_score_time')] = None
data.loc[empty_rows,('18.4_score_time')] = None
data.loc[time_rows,('18.4_score_time')] = data.loc[time_rows,('18.4_score')]

# Let's change columns containing time to seconds for the Tableau analysis
data.loc[time_rows,('18.4_score_time')] = data.loc[time_rows,('18.4_score_time')].map(lambda x: pd.to_timedelta(x).seconds)

#%% Adding column for sex and Rx/Scaled

male_rows = data['Division'].str.contains("Men") | data['Division'].str.contains("Boys")
female_rows = data['Division'].str.contains("Women") | data['Division'].str.contains("Girls")
data['Sex'] = data['Division']
data.loc[male_rows, ('Sex')] = 'Male'
data.loc[female_rows, ('Sex')] = 'Female'

rx_rows = data['Division'].str.contains("Rx")
sc_rows = data['Division'].str.contains("Sc")
data['Rx/Scaled'] = data['Division']
data.loc[rx_rows, ('Rx/Scaled')] = 'Rx'
data.loc[sc_rows, ('Rx/Scaled')] = 'Scaled'

#%% Save excel for Tableau analysis

data.to_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataTableau\\Open_2018_Tableau')
data.to_csv('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataTableau\\Open_2018_Tableau.csv')

# Write to excel
writer = pd.ExcelWriter('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataTableau\\Open_2018_Tableau.xlsx')
data.to_excel(writer)
writer.save()
    
    
    
    


    