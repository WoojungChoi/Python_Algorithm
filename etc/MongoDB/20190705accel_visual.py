import pandas as pd
import matplotlib.pyplot as plt
import datetime
import re

accel_df = pd.read_excel('../accel_and_decel_count_add_gps_info_test.xlsx', sheet_name='accel_data')
print(accel_df)
print(accel_df.dtypes)

accel_df_month = accel_df.copy()
accel_df_month['Month'] = accel_df_month['time']
accel_df_month['Month_num'] = accel_df_month['time']
accel_df_month['day'] = 0
accel_df_month['day_num'] = 0

mon_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mon_list_num = [0,1,2,3,4,5,6,7,8,9,10,11,12]
dateStr = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
dateStr_num = [0,1,2,3,4,5,6]

for i in range(len(accel_df_month)):
    year = str(accel_df_month['time'][i])[0:4]
    month = str(accel_df_month['time'][i])[5:7]
    day = str(accel_df_month['time'][i])[8:10]

    accel_df_month['Month'][i] = mon_list[int(month)-1]
    accel_df_month['Month_num'][i] = mon_list_num[int(month)-1]

    date = datetime.date(int(year), int(month), int(day))
    accel_df_month['day'][i] = dateStr[date.weekday()]
    accel_df_month['day_num'][i] = date.weekday()

    print(i)

print(accel_df_month.head())

accel_df_month.to_csv('accel_df_month.csv')
