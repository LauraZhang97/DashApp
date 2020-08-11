import spade
import pandas as pd
import numpy as np 
import datetime

## Node ID
DC_R_nodeid = 15345
LV5_UNIT1_nodeid = 242624
FAL_FALCONG1_nodeid = 15336
EXGNSND_RN_nodeid = 241996
LZ_SOUTH_nodeid = 15171
CHALUP_ALL_nodeid = 261870
RN_SR_WIND1_nodeid = 244256
SIL_SILAS_10_nodeid = 15168
CAMWIND_RN_nodeid = 241985
PALMWI_UNIT1_nodeid = 261094
LV1A_LV1B_nodeid = 34737
REDFISH_ALL_nodeid = 24734
MIRASOLE_GEN_nodeid = 244418
CABEZON_ALL_nodeid = 255975
LV3_UNIT1_nodeid = 244412
LV4_UNIT_1_nodeid = 243505
MESTENO_RN_nodeid = 261137
BORDAS_345_nodeid = 244413
DUKE_GST1CCU_nodeid = 15447
NED_NEDIN_G1_nodeid = 15262

## Zone ID
DC_R_zoneid = 1700
LV5_UNIT1_zoneid = 390
FAL_FALCONG1_zoneid = 1700
EXGNSND_RN_zoneid = 390
LZ_SOUTH_zoneid = 390
CHALUP_ALL_zoneid = 390
RN_SR_WIND1_zoneid = 390
SIL_SILAS_10_zoneid = 1700
CAMWIND_RN_zoneid = 390
PALMWI_UNIT1_zoneid = 390
LV1A_LV1B_zoneid = 388
REDFISH_ALL_zoneid = 390
MIRASOLE_GEN_zoneid = 390
CABEZON_ALL_zoneid = 390
LV3_UNIT1_zoneid = 390
LV4_UNIT_1_zoneid = 390
MESTENO_RN_zoneid = 390
BORDAS_345_zoneid = 390
DUKE_GST1CCU_zoneid = 1700
NED_NEDIN_G1_zoneid = 1700

## Get LMP data
def getLMPData(start_date, end_date, node_id, zone_id):
    lmpData_RT = spade.sesco.series.get_prices(iso_id = 9, start_date = start_date, end_date = end_date,
                                               ignore_cache = True)
    lmpData_RT = lmpData_RT.loc[(lmpData_RT['NODE_ID'] == node_id) & 
                                (lmpData_RT['ZONE_ID'] == zone_id)].groupby('DATETIME').last()['RT_LMP']

    lmpData_DA = spade.sesco.series.get_prices(iso_id = 9, start_date = start_date, end_date = end_date, da = True,
                                               ignore_cache = True)
    lmpData_DA = lmpData_DA.loc[(lmpData_DA['NODE_ID'] == node_id) & 
                                (lmpData_DA['ZONE_ID'] == zone_id)].groupby('DATETIME').last()['DA_LMP']
    return lmpData_RT, lmpData_DA


