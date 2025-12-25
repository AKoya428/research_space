import json


jsonl_file = "data/input/linear_algebra/gpt-4o/samples_linear_algebra_480_chatgpt_2025-12-10T05-35-57.451361.jsonl"

with open(jsonl_file, encoding="utf-8") as f:
    data = [json.loads(line) for line in f if line.strip()]

data_slices = [data[i : i + 5] for i in range(0, len(data), 5)]

results = []
for _, s in enumerate(data_slices):
    if s[0]["exact_match"]:
        results.append(s[0])

results = results[:5]

output_file = "./data/output/failed_analyze_task15/test_data.jsonl"
with open(output_file, "w", encoding="utf-8") as f:
    for item in results:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
