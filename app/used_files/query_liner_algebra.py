import json
import re

from external_api.post_chatgpt import GPTHandler

data = []

pattern = r"College--Linear Algebra"
input_file_name = "data/input/mathbench_v1/college/single_choice_en.jsonl"
input_file_name2 = "data/input/mathbench_v1/college_knowledge/single_choice_en.jsonl"

with open(input_file_name, "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        if re.search(pattern, obj["topic"]):
            data.append(obj)

with open(input_file_name2, "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        if re.search(pattern, obj["topic"]):
            data.append(obj)

question = [d["question"] for d in data]
# GPTHandler.post_list(question)
