# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 22:03:01 2018

@author: ollih
"""

#%% Innert join for two years of athletes

# Renaming columns    
data_Men_Rx_2017.rename(columns={'Name': 'Name17', 
                                 'Height': 'Height17',
                                 'Weight': 'Weight17',
                                 'Age': 'Age17',
                                 'Regionid': 'Regionid17',
                                 'Regionname': 'Regionname17',
                                 'Affiliateid': 'Affiliateid17',
                                 'Overallrank': 'Overallrank17',
                                 'Overallscore': 'Overallscore17',
                                 }, inplace=True)

data_Men_Rx_2018.rename(columns={'Name': 'Name18',
                                 'Height': 'Height18',
                                 'Weight': 'Weight18',
                                 'Age': 'Age18',
                                 'Regionid': 'Regionid18',
                                 'Regionname': 'Regionname18',
                                 'Affiliateid': 'Affiliateid18',
                                 'Affiliatename': 'Affiliatename18',
                                 'Overallrank': 'Overallrank18',
                                 'Overallscore': 'Overallscore18',
                                 }, inplace=True)
# Merging data
two_years = pd.merge(data_Men_Rx_2018,
                     data_Men_Rx_2017,
                     on='Userid',
                     how='inner')

# Changing object datatype to better
two_years= two_years.infer_objects()

# Calculating new columns
two_years.loc[:,'OverallrankChange'] = two_years.loc[:,'Overallrank18'] - two_years.loc[:,'Overallrank17']
two_years.loc[:,'OverallscoreChange'] = two_years.loc[:,'Overallscore18'] - two_years.loc[:,'Overallscore17']   

# Analyzing data
two_years.groupby('Regionname18')['OverallrankChange'].mean()
two_years.groupby('Regionname18').agg({"OverallrankChange" : "mean"})

grouped = two_years.groupby("Regionname18").agg({
            "Overallrank18": "mean",
            "Overallrank17": "mean",
            "OverallrankChange": "mean",
            "Userid": "count"
        })   
