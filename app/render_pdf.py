import copy
from latex.util import basic_template, export_as_pdf, fix_llms_latex
import json

input_file_name = "data/input/base_questions.json"
with open(input_file_name, "r", encoding="utf-8") as f:
    data = json.load(f)

for thema, json_data in data.items():
    question_list = [fix_llms_latex(q) for q in json_data.values()]
    template = basic_template("\n\n".join(question_list))
    export_as_pdf(template, thema, "data/output/all_question_pdf")
