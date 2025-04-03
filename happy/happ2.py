#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 17:42:37 2025

@author: oh
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from functools import reduce

# 파일 경로 리스트
file_paths = [
    "./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_건강.xlsx",
    "./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_경제.xlsx",
    "./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_관계및사회참여.xlsx",
    "./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_교육.xlsx",
    "./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_삶의만족도.xlsx",
    "./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_안전.xlsx",
    "./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_여가.xlsx",
    "./데이터 분석 데이터/행복지수 데이터/대한민국행복지도_환경.xlsx"
]

# 데이터프레임 리스트
dfs = [pd.read_excel(file) for file in file_paths]

# 공통 열 찾기 (예시: '구군'을 기준으로 병합)
common_column = '구군'

# 데이터 병합
merged_df = reduce(lambda left, right: pd.merge(left, right, on=common_column, how='outer'), dfs)

# 결측치 확인 및 처리
merged_df.fillna(0, inplace=True)

# 데이터 시각화
plt.figure(figsize=(10, 5))
sns.lineplot(data=merged_df.set_index(common_column))
plt.title("시도별 행복 지수 요소별 변화")
plt.xticks(rotation=45)
plt.legend(merged_df.columns[1:])
plt.show()

# 행복 지수 요소별 막대 그래프 (서브플롯 사용)
fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(15, 12))
axes = axes.flatten()

for idx, col in enumerate(merged_df.columns[1:]):
    sns.barplot(x=common_column, y=col, data=merged_df, ax=axes[idx])
    axes[idx].set_title(col)
    axes[idx].tick_params(axis='x', rotation=90)

plt.tight_layout()
plt.show()

# 요소 간 상관관계 히트맵
plt.figure(figsize=(10, 8))
sns.heatmap(merged_df.iloc[:, 1:].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("행복 지수 요소 간의 상관관계")
plt.show()
