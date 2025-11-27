
---
## transformers_Text_Summarizer
## 📰 Korean News Summarization Project

## 프로젝트 목표

한국어 뉴스 기사를 Hugging Face Transformers 기반 **BART 모델**로 자동 요약하는 경험을 해보고,
대용량 텍스트 처리 및 GPU 활용 경험을 쌓기 위해 진행한 개인 프로젝트입니다.

---

## 프로젝트 설명

* 대규모 한국어 뉴스 데이터를 배치 처리로 요약
* 작은 샘플 CSV(`train_small.csv`)로 **포트폴리오용 결과물 생성**
* 학습 과정에서 **GPU, PyTorch, Transformers 사용 경험** 확보

---

## 🧩 프로젝트 구성

```
transformers_Text_Summarizer/
├─ data/
│  ├─ raw/
│  │  └─ train.csv           # 원본 뉴스 데이터
│  └─ processed/
│     ├─ train_small.csv     # 테스트용 샘플 CSV
│     └─ summarized_small.csv # 요약 결과
├─ src/
│  ├─ run_summarization_small.py  # 작은 CSV 요약
│  ├─ summarizer.py               # 배치 요약 함수
│  └─ small.py                     # 작은 CSV 생성
├─ .gitignore                     # Git 관리 제외 파일
├─ requirements.txt
└─ README.md
```

> **.gitignore 예시 내용**

```
__pycache__/
*.pyc
*.pyo
*.pyd
*.csv
*.env
.venv/
venv_gpu/
.ipynb_checkpoints/
```

---

## 사용 기술

* Python, Pandas: 데이터 처리 및 CSV 관리
* Hugging Face Transformers, PyTorch: 텍스트 요약 모델 사용
* TQDM: 배치 처리 진행률 확인
* GPU 활용: 모델 추론 속도 향상

---

## 실행 방법

### 1️⃣ 환경 설치

```bash
pip install -r requirements.txt
```

### 2️⃣ 작은 CSV로 테스트

```bash
python src/run_summarization_small.py
```

* `train_small.csv`를 불러와 요약
* `summarized_small.csv`로 결과 저장

> ⚠️ 전체 데이터(`train.csv`)는 처리 시간이 오래 걸려 **포트폴리오에서는 작은 CSV로 실행**

---

## 🔄 코드 요약

* `small.py`: 전체 CSV에서 일부 샘플만 추출하여 `train_small.csv` 생성
* `summarizer.py`: BART 모델로 **배치 단위 요약**, GPU 최적화 적용
* `run_summarization_small.py`: 작은 CSV 로드 → 배치 요약 → 결과 CSV 저장

---

## 결과 예시

| document (뉴스 기사 일부) | summary (모델 생성 요약) |
| ------------------- | ------------------ |
| 한국어 뉴스 원문 텍스트       | 모델이 생성한 요약문        |
| ...                 | ...                |

---

## 배운 점

* Transformers 모델을 활용한 한국어 텍스트 요약 실습
* GPU 배치 처리 경험 → 대용량 데이터 처리 이해
* 데이터 전처리, CSV 관리, Python 프로젝트 구조 경험

---