DC_R_LMP_rt, DC_R_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = DC_R_nodeid, zone_id = DC_R_zoneid)
LV5_UNIT1_LMP_rt, LV5_UNIT1_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = LV5_UNIT1_nodeid, zone_id = LV5_UNIT1_zoneid)
FAL_FALCONG1_LMP_rt, FAL_FALCONG1_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = FAL_FALCONG1_nodeid, zone_id = FAL_FALCONG1_zoneid)
EXGNSND_RN_LMP_rt, EXGNSND_RN_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = EXGNSND_RN_nodeid, zone_id = EXGNSND_RN_zoneid)
LZ_SOUTH_LMP_rt, LZ_SOUTH_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = LZ_SOUTH_nodeid, zone_id = LZ_SOUTH_zoneid)
CHALUP_ALL_LMP_rt, CHALUP_ALL_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = CHALUP_ALL_nodeid, zone_id = CHALUP_ALL_zoneid)
RN_SR_WIND1_LMP_rt, RN_SR_WIND1_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = RN_SR_WIND1_nodeid, zone_id = RN_SR_WIND1_zoneid)
SIL_SILAS_10_LMP_rt, SIL_SILAS_10_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = SIL_SILAS_10_nodeid, zone_id = SIL_SILAS_10_zoneid)
CAMWIND_RN_LMP_rt, CAMWIND_RN_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = CAMWIND_RN_nodeid, zone_id = CAMWIND_RN_zoneid)
PALMWI_UNIT1_LMP_rt, PALMWI_UNIT1_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = PALMWI_UNIT1_nodeid, zone_id = PALMWI_UNIT1_zoneid)
LV1A_LV1B_LMP_rt, LV1A_LV1B_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = LV1A_LV1B_nodeid, zone_id = LV1A_LV1B_zoneid)
REDFISH_ALL_LMP_rt, REDFISH_ALL_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = REDFISH_ALL_nodeid, zone_id = REDFISH_ALL_zoneid)
MIRASOLE_GEN_LMP_rt, MIRASOLE_GEN_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = MIRASOLE_GEN_nodeid, zone_id = MIRASOLE_GEN_zoneid)
CABEZON_ALL_LMP_rt, CABEZON_ALL_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = CABEZON_ALL_nodeid, zone_id = CABEZON_ALL_zoneid)
LV3_UNIT1_LMP_rt, LV3_UNIT1_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = LV3_UNIT1_nodeid, zone_id = LV3_UNIT1_zoneid)
LV4_UNIT_1_LMP_rt, LV4_UNIT_1_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = LV4_UNIT_1_nodeid, zone_id = LV4_UNIT_1_zoneid)
MESTENO_RN_LMP_rt, MESTENO_RN_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = MESTENO_RN_nodeid, zone_id = MESTENO_RN_zoneid)
BORDAS_345_LMP_rt, BORDAS_345_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = BORDAS_345_nodeid, zone_id = BORDAS_345_zoneid)
DUKE_GST1CCU_LMP_rt, DUKE_GST1CCU_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = DUKE_GST1CCU_nodeid, zone_id = DUKE_GST1CCU_zoneid)
NED_NEDIN_G1_LMP_rt, NED_NEDIN_G1_LMP_da = getLMPData(start_date = '2020-1-1', end_date = '2020-8-6', node_id = NED_NEDIN_G1_nodeid, zone_id = NED_NEDIN_G1_zoneid)


LMP_df = pd.DataFrame(columns = ['Source', 'Sink', 'HE', 'Date','DA', 'RT'])
LMP_temp = pd.DataFrame(columns = ['Source', 'Sink', 'HE', 'Date','DA', 'RT'])

