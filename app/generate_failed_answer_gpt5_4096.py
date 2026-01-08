import json
import copy

from core.util import save_as_jsonl
from external_api.post_chatgpt import GPTHandler
from latex.util import fix_llm_answer_for_latex


def prompt1(data, answer, failed_type):
    prompt = rf"""
    私は数学教育の研究者です。
    学習者の誤答データを収集しています。
    あなたは学生になりきり、{failed_type}を犯した場合の誤答を生成してください。

    問題と模範解答は以下の通りです。
    問題: {data["doc"]["question"]}
    
    選択肢: 
    A: {data["doc"]["options"]["A"]}
    B: {data["doc"]["options"]["B"]}
    C: {data["doc"]["options"]["C"]}
    D: {data["doc"]["options"]["D"]}


    模範解答: {answer}

    ## 条件:
    1. 「誤答を生成します」などの前置きを行わず、誤答のみを返すこと。
    2. 途中計算の数式はLatex形式で記述すること。インラインは $...$、ブロックは \[...\] を使用すること。
    """
    return prompt


jsonl_file = "./data/output/failed_analyze_task15/benchmark_base_data.jsonl"
failed_types = ["定義の概念誤り", "計算間違い", "論理の誤り"]
results = []

with open(jsonl_file, encoding="utf-8") as f:
    datas = [json.loads(line) for line in f if line.strip()]

for data in datas:
    prompts = [
        prompt1(
            data,
            fix_llm_answer_for_latex(data["resps"][0][0]),
            failed_type,
        )
        for failed_type in failed_types
    ]
    res_list = GPTHandler.simple_post_list(prompts, max_token=4096)
    for failed_type, res in zip(failed_types, res_list):
        save_obj = copy.deepcopy(data)
        save_obj["failed_reason"] = failed_type
        save_obj["failed_answer"] = res
        results.append(save_obj)
save_as_jsonl(
    "./data/output/analyze_answer_benchmark/analyze_failed_answer_gpt5_4096.jsonl",
    results,
)
