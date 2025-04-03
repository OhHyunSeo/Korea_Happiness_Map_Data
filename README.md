# 😊 Korea Happiness Map Data Analysis

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)

## 🔍 소개

**Korea Happiness Map Data** 프로젝트는 대한민국 각 지역의 행복도와 날씨, 미세먼지 등의 환경 요인을 분석하여  
행복도와의 관계를 시각화하는 데이터 기반 프로젝트입니다. 크롤링부터 전처리, 분석, 시각화까지 전 과정이 포함되어 있습니다.

---

## 🧩 주요 기능

- 😀 행복도 관련 데이터 수집 및 분석
- 🌫️ 미세먼지, 날씨 데이터 연동
- 🧹 정교한 전처리 및 통합 분석
- 🗺️ 지역별 행복도 시각화

---

## 📁 프로젝트 구조

```
📁 Korea_Happiness_Map_Data-master/
│
├── 1_Crawling.py              # 행복 관련 데이터 크롤링
├── 2_Preprocessing.py         # 데이터 전처리
├── 3_Product_Analysis.py      # 제품/행복도 종합 분석
│
├── 📁 happy/
│   ├── happ2.py               # 행복도 수치 분석 및 지도 시각화
│   └── happy_preprocessing.py # 행복도 관련 전처리
│
└── 📁 weather/
    ├── dust.py                # 미세먼지 데이터 수집/처리
    └── dust2.py               # 미세먼지 추가 분석
```

---

## 🚀 실행 방법

### 1. 환경 구성

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # 필요시 직접 생성
```

### 2. 분석 순서 예시

1. `1_Crawling.py` → 행복 데이터 수집
2. `2_Preprocessing.py` → 통합 전처리 수행
3. `happy/happ2.py` → 행복도 지도 시각화
4. `weather/dust.py` → 미세먼지 데이터 반영

---

## 🗺️ 분석 예시

- 행복도 점수를 지도 기반으로 표현
- 환경 요인(미세먼지 등)과의 상관관계 탐색
- 지역별 패턴 비교 분석

---

## 🤝 기여 방법

1. 이 레포지토리를 포크하세요.
2. 새 브랜치를 생성하세요: `git checkout -b feature/기능명`
3. 변경사항을 커밋하세요: `git commit -m "Add 기능"`
4. 브랜치에 푸시하세요: `git push origin feature/기능명`
5. Pull Request를 생성하세요.
