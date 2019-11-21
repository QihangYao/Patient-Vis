# -*- coding: utf-8 -*-


""" Demo for reading dataset from MIMIC-III in Athena """

from pyathena import connect
from datetime import datetime
import pandas as pd
import numpy as np
import json


def line_todict(line, col_names):
    new_dict = dict()
    for i in range(len(line)):
        new_dict[col_names[i]] = line[i]
    return new_dict

def nest_convert(df):
    result = []
    col_names = df.columns.values
    for line in df.values:
        new_dict = line_todict(line, col_names)
        result.append(new_dict)
    return result

def time_reform(df, col_name):
    arr = []
    tt = df[col_name]
    indices= tt.index
    for i in range(len(indices)):
        if(isinstance(tt[indices[i]], pd._libs.tslibs.timestamps.Timestamp)):
            val = tt[indices[i]].strftime('%Y-%m-%d %H:%M:%S')
        else:
            val = ''
        arr.append(val)
        
    series=pd.Series(arr)
    series.index = indices
    df.pop(col_name)
    df.insert(0, col_name, series)
            
aws_access_key_id = "AKIAUXPGEYVLHD4JGCSV"
aws_secret_access_key = "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"
s3_staging_dir = "s3://mimiciii-query-result/"
region_name = "us-east-1"

conn = connect(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    s3_staging_dir=s3_staging_dir,
    region_name=region_name,
    schema_name="mimiciii",
)
# Example SQL
subject_id = '222'
patient_data = pd.read_sql("SELECT subject_id, gender, dob from PATIENTS where subject_id=" + subject_id, conn)
admission_data = pd.read_sql("SELECT subject_id, hadm_id, diagnosis, ethnicity FROM ADMISSIONS where subject_id=" + subject_id, conn) #HADM_ID
patient_data = patient_data.dropna()
admission_data = admission_data.dropna()

#print(admission_data)
note_data = pd.read_sql("SELECT subject_id, hadm_id, category, text, charttime from NOTEEVENTS where subject_id=" + subject_id, conn)
note_data = note_data.dropna()
note_data['timestamp'] = note_data.charttime.values.astype(np.int64) // 10 ** 9

chart_data = pd.read_sql("SELECT subject_id, hadm_id, itemid, charttime as chart_time, valuenum as value_num from CHARTEVENTS where subject_id=" + subject_id, conn)
d_items = pd.read_sql("SELECT itemid, label as key from D_ITEMS", conn)
chart_data = pd.merge(chart_data, d_items, how='left', on=['itemid'])
chart_data = chart_data.dropna()
chart_data['timestamp'] = chart_data.chart_time.values.astype(np.int64) // 10 ** 9
chart_data['category'] = 'Vitals'

lab_data = pd.read_sql("SELECT subject_id, hadm_id, itemid, charttime as chart_time, value, valuenum as value_num FROM LABEVENTS  where subject_id=" + subject_id, conn)
d_labitems = pd.read_sql("SELECT itemid, label as key FROM D_LABITEMS", conn)  
lab_data = pd.merge(lab_data, d_labitems, how='left', on=['itemid'])
lab_data = lab_data.dropna()
lab_data['timestamp'] = lab_data.chart_time.values.astype(np.int64) // 10 ** 9
lab_data['category'] = 'Labs'

hadm_id = 103002
temp_add = admission_data.loc[admission_data['hadm_id']==hadm_id]
temp_note = note_data.loc[note_data['hadm_id']==hadm_id]
temp_vital = chart_data.loc[chart_data['hadm_id']==hadm_id]
temp_lab = lab_data.loc[lab_data['hadm_id']==hadm_id]

time_reform(patient_data, 'dob')
time_reform(temp_note, 'charttime')
time_reform(temp_vital, 'chart_time')
time_reform(temp_lab, 'chart_time')


patient_dict = line_todict(patient_data.values[0], patient_data.columns.values)
admission_dict = line_todict(temp_add.values[0], temp_add.columns.values)
patient_dict.update(admission_dict)

note_list = nest_convert(temp_note)
vital_list = nest_convert(temp_vital)
lab_list = nest_convert(temp_lab)
events = vital_list + lab_list
patient_dict['notes'] = note_list
patient_dict['events'] = events

patient_dict['patient_dict'] = True

filename = 'test3.json'
with open(filename, 'w', encoding='UTF-8') as f:
    json.dump(patient_dict, f, ensure_ascii=False)
#patient_data = pd.concat([patient_data, temp_add], axis = 1)


    
    
    
    
    
    
    
    
    