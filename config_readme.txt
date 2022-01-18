if parameter == 'AirTemp':
        table = 'tblAirTempGauging'
        datetime = 'A_TimeDate'
        column = 'A_Value'
    if parameter == 'Barometer':
        table = 'tblBarometerGauging'
        datetime = 'B_TimeDate'
        column = 'B_Value'

B_TimeDate
B_UTC_Offset
B_Value
B_Est
B_Lock
B_Warning
AutoDTStamp
B_Provisional

    if parameter == 'Conductivity':
        table = 'tblConductivityGauging'
        datetime = 'C_TimeDate'
        column = 'C_Value'

	C_TimeDate
	C_UTC_Offset
	C_Value
	C_ValueCorrected
	C_Est
	C_Lock
	C_Warning

AutoDTSTamp
    if parameter == 'DO':
        table = 'tblDOGauging'
        datetime = 'O_TimeDate'
        column = 'O_DO_Grams'
    if parameter == 'FlowLevel':
        table = 'tblDischargeGauging'
        datetime = 'D_TimeDate'
        column = 'D_Stage'
        D_UTCOffset
	D_Value
	D_Stage
        D_Discharge
        D_Est
        D_Lock
        D_Warning
        AutoDTStamp
        D_Provisional
	observation_type = 2

    if parameter == 'Humidity':
        table = 'tblRelativeHumidityGauging'
        datetime = 'H_TimeDate'
        column = 'H_Value'
    if parameter == 'LakeLevel':
        table = 'tblLakeLevelGauging'
        datetime = 'L_TimeDate'
        column = 'L_Level'

	G_ID
	L_TimeDate
	L_UTCOffset
	L_Value
	L_Level
	L_Est
	L_Lock
	L_Provisional
	L_Warning

AutoDTStamp
    if parameter == 'pH':
        table = 'tblpHGauging'
        datetime = 'pH_TimeDate'
        column = 'pH_ValueCorrected'
    if parameter == 'Piezometer':
        table = 'tblPiezometerGauging'
        datetime = 'P_TimeDate'
        column = 'P_Level'

	P_TimeDate
	P_Value
	P_Level
	P_GallonsPumped
	P_Pump_On
	P_Est
	P_Lock
	P_Warning
	P_Provisional

    if parameter == "Precip":
        table = 'tblRainGauging'
        datetime = 'R_TimeDate'
        column = 'R_Value'
    if parameter == 'SolarRad':
        table = 'tblSolarRadiationGauging'
        datetime = 'S_TimeDate'
        column = 'S_Value'
    if parameter == 'WaterTemp':
        table = 'tblWaterTempGauging'
        datetime = 'W_TimeDate'
        column = 'W_ValueCorrected'
    if parameter == 'Turbidity':
        table = 'tblTurbidityGauging'
        datetime = 'T_TimeDate'
        column = 'T_ValueCorrected'
    if parameter == 'Wind':
        table = 'tblWindSpeedGauging'
        datetime = 'W_TimeDate'
        column = 'Wi_Value'

# Field Observations
# This gets confusing because in gData field observations are stored with metadata, an identifier "FieldVisitID" and stage in "TBLFIELDVISITINFO"
# in gData other parameters are stored in other table
# program calls observations "observation"
# in gData tblFieldVisitInfo stores waterlevel/stage as Stage_Feet

observation  # in gData this stores the metadata and stage,  observations are referenced with "observation_id" which is "FieldVisit_ID" in GData
config_file['observation']
    observation_table = tblFieldVisitInfo
    observation_id = FieldVisit_ID
    site_sql_id  = G_ID
    datetime = Date_Time
    observation_number = Measurement_Number 
    observation_stage = Stage_Feet
    observation_value_table = tblFieldData
    observation_id = FieldVisit_ID
    observation_type = Parameter
    observation_value = Parameter_Value
