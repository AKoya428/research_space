from pathlib import Path
import shutil
import subprocess
import os


def fix_llms_latex(text: str) -> str:
    """LLMが成形するlatexをレンダリング可能な形に修正する"""
    return text.replace("\\\\", "\\")


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
    """latexのテンプレートを返す"""
    latex = f"""
    \\documentclass{{article}}
    \\usepackage{{amsmath}}
    \\usepackage{{fontspec}}  % LuaLaTeXでフォント指定可能
    \\setmainfont{{IPAexMincho}}   % 明朝
    \\setsansfont{{IPAexGothic}}   % ゴシック
    \\usepackage[a4paper,margin=25mm]{{geometry}}

    \\begin{{document}}

    {input}
    \\end{{document}}
    """
    return latex
