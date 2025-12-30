import json

jsonl_file = "./data/output/analyze_answer_benchmark/solved_data_base.jsonl"

with open(jsonl_file, encoding="utf-8") as f:
    data = [json.loads(line) for line in f if line.strip()]

target = '"GPTが作成した誤答": \n'
results = [d for d in data if target not in d["latex_data"]]
print(len(results))
