import copy
from core.util import load_jsonl, save_as_jsonl
import os


def count_equal_problem(data, data_list):
    """問題が一致、選択肢も完全一致"""
    count = 0
    for d in data_list:
        if data["question"] != d["question"]:
            continue

        if set(data["options"].values()) == set(d["options"].values()):
            count += 1

    return count


all_files = []
base_dir = "data/input/base_learn_data"  # 対象フォルダ
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".jsonl"):
            all_files.append(
                os.path.relpath(os.path.join(base_dir, root, file), base_dir)
            )
benchmark_question = load_jsonl("data/input/linear_algebra_480.jsonl")

for input_file in all_files:
    learning_data = load_jsonl(input_file)

    question_data = copy.deepcopy(learning_data)
    question_data.extend(benchmark_question)

    save_list = []
    for d in learning_data:
        if count_equal_problem(d, question_data) == 1:
            save_list.append(d)

    base = os.path.splitext(os.path.basename(input_file))[0]
    output_file_path = f"./data/input/exclude_learn_data/{base}.jsonl"
    if len(save_list) > 0:
        save_as_jsonl(output_file_path, save_list)
    print(len(save_list))
