# run_summarization.py
import pandas as pd
from tqdm import tqdm
from summarizer import batch_summarize
import os

# --------------------------
# 1. CSV 경로 설정
# --------------------------
input_csv = "../data/raw/train.csv"        # 원본 CSV
output_csv = "../data/processed/summarized.csv"  # 결과 CSV

# --------------------------
# 2. CSV 로드 (인코딩 안전)
# --------------------------
for enc in ['utf-8', 'cp949', 'latin1']:
    try:
        df = pd.read_csv(input_csv, encoding=enc)
        print(f"CSV 로드 성공! (encoding={enc})")
        break
    except Exception as e:
        print(f"encoding={enc} 실패: {e}")
else:
    raise ValueError(f"CSV 파일을 로드할 수 없습니다: {input_csv}")

# --------------------------
# 3. 요약할 컬럼 체크
# --------------------------
possible_cols = ['document', 'text', 'content']  # CSV에 있는 컬럼명 확인
for col in possible_cols:
    if col in df.columns:
        text_col = col
        break
else:
    raise ValueError(f"CSV에 요약할 컬럼이 없습니다. 가능한 컬럼: {possible_cols}, 실제 컬럼: {df.columns.tolist()}")

# --------------------------
# 4. 배치 요약 수행
# --------------------------
batch_size = 8  # GPU 메모리 여유에 맞게 조절 가능
df['summary'] = batch_summarize(df[text_col].tolist(), batch_size=batch_size)

# --------------------------
# 5. 결과 CSV 저장
# --------------------------
os.makedirs(os.path.dirname(output_csv), exist_ok=True)
df.to_csv(output_csv, index=False, encoding='utf-8-sig')
print(f"요약 완료! 저장 경로: {output_csv}")
