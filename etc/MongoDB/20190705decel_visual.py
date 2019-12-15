import pandas as pd
import matplotlib.pyplot as plt
import datetime
import re

decel_df = pd.read_excel('../accel_and_decel_count_add_gps_info_test.xlsx', sheet_name='decel_data')
print(decel_df)
print(decel_df.dtypes)

decel_df_month = decel_df.copy()
decel_df_month['Month'] = decel_df_month['time']
decel_df_month['Month_num'] = decel_df_month['time']
decel_df_month['day'] = 0
decel_df_month['day_num'] = 0

mon_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mon_list_num = [0,1,2,3,4,5,6,7,8,9,10,11,12]
dateStr = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
dateStr_num = [0,1,2,3,4,5,6]

for i in range(len(decel_df_month)):
    year = str(decel_df_month['time'][i])[0:4]
    month = str(decel_df_month['time'][i])[5:7]
    day = str(decel_df_month['time'][i])[8:10]

    decel_df_month['Month'][i] = mon_list[int(month)-1]
    decel_df_month['Month_num'][i] = mon_list_num[int(month)-1]

    date = datetime.date(int(year), int(month), int(day))
    decel_df_month['day'][i] = dateStr[date.weekday()]
    decel_df_month['day_num'][i] = date.weekday()

    print(i)

print(decel_df_month.head())

decel_df_month.to_csv('decel_df_month.csv')
