import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

#--------------------------------------------------------------------------------------
#_1.Data object 생성하기

#pd.Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])

#date_range를 통해 날짜 기간 배열 생성
dates = pd.date_range('20130101', periods =6)

#난수 생성 randn(x행, y열)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns = list('ABCD'))

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3]*4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})

#--------------------------------------------------------------------------------------
#_2.데이터 확인하기

print(df.head(), df.tail())
print(df.values)

#columns별 간단한 통계정보
print(df.describe())

#전치행렬(Transposed matrix)
print(df.T)

#행, 열 Sorting하기
print(df.sort_index(axis=0, ascending=True))
print(df.sort_values(by='B'))


#데이터 선택하기 R이랑 거의 비슷함
print(df['A'])
print(df.A)

print(df[0:3])
print(df['20130102':'20130104'])
print(df['20130102':'20130102'])

print(df.loc[dates[0]])
print(df.loc['20130101'])
print(df.loc[:, ['A','B']])
print(df.loc['20130102':'20130104',['A','B']])
print(df.loc[dates[0], ['A', 'B']])

print(df.at[dates[0], 'A'])
print(df.iloc[[1,2,4],[0,2]])
print(df.iloc[:, 1:3])

#조건을 이용하여 선택하기
print(df[df.A>0])
print(df[df>0])