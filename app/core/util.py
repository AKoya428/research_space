import json


def load_jsonl(input_file: str) -> list:
    with open(input_file, encoding="utf-8") as f:
        data = [json.loads(line) for line in f if line.strip()]
    return data


def save_as_jsonl(output_file: str, save_list: list):
    """jsonlとしてセーブする"""
    with open(output_file, "w", encoding="utf-8") as f:
        for item in save_list:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
