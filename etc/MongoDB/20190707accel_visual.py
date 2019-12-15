import pandas as pd
import matplotlib.pyplot as plt
import datetime
import re
import numpy as np

accel_df = pd.read_csv('accel_df_month.csv')
#decel_df = pd.read_csv('decel_df_month.csv')
print(accel_df)
print(accel_df.dtypes)
accel_id_list = list(accel_df['carid'].drop_duplicates())
#decel_id_list = list(decel_df['carid'].drop_duplicates())

mon_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
dateStr = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

accel_id_mon_count = pd.DataFrame(0, index=accel_id_list, columns=mon_list)
accel_id_day_count = pd.DataFrame(0, index=accel_id_list, columns=dateStr)

#decel_id_mon_count = pd.DataFrame(0, index=decel_id_list, columns=mon_list)
#decel_id_day_count = pd.DataFrame(0, index=decel_id_list, columns=dateStr)

for i in range(len(accel_df)):
    carid = accel_df.loc[i:i , ['carid']]
    Month = accel_df.loc[i:i , ['Month_num']]
    day = accel_df.loc[i:i , ['day_num']]

    print('carid: ', carid, '\nMonth: ', Month, '\nday: ', day)
    print(accel_id_mon_count.loc[[carid], [Month]])
    print(accel_id_mon_count.loc[[carid], [day]])
    accel_id_mon_count.loc[[carid], [Month]] += 1
    accel_id_day_count.loc[[carid], [day]] += 1

print(accel_id_mon_count.head())
