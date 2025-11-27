# -*- coding: utf-8 -*-
"""
CSV 기반 텍스트 요약
- Extractive 요약: Sumy LSA
- AI 요약: Transformers
"""

import pandas as pd
import numpy as np
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from transformers import pipeline

# Extractive 요약 함수
def sumy_summarize(text, num_sentences=3):
    parser = PlaintextParser.from_string(text, Tokenizer("korean"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, num_sentences)
    return ' '.join([str(sentence) for sentence in summary])

if __name__ == "__main__":
    # 1. CSV 불러오기
    df = pd.read_csv('1_Text_Summarizer/Book_test.csv')
    df = df.iloc[0:100]
    df.reset_index(drop=True, inplace=True)

    # 2. AI 요약 파이프라인 준비 (KoBART 추천, 없으면 fallback)
    try:
        summarizer = pipeline("summarization", model="hyunwoong-ko/kobart-summarization")
    except:
        summarizer = pipeline("summarization")  # 영어 모델 fallback

    # 3. 전체 데이터 요약 적용
    df['AI_summary'] = df['passage'].apply(lambda x: summarizer(x, max_length=100, min_length=30, do_sample=False)[0]['summary_text'])
    df['extract'] = df['passage'].apply(lambda x: sumy_summarize(x, num_sentences=3))

    # 4. 시각화 / 비교 출력
    random_number = np.random.randint(0, len(df), size=1)[0]
    print("=" * 120)
    print(f'{random_number} 번째 문서\n')
    print('원문:\n\n' + df['passage'][random_number] + '\n\n')
    print('AI 요약:\n\n' + df['AI_summary'][random_number] + '\n\n')
    print('Extractive 요약 (Sumy LSA):\n\n' + df['extract'][random_number] + '\n\n')
