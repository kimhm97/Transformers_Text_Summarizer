# summarizer.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from tqdm import tqdm
import math

# --------------------------
# 1. 모델 초기화
# --------------------------
MODEL_NAME = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

# GPU 감지
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()  # 평가 모드 -> 속도/메모리 최적화

# --------------------------
# 2. 안전 요약 함수 (배치 처리)
# --------------------------
def batch_summarize(texts, batch_size=8, max_input_tokens=1024, max_length=150, min_length=50):
    """
    texts: list of strings
    batch_size: 한 번에 GPU로 처리할 텍스트 개수
    """
    summaries = []
    num_batches = math.ceil(len(texts) / batch_size)

    for i in tqdm(range(num_batches), desc="Summarizing Batches"):
        batch_texts = texts[i*batch_size : (i+1)*batch_size]

        # 빈 문자열 처리
        batch_texts = [t.replace("\n", " ").strip() if t else "" for t in batch_texts]

        # 토크나이즈 + GPU 전송
        inputs = tokenizer(batch_texts, return_tensors="pt", truncation=True,
                           padding=True, max_length=max_input_tokens).to(device)

        # 요약 생성
        with torch.no_grad():
            summary_ids = model.generate(
                **inputs,
                max_length=max_length,
                min_length=min_length,
                num_beams=4,
                length_penalty=2.0,
                do_sample=False
            )

        # 디코딩
        batch_summaries = [tokenizer.decode(g, skip_special_tokens=True) for g in summary_ids]
        summaries.extend(batch_summaries)

    return summaries

# --------------------------
# 3. 단일 텍스트 요약 함수
# --------------------------
def summarize_text(text, max_input_tokens=1024, max_length=150, min_length=50):
    """배치 처리 없이 한 문장 요약"""
    if not text:
        return ""
    inputs = tokenizer(str(text).replace("\n", " ").strip(),
                       return_tensors="pt", truncation=True, max_length=max_input_tokens).to(device)
    with torch.no_grad():
        summary_ids = model.generate(
            **inputs,
            max_length=max_length,
            min_length=min_length,
            num_beams=4,
            length_penalty=2.0,
            do_sample=False
        )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
