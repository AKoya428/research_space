from latex.util import basic_template, export_as_pdf, fix_llm_answer_for_latex
import json

input_file_name = "./data/output/failed_analyze_task15/prompt2.jsonl"
with open(input_file_name, "r", encoding="utf-8") as f:
    datas = [json.loads(line) for line in f if line.strip()]

for i, data in enumerate(datas):
    latex = fix_llm_answer_for_latex(data["latex_data"])
    template = basic_template(latex)
    export_as_pdf(
        template,
        f"created_failed_answer_pattern2_{i}",
        "data/output/failed_analyze_task15/prompt2",
    )
