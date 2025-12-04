from core.prompts import solve_question_prompts
from external_api.post_chatgpt import GPTHandler
import json


question = """
ある行列 $A$ で定まる1次写像 $f$ について，基底
\[
\begin{bmatrix}
-1 \\ 1 \\ 0
\end{bmatrix},
\begin{bmatrix}
1 \\ -1 \\ -1
\end{bmatrix},
\begin{bmatrix}
1 \\ 0 \\ -1
\end{bmatrix}
\]
に関する $f$ の表現行列が
\[
B = 
\begin{pmatrix}
1 & 1 & 1 \\
-2 & -1 & -1 \\
-1 & 1 & 0
\end{pmatrix}
\]
になるという．$A$ を求めよ．
"""
five_question = [question] * 5
prompts = [solve_question_prompts(p) for p in five_question]
res_list = GPTHandler.post_list(prompts, max_token=4096)
save_data = [
    {
        "question": question,
        "answer": r.content,
        "finish_reason": r.finish_reason,
    }
    for r in res_list
]

output_file = "data/output/tmp/tmp.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(save_data, f, ensure_ascii=False, indent=4)
