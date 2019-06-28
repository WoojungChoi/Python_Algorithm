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

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)

#데이터 변경하기
s1 = pd.Series([1,2,3,4,5,6], index= pd.date_range('20130102', periods=6))
df['F']=s1
df['G']=s1
df['H']=s1

print('\n',df)
df.at[dates[0], 'A']=0
df.iat[0,1]=0
print(df)

#여러 값을 한번에 변경하기
df.loc[:,'D']=np.array([5]*len(df))
print(len(df.T))

#0보다 큰 값들을 음수로 바꾸기
df2 = df.copy()
df2[df2 >0] = -df2
print(df2)

#결측치 처리
#Reindex는 해당 축에 대하여 인덱스를 변경/추가/삭제 할 수 있따. 이는 복사된 데이터프레임을 반환함
print(df)
df1 = df.reindex(index = dates[0:4], columns = list(df.columns) + ['E'])
print('\n\n', df1)
df1.loc[dates[0]:dates[1], 'E'] = 1
print('\n\n', df1)

#결측치가 있는 레코드 떨구기
df1_drop = df1.dropna(how='any')
print('Dropped Na Value\n', df1)

#결측치 채우기
df1_fillna = df1.fillna(value=9.999)
print(df1_fillna)

#결측치 -> True/False
df1_bullna = pd.isna(df1)
print(df1_bullna)


#--------------------------------------------------------------------------------------
#_3.연산(Operations)

#Column을 기준으로 연산
print(df.mean())
#Index를 기준으로 연산
print(df.mean(1))

#index를 축으로 하여 계산하기
s = pd.Series([1,3,5, np.nan, 6,8], index = dates).shift(2)
print('\n\n',s)

df_subindex = df.sub(s, axis = 'index')
print(df_subindex)

#사용자 지정 함수 적용하기
print(df.apply(np.cumsum))
print(df.apply(lambda x: x.max() - x.min()))

#히스토그램
s = pd.Series(np.random.randint(0,7, size = 10))
print(s)
print(s.value_counts())

#문자열 관련 메소드
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog' 'cat'])
print(s.str.lower())

#데이터 쪼개기 잇기
df = pd.DataFrame(np.random.randn(10,4))
print(df)

pieces = [df[:3], df[3:7], df[7:]]
print(pieces)

pd.concat(pieces)
print(pd.concat(pieces))

#Join SQL 스타일의 합치기 기능

left = pd.DataFrame({'key': ['foo' 'foo'], 'lval': [1,2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval':[4,5]})

merged = pd.merge(left, right, on='key')

left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1,2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4,5]})

merged = pd.merge(left, right, on= 'key')

#Append 행 추가하기
df = pd.DataFrame(np.random.randn(8,4), columns=['A', 'B', 'C', 'D'])

s = df.iloc[3]
df.append(s, ignore_index=True)