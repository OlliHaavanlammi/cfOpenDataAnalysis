# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 21:30:11 2019

@author: ollih
"""

import pandas as pd
import numpy as np

#%% Importing data on men and joining to one dataframe
data_Men_Rx_2019_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_Rx_2019_1')
data_Men_Rx_2019_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_Rx_2019_2')
data_Men_Rx_2019_3 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_Rx_2019_3')
data_Men_Rx_2019_4 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_Rx_2019_4')
data_Men_Rx_2019_5 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_Rx_2019_5')
data_Men_Rx_2019_6 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_Rx_2019_6')
data_Men_Rx_2019_7 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_Rx_2019_7')
data_Men_Rx_2019_8 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_Rx_2019_8')

data_Men_Rx_2019 = data_Men_Rx_2019_1
data_Men_Rx_2019 = data_Men_Rx_2019.append(data_Men_Rx_2019_2)
data_Men_Rx_2019 = data_Men_Rx_2019.append(data_Men_Rx_2019_3)
data_Men_Rx_2019 = data_Men_Rx_2019.append(data_Men_Rx_2019_4)
data_Men_Rx_2019 = data_Men_Rx_2019.append(data_Men_Rx_2019_5)
data_Men_Rx_2019 = data_Men_Rx_2019.append(data_Men_Rx_2019_6)
data_Men_Rx_2019 = data_Men_Rx_2019.append(data_Men_Rx_2019_7)
data_Men_Rx_2019 = data_Men_Rx_2019.append(data_Men_Rx_2019_8)

del data_Men_Rx_2019_1
del data_Men_Rx_2019_2
del data_Men_Rx_2019_3
del data_Men_Rx_2019_4
del data_Men_Rx_2019_5
del data_Men_Rx_2019_6
del data_Men_Rx_2019_7
del data_Men_Rx_2019_8

data_Men_Rx_2019['Division'] = 'Men, Rx'

#%% Importing data on women and joining to one dataframe
data_Women_Rx_2019_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_Rx_2019_1')
data_Women_Rx_2019_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_Rx_2019_2')
data_Women_Rx_2019_3 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_Rx_2019_3')
data_Women_Rx_2019_4 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_Rx_2019_4')
data_Women_Rx_2019_5 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_Rx_2019_5')
data_Women_Rx_2019_6 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_Rx_2019_6')

data_Women_Rx_2019 = data_Women_Rx_2019_1
data_Women_Rx_2019 = data_Women_Rx_2019.append(data_Women_Rx_2019_2)
data_Women_Rx_2019 = data_Women_Rx_2019.append(data_Women_Rx_2019_3)
data_Women_Rx_2019 = data_Women_Rx_2019.append(data_Women_Rx_2019_4)
data_Women_Rx_2019 = data_Women_Rx_2019.append(data_Women_Rx_2019_5)
data_Women_Rx_2019 = data_Women_Rx_2019.append(data_Women_Rx_2019_6)

del data_Women_Rx_2019_1
del data_Women_Rx_2019_2
del data_Women_Rx_2019_3
del data_Women_Rx_2019_4
del data_Women_Rx_2019_5
del data_Women_Rx_2019_6

data_Women_Rx_2019['Division'] = 'Women, Rx'

#%% Importing data on other dividions

data_Men_45_49_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_45-49_Rx_2019_1')
data_Men_45_49_Rx_2019['Division'] = 'Men 45-49, Rx'
data_Women_45_49_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_45-49_Rx_2019_1')
data_Women_45_49_Rx_2019['Division'] = 'Women 45-49, Rx'

data_Men_50_54_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_50-54_Rx_2019_1')
data_Men_50_54_Rx_2019['Division'] = 'Men 50-54, Rx'
data_Women_50_54_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_50-54_Rx_2019_1')
data_Women_50_54_Rx_2019['Division'] = 'Women 50-54, Rx'

data_Men_55_59_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_55-59_Rx_2019_1')
data_Men_55_59_Rx_2019['Division'] = 'Men 55-59, Rx'
data_Women_55_59_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_55-59_Rx_2019_1')
data_Women_55_59_Rx_2019['Division'] = 'Women 55-59, Rx'

data_Men_60_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_60+_Rx_2019_1')
data_Men_60_Rx_2019['Division'] = 'Men 60+, Rx'
data_Women_60_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_60+_Rx_2019_1')
data_Women_60_Rx_2019['Division'] = 'Women 60+, Rx'

data_Men_40_44_Rx_2019_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_40-44_Rx_2019_1')
data_Men_40_44_Rx_2019_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_40-44_Rx_2019_2')
data_Men_40_44_Rx_2019 = data_Men_40_44_Rx_2019_1
data_Men_40_44_Rx_2019 = data_Men_40_44_Rx_2019.append(data_Men_40_44_Rx_2019_2)
del data_Men_40_44_Rx_2019_1
del data_Men_40_44_Rx_2019_2
data_Men_40_44_Rx_2019['Division'] = 'Men 40-44, Rx'

data_Women_40_44_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_40-44_Rx_2019_1')
data_Women_40_44_Rx_2019['Division'] = 'Women 40-44, Rx'

data_Boys_14_15_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Boys_14-15_Rx_2019_1')
data_Boys_14_15_Rx_2019['Division'] = 'Boys 14-15, Rx'
data_Girls_14_15_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Girls_14-15_Rx_2019_1')
data_Girls_14_15_Rx_2019['Division'] = 'Girls 14-15, Rx'

data_Boys_16_17_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Boys_16-17_Rx_2019_1')
data_Boys_16_17_Rx_2019['Division'] = 'Boys 16-17, Rx'
data_Girls_16_17_Rx_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Girls_16-17_Rx_2019_1')
data_Girls_16_17_Rx_2019['Division'] = 'Girls 16-17, Rx'

data_Men_35_39_Rx_2019_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_35-39_Rx_2019_1')
data_Men_35_39_Rx_2019_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_35-39_Rx_2019_2')
data_Men_35_39_Rx_2019 = data_Men_35_39_Rx_2019_1
data_Men_35_39_Rx_2019 = data_Men_35_39_Rx_2019.append(data_Men_35_39_Rx_2019_2)
del data_Men_35_39_Rx_2019_1
del data_Men_35_39_Rx_2019_2
data_Men_35_39_Rx_2019['Division'] = 'Men 35-39, Rx'

data_Women_35_39_Rx_2019_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_35-39_Rx_2019_1')
data_Women_35_39_Rx_2019_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_35-39_Rx_2019_2')
data_Women_35_39_Rx_2019 = data_Women_35_39_Rx_2019_1
data_Women_35_39_Rx_2019 = data_Women_35_39_Rx_2019.append(data_Women_35_39_Rx_2019_2)
del data_Women_35_39_Rx_2019_1
del data_Women_35_39_Rx_2019_2
data_Women_35_39_Rx_2019['Division'] = 'Women 35-39, Rx'


#%% Importing data on scaled divisions
data_Men_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_Sc_2019_1')
data_Men_Sc_2019['Division'] = 'Men, Scaled'

data_Women_Sc_2019_1 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_Sc_2019_1')
data_Women_Sc_2019_2 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_Sc_2019_2')
data_Women_Sc_2019 = data_Women_Sc_2019_1
data_Women_Sc_2019 = data_Women_Sc_2019.append(data_Women_Sc_2019_2)
del data_Women_Sc_2019_1
del data_Women_Sc_2019_2
data_Women_Sc_2019['Division'] = 'Women, Scaled'

data_Men_45_49_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_45-49_Sc_2019_1')
data_Men_45_49_Sc_2019['Division'] = 'Men 45-49, Scaled'
data_Women_45_49_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_45-49_Sc_2019_1')
data_Women_45_49_Sc_2019['Division'] = 'Women 45-49, Scaled'

data_Men_50_54_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_50-54_Sc_2019_1')
data_Men_50_54_Sc_2019['Division'] = 'Men 50-54, Scaled'
data_Women_50_54_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_50-54_Sc_2019_1')
data_Women_50_54_Sc_2019['Division'] = 'Women 50-54, Scaled'

data_Men_55_59_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_55-59_Sc_2019_1')
data_Men_55_59_Sc_2019['Division'] = 'Men 55-59, Scaled'
data_Women_55_59_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_55-59_Sc_2019_1')
data_Women_55_59_Sc_2019['Division'] = 'Women 55-59, Scaled'

data_Men_60_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_60+_Sc_2019_1')
data_Men_60_Sc_2019['Division'] = 'Men 60+, Scaled'
data_Women_60_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_60+_Sc_2019_1')
data_Women_60_Sc_2019['Division'] = 'Women 60+, Scaled'

data_Men_40_44_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_40-44_Sc_2019_1')
data_Men_40_44_Sc_2019['Division'] = 'Men 40-44, Scaled'
data_Women_40_44_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_40-44_Sc_2019_1')
data_Women_40_44_Sc_2019['Division'] = 'Women 40-44, Scaled'

data_Boys_14_15_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Boys_14-15_Sc_2019_1')
data_Boys_14_15_Sc_2019['Division'] = 'Boys 14-15, Scaled'
data_Girls_14_15_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Girls_14-15_Sc_2019_1')
data_Girls_14_15_Sc_2019['Division'] = 'Girls 14-15, Scaled'

data_Boys_16_17_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Boys_16-17_Sc_2019_1')
data_Boys_16_17_Sc_2019['Division'] = 'Boys 16-17, Scaled'
data_Girls_16_17_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Girls_16-17_Sc_2019_1')
data_Girls_16_17_Sc_2019['Division'] = 'Girls 16-17, Scaled'

data_Men_35_39_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Men_35-39_Sc_2019_1')
data_Men_35_39_Sc_2019['Division'] = 'Men 35-39, Scaled'
data_Women_35_39_Sc_2019 = pd.read_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataFinal\\2019\\Women_35-39_Sc_2019_1')
data_Women_35_39_Sc_2019['Division'] = 'Women 35-39, Scaled'

#%% Joining all data to one DataFrame 
#(First scaled masters/teens then rx masters/tees then scaled and then rx for the purpose on marking duplicates)

data = data_Men_45_49_Sc_2019
data = data.append(data_Women_45_49_Sc_2019)
data = data.append(data_Men_50_54_Sc_2019)
data = data.append(data_Women_50_54_Sc_2019)
data = data.append(data_Men_55_59_Sc_2019)
data = data.append(data_Women_55_59_Sc_2019)
data = data.append(data_Men_60_Sc_2019)
data = data.append(data_Women_60_Sc_2019)
data = data.append(data_Men_40_44_Sc_2019)
data = data.append(data_Women_40_44_Sc_2019)
data = data.append(data_Boys_14_15_Sc_2019)
data = data.append(data_Girls_14_15_Sc_2019)
data = data.append(data_Boys_16_17_Sc_2019)
data = data.append(data_Girls_16_17_Sc_2019)
data = data.append(data_Men_35_39_Sc_2019)
data = data.append(data_Women_35_39_Sc_2019)

data = data.append(data_Men_45_49_Rx_2019)
data = data.append(data_Women_45_49_Rx_2019)
data = data.append(data_Men_50_54_Rx_2019)
data = data.append(data_Women_50_54_Rx_2019)
data = data.append(data_Men_55_59_Rx_2019)
data = data.append(data_Women_55_59_Rx_2019)
data = data.append(data_Men_60_Rx_2019)
data = data.append(data_Women_60_Rx_2019)
data = data.append(data_Men_40_44_Rx_2019)
data = data.append(data_Women_40_44_Rx_2019)
data = data.append(data_Boys_14_15_Rx_2019)
data = data.append(data_Girls_14_15_Rx_2019)
data = data.append(data_Boys_16_17_Rx_2019)
data = data.append(data_Girls_16_17_Rx_2019)
data = data.append(data_Men_35_39_Rx_2019)
data = data.append(data_Women_35_39_Rx_2019)

data = data.append(data_Men_Sc_2019)
data = data.append(data_Women_Sc_2019)

data = data.append(data_Men_Rx_2019)
data = data.append(data_Women_Rx_2019)

del data_Men_Rx_2019
del data_Women_Rx_2019
del data_Men_45_49_Rx_2019
del data_Women_45_49_Rx_2019
del data_Men_50_54_Rx_2019
del data_Women_50_54_Rx_2019 
del data_Men_55_59_Rx_2019
del data_Women_55_59_Rx_2019
del data_Men_60_Rx_2019
del data_Women_60_Rx_2019
del data_Men_40_44_Rx_2019
del data_Women_40_44_Rx_2019
del data_Boys_14_15_Rx_2019
del data_Girls_14_15_Rx_2019
del data_Boys_16_17_Rx_2019
del data_Girls_16_17_Rx_2019
del data_Men_35_39_Rx_2019
del data_Women_35_39_Rx_2019

del data_Men_Sc_2019
del data_Women_Sc_2019
del data_Men_45_49_Sc_2019
del data_Women_45_49_Sc_2019
del data_Men_50_54_Sc_2019
del data_Women_50_54_Sc_2019 
del data_Men_55_59_Sc_2019
del data_Women_55_59_Sc_2019
del data_Men_60_Sc_2019
del data_Women_60_Sc_2019
del data_Men_40_44_Sc_2019
del data_Women_40_44_Sc_2019
del data_Boys_14_15_Sc_2019
del data_Girls_14_15_Sc_2019
del data_Boys_16_17_Sc_2019
del data_Girls_16_17_Sc_2019
del data_Men_35_39_Sc_2019
del data_Women_35_39_Sc_2019

#%% Marking duplicate rows
duplicates = data["Userid"].duplicated(keep='first')
data["duplicate"] = duplicates

#countries = pd.unique(data['Country'])
#len(countries)

#%% Separating 19.2 score to to different columns
"""
19.2_score_rep: If athlete has time, this column is 165 (=max reps in the event), otherwise this is 18.4_score column
19.2_score_time: If athlete has reps, this column in 'None', otherwise this is 19.2_score column
"""
data['19.2_score_rep'] = data['19.2_score']
data['19.2_score_time'] = data['19.2_score']

rep_rows = data.applymap(lambda x: isinstance(x, (int)))['19.2_score']
empty_rows = data.applymap(lambda x: isinstance(x, (float)))['19.2_score']
time_rows = ~(rep_rows | empty_rows)

data.loc[rep_rows,('19.2_score_rep')] = data.loc[rep_rows,('19.2_score')]
data.loc[empty_rows,('19.2_score_rep')] = None
data.loc[time_rows,('19.2_score_rep')] = 430

data.loc[rep_rows,('19.2_score_time')] = None
data.loc[empty_rows,('19.2_score_time')] = None
data.loc[time_rows,('19.2_score_time')] = data.loc[time_rows,('19.2_score')]

# Let's change columns containing time to seconds for the Tableau analysis
data.loc[time_rows,('19.2_score_time')] = data.loc[time_rows,('19.2_score_time')].map(lambda x: pd.to_timedelta(x).seconds)


#%% Save excel for Tableau analysis

data.to_pickle('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataTableau\\Open_2019_Tableau')
#data.to_csv('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataTableau\\Open_2019_Tableau.csv')

# Write to excel
writer = pd.ExcelWriter('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataTableau\\Open_2019_Tableau.xlsx')
data.to_excel(writer)
writer.save()
    
    
    
    


    