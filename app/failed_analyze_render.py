from core.util import save_as_jsonl
from latex.util import basic_template, export_as_pdf, fix_llm_answer_for_latex
import json

input_file_name = "data/output/analyze_answer_benchmark/analyze_failed_answer_gpt5_4096.jsonl"
with open(input_file_name, "r", encoding="utf-8") as f:
    datas = [json.loads(line) for line in f if line.strip()]

for i, data in enumerate(datas):
    data["failed_classification_id"] = i
save_as_jsonl(input_file_name, datas)

print(f'len: {len([d for d in datas if d["failed_answer"]])}')

for i, data in enumerate(datas):
    if not data["failed_answer"]:
        continue
    text = rf"""
問題: {data["doc"]["question"]}

選択肢: 
A: {data["doc"]["options"]["A"]}

B: {data["doc"]["options"]["B"]}

C: {data["doc"]["options"]["C"]}

D: {data["doc"]["options"]["D"]}

正答の選択肢: {data["doc"]["answer"]}

指定した誤答タイプ: {data["failed_reason"]}

GPTが作成した誤答: {data["failed_answer"]}
"""
    latex = fix_llm_answer_for_latex(text)
    template = basic_template(latex)
    export_as_pdf(
        template,
        f'failed_data_{data["failed_classification_id"]}',
        "data/output/analyze_answer_benchmark/failed_answer_benchmark_pdf_4096",
    )
