#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:53:29 2025

@author: oh
강사님 버전
미세먼지 데이터 분석

"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 미세먼지 데이터
dust = pd.read_excel("./데이터 분석 데이터/환경 관련 데이터/dust.xlsx")
dust.shape # (744, 7)

# 결측치 확인
dust.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 744 entries, 0 to 743
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   날짜      744 non-null    object 
 1   아황산가스   740 non-null    float64
 2   일산화탄소   740 non-null    float64
 3   오존      740 non-null    float64
 4   이산화질소   740 non-null    float64
 5   PM10    725 non-null    float64
 6   PM2.5   739 non-null    float64
dtypes: float64(6), object(1)
memory usage: 40.8+ KB
'''

# 데이터 가공
# 컬럼의 이름을 영문으로 변경
dust.rename(columns = {'날짜' : 'date',
                       '아황산가스' : 'so2',
                       '일산화탄소' : 'co',
                       '오존' : 'o3',
                       '이산화질소' : 'no2'},
               inplace = True)

dust.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 744 entries, 0 to 743
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   date    744 non-null    object 
 1   so2     740 non-null    float64
 2   co      740 non-null    float64
 3   o3      740 non-null    float64
 4   no2     740 non-null    float64
 5   PM10    725 non-null    float64
 6   PM2.5   739 non-null    float64
dtypes: float64(6), object(1)
memory usage: 40.8+ KB
'''

# 날짜 데이터에서 년도-월-일만 추출
dust['date'] = dust['date'].str[:11]

# 날짜 컬럼의 자료형을 날짜형으로 변환
dust['date'] = pd.to_datetime(dust['date'])

# 날짜 칼럼에서 년도, 월, 일을 추출하여 각각 새로운 칼럼으로 추
# 후, 여러 년도로 분석 시 필요할 수 동 있기 때문
dust['year'] = dust['date'].dt.year
dust['month'] = dust['date'].dt.month
dust['day'] = dust['date'].dt.day

dust = dust[['date', 'year', 'month', 'day', 'so2', 'co', 'o3', 'no2', 'PM10', 'PM2.5']]

dust.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 744 entries, 0 to 743
Data columns (total 10 columns):
 #   Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   date    744 non-null    datetime64[ns]
 1   year    744 non-null    int32         
 2   month   744 non-null    int32         
 3   day     744 non-null    int32         
 4   so2     740 non-null    float64       
 5   co      740 non-null    float64       
 6   o3      740 non-null    float64       
 7   no2     740 non-null    float64       
 8   PM10    725 non-null    float64       
 9   PM2.5   739 non-null    float64       
dtypes: datetime64[ns](1), float64(6), int32(3)
memory usage: 49.5 KB
'''

# 데이터 전처리
# 각 컬럼별(변수) 결측치(null) 수 확인
dust.isna().sum()
'''
date      0
year      0
month     0
day       0
so2       4
co        4
o3        4
no2       4
PM10     19
PM2.5     5
dtype: int64
'''
# 결측값을 앞 방향 혹은 뒷 방향으로 채우기
dust = dust.fillna(method='pad')

# 이전값이 없는 경우는 특정수(20)으로 채움
dust.fillna(20, inplace = True)

dust.isna().sum()
'''
date     0
year     0
month    0
day      0
so2      0
co       0
o3       0
no2      0
PM10     0
PM2.5    0
dtype: int64
'''

# 두번째 데이터 불러오기
weather = pd.read_excel("./데이터 분석 데이터/환경 관련 데이터/weather.xlsx")
weather.shape # (743, 7)

weather.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 743 entries, 0 to 742
Data columns (total 7 columns):
 #   Column   Non-Null Count  Dtype         
---  ------   --------------  -----         
 0   지점       743 non-null    int64         
 1   지점명      743 non-null    object        
 2   일시       743 non-null    datetime64[ns]
 3   기온(°C)   743 non-null    float64       
 4   풍속(m/s)  743 non-null    float64       
 5   강수량(mm)  743 non-null    float64       
 6   습도(%)    743 non-null    float64       
dtypes: datetime64[ns](1), float64(4), int64(1), object(1)
memory usage: 40.8+ KB
'''

# 필요없는 열 삭제
weather.drop('지점', axis = 1, inplace = True)
weather.drop('지점명', axis = 1, inplace = True)

