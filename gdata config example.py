# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:40:16 2022

@author: IHiggins
"""


import pyodbc
import pandas as pd

from datetime import timedelta

import configparser
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import PyPDF2
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=KCITSQLPRNRPX01;'
                      'Database=gData;'
                      'Trusted_Connection=yes;')


config = configparser.ConfigParser()
# config file in working directory, can also add a file extension
# need to be moderatly careful with version control
config.read('gdata_config.ini')

parameter = 'conductivity'
# get gData names from standardized configuration names
# config works with string names
data_type = config['conductivity']["corrected_data"]
# config works with a variable
datetime = config[parameter]["datetime"]
table = config[parameter]["table"]
# site_sql_numeber is g_id
site_sql_number = '1108'

## Time Range
# Start Time
start_time = '10-01-2020'
start_time = pd.to_datetime(start_time) + timedelta(hours=7)

# End Time
end_time = '05-12-2022'
end_time = pd.to_datetime(end_time)+ timedelta(hours=7)

# example 1: get site ID

# You could use tblGaugeLLID to find out if a site is a lakelevel well or ect, but this does take some processing power I dont want to commit to right now
# Gage_Lookup = pd.read_sql_query('select G_ID, SITE_CODE, SITE_NAME, GAGETAG from tblGaugeLLID WHERE G_ID = '+str(SITE_SQL_NUMBER)+';',conn)
site_id_lookup = pd.read_sql_query('select SITE_CODE from tblGaugeLLID WHERE G_ID = '+str(site_sql_number)+';',conn)
site_id = site_id_lookup.to_numpy().reshape(-1)[0]

# example 2: get data
site_df = pd.read_sql_query('select '+str(datetime)+', '+str(data_type)+' from '+str(table)+' WHERE G_ID = '+str(site_sql_number)+' AND '+str(datetime)+' between ? and ?',conn, params=[str(start_time), str(end_time)])
site_df[str(datetime)] = pd.to_datetime(site_df[str(datetime)]) - timedelta(hours=7)
site_df.rename(columns={ site_df.columns[0]: "datetime" }, inplace = True)
site_df.rename(columns={ site_df.columns[1]: site_id }, inplace = True)
    
print(site_df)
