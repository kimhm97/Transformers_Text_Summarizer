
---
## transformers_Text_Summarizer

## 📘 한국어 뉴스 기사 자동 요약 프로젝트

---

## 📝 프로젝트 소개

* **프로젝트 목표:**
  한국어 뉴스 기사를 읽고 핵심 내용을 자동으로 요약하는 시스템 구현
* **사용 기술:**
  Python, Hugging Face Transformers(BART), PyTorch, Pandas, tqdm
* **주요 특징:**

  1. 배치 단위 처리로 GPU 메모리 효율 최적화
  2. 진행률 표시(tqdm)로 처리 상태 확인 가능
  3. 샘플 CSV 제공 → 빠른 시연 가능

---

## 📂 프로젝트 구조

```
transformers_Text_Summarizer/
│
├─ data/
│   ├─ raw/                # 원본 데이터(train.csv)
│   └─ processed/          # 처리/요약 결과(summarized.csv, train_small.csv)
│
├─ src/
│   ├─ run_summarization_full.py   # 전체 데이터 요약 스크립트
│   ├─ run_summarization_small.py  # 샘플 데이터 요약 스크립트
│   ├─ summarizer.py               # 배치 요약 함수
│   └─ small.py                    # 샘플 CSV 생성
│
├─ venv_gpu/                        # 가상환경
├─ .gitignore                       # 불필요 파일 제외
└─ README.md                        # 프로젝트 설명
```

---

## 📊 사용 데이터

* **데이터셋:** [Naver News Summarization KO](https://huggingface.co/datasets/daekeun-ml/naver-news-summarization-ko/viewer/default/train?views%5B%5D=train)
* **설명:** 뉴스 기사와 요약문이 포함된 한국어 데이터셋
* **활용 방법:**

  1. 전체 데이터(`train.csv`) → `data/raw/`에 저장
  2. 샘플 CSV(`train_small.csv`) → `small.py`로 추출 가능 (빠른 시연용)

---

## ⚙️ 실행 방법

### 가상환경 및 패키지 설치

```bash
python -m venv venv_gpu
source venv_gpu/Scripts/activate  # Windows
pip install -r requirements.txt
```

### 샘플 데이터 요약 

```bash
python src/run_summarization_small.py
```

* `train_small.csv` 기반
* 120분 내 완료 가능 (GPU 사용 시 더 빠름)

### 전체 데이터 요약 

```bash
python src/run_summarization.py
```

* 배치 크기와 GPU 성능에 따라 수 시간 소요 가능
* 완료 시 `summarized.csv` 생성

---

## 💻 핵심 기능

### summarize

* **설명:** 배치 단위로 요약 → GPU 메모리 효율 최적화
* **주요 파라미터:**

  * `num_beams=4` → Beam Search로 품질 높은 요약 생성
  * `length_penalty=2.0` → 길이 조정
* **추가 기능:** `tqdm` 진행률 표시

### small.py

* 전체 CSV에서 샘플 추출 → `train_small.csv` 생성
* 시연용으로 **빠르게 결과 확인 가능**

---

## 🌟 프로젝트 경험 & 배운 점

* GPU 활용으로 대용량 데이터 처리 경험
* 배치 단위 요약 최적화 → 실제 데이터 처리 방식 이해

---



