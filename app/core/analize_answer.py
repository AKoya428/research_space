import copy
from math_verify import parse, verify
import json
import os


def query_same_answer_row(file: list, query_row: dict) -> dict:
    """同一問題の回答データを取得"""
    return [row for row in file if row["question"] == query_row["question"]][0]


def compare_numerical_value(
    row1: dict,
    row2: dict,
    path1: str,
    path2: str,
) -> dict:
    """回答の数値比較を行う"""
    try:
        answer1 = parse(row1["answer"])
        answer2 = parse(row2["answer"])
        return {
            "question": row1["question"],
            f"{os.path.splitext(os.path.basename(path1))[0]}": row1["answer"],
            f"{os.path.splitext(os.path.basename(path2))[0]}": row2["answer"],
            "is_correct": verify(answer1, answer2),
        }
    except:
        print(f"compare_numerical_value error:{row1['question']}")
        return


def compare_answer_file(
    file1: str,
    file2: str,
) -> tuple[set[str], dict]:
    """2つのファイルを比較して分析する"""
    with open(file1, "r", encoding="utf-8") as f:
        file1_data = json.load(f)
    with open(file2, "r", encoding="utf-8") as f:
        file2_data = json.load(f)

    length_error_question = set()
    compared_datas = []

    for row1 in file1_data:
        row2 = query_same_answer_row(file2_data, row1)
        if row1.get("error") or row2.get("error"):
            assert "row has Error"

        # finish_reasonが存在するかつ終了理由がstopまたはlengthではない
        if any(
            r.get("finish_reason") not in (None, "stop", "length") for r in (row1, row2)
        ):
            assert "finish reason is not stop or length"

        # length終了は別変数に格納
        if any(r.get("finish_reason") == "length" for r in (row1, row2)):
            length_error_question.add(row1["question"])
        else:
            result = compare_numerical_value(row1, row2, file1, file2)
            compared_datas.append(result)

    return length_error_question, compared_datas


def compare_answer_files(files: list[str]) -> tuple[dict, dict, str]:
    """複数のファイルを比較"""
    base_file = files[0]

    failed_answers = []
    length_error_questions = set()

    with open(base_file, "r", encoding="utf-8") as f:
        base_file_data = json.load(f)
    all_correct_answers = copy.deepcopy(base_file_data)

    for file in files[1:]:
        length_error_question_datas, compared_datas = compare_answer_file(
            base_file,
            file,
        )
        length_error_questions.update(length_error_question_datas)

        # 不正解の問題データを追加
        false_data = [data for data in compared_datas if not data["is_correct"]]
        failed_answers.extend(false_data)

        # 正解データ以外を除外する
        correct_data = [data for data in compared_datas if data["is_correct"]]
        correct_data_question = set(q["question"] for q in correct_data)
        all_correct_answers = [
            data
            for data in all_correct_answers
            if data["question"] in correct_data_question
        ]
    print(f"all_correct_answesr: {len(all_correct_answers)}")
    print(f"failed_ansers: {len(failed_answers)}")
    print(f"length_error_questions: {len(length_error_questions)}")

    return (
        all_correct_answers,
        failed_answers,
        length_error_questions,
    )
