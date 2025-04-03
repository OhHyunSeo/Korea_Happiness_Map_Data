#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 09:11:04 2025

@author: oh

전처리 끝난 데이터 시각화 및 분석
danawa_data_final_xlsx
"""

# 무선청소리 모델별 비교 분석

import pandas as pd
danawa_data = pd.read_excel("./files/danawa_data_final.xlsx")

# 흡입력 기준 설 : 평균
price_mean_value = danawa_data['가격'].mean()
suction_mean_value = danawa_data['흡입력'].mean()
use_time_mean_value = danawa_data['사용시간'].mean()

# 가성비 좋은 제품 탐색
condition_data = danawa_data[
    (danawa_data['가격'] <= price_mean_value) &
    (danawa_data['흡입력'] >= suction_mean_value) &
    (danawa_data['사용시간'] >= use_time_mean_value)
  ]

condition_data.info()
'''
<class 'pandas.core.frame.DataFrame'>
Index: 18 entries, 0 to 205
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   카테고리    18 non-null     object 
 1   회사명     18 non-null     object 
 2   제품      18 non-null     object 
 3   가격      18 non-null     int64  
 4   사용시간    18 non-null     float64
 5   흡입력     18 non-null     float64
dtypes: float64(2), int64(1), object(3)
memory usage: 1008.0+ bytes
'''
# 데이터 시각화

import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic' 

# 결측값 없애기

condition_data.isna().sum()
'''
카테고리    0
회사명     0
제품      0
가격      0
사용시간    0
흡입력     0
dtype: int64
'''
chart_data = condition_data.dropna(axis = 0)

# 흡입력, 사용시간 최대, 최소
suction_max_value = chart_data['흡입력'].max()
suction_mean_value = chart_data['흡입력'].mean()

use_time_max_value = chart_data['사용시간'].max()
use_time_mean_value = chart_data['사용시간'].mean()

# 성능 시각화

plt.figure(figsize = (20, 10))
plt.title("청소기 성능")

sns.scatterplot(
    x = '흡입력',
    y = '사용시간',
    size = '가격',
    hue = chart_data['회사명'],
    data = chart_data,
    sizes = (10, 1000),
    legend= False)

plt.plot(
    [0, suction_max_value],
    [use_time_mean_value, use_time_mean_value],
    'r--',
    lw = 1)

plt.plot(
    [suction_mean_value, suction_mean_value],
    [0, use_time_max_value],
    'r--',
    lw = 1)

plt.show()

# 인기 제품의 데이터 시각화
chart_data_selected = chart_data[:20]

# 흡입력, 사용시간 최대, 최소
suction_max_value = chart_data_selected['흡입력'].max()
suction_mean_value = chart_data_selected['흡입력'].mean()

use_time_max_value = chart_data_selected['사용시간'].max()
use_time_mean_value = chart_data_selected['사용시간'].mean()

plt.figure(figsize = (20, 10))
plt.title('무선/핸디 청소기 top 20')

sns.scatterplot(x = '흡입력',
                y = '가격',
                hue = chart_data_selected['회사명'],
                data = chart_data_selected,
                sizes = (100, 2000),
                legend= False)

plt.plot([60, suction_max_value],
         [use_time_mean_value, use_time_mean_value],
         'r--',
         lw = 1)

plt.plot([suction_mean_value, suction_mean_value],
         [20, use_time_max_value],
         'r--',
         lw = 1)

for index, row in chart_data_selected.iterrows():
    x = row['흡입력']
    y = row['사용시간']
    s = row['제품'].split(' ')[0]
    plt.text(x, y, s, size = 20)
    
plt.show()






















