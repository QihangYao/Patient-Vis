


""" Demo for reading dataset from MIMIC-III in Athena """

from pyathena import connect
from datetime import datetime
import pandas as pd
import numpy as np
import json
import csv


            
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


data1 = pd.read_sql("SELECT  subject_id, COUNT(charttime) AS count_note from NOTEEVENTS GROUP BY subject_id;", conn)
data2 = pd.read_sql("SELECT subject_id, COUNT(charttime) AS count_chart from CHARTEVENTS GROUP BY subject_id;", conn)
data3= pd.read_sql("SELECT subject_id, COUNT(charttime) AS count_lab from LABEVENTS GROUP BY subject_id;", conn)

data= pd.merge(data1,data2, how='left', on=['subject_id'])
data= pd.merge(data,data3, how='left', on=['subject_id'])

print(data1)







export_csv = data.to_csv (r'./test.csv', index = None, header=True) #Don't forget to add '.csv' at the end of the path



    
    
    
    
    
    
    

