# src/small.py
import pandas as pd
import os

input_csv = "../data/raw/train.csv"
output_csv = "../data/processed/train_small.csv"

# 원본 CSV 로드
df = pd.read_csv(input_csv, encoding="utf-8")
print("원본 CSV 로드 성공!")

# 샘플 500개 추출 (GPU 빠른 테스트용)
df_small = df.sample(n=500, random_state=42)

# 저장
os.makedirs(os.path.dirname(output_csv), exist_ok=True)
df_small.to_csv(output_csv, index=False, encoding="utf-8-sig")
print(f"작은 CSV 생성 완료! 경로: {output_csv}")