LMP_df['HE'] = DC_R_LMP_rt.index.hour
LMP_df['Date'] = DC_R_LMP_rt.index.date
LMP_df['Source'] = 'DC_R'
LMP_df['Sink'] = 'LV5_UNIT1'
LMP_df['DA'] = LV5_UNIT1_LMP_da.values - DC_R_LMP_da.values
LMP_df['RT'] = LV5_UNIT1_LMP_rt.values - DC_R_LMP_rt.values

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'PALMWI_UNI1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DC_R_LMP_rt.index.hour
LMP_temp['Date'] = DC_R_LMP_rt.index.date
LMP_temp['Source'] = 'DC_R'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - DC_R_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - DC_R_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'PALMWI_UNI1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV5_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV5_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV5_UNIT1'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - LV5_UNIT1_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - LV5_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'PALMWI_UNI1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = FAL_FALCONG1_LMP_rt.index.hour
LMP_temp['Date'] = FAL_FALCONG1_LMP_rt.index.date
LMP_temp['Source'] = 'FAL_FALCONG1'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - FAL_FALCONG1_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - FAL_FALCONG1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'PALMWI_UNI1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = EXGNSND_RN_LMP_rt.index.hour
LMP_temp['Date'] = EXGNSND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'EXGNSND_RN'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - EXGNSND_RN_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - EXGNSND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'PALMWI_UNI1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LZ_SOUTH_LMP_rt.index.hour
LMP_temp['Date'] = LZ_SOUTH_LMP_rt.index.date
LMP_temp['Source'] = 'LZ_SOUTH'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - LZ_SOUTH_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - LZ_SOUTH_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'PALMWI_UNI1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = RN_SR_WIND1_LMP_rt.index.hour
LMP_temp['Date'] = RN_SR_WIND1_LMP_rt.index.date
LMP_temp['Source'] = 'RN_SR_WIND1'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - RN_SR_WIND1_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - RN_SR_WIND1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'PALMWI_UNI1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = SIL_SILAS_10_LMP_rt.index.hour
LMP_temp['Date'] = SIL_SILAS_10_LMP_rt.index.date
LMP_temp['Source'] = 'SIL_SILAS_10'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - SIL_SILAS_10_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - SIL_SILAS_10_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'PALMWI_UNI1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CAMWIND_RN_LMP_rt.index.hour
LMP_temp['Date'] = CAMWIND_RN_LMP_rt.index.date
LMP_temp['Source'] = 'CAMWIND_RN'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - CAMWIND_RN_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - CAMWIND_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = PALMWI_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = PALMWI_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'PALMWI_UNIT1'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - PALMWI_UNIT1_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - PALMWI_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV1A_LV1B_LMP_rt.index.hour
LMP_temp['Date'] = LV1A_LV1B_LMP_rt.index.date
LMP_temp['Source'] = 'LV1A_LV1B'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - LV1A_LV1B_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - LV1A_LV1B_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = REDFISH_ALL_LMP_rt.index.hour
LMP_temp['Date'] = REDFISH_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'REDFISH_ALL'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - REDFISH_ALL_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - REDFISH_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MIRASOLE_GEN_LMP_rt.index.hour
LMP_temp['Date'] = MIRASOLE_GEN_LMP_rt.index.date
LMP_temp['Source'] = 'MIRASOLE_GEN'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - MIRASOLE_GEN_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - MIRASOLE_GEN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = CABEZON_ALL_LMP_rt.index.hour
LMP_temp['Date'] = CABEZON_ALL_LMP_rt.index.date
LMP_temp['Source'] = 'CABEZON_ALL'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - CABEZON_ALL_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - CABEZON_ALL_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV3_UNIT1_LMP_rt.index.hour
LMP_temp['Date'] = LV3_UNIT1_LMP_rt.index.date
LMP_temp['Source'] = 'LV3_UNIT1'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - LV3_UNIT1_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - LV3_UNIT1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = LV4_UNIT_1_LMP_rt.index.hour
LMP_temp['Date'] = LV4_UNIT_1_LMP_rt.index.date
LMP_temp['Source'] = 'LV4_UNIT_1'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - LV4_UNIT_1_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - LV4_UNIT_1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = MESTENO_RN_LMP_rt.index.hour
LMP_temp['Date'] = MESTENO_RN_LMP_rt.index.date
LMP_temp['Source'] = 'MESTENO_RN'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - MESTENO_RN_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - MESTENO_RN_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = BORDAS_345_LMP_rt.index.hour
LMP_temp['Date'] = BORDAS_345_LMP_rt.index.date
LMP_temp['Source'] = 'BORDAS_345'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - BORDAS_345_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - BORDAS_345_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = DUKE_GST1CCU_LMP_rt.index.hour
LMP_temp['Date'] = DUKE_GST1CCU_LMP_rt.index.date
LMP_temp['Source'] = 'DUKE_GST1CCU'
LMP_temp['Sink'] = 'NED_NEDIN_G1'
LMP_temp['DA'] = NED_NEDIN_G1_LMP_da.values - DUKE_GST1CCU_LMP_da.values
LMP_temp['RT'] = NED_NEDIN_G1_LMP_rt.values - DUKE_GST1CCU_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

############################################################################

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'DC_R'
LMP_temp['DA'] = DC_R_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = DC_R_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'LV5_UNIT1'
LMP_temp['DA'] = LV5_UNIT1_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = LV5_UNIT1_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'FAL_FALCONG1'
LMP_temp['DA'] = FAL_FALCONG1_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = FAL_FALCONG1_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'EXGNSND_RN'
LMP_temp['DA'] = EXGNSND_RN_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = EXGNSND_RN_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'LZ_SOUTH'
LMP_temp['DA'] = LZ_SOUTH_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = LZ_SOUTH_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'RN_SR_WIND1'
LMP_temp['DA'] = RN_SR_WIND1_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = RN_SR_WIND1_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'SIL_SILAS_10'
LMP_temp['DA'] = SIL_SILAS_10_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = SIL_SILAS_10_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'CAMWIND_RN'
LMP_temp['DA'] = CAMWIND_RN_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = CAMWIND_RN_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'PALMWI_UNIT1'
LMP_temp['DA'] = PALMWI_UNIT1_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = PALMWI_UNIT1_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'LV1A_LV1B'
LMP_temp['DA'] = LV1A_LV1B_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = LV1A_LV1B_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'REDFISH_ALL'
LMP_temp['DA'] = REDFISH_ALL_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = REDFISH_ALL_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'MIRASOLE_GEN'
LMP_temp['DA'] = MIRASOLE_GEN_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = MIRASOLE_GEN_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'CABEZON_ALL'
LMP_temp['DA'] = CABEZON_ALL_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = CABEZON_ALL_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'LV3_UNIT1'
LMP_temp['DA'] = LV3_UNIT1_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = LV3_UNIT1_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'LV4_UNIT_1'
LMP_temp['DA'] = LV4_UNIT_1_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = LV4_UNIT_1_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'MESTENO_RN'
LMP_temp['DA'] = MESTENO_RN_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = MESTENO_RN_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'BORDAS_345'
LMP_temp['DA'] = BORDAS_345_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = BORDAS_345_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)

