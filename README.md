---

# 📝 Transformers Text Summarizer

---

## 📌 프로젝트 소개

Hugging Face Transformers 모델을 활용해 한국어 뉴스 기사를 자동으로 요약 하는 프로젝트.

* 데이터셋: `naver-news-summarization-ko`
* 입력: 뉴스 기사 (`passage`)
* 출력: 요약문 (`generated_summary`)

-뉴스 요약, 데이터 처리 및 자연어 처리(NLP)-

---
## 프로젝트 목적

한국어 뉴스 기사 자동 요약

* Hugging Face Transformers의 Seq2Seq 모델(facebook/bart-large-cnn) 활용
* CSV 파일(train.csv)을 읽어서 요약 후, 새로운 CSV(summarized.csv)로 저장

## 🗂 프로젝트 구조

```
transformers_Text_Summarizer/
│
├─ data/
│   ├─ raw/                # 원본 CSV
│   │   └─ train.csv
│   └─ processed/          # 요약 결과 저장
│       └─ train_summarized.csv
│
├─ src/
│   ├─ summarizer.py       # 요약 함수
│   └─ run_summarization.py # 실행 코드

│
├─ .gitignore
├─ requirements.txt
└─ README.md
```

---

## 🧠 모델 정보

| 항목 | 내용                        |
| -- | ------------------------- |
| 모델 | `facebook/bart-large-cnn` |
| 유형 | Seq2Seq (텍스트 요약)          |
| 장점 | 빠른 요약, 메모리 효율적            |
| 주의 | 입력 길이 1024 토큰 제한          |

---

