from dataclasses import dataclass


'''
def solve_question_prompts(question: str) -> str:
    """問題を解くプロンプト"""
    prompt = rf"""
    {question}
    step by stepで考えてください。
    
    ## 条件
    1. 途中計算の数式はLatex形式で記述すること。インラインは $...$、ブロックは \[...\] を使用すること。
    2. 最終回答は \boxed{{}} の中に入れること。
    """
    return prompt
'''


def solve_question_prompts(question: str) -> str:
    """問題を解くプロンプト"""
    prompt = rf"""
    {question}
    step by stepで考えてください。
    
    ## 条件
    1. 途中計算の数式はLatex形式で記述すること。インラインは $...$、ブロックは \[...\] を使用すること。
    2. 最終回答は \boxed{{}} の中に入れること。
    3. sympyで評価できるよう
    """
    return prompt


@dataclass
class AnalyzeFailedTask:
    question: str
    failed_answer: str
    failed_reason_choice: list[str]


def analyze_failed(task: AnalyzeFailedTask) -> str:
    """誤答分析を行うプロンプト"""
    prompt = f"""
    あなたは優秀な数学チューターです。

    問題: {task.question}
    学生の誤答: {task.failed_answer}
    
    1. 学生の誤答分析をstep by stepで行ってください。
    2. 学生の誤答原因と最も近いものを選択肢から1つ選び、A ~ Eのアルファベットで回答しなさい。
       出力形式は以下の形式に従うこと。
       例)
       answer: A

    ## 選択肢
    A: {task.failed_reason_choice[0]}
    B: {task.failed_reason_choice[1]}
    C: {task.failed_reason_choice[2]}
    D: {task.failed_reason_choice[3]}
    E: その他

    ## 条件
    1. 数式はLatex形式で記述すること。インラインは $...$、ブロックは \[...\] を使用すること。
    """
    return prompt


@dataclass
class ClassifyFailedTask:
    question: str
    failed_answer: str
    analyze_failed: str
    classify_failed_choice: list[str]


def classify_failed(task: ClassifyFailedTask) -> str:
    """誤答分析を行うプロンプト"""
    prompt = f"""
    あなたは優秀な数学チューターです。

    問題: {task.question}
    学生の誤答: {task.failed_answer}
    誤答分析結果: {task.analyze_failed}

    1. 学生の誤答分類をstep by stepで行ってください。
    2. 学生の誤答分類と最も近いものを選択肢から1つ選び、A ~ Eのアルファベットで回答しなさい。
       出力形式は以下の形式に従うこと。
       例)
       answer: A

    ## 誤答分類の選択肢
    A: {task.classify_failed_choice[0]}
    B: {task.classify_failed_choice[1]}
    C: {task.classify_failed_choice[2]}
    D: {task.classify_failed_choice[3]}
    E: その他

    ## 条件
    1. 数式はLatex形式で記述すること。インラインは $...$、ブロックは \[...\] を使用すること。
    """
    return prompt

def tutor_prompts(fewshot: list, question, failed_answer) -> str:
    """
    Docstring for tutor_prompts
    
    :param fewshot: Description
    :type fewshot: list
    :return: Description
    :rtype: str
    """
    prompt = f"""
    あなたは優秀な数学チューターです。
    以下の誤答をした学生にアドバイスを送ってください。

    問題: {question}
    誤答: {failed_answer}

    
    問題: {}
    誤答: {}
    フィードバック: {}
    """
    return prompt