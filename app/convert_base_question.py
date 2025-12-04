import json

QUESTION_THEMAS_TRANSRATE = {
    "平面ベクトル": "plane_vectors",
    "空間ベクトル": "spatial_vectors",
    "写像の定義": "definition_of_mapping",
    "空間内の直線": "line_in_space",
    "平面の方程式": "plane_equation",
    "数ベクトル空間": "vector_spaces",
    "正則行列": "invertible_matrices",
    "一次写像・一次変換": "linear_maps_transformations",
    "行列の定義": "matrix_definition",
    "行列の演算（和・スカラー倍・積・性質・べき乗）": "matrix_operations",
    "基本行列": "elementary_matrices",
    "連立一次方程式と拡大係数行列": "linear_systems_augmented_matrices",
    "行列の基本変形と簡約化": "matrix_row_operations_reduction",
    "行列の階数": "matrix_rank",
    "掃き出し法による連立一次方程式の解法": "gaussian_elimination",
    "逆行列": "inverse_matrices",
    "行列式の計算（2次・3次）": "determinants_2x2_3x3",
    "行列式の性質": "determinant_properties",
    "余因子展開": "cofactor_expansion",
    "クラーメルの公式": "cramers_rule",
}
to_japanese = {v: k for k, v in QUESTION_THEMAS_TRANSRATE.items()}

with open("data/input/base_questions.json") as f:
    data = json.load(f)

save_data = []
for thema, problem in data.items():
    for _, question in problem.items():
        input_data = {
            "thema": to_japanese[thema],
            "question": question,
        }
        save_data.append(input_data)

with open("base_questions.json", "w", encoding="utf-8") as f:
    json.dump(save_data, f, ensure_ascii=False, indent=4)