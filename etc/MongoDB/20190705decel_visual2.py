import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns


##히스토그램 생성
def leadtime_histogram(data, title):
    plt.hist(data)
    plt.title(title)
    plt.ylabel('frequency')
    plt.xlabel('leadtime')

accel_df = pd.read_csv('accel_df_month.csv')
decel_df = pd.read_csv('decel_df_month.csv')

print(accel_df.head())
print(decel_df.head())

accel_count = accel_df.ix[::2,['carid', 'Month', 'day']]
decel_count = decel_df.ix[::2,['carid', 'Month', 'day']]

#accel_count.to_csv('accel_count.csv')
#decel_count.to_csv('decel_count.csv')

#columns=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#index = ['513', '1308', '1360', '1365', '1366', '1367', '1368', '1384', '8776', '8791',\
#        '8792', '8804', '11005', '11296', '11325', '11332', '11333', '11359', '21356']

accel_month = pd.DataFrame(accel_count.groupby('Month')['carid'].count())
accel_day = pd.DataFrame(accel_count.groupby('day')['carid'].count())
decel_month = pd.DataFrame(decel_count.groupby('Month')['carid'].count())
decel_day = pd.DataFrame(decel_count.groupby('day')['carid'].count())

#전체 데이터에 대한 값 보여주기
#print('월별 급가속 빈도표\n', accel_month)
#print('요일별 급가속 빈도표\n', accel_day)
#print('월별 급감속 빈도표\n', decel_month)
#print('요일별 급감속 빈도표\n', decel_day)

columns_day = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
columns_month=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
index = ['513', '1308', '1360', '1365', '1366', '1367', '1368', '1384', '8776', '8791',\
        '8792', '8804', '11005', '11296', '11325', '11332', '11333', '11359', '21356']


#시각화
plt.subplot(221)
#plt.bar(columns_day, )
plt.xlabel('Month')
plt.ylabel('Freq. of Accel')

plt.subplot(222)

plt.subplot(223)

plt.subplot(224)
plt.show()


#데이터 매핑?


#accel_group_carid_day = pd.DataFrame(accel_count.groupby(['carid', 'Month']).count().unstack(fill_value=0).stack())
#accel_group_carid_Month =
#print('\n\n\n\n', accel_group_carid_day.head())

'''


plt.hist(accel_count['carid'])
plt.title('Histogram')
plt.ylabel('frequency')
plt.xlabel('Month')

plt.show()


plt.hist(decel_count['carid'])
plt.title('Histogram')
plt.ylabel('frequency')
plt.xlabel('Month')

plt.show()

'''