from core.analize_answer import compare_answer_files
import json

files = [
    "data/output/solve_problem_cloud_llm/chatgpt_answer1.json",
    "data/output/solve_problem_cloud_llm/chatgpt_answer2.json",
    "data/output/solve_problem_cloud_llm/chatgpt_answer3.json",
    "data/output/solve_problem_cloud_llm/chatgpt_answer4.json",
    "data/output/solve_problem_cloud_llm/chatgpt_answer5.json",
]
all_correct_answer, failed_answers, length_error_questions = compare_answer_files(
    files=files
)


with open(
    "data/output/compare_gpt_answers/all_correct_answer.json", "w", encoding="utf-8"
) as f:
    json.dump(all_correct_answer, f, ensure_ascii=False, indent=4)
with open(
    "data/output/compare_gpt_answers/failed_answers.json", "w", encoding="utf-8"
) as f:
    json.dump(failed_answers, f, ensure_ascii=False, indent=4)
with open(
    "data/output/compare_gpt_answers/length_error_questions.json", "w", encoding="utf-8"
) as f:
    json.dump(list(length_error_questions), f, ensure_ascii=False, indent=4)
