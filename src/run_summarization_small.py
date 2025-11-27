# src/run_summarization_small.py
import pandas as pd
from summarizer import batch_summarize  # 최적화된 batch_summarize 함수
import os

input_csv = "../data/processed/train_small.csv"
output_csv = "../data/processed/summarized_small.csv"

# CSV 로드
df = pd.read_csv(input_csv, encoding="utf-8")
print("샘플 CSV 로드 완료!")

# 컬럼 확인
possible_cols = ['document', 'text', 'content']
for col in possible_cols:
    if col in df.columns:
        text_col = col
        break
else:
    raise ValueError(f"CSV에 요약할 컬럼이 없습니다. 가능한 컬럼: {possible_cols}, 실제 컬럼: {df.columns.tolist()}")

# 배치 요약 수행
df['summary'] = batch_summarize(df[text_col].tolist(), batch_size=8)

# 저장
os.makedirs(os.path.dirname(output_csv), exist_ok=True)
df.to_csv(output_csv, index=False, encoding='utf-8-sig')
print(f"샘플 CSV 요약 완료! 경로: {output_csv}")
