#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:30:19 2025

@author: oh
"""
'''
7개의 엑셀 파일을 병합

시도별 행복 지수 요소별 시각화 : 선그래프
행복 지수 요소별 각각 시각화 : 막대 그래프(서브플롯 사용)
행복 지수 요소간의 상관관계 시각화 : 히트맵	

결론 도출
'''

# 필요 모듈 임포트
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# 데이터 일괄 로딩
health_df = pd.read_excel("./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_건강.xlsx")
eco_df = pd.read_excel("./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_경제.xlsx")
rel_df = pd.read_excel("./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_관계및사회참여.xlsx")
edu_df = pd.read_excel("./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_교육.xlsx")
life_df = pd.read_excel("./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_삶의만족도.xlsx")
safe_df = pd.read_excel("./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_안전.xlsx")
les_df = pd.read_excel("./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_여가.xlsx")
env_df = pd.read_excel("./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_환경.xlsx")
#-----------------------------------

# 평균값 계산
health_df_mean = health_df['평균'].mean()

average_df_health = health_df.groupby('시도', as_index=False)['평균'].mean()
print(average_df_health)

average_df_health.rename(columns = {'평균' : '평균_건강'},inplace = True)

average_df_health.columns
#------------------
eco_df_mean = eco_df['평균'].mean()

average_df_eco = eco_df.groupby('시도', as_index=False)['평균'].mean()
print(average_df_eco)

average_df_eco.rename(columns = {'평균' : '평균_경제'},inplace = True)


average_df_eco.columns
#--------------------
rel_df_mean = rel_df['평균'].mean()

average_df_rel = rel_df.groupby('시도', as_index=False)['평균'].mean()
print(average_df_rel)

average_df_rel.rename(columns = {'평균_경제' : '평균_관계및사회참여'},inplace = True)


average_df_rel.columns
#--------------------
edu_df_mean = edu_df['평균'].mean()

average_df_edu = edu_df.groupby('시도', as_index=False)['평균'].mean()
print(average_df_edu)

average_df_edu.rename(columns = {'평균' : "평균_교육"},inplace = True)


average_df_edu.columns
#--------------------
life_df_mean = life_df['삶의 만족도'].mean()

average_df_life = life_df.groupby('시도', as_index=False)['삶의 만족도'].mean()
print(average_df_life)

average_df_life.rename(columns = {'삶의 만족도' : "평균_삶의만족도"},inplace = True)


average_df_life.columns
#--------------------
safe_df_mean = safe_df['평균'].mean()

average_df_safe = safe_df.groupby('시도', as_index=False)['평균'].mean()
print(average_df_safe)

average_df_safe.rename(columns = {'평균' : "평균_안전"},inplace = True)


average_df_safe.columns
#--------------------
les_df_mean = les_df['평균'].mean()

average_df_les = les_df.groupby('시도', as_index=False)['평균'].mean()
print(average_df_les)

average_df_les.rename(columns = {'평균' : "평균_여가"},inplace = True)


average_df_les.columns

#--------------------
les_df_mean = les_df['평균'].mean()

average_df_env = env_df.groupby('시도', as_index=False)['평균'].mean()
print(average_df_env)

average_df_env.rename(columns = {'평균' : "평균_환경"},inplace = True)


average_df_env.columns
# -----------------------------------
# 머지

merged_df = average_df_health.merge(average_df_eco, on="시도", how="outer") \
                             .merge(average_df_rel, on="시도", how="outer") \
                             .merge(average_df_edu, on="시도", how="outer") \
                             .merge(average_df_life, on="시도", how="outer") \
                             .merge(average_df_safe, on="시도", how="outer") \
                             .merge(average_df_les, on="시도", how="outer") \
                             .merge(average_df_env, on="시도", how="outer")

# 병합된 데이터 확인
print(merged_df.head())

plt.rcParams['font.family'] = 'AppleGothic'


# 시도별 행복 지수 요소 선 그래프
plt.figure(figsize=(12, 6))

for column in merged_df.columns[1:]:  # '시도' 제외한 나머지 열을 그래프에 추가
    plt.plot(merged_df['시도'], merged_df[column], marker='o', label=column)

plt.xticks(rotation=45)
plt.xlabel("시도")
plt.ylabel("행복 지수")
plt.title("시도별 행복 지수 요소 비교")
plt.grid(True)
plt.show()


import numpy as np

# 서브플롯을 위한 설정
fig, axes = plt.subplots(4, 2, figsize=(15, 15))  # 4행 2열 서브플롯
axes = axes.flatten()  # 8개의 서브플롯을 1차원 배열로 변환

for i, column in enumerate(merged_df.columns[1:]):  # '시도' 제외한 나머지 열
    axes[i].bar(merged_df['시도'], merged_df[column], color=np.random.rand(3,))
    axes[i].set_title(column)
    axes[i].set_xticklabels(merged_df['시도'], rotation=45)

plt.tight_layout()
plt.show()


import seaborn as sns

# '시도' 제외한 데이터만 사용하여 상관관계 계산
corr_matrix = merged_df.iloc[:, 1:].corr()

# 히트맵 생성
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("행복 지수 요소 간의 상관관계")
plt.show()

















# -----------------------------------
# 데이터 병합을 위해 각각의 info 확인
# 1. 건강 데이터 확인
list(health_df.columns)
'''
['No',
 '시도',
 '구군',
 '평균',
 '주관적 건강수준 인지율',
 '인구 십만명당 정신건강증진기관 수',
 '인구 천명당 의료기관 종사 의사수',
 '건강생활실천율',
 '인구 천명당 의료기관병상수']
'''
# 2. 경제 데이터 확인
list(eco_df.columns)
'''
['No',
 '시도',
 '구군',
 '평균',
 '1인당 지역내총생산(GRDP)',
 '인구 천명당 사업체수',
 '인구 천명당 종사자수',
 '국민기초생활보장 수급자비율 a)',
 '종사자 천명당 영세자영업자 수 a)']
'''
# 3. 관계및사회참여 데이터 확인
list(rel_df.columns)
'''
['No',
 '시도',
 '구군',
 '평균',
 '인구 십만명당 자살률 a)',
 '1인가구(독거노인 제외) 비율 a)',
 '독거노인가구 비율 a)',
 '인구 십만명당 사회적기업수',
 '가족관계 만족도 b)']
'''
# 4. 교육 데이터 컬럼 확인
list(edu_df.columns)
'''
['No',
 '시도',
 '구군',
 '평균',
 '교원 1인당 학생수',
 '영유아 천명당 보육시설 수',
 '인구 십만명당 학교수',
 '인구 천명당 사설학원수']
'''

# 5. 삶의 만족도 컬럼 확인
list(life_df.columns)
'''
['No', '시도', '구군', '삶의 만족도']
'''

# 6. 안전 
list(safe_df.columns)
'''
['No',
 '시도',
 '구군',
 '평균',
 '사회안전에 대한 인식 b)',
 '인구 천명당 cctv 대수 b)',
 '인구 십만명당 응급의료기관 및 응급실 운영기관수',
 '단위면적당 지역경찰관서 수',
 "지역안전등급 현황 중 '교통사고 및 화재' a)"]
'''

# 7. 여가
list(les_df.columns)
'''
['No',
 '시도',
 '구군',
 '평균',
 '여가활용 만족도 b)',
 '노인 천명당 노인여가복지시설수',
 '인구 십만명당 도서관수',
 '인구 십만명당 문화기반시설수',
 '인구 천명당 체육관련 여가시설수']
'''

# 8 환경
list(env_df.columns)
'''
['No',
 '시도',
 '구군',
 '평균',
 '환경체감도 b)',
 '인구 천명당 1일 산업폐수 방류량 a)',
 "도시지역 중 '녹지지역 비율'",
 '미세먼지(PM2.5) a) b)',
 '주민 1인당 생활폐기물배출량 a)']
'''
# 머지할 때 사용할 키값 선택
# -> 구군을 키로 사용, 전에 삶의 데이터에서 칼럼값 변경후 머지
life_df.rename(columns = {'삶의 만족도' : '평균'},inplace = True)

# 데이터프레임에서 평균 열을 제외하고 모두 삭제


health_df_edit = health_df.drop(['주관적 건강수준 인지율', 
                                 '인구 십만명당 정신건강증진기관 수', 
                                 '인구 천명당 의료기관 종사 의사수',
                                 '건강생활실천율',
                                 '인구 천명당 의료기관병상수'], axis=1)

eco_df_edit = eco_df.drop(['1인당 지역내총생산(GRDP)',
                           '인구 천명당 사업체수',
                           '인구 천명당 종사자수',
                           '국민기초생활보장 수급자비율 a)',
                           '종사자 천명당 영세자영업자 수 a)'], axis=1)

rel_df_edit = rel_df.drop(['인구 십만명당 자살률 a)',
                           '1인가구(독거노인 제외) 비율 a)',
                           '독거노인가구 비율 a)',
                           '인구 십만명당 사회적기업수',
                           '가족관계 만족도 b)'], axis = 1)

edu_df_edit = edu_df.drop(['교원 1인당 학생수',
                      '영유아 천명당 보육시설 수',
                      '인구 십만명당 학교수',
                      '인구 천명당 사설학원수'], axis = 1)

life_df_edit = life_df

safe_df_edit = safe_df.drop(['사회안전에 대한 인식 b)',
                             '인구 천명당 cctv 대수 b)',
                             '인구 십만명당 응급의료기관 및 응급실 운영기관수',
                             '단위면적당 지역경찰관서 수',
                             "지역안전등급 현황 중 '교통사고 및 화재' a)"], axis = 1)

les_df_edit = les_df.drop(['여가활용 만족도 b)',
                           '노인 천명당 노인여가복지시설수',
                           '인구 십만명당 도서관수',
                           '인구 십만명당 문화기반시설수',
                           '인구 천명당 체육관련 여가시설수'], axis = 1)

env_df_edit = env_df.drop(['환경체감도 b)',
                           '인구 천명당 1일 산업폐수 방류량 a)',
                           "도시지역 중 '녹지지역 비율'",
                           '미세먼지(PM2.5) a) b)',
                           '주민 1인당 생활폐기물배출량 a)'], axis = 1)

# 각 데이터별 평균 컬럼에 이름추가
# 각 데이터 프레임에 평균 값 옆에 이름 추가 예) 평균_건강, 평균_경제
health_df_edit.rename(columns = {'평균' : '평균_건강'},inplace = True)
eco_df_edit.rename(columns = {'평균' : '평균_경제'},inplace = True)
rel_df_edit.rename(columns = {'평균' : '평균_관게및사회참여'},inplace = True)
edu_df_edit.rename(columns = {'평균' : '평균_교육'},inplace = True)
life_df_edit.rename(columns = {'평균' : '평균_삶의만족도'},inplace = True)
safe_df_edit.rename(columns = {'평균' : '평균_안전'},inplace = True)
les_df_edit.rename(columns = {'평균' : '평균_여가'},inplace = True)
env_df_edit.rename(columns = {'평균' : '평균_환경'},inplace = True)

# 병합
health_df_edit.shape #  (229, 4)
eco_df_edit.shape #  (229, 4)
rel_df_edit.shape # (229, 4)
edu_df_edit.shape # (229, 4)
life_df_edit.shape # (229, 4)
safe_df_edit.shape # (229, 4)
les_df_edit.shape #  (229, 4)
env_df_edit.shape # (229, 4)

happy_df = pd.merge(health_df_edit, 
                    eco_df_edit,
                    rel_df_edit,
                    edu_df_edit,
                    life_df_edit,
                    safe_df_edit,
                    les_df_edit,
                    env_df_edit,
                    on = '구군')

from functools import reduce

dfs = [health_df_edit, eco_df_edit, rel_df_edit, edu_df_edit, 
       life_df_edit, safe_df_edit, les_df_edit, env_df_edit]

happy_df = reduce(lambda left, right: pd.merge(left, right, on='구군', how='left'), dfs)

# 결과 데이터프레임 크기 확인
print(happy_df.shape)