# 특수기호가 포함된 컬럼명을 변경
weather.columns = ['date', 'temp', 'wind', 'rain', 'humid']

weather.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 743 entries, 0 to 742
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype         
---  ------  --------------  -----         
 0   date    743 non-null    datetime64[ns]
 1   temp    743 non-null    float64       
 2   wind    743 non-null    float64       
 3   rain    743 non-null    float64       
 4   humid   743 non-null    float64       
dtypes: datetime64[ns](1), float64(4)
memory usage: 29.2 KB
'''

# 미세먼지데이터와 동일한 타입을 만들기 위해서 컬럼 일부 데이터(시간) 제거한 후 , 데이터 타입 변경
weather['date'] = pd.to_datetime(weather['date']).dt.date

# 데이터타입 변경
weather['date'] = weather['date'].astype('datetime64[ns]')

weather.isna().sum()

weather['rain'].value_counts()
'''
rain
0.0    720
0.5      9
1.0      7
1.5      3
2.5      2
2.0      2
Name: count, dtype: int64

0이 많은 이유 :
    기상청에서는 0.1 단위로 강수량을 측정,
    0.1 이하로 비가 내리면 0으로 표시
    따라서 좀 더 세부적인 값을 측정하기 위해
    강수량이 0이면 0.01로
'''
#  강수량이 0이면 0.01로 변환
weather['rain'] = weather['rain'].replace([0], 0.01)
weather['rain'].value_counts()
'''
rain
0.01    720
0.50      9
1.00      7
1.50      3
2.50      2
2.00      2
Name: count, dtype: int64
'''
# 데이터 병합 
# 미세먼지 데이터와 낧씨 데이터를 병합
dust.shape # (744, 10)
weather.shape # (743, 5)

# 미세먼지 데이터와 날씨 데이터의 공통적인 내용이 아닌 행을 제거
dust.drop(index = 743, inplace = True)

# 병합 date 기준으로 머지
df = pd.merge(dust, weather, on = 'date')

# 데이터 분석 및 시각화
# 두 데이터의 모든 요소별 상관 관계
df.corr() #=> 상관

corr = df.corr()
corr['PM10'].sort_values(ascending= False)
'''
PM10     1.000000
PM2.5    0.825433
co       0.529720
no2      0.420554
humid    0.216753
temp     0.175430
so2      0.160874
rain     0.026272
date     0.016124
day      0.016124
wind    -0.108474
o3      -0.348229
year          NaN
month         NaN
Name: PM10, dtype: float64
'''

df.hist(bins = 50, figsize = (20,15))

# 막대 그래프로 시각화 : 일별 미세먼지 평균현황
plt.figure(figsize = (20, 15))
sns.barplot(x = 'day',
            y = 'PM10',
            data = df,
            palette= "Set1")
plt.xticks(rotation = 0)

# 각 요소별 관계를 히트맵으로 시각화
plt.figure(figsize = (15, 12))
sns.heatmap(data = corr, annot = True, fmt = '.2f', cmap = 'hot')
plt.show()

'''결론
pm10, pm2.5, no2, co : 이들은 모두 대기 오염 물질이기에 관련성있음
바람과 오존은 약한 관계성을 가짐
'''

# 산점도를 이용해 온도와 미세먼지 상관관계
plt.figure(figsize = (15, 10))
x = df['temp']
y = df['PM10']
plt.plot(x, y, marker = 'o', linestyle = 'none' , alpha = 0.5)
plt.title('temp - pm10')
plt.xlabel('temp')
plt.ylabel('pm10')

'''결론
온도와 미세먼지는 큰 상관관계가 없어보임
'''

# 산점그래프로 시각화 : 미세먼지와 초미세먼지
plt.figure(figsize = (15, 10))
x = df['PM10']
y = df['PM2.5']
plt.plot(x, y, marker = 'o', linestyle = 'none', color = 'red', alpha = 0.5)
plt.title('pm10 - pm2.5')
plt.xlabel('pm10')
plt.ylabel('pm2.5')

'''결론
미세먼지와 초미세먼지는 선형적인 관계 따라서 관계가 깊다
'''

# 최종결론
# 미세먼지와 초미세먼지는 강한관계성
# 미세먼지 중 대기오염과 관련된 변수들은 관련성이 있다.
# 일산화탄소와 이산화질소는 강한 관계성
# 오존과 바람은 약한 관계성
# 기온과 미세먼지는 무