LMP_temp['HE'] = NED_NEDIN_G1_LMP_rt.index.hour
LMP_temp['Date'] = NED_NEDIN_G1_LMP_rt.index.date
LMP_temp['Source'] = 'NED_NEDIN_G1'
LMP_temp['Sink'] = 'DUKE_GST1CCU'
LMP_temp['DA'] = DUKE_GST1CCU_LMP_da.values - NED_NEDIN_G1_LMP_da.values
LMP_temp['RT'] = DUKE_GST1CCU_LMP_rt.values - NED_NEDIN_G1_LMP_rt.values
LMP_df = LMP_df.append(LMP_temp, ignore_index = True)


LMP_df['Return'] = LMP_df['RT'] / LMP_df['DA']
LMP_df['HE'] = LMP_df['HE'] + 1
LMP_df = LMP_df.astype({'Source': 'str', 'Sink':'str', 'HE': 'str', 'Date': 'str'})



import os
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime as dt
from dash.dependencies import Input, Output, State, ALL, MATCH
import dash_table

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.Div(children = [
        html.Button('Add', id = 'Add', n_clicks = 0)
    ]),
    html.Div(id = 'dropdown-container', children = [])
])


@app.callback(
    Output('dropdown-container', 'children'),
    [Input('Add', 'n_clicks')],
    [State('dropdown-container', 'children')]
)
def display_dropdown(n_clicks, children):
    new_element = html.Div(
        children = [
            html.Div([
                dcc.Dropdown(
                    id = {'type': 'dynamic-dropdown-source',
                          'index': n_clicks},
                    options = [{'label': i, 'value': i} for i in LMP_df['Source'].unique()],
                    placeholder = 'Source'
                )
            ],
            style = {'width': '20%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    id = {'type': 'dynamic-dropdown-sink',
                          'index': n_clicks},
                    options = [{'label': i, 'value': i} for i in LMP_df['Sink'].unique()],
                    placeholder = 'Sink'
                )
            ],
            style = {'width': '20%', 'display': 'inline-block'}),

            html.Div([
                dcc.Dropdown(
                    id = {'type': 'dynamic-dropdown-HE',
                          'index': n_clicks},
                    options = [{'label': i, 'value': i} for i in LMP_df['HE'].unique()],
                    placeholder = 'HE'
                )
            ],
            style = {'width': '20%', 'display': 'inline-block'}),

            html.Div([
                dcc.DatePickerSingle(
                    id = {'type': 'dynamic-dropdown-date',
                          'index': n_clicks},
                    date = dt(2020, 1, 1),
                    placeholder = 'Date'
                )
            ],
            style = {'width': '20%', 'display': 'inline-block'}),

            html.Div([
                dash_table.DataTable(
                    id = {'type': 'dropdown-container-output',
                          'index': n_clicks},
                    #data = LMP_df.to_dict('records'),
                    columns = [
                        {'id': 'Source', 'name': 'Source', 'presentation': 'dropdown'},
                        {'id': 'Sink', 'name': 'Sink', 'presentation': 'dropdown'},
                        {'id': 'HE', 'name': 'HE', 'presentation': 'dropdown'},
                        {'id': 'Date', 'name': 'Date', 'presentation': 'dropdown'},
                        {'id': 'DA', 'name': 'DA'},
                        {'id': 'RT', 'name': 'RT'},
                        {'id': 'Return', 'name': 'Return'}
                    ],
                    editable = False
                )
            ]) 
        ]
    )
    
    children.append(new_element)
    return children

@app.callback(
    Output({'type': 'dropdown-container-output', 'index': MATCH}, 'data'),
    [Input({'type': 'dynamic-dropdown-source', 'index': MATCH}, 'value'),
     Input({'type': 'dynamic-dropdown-sink', 'index': MATCH}, 'value'),
     Input({'type': 'dynamic-dropdown-HE', 'index': MATCH}, 'value'),
     Input({'type': 'dynamic-dropdown-date', 'index': MATCH}, 'date')]
)
def update_data(source_name, sink_name, HE_value, date):
    LMP_dff = LMP_df[(LMP_df['Source'] == source_name) &
                     (LMP_df['Sink'] == sink_name) &
                     (LMP_df['HE'] == HE_value) &
                     (LMP_df['Date'] == date)]
    return LMP_dff.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug = True)