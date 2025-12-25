import os
import re
from pypdf import PdfReader, PdfWriter

pdf_dir = "./data/output/failed_analyze_task15/prompt1"
output_pdf = "./data/output/failed_answer_created_by_gpt.pdf"

writer = PdfWriter()
broken_files = []


def natural_key(text):
    # 数字を数値として扱うためのキー
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r"(\d+)", text)]


# PDFファイルのみ取得して自然順ソート
pdf_files = sorted(
    [f for f in os.listdir(pdf_dir) if f.lower().endswith(".pdf")], key=natural_key
)

# ファイル名順で結合
for file_name in pdf_files:
    file_path = os.path.join(pdf_dir, file_name)
    try:
        reader = PdfReader(file_path)
        for page in reader.pages:
            writer.add_page(page)
    except Exception as e:
        print(f"壊れた PDF: {file_name} -> {e}")
        broken_files.append(file_name)

# 正常なPDFを保存
if writer.pages:
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"正常な PDF をまとめました: {output_pdf}")
else:
    print("正常な PDF がありません。")

# 壊れたPDF一覧
if broken_files:
    print("\n壊れた PDF ファイル一覧:")
    for f in broken_files:
        print(f)
