
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 23:08:34 2018
@author: Ray
Download Crossfit open data and save as a pandas DataFrame.
"""

import os, sys
os.chdir('C:\\Users\\ollih\\Python-projects\\cfDataAnalysis')
ddir = 'C:\\Users\\ollih\\Python-projects\\cfDataAnalysis\\DataTemp'
if not os.path.isdir(ddir):
    os.makedirs(ddir)


import requests # HTTP library
import pandas as pd
import numpy as np
import time
from bisect import bisect

start_time = time.time()


def div_to_name(a):
    """Division number to a string.
    
    Parameters
    ----------
    a : integer (1-17)
        Numerical values of the division.
        1 : Men
        2 : Women
    
    Returns
    -------
    out : string
        Name of the division.
    
    """
    div_dict = {'1':"Men", '2':"Women", '3':"Men_45-49", '4':"Women_45-49", 
                '5':"Men_50-54", '6':"Women_50-54", '7':"Men_55-59",
                '8':"Women_55-59", '9':"Men_60+", '10':"Women_60+",
                '11':"Team", '12':"Men_40-44", '13':"Women_40-44",
                '14':"Boys_14-15", '15':"Girls_14-15", '16':"Boys_16-17",
                '17':"Girls_16-17", '18':"Men_35-39", '19':"Women_35-39"}
    return div_dict[str(a)]


def scaled_to_name(a):
    """Scaled number to a string.
    
    Parameters
    ----------
    a : integer (0,1)
        Numerical values if workout was RX'd or Scaled.
        0 : Rx
        1 : Sc
    
    Returns
    -------
    out : string
        Workout type.
    
    """
    wt_list = ['Rx','Sc']
    return wt_list[a]    
    

def get_page(path, headers, div, scal, page):
    """Get a page of results.
    
    Parameters
    ----------
    path : str
        URL path of results.
    headers : dict
        Dictionary to initialize requests.
    div : integer (1-17)
        Numerical values of the division.
        1 : Men
        2 : Women
    scal : integer (0,1)
        Numerical values if workout was Scaled or RX'd.
        0 : Rx
        1 : Sc
    p : interger (>= 1)
        Page of results.
        
    Returns
    -------
    out : dict
        Response.
    """
    try:
        return requests.get(path,
                params={"division": div,
                        "scaled": scal,
                        "sort": "0",
                        "fittest": "1",
                        "fittest1": "0",
                        "occupation": "0",
                        "competition": "1",
                        "page": page},
                headers=headers).json()
       
    except ValueError:
        return 'No response'
    except KeyError:
        return 'No response'
    

def check_if_empty(a):
    """Check if a score is empty.
    
    Parameters
    ----------
    a : str
        Workout score.
        
    Returns
    -------
    out : bool
        True is empty. False is not. 
    """
    if a == '0':
        return True
    elif a == '':
        return True
    else:
        return False


def check_if_scaled(a):
    """Check if a score is scaled.
    
    Parameters
    ----------
    a : str
        Workout score.
        
    Returns
    -------
    out : bool
        True is scaled score. False is Rx score.
    """
    if a.split(" ")[-1] == 's':
        return True
    else:
        return False
    

def extract_score(a):
    """Convert workout score to a pd.Timedelta or integer.
    
    Parameters
    ----------
    a : str
        Workout score.
        
    Returns
    -------
    out : empty list, pd.Timedelta or int
        Workout score.
    """        
    if "reps" in a:
        return int(a.split(" ")[0])
    elif "kg" in a:
        return int(a.replace(" kg",""))
    elif "lb" in a:
        lb =  int(a.replace(" lb",""))
        kg = round(lb * 0.45359237, 0)
        return kg
    else:
        return pd.to_timedelta('0:'+a)


def workout_score(a, scal):
    """Convert workout score to a np.nan, pd.Timedelta or integer.
       
    
    Parameters
    ----------
    a : str
        Workout score.
    scal : integer (0,1)
        Numerical values if workout was Scaled or RX'd.
        0 : Rx
        1 : Sc
        
    Returns
    -------
    out : np.nan, pd.Timedelta or int
        Workout score.
    """
    # Check if score is empty
    if check_if_empty(a):
        return np.nan
    if scal == 0:
        # Some people sign up for Rx then enter scaled scores...
        if check_if_scaled(a):
            return np.nan
    if a.split(" ")[-1] == 's':
        return extract_score(a.replace(" - s",""))
    return extract_score(a)


def workout_rank(a, rank):
    """If workout score is empty make workout rank empty.
    Parameters
    ----------
    a : empty list, pd.Timedelta or integer
        Workout score.
   rank : str
        Workout rank.
        
    Returns
    -------
    out : np.nan  or int
        Workout rank.
    """
    # Check if workout score is empty
    if pd.isnull(a):
        return np.nan
    else:
        return int(rank)

def athlete_height(a):
    """Convert athlete height to cm
    
    Parameters
    ----------
    a : str
        Height in cm or in inches.
        
    Returns
    -------
    out : int
        Height in cm
    """
    if pd.isnull(a):
        return np.nan
    if "cm" in a:
        temp = round(int(a.replace(" cm","")),0)
    if "'" in a:
        temp = a.split('"')[0]
        feet = int(temp.split("'")[0])
        inches = int(temp.split("'")[1])
        cm = round(feet*30.48 + 2.54*inches,0)
        temp = cm
    if "in" in a:
        inches = round(int(a.replace(" in","")), 0)
        kg = round(2.54 * inches,0)
        temp = kg    
        
        if temp < 120 or temp > 225:
            return np.nan
        else:
            return temp 
    
def athlete_weight(a):
    """Convert athlete weight to kg
    
    Parameters
    ----------
    a : str
        Weight in lbs or in kgs.
        
    Returns
    -------
    out : int
        Weight in kg
    """
    if pd.isnull(a):
        return np.nan
    if "kg" in a:
        temp = round(int(a.replace(" kg","")), 0)
    if "lb" in a:
        lb = int(a.replace(" lb",""))
        kg = round(lb * 0.45359237,0)
        temp = kg
        
        if temp < 40 or temp > 200:
            return np.nan
        else:
            return temp
        
def main():
    # Choose parameters to get data.
    year = 2019
    division = [1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19]
    scaled = [0,1]
    
    for iii in range(len(scaled)):
        
        for ii in range(len(division)):
    
            dname = div_to_name(division[ii])+'_'+scaled_to_name(scaled[iii])+'_'+str(year)
        
            # Initilize request
            headers = {'Host': 'games.crossfit.com',
                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2'+\
                       ') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.13'+\
                       '2 Safari/537.36'}
            
            basepath = 'https://games.crossfit.com/competitions/api/v1/competitions/'+\
                       'open/'+str(year)+'/leaderboards?'
                       
            # Setup DataFrame (add columns as scores for workouts are added)
            columns = ['Userid', 'Name', 'Height', 'Weight', 'Age', 'Countryid',
                       'Country', 'Affiliateid', 'Affiliatename', 'Divisionid', 'Gender',
                       'Overallrank', 'Overallscore', 'PostCompStatus', 'CountryChampion', 
                       str(year)[2:]+'.1_score', str(year)[2:]+'.1_rank',
                       str(year)[2:]+'.2_score', str(year)[2:]+'.2_rank',
                       str(year)[2:]+'.3_score', str(year)[2:]+'.3_rank']
            data = pd.DataFrame(columns=columns)
        
            # Request first page to set things up
            page = 1
            response = get_page(basepath, headers, division[ii], scaled[iii], page)
            npages = response['pagination']['totalPages'] #get the number of pages
            #npages = min(10, npages)
            save = [500,1000,1500,2000,2500,3000,3500,4000,4500]
            # Loop over pages
            for i in range(npages):
                print(i)
                response = get_page(basepath, headers, division[ii], scaled[iii], i+1)
                if response != 'No response':
                    athletes = response['leaderboardRows']
                    nathletes = len(athletes)
                    # Loop over athletes in the page
                    for j in range(nathletes):
                        athlete = athletes[j]
                        #print(athlete)
                        _id = int(athlete['entrant']['competitorId'])
                        name = athlete['entrant']['competitorName']
                        height = athlete_height(athlete['entrant']['height'])
                        weight = athlete_weight(athlete['entrant']['weight'])
                        age = int(athlete['entrant']['age'])
                        ci = athlete['entrant']['countryOfOriginCode']
                        cn = athlete['entrant']['countryOfOriginName']
                        ai = int(athlete['entrant']['affiliateId'])
                        an = athlete['entrant']['affiliateName']
                        di = int(athlete['entrant']['divisionId'])
                        ge = athlete['entrant']['gender']
                        _or = int(athlete['overallRank'])
                        _os = int(athlete['overallScore'])
                        st = athlete['entrant']['postCompStatus']
                        cc = athlete['ui']['countryChampion']
                        
                        # workouts (add columns as scores for workouts are added, also to df below)
                        w1s = workout_score(athlete['scores'][0]['scoreDisplay'], scaled[iii])
                        w1r = workout_rank(w1s, athlete['scores'][0]['rank'])
                        w2s = workout_score(athlete['scores'][1]['scoreDisplay'], scaled[iii])
                        w2r = workout_rank(w2s, athlete['scores'][1]['rank'])
                        w3s = workout_score(athlete['scores'][2]['scoreDisplay'], scaled[iii])
                        w3r = workout_rank(w3s, athlete['scores'][2]['rank'])
                        #w4s = workout_score(athlete['scores'][3]['scoreDisplay'], scaled[iii])
                        #w4r = workout_rank(w4s, athlete['scores'][3]['rank'])
                        #w5s = workout_score(athlete['scores'][4]['scoreDisplay'], scaled[iii])
                        #w5r = workout_rank(w5s, athlete['scores'][4]['rank'])
                        #w6s = workout_score(athlete['scores'][5]['scoreDisplay'], scaled[iii])
                        #w6r = workout_rank(w6s, athlete['scores'][5]['rank'])
                        
                        df = pd.DataFrame([[_id, name, height, weight, age, ci, cn, ai, an,
                                            di, ge, _or, _os, st, cc, w1s, w1r, w2s, w2r, w3s, w3r]], columns=columns)
                        data = data.append(df)
                        
                    if i+1 in save:
                        index = str(save.index(i+1)+1)
                        data = data.reset_index(drop=True)
                        data.to_pickle(ddir+'/'+dname+'_'+index)
                        data.to_csv(path_or_buf=ddir+'/'+dname+'_'+index+'.csv')
                        del data
                        data = pd.DataFrame(columns=columns)
            
            data = data.reset_index(drop=True)
            #print('')
            #print(data)
            index = str(bisect(save,i+1)+1)
            data.to_pickle(ddir+'/'+dname+'_'+index)
            data.to_csv(path_or_buf=ddir+'/'+dname+'_'+index+'.csv')
            
    


    print('')
    print("script took " + str((time.time() - start_time) / 60.0) + " minutes")
    
    
if __name__ == '__main__':
    main()