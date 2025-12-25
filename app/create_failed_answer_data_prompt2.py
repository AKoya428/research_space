import json

from core.util import save_as_jsonl
from external_api.post_chatgpt import GPTHandler
from latex.util import fix_llm_answer_for_latex


def prompt2(data, answer, failed_choise):
    prompt = rf"""
    私は数学教育の研究者です。
    学習者の誤答データを収集しています。

    問題と模範解答は以下の通りです。
    問題: {data["doc"]["question"]}
    
    選択肢: 
    A: {data["doc"]["options"]["A"]}
    B: {data["doc"]["options"]["B"]}
    C: {data["doc"]["options"]["C"]}
    D: {data["doc"]["options"]["D"]}

    模範解答: {answer}

    学習者は最終回答に選択肢: {failed_choise}を選びました。
    学習者が誤答に至った思考回路を想像し、途中回答を含む形で再現してください。

    ## 条件:
    1. 「誤答を生成します」などの前置きを行わず、誤答のみを返すこと。
    2. 途中計算の数式はLatex形式で記述すること。インラインは $...$、ブロックは \[...\] を使用すること。
    """
    return prompt


jsonl_file = "./data/output/failed_analyze_task15/test_data.jsonl"
results = []

with open(jsonl_file, encoding="utf-8") as f:
    datas = [json.loads(line) for line in f if line.strip()]
for data in datas:
    failed_choises: list = [
        i for i in ["A", "B", "C", "D"] if i != data["doc"]["answer"]
    ]
    if len(failed_choises) != 3:
        print("error")
    prompts = [
        prompt2(
            data,
            fix_llm_answer_for_latex(data["resps"][0][0]),
            failed_choise,
        )
        for failed_choise in failed_choises
    ]
    res_list = GPTHandler.simple_post_list(prompts, max_token=2048)
    save_objs = [
        {
            "latex_data": rf"""
問題: {data["doc"]["question"]}

選択肢: 
A: {data["doc"]["options"]["A"]}

B: {data["doc"]["options"]["B"]}

C: {data["doc"]["options"]["C"]}

D: {data["doc"]["options"]["D"]}

正答の選択肢: {data["doc"]["answer"]}

"ユーザーの誤答": {failed_answer}

"GPTが作成した誤答": {res}
"""
        }
        for res, failed_answer in zip(
            res_list,
            failed_choises,
        )
    ]
    results.extend(save_objs)
save_as_jsonl(
    "./data/output/failed_analyze_task15/prompt2.jsonl",
    results,
)
