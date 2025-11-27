from pathlib import Path
import base64
from PIL import Image, UnidentifiedImageError
import io
import matplotlib.pyplot as plt

def encode_image_to_base64(image_path: Path) -> str:
    """이미지 파일을 base64 문자열로 변환 (파일 없으면 예외 처리)"""
    if not image_path.exists():
        raise FileNotFoundError(f"[ERROR] 파일이 존재하지 않습니다: {image_path}")
    try:
        with image_path.open("rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"[ERROR] 이미지 인코딩 실패: {e}")

def decode_base64_to_image(encoded_str: str, output_path: Path) -> Image.Image:
    """base64 문자열을 이미지로 디코딩하고 파일로 저장 (잘못된 base64, 이미지 손상 처리)"""
    try:
        decoded_bytes = base64.b64decode(encoded_str)
    except (base64.binascii.Error, ValueError) as e:
        raise ValueError(f"[ERROR] 잘못된 base64 문자열: {e}")
    try:
        image = Image.open(io.BytesIO(decoded_bytes))
    except UnidentifiedImageError:
        raise ValueError("[ERROR] 디코딩한 데이터가 유효한 이미지가 아닙니다.")
    try:
        image.save(output_path)
    except Exception as e:
        raise RuntimeError(f"[ERROR] 이미지 저장 실패: {e}")
    return image

def visualize_image(image: Image.Image, title: str = "Decoded Image"):
    """이미지 시각화"""
    if image is None:
        raise ValueError("[ERROR] 시각화할 이미지가 없습니다.")
    plt.imshow(image)
    plt.axis('off')
    plt.title(title)
    plt.show()

def main():
    input_path = Path("img/Original.jpg")
    output_path = Path("img/decoded.jpg")

    try:
        # 이미지 → base64
        encoded_str = encode_image_to_base64(input_path)

        # base64 → 이미지 파일 + PIL 이미지 객체
        decoded_image = decode_base64_to_image(encoded_str, output_path)

        # 시각화
        visualize_image(decoded_image, title=f"{input_path.name} Decoded")

        print(f"[check] {input_path.name} → base64 인코딩 → 디코딩 후 {output_path.name} 저장 및 시각화 완료")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
