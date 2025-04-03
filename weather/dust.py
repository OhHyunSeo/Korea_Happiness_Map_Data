#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:36:08 2025

@author: oh

1. 미세먼지와 초미세먼지의 상관관계
2. 미세먼지 변수 중 대기오염과 관련된 변수
3. 일산화탄소와 이산화질소 관계
4. 오존과 바람 관계
5. 기온과 미세먼지 관계
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

plt.rcParams['font.family'] = 'AppleGothic' 


# 1. 미세먼지와 초미세먼지의 상관관계
dust_df = pd.read_excel("./데이터 분석 데이터/환경 관련 데이터/dust.xlsx")

# 데이터 베이스 길이 확인
len(dust_df) # 744

# 결측치 개수 확인
dust_df.isna().sum()
'''
날짜        0
아황산가스     4
일산화탄소     4
오존        4
이산화질소     4
미세먼지     19
초미세먼지     5
dtype: int64
'''

# 결측치 비율 확인
dust_df.isna().sum() / len(dust_df) * 100
'''
날짜       0.000000
아황산가스    0.537634
일산화탄소    0.537634
오존       0.537634
이산화질소    0.537634
미세먼지     2.553763
초미세먼지    0.672043
dtype: float64
'''

# 결측치의 비율이 5% 미만이므로 해당 행을 삭제후 진행
dust_df.dropna(inplace = True)

# 결측치 제거 확인
dust_df.isna().sum()
'''
날짜       0
아황산가스    0
일산화탄소    0
오존       0
이산화질소    0
미세먼지     0
초미세먼지    0
dtype: int64
'''

# 정보 확인 (결측치 제거전)
dust_df.info()
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

# 결측치 제거후
dust_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
Index: 725 entries, 1 to 743
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   날짜      725 non-null    object 
 1   아황산가스   725 non-null    float64
 2   일산화탄소   725 non-null    float64
 3   오존      725 non-null    float64
 4   이산화질소   725 non-null    float64
 5   미세먼지    725 non-null    float64
 6   초미세먼지   725 non-null    float64
dtypes: float64(6), object(1)
memory usage: 45.3+ KB
'''

# PM10 : 미세먼지, PM2.5 : 초미세먼지
# 위와 같이 칼럼명 변경

dust_df.rename(columns = {'PM10' : '미세먼지',
                         'PM2.5' : '초미세먼지'},
               inplace = True)

# 칼럼 이름 변경 확인
dust_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
Index: 725 entries, 1 to 743
Data columns (total 7 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   날짜      725 non-null    object 
 1   아황산가스   725 non-null    float64
 2   일산화탄소   725 non-null    float64
 3   오존      725 non-null    float64
 4   이산화질소   725 non-null    float64
 5   미세먼지    725 non-null    float64
 6   초미세먼지   725 non-null    float64
dtypes: float64(6), object(1)
memory usage: 45.3+ KB
'''

# 전처리 완료, 분석 시작(시각화)
correlation = dust_df[['미세먼지', '초미세먼지']].corr()
print(correlation)
'''
           미세먼지     초미세먼지
미세먼지   1.000000  0.830959
초미세먼지  0.830959  1.000000
'''
# 미세먼지와 초미세먼지 모두 양의 상관관계와 가까운값을 가지고 있다.

# 산점도 시각화
plt.figure(figsize=(10, 6))
sns.scatterplot(x=dust_df['미세먼지'], y=dust_df['초미세먼지'])

plt.xlabel('미세먼지 (PM10)')
plt.ylabel('초미세먼지 (PM2.5)')
plt.title('미세먼지 vs 초미세먼지 상관관계')
plt.grid(True)

# 시각화 그래프에서 점들이 우상향하므로 양의 상관관계를 가진다고 볼수 있다.
# 즉, 미세먼지가 증가하면 초미세먼지도 동시에 증가하는 경향이 강하다.
# --------------------------------------------------------------------------
# 2. 미세먼지 변수 중 대기오염과 관련된 변수
# 대기오염 관련 변수 상관계수 분석




# --------------------------------------------------------------------------
# 3. 일산화탄소와 이산화질소 관계
# 전처리 완료, 분석 시작(시각화)
correlation = dust_df[['일산화탄소', '이산화질소']].corr()
print(correlation)
'''
          일산화탄소     이산화질소
일산화탄소  1.000000  0.846364
이산화질소  0.846364  1.000000
'''
# 일산화탄소와 이산화질소 역시 미세먼지와 초미세먼지 처럼 밀접한 관계를 가지고 있다.
# -> 양의 상관관계를 가지고 있음

# 산점도 시각화
plt.figure(figsize=(10, 6))
sns.scatterplot(x=dust_df['일산화탄소'], y=dust_df['이산화질소'])

plt.xlabel('일산화탄소')
plt.ylabel('이산화질소')
plt.title('일산화탄소 vs 이산화질소 상관관계')
plt.grid(True)

# 시각화 그래프에서 점들이 우상향하므로 양의 상관관계를 가진다고 볼수 있다.
# 즉, 일산화탄소가 증가하면 이산화질소도 증가하는 경향이 강하다.


# --------------------------------------------------------------------------
# 4. 오존과 바람 관계

# 바람이 있는 데이터프레임 불러오기
weather_df = pd.read_excel("./데이터 분석 데이터/환경 관련 데이터/weather.xlsx")

# 데이터 베이스 길이 확인
len(weather_df) # 743

# 결측치 개수 확인
weather_df.isna().sum()
'''
지점         0
지점명        0
일시         0
기온(°C)     0
풍속(m/s)    0
강수량(mm)    0
습도(%)      0
dtype: int64
'''
# 결측치 없음

# 정보확인
weather_df.info()
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

# dust_df, weather_df merge
# 날짜 칼럼을 기준으로 merge 진행
# 첫번째 데이터프레임 칼럼 : 날짜, 두번째는 일시
# 첫번째 데이터프레임 날짜 칼럼 "2021-01-01 01", 두번 째 "2021.1.1 1:00" (24시간 형식)

# 0:00 -> 24:00 로 변환
def adjust_midnight_time(date_str):
    # '0:00'을 포함하는 경우
    if " 0:" in date_str:
        prev_day = pd.to_datetime(date_str.split(" ")[0], format="%Y-%m-%d") - pd.Timedelta(days=1)
        date_str = prev_day.strftime("%Y.%m.%d") + " 24:00"
    return date_str

weather_df['일시'] = [adjust_midnight_time(date) for date in weather_df['일시']]
# 두번째 데이터프레임의 날짜 컬럼을 첫번째에 맞춤
# 날짜 형식을 변경 

#----

now = datetime.datetime.now()
now_date = now.strftime('%Y-%m-%d %H')

print(now_date)
now_date = now.strftime('%Y-%m-%d %H')



# --------------------------------------------------------------------------
# 5. 기온과 미세먼지 관계















