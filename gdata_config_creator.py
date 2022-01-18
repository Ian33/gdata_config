# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 08:06:05 2022

@author: IHiggins
"""

#import module
import configparser
 
#create configparser object
config_file = configparser.ConfigParser()
 
#define sections and their key and value pairs
config_file["sql_connection"]={
        "Driver": 'SQL Server',
        "Server": 'KCITSQLPRNRPX01',
        "Database": 'gData',
        "Trusted_Connection": 'yes'
        }

# Data is the raw data
# data = raw waterlevel for discharge
# column is the column we are reading when pulling from sql

# corrected_data is the corrected data
# Corrected Data is stage for discharge

# Program used Discharge as discharge file
# Need to convert Discharge to D_Discharge for SQL

# Program uses utc_offset, defined for sql below
# Program uses est, defined for sql below

# Program uses lock, defined for sql below
# Program uses warning, defined for sql below
# Program uses auto_timestamp, defined for sql below
# Program uses provisional, defined for sql below

config_file['AirTemp']={
        "table" : 'tblAirTempGauging',
        "datetime" : 'A_TimeDate',
        "column" : 'A_Value',
        }
config_file['Barometer']={
        "table" : 'tblBarometerGauging',
        "datetime" : 'B_TimeDate',
        "column" : 'B_Value',
        # Barometer doesnt have a data/corrected data column
        # I am calling the B_Value column as both right now
        "data" : "B_Value",
        "corrected_data" : "B_Value",
        "utc_offset" : "B_UTCOffset",
        "est" : "B_Est",
        "lock" : "B_Lock",
        "warning" : "B_Warning",
        "auto_timestamp" : "AutoDTStamp",
        "provisional" : "B_Provisional",
        
        }
config_file['Conductivity']={
        "table" : 'tblConductivityGauging',
        "datetime" : 'C_TimeDate',
        "column" : 'C_Value',
        "data" : "C_Value",
        "corrected_data" : "C_ValueCorrected",
        "utc_offset" : "C_UTCOffset",
        "est" : "D_Est",
        "lock" : "D_Lock",
        "warning" : "D_Warning",
        "auto_timestamp" : "AutoDTStamp",
        }
config_file['DO']={
        "table" : 'tblDOGauging',
        "datetime" : 'O_TimeDate',
        "column" : 'O_DO_Grams',
        }
config_file['FlowLevel']={
        "table" : 'tblDischargeGauging',
        "datetime" : 'D_TimeDate',
        "column" : 'D_Stage',
        "data" : "D_Value",
        "corrected_data" : "D_Stage",
        "discharge" : "D_Discharge",
        "utc_offset" : "UTCOffset",
        "est" : "D_Est",
        "lock" : "D_Lock",
        "warning" : "D_Warning",
        "auto_timestamp" : "AutoDTStamp",
        "provisional" : "D_Provisional",
        "observation_type" : 2
        }
config_file['Humidity']={
        "table" : 'tblRelativeHumidityGauging',
        "datetime" : 'H_TimeDate',
        "column" : 'H_Value',
        }
config_file['LakeLevel']={
        "table" : 'tblLakeLevelGauging',
        "datetime" : 'L_TimeDate',
        "column" : 'L_Level',
        "data" : "L_Value",
        "corrected_data" : "L_Level",
        "utc_offset" : "L_UTCOffset",
        "est" : "L_Est",
        "lock" : "L_Lock",
        "warning" : "L_Warning",
        "auto_timestamp" : "AutoDTStamp",
        "provisional" : "L_Provisional",

        }
config_file['pH']={
        "table" : 'tblpHGauging',
        "datetime" : 'pH_TimeDate',
        "column" : 'pH_ValueCorrected',
        }
config_file['Piezometer']={
        "table" : 'tblPiezometerGauging',
        "datetime" : 'P_TimeDate',
        "column" : 'P_Level',
        
        "data" : "P_Value",
        "corrected_data" : "P_Level",
        "utc_offset" : "P_UTCOffset",
        "est" : "P_Est",
        "lock" : "P_Lock",
        "warning" : "P_Warning",
        "auto_timestamp" : "AutoDTStamp",
        "provisional" : "P_Provisional",
        "gallons_pumped" : "P_GallonsPumped",
        "pump_on" : "P_Pump_On"
        }
config_file["Precip"]={
        "table" : 'tblRainGauging',
        "datetime" : 'R_TimeDate',
        "column" : 'R_Value',
        }
config_file['SolarRad']={
        "table" : 'tblSolarRadiationGauging',
        "datetime" : 'S_TimeDate',
        "column" : 'S_Value',
        }
config_file['WaterTemp']={
        "table" : 'tblWaterTempGauging',
        "datetime" : 'W_TimeDate',
        "column" : 'W_ValueCorrected',
        }
config_file['Turbidity']={
        "table" : 'tblTurbidityGauging',
        "datetime" : 'T_TimeDate',
        "column" : 'T_ValueCorrected',
        }
config_file['Wind']={
        "table" : 'tblWindSpeedGauging',
        "datetime" : 'W_TimeDate',
        "column" : 'Wi_Value',
        }
# Site Identification
config_file['site_identification']={
    "site" : "SITE_CODE",
    "site_sql_id" : "G_ID",
    }

# Field Observations
# This gets confusing because in gData field observations are stored with metadata, an identifier "FieldVisitID" and stage in "TBLFIELDVISITINFO"
# in gData other parameters are stored in other table
# program calls observations "observation"
# in gData tblFieldVisitInfo stores waterlevel/stage as Stage_Feet

config_file['observation']={
    "observation_table" : "tblFieldVisitInfo",
    "observation_value_table" : "tblFieldData",
    "observation_id" : "FieldVisit_ID",
    "site_sql_id" : "G_ID",
    "datetime" : "Date_Time",
    "observation_number" : "Measurement_Number",
    "observation_stage" : "Stage_Feet",
    # these live in observation_values_table -> tblFieldData
    "observation_type" : "Parameter",
    "observation_value" : "Parameter_Value"
    }

# in gData tblFieldData stors other parameter values that are referenced by FieldVIsit_ID and parameter number
# FieldData_ID # this isnt really used by gData



config_file["Education"]={
        "College":"IIITA",
        "Branch" : "IT"
        }
config_file["Favorites"]={
        "Sports": "VolleyBall",
        "Books": "Historical Books"
        }
 
#SAVE CONFIG FILE
with open(r"C:\Users\ihiggins\Cache_gData\Browser_Workup_Config.ini","w") as file_object:
    config_file.write(file_object)
print("Config file 'Browser_Workup_Config.ini' created")
 
#print file content
read_file=open("Browser_Workup_Config.ini","r")
content=read_file.read()
print("content of the config file is:")
print(content)