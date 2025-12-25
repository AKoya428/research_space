from pathlib import Path
import shutil
import subprocess
import re


def fix_llm_answer_for_latex2(text: str) -> str:
    """LLMが成形するlatexをレンダリング可能な形に修正する"""
    return text.replace("\\\\", "\\")


def fix_llm_answer_for_latex3(text: str) -> str:
    """
    行列内はそのままにして、その他の部分で \\ を \ に置換
    """
    # 行列パターン
    matrix_pattern = re.compile(r"(\\begin\{pmatrix\}.*?\\end\{pmatrix\})", re.DOTALL)

    # split すると行列部分は消えるので、capture group を使って findall で後で復元
    segments = matrix_pattern.split(text)

    result = []
    for i, seg in enumerate(segments):
        if i % 2 == 1:
            # 奇数番目は行列部分 → そのまま
            result.append(seg)
        else:
            # 偶数番目は行列以外 → 置換
            result.append(seg.replace("\\\\", "\\"))

    return "".join(result)


def fix_llm_answer_for_latex(text: str) -> str:
    """
    pmatrix / vmatrix（行列・行列式）内はそのままにして、
    その他の部分で \\ を \ に置換
    """
    matrix_pattern = re.compile(
        r"(\\begin\{(?:pmatrix|vmatrix|bmatrix|Bmatrix|matrix)\}.*?"
        r"\\end\{(?:pmatrix|vmatrix|bmatrix|Bmatrix|matrix)\})",
        re.DOTALL,
    )

    segments = matrix_pattern.split(text)

    result = []
    for i, seg in enumerate(segments):
        if i % 2 == 1:
            # 行列 or 行列式部分
            result.append(seg)
        else:
            # それ以外
            result.append(seg.replace("\\\\", "\\"))

    return "".join(result)


def export_as_pdf(
    latex_template: str,
    output_file_name: str,
    output_dir: str,
) -> subprocess.CompletedProcess:
    """latexをpdf出力する"""

    build_dir = Path("latex/build")
    build_path = build_dir / f"{output_file_name}"
    build_path.write_text(latex_template, encoding="utf-8")

    # lualatexを呼んでPDFを生成
    result = subprocess.run(
        [
            "lualatex",
            "--interaction=nonstopmode",
            f"-output-directory={build_dir}",
            build_path.name,
        ],
        capture_output=True,
        text=True,
    )
    try:
        shutil.move(
            f"{build_path}.pdf",
            f"{output_dir}/{output_file_name}.pdf",
        )
    except:
        print(f"{output_file_name}.pdfの生成に失敗しました")
    return result


def basic_template(input: str) -> str:
    latex = f"""
\\documentclass{{ltjsarticle}}
\\usepackage{{amsmath}}
\\usepackage{{fontspec}}
\\setmainfont{{IPAexMincho}}
\\setsansfont{{IPAexGothic}}
\\usepackage[a4paper,margin=25mm]{{geometry}}

\\begin{{document}}

{input}

\\end{{document}}
"""
    return latex
