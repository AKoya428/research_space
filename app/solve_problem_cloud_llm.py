from core.prompts import solve_question_prompts
from external_api.post_chatgpt import GPTHandler, GPTResponse
import json

input_file_name = "data/input/base_questions.json"
output_file_name = "data/output/solve_problem_cloud_llm/chatgpt_answer5.json"
save_data = []

with open(input_file_name, "r", encoding="utf-8") as f:
    input_data = json.load(f)

question_list = [q["question"] for q in input_data]
prompts = [solve_question_prompts(q) for q in question_list]
response_list: list[GPTResponse] = GPTHandler.post_list(prompts)
save_data = [
    {
        "question": question,
        "answer": res.content,
        "finish_reason": res.finish_reason,
        "error": res.error,
    }
    for question, res in zip(question_list, response_list)
]

with open(output_file_name, "w", encoding="utf-8") as f:
    json.dump(save_data, f, ensure_ascii=False, indent=4)
