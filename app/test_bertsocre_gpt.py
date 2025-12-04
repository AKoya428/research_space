import json
import random

input_file_name = "data/input/test_feedback.json"
with open(input_file_name, "r", encoding="utf-8") as f:
    datas = json.load(f)

datas = []
for _, v in datas:
    datas.append(v[1])

random.shuffle(datas)

few_shot = datas[:3]
input_data = datas[3:]
