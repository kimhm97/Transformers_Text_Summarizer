# src/run_summarization.py
import pandas as pd
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import math

# --------------------------
# 1. 모델 초기화 (GPU 사용)
# --------------------------
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()  # 평가 모드로 변경 (GPU 효율 향상)


# --------------------------
# 2. 안전 요약 함수 (배치 처리)
# --------------------------
def batch_summarize(texts, batch_size=4, max_input_tokens=1024, max_length=200, min_length=50):
    summaries = []
    num_batches = math.ceil(len(texts) / batch_size)

    for i in tqdm(range(num_batches), desc="Summarizing Batches"):
        batch_texts = texts[i * batch_size: (i + 1) * batch_size]
        inputs = tokenizer(batch_texts, return_tensors="pt", truncation=True, padding=True, max_length=max_input_tokens)
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():  # 기울기 계산 X → 메모리 절약
            summary_ids = model.generate(
                **inputs,
                max_length=max_length,
                min_length=min_length,
                do_sample=False,
                length_penalty=2.0,
                num_beams=4
            )

        batch_summaries = [tokenizer.decode(g, skip_special_tokens=True) for g in summary_ids]
        summaries.extend(batch_summaries)

    return summaries


# --------------------------
# 3. CSV 불러오기
# --------------------------
input_csv = "../data/raw/train.csv"
output_csv = "../data/processed/summarized.csv"

for enc in ['utf-8', 'cp949', 'latin1']:
    try:
        df = pd.read_csv(input_csv, encoding=enc)
        print(f"CSV 로드 성공! (encoding={enc})")
        break
    except Exception as e:
        print(f"encoding={enc} 실패: {e}")

# --------------------------
# 4. 컬럼명 체크
# --------------------------
possible_cols = ['document', 'summary']
for col in possible_cols:
    if col in df.columns:
        text_col = col
        break
else:
    raise ValueError(f"CSV에 요약할 컬럼이 없습니다. 가능한 컬럼: {possible_cols}, 실제 컬럼: {df.columns.tolist()}")

# --------------------------
# 5. 배치 요약 수행
# --------------------------
batch_size = 4  # GPU VRAM 여유에 맞게 조절 가능
df['summary'] = batch_summarize(df[text_col].tolist(), batch_size=batch_size)

# --------------------------
# 6. CSV 저장
# --------------------------
df.to_csv(output_csv, index=False, encoding='utf-8-sig')
print(f"요약 완료! 저장 경로: {output_csv}")
