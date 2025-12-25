from latex.util import basic_template, export_as_pdf, fix_llm_answer_for_latex
import json


def create_latex_text(data):
    latex_text = rf"""
    id: {data["doc_id"]}

    問題: {data["doc"]["question"]}
    
    選択肢: 
    A: {data["doc"]["options"]["A"]}
    B: {data["doc"]["options"]["B"]}
    C: {data["doc"]["options"]["C"]}
    D: {data["doc"]["options"]["D"]}


    回答: {data["doc"]["answer"]}

    LLM: {fix_llm_answer_for_latex(data["resps"][0][0])}
    \newpage
    """
    return latex_text


jsonl_file = "data/input/linear_algebra/gpt-4o/samples_linear_algebra_480_chatgpt_2025-12-10T05-35-57.451361.jsonl"
# jsonl_file = "data/input/linear_algebra/gpt-5/samples_linear_algebra_480_chatgpt_2025-12-10T08-31-11.522663.jsonl"

with open(jsonl_file, encoding="utf-8") as f:
    data = [json.loads(line) for line in f if line.strip()]
data = [d for d in data if d["doc_id"] // 5 in [3, 38, 39, 56, 64, 70, 86, 89]]

print_data = []
for i in range(0, len(data), 5):
    slice = data[i : i + 5]
    print_data.append([d for d in slice if d["exact_match"] == 0.0][0])
    print_data.append([d for d in slice if d["exact_match"] == 1.0][0])

# print_data.append([d for d in data if d["doc_id"] == 442][0])

print(len(print_data))


for d in print_data:
    input_text = create_latex_text(d)
    template = basic_template(input_text)
    export_as_pdf(template, f"gpt-4o_failed_no{d['doc_id']}", "data/output/gpt-4o_40")
