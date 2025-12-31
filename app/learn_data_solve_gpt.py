import copy
import os

from core.util import load_jsonl, save_as_jsonl
from external_api.post_chatgpt import GPTHandler


def prompt(question: str, options: dict):
    return rf"""
    あなたは優秀な数学教師です。
    以下の問題をstep by stepで考えてください。
    問題: {question}

    ## 条件
    数式はLatex形式で記述すること。インラインは $...$、ブロックは \[...\] を使用すること。
    最後に、選択肢A~Dから一つ選び、'ANSWER: X'(XはA~Dのアルファベット)と回答すること。

    ## 選択肢
    A. {options["A"]}
    B. {options["B"]}
    C. {options["C"]}
    D. {options["D"]}
    """


all_files = []
base_dir = "data/input/exclude_learn_data"  # 対象フォルダ
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".jsonl"):
            all_files.append(
                os.path.relpath(os.path.join(base_dir, root, file), base_dir)
            )
all_files.sort()

for input_file in all_files[1:5]:
    datas = load_jsonl(input_file)
    save_list = copy.deepcopy(datas)
    prompts = [prompt(d['question'], d['options']) for d in datas]
    results = GPTHandler.simple_post_list(prompts, max_token=4096)

    for asave, p in zip(save_list, prompts):
        asave['prompt'] = p
    for asave, result in zip(save_list, results):
        asave['gpt_answer'] = result

    base = os.path.splitext(os.path.basename(input_file))[0]
    output_file_path = f"./data/output/learn_data/{base}.jsonl"
    save_as_jsonl(output_file_path, save_list)
    print(f"save: {output_file_path}")
