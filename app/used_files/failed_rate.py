import json


jsonl_file = "data/input/linear_algebra/gpt-4o/samples_linear_algebra_480_chatgpt_2025-12-10T05-35-57.451361.jsonl"
# jsonl_file = "data/input/linear_algebra/gpt-5/samples_linear_algebra_480_chatgpt_2025-12-10T08-31-11.522663.jsonl"

with open(jsonl_file, encoding="utf-8") as f:
    data = [json.loads(line) for line in f if line.strip()]

data_slices = [data[i : i + 5] for i in range(0, len(data), 5)]

results = []
for idx, s in enumerate(data_slices):
    results.append({idx: sum([d["exact_match"] for d in s]) * 20})

# 分類用の辞書
categories = {0: [], 20: [], 40: [], 60: [], 80: [], 100: []}

# 分類処理
for item in results:
    for index, value in item.items():
        if value in categories:
            categories[value].append(index)
        else:
            # もしカテゴリにない場合、四捨五入などで分類したい場合は調整可能
            pass

# 結果表示
for percent, indices in categories.items():
    print(f"{percent}%: {indices}: {len(indices)}個")
