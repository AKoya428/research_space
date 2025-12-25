from math_verify import parse, verify

q1 = "以下の手順で求めます。\n\n1. 原点まわりに角度 $\\theta$ 回転する回転行列は\n\\[\nR(\\theta)=\n\\begin{pmatrix}\n\\cos\\theta & -\\sin\\theta\\\\\n\\sin\\theta & \\cos\\theta\n\\end{pmatrix}\n\\]\nである。\n\n2. 今回は $\\theta=90^\\circ=\\frac{\\pi}{2}$ なので，$\\cos\\frac{\\pi}{2}=0,\\ \\sin\\frac{\\pi}{2}=1$ より\n\\[\nR\\!\\left(\\frac{\\pi}{2}\\right)=\n\\begin{pmatrix}\n0 & -1\\\\\n1 & \\,0\n\\end{pmatrix}.\n\\]\n\n3. 与えられたベクトル $\\mathbf{x}=\\begin{pmatrix}3\\\\1\\end{pmatrix}$ に作用させると\n\\[\n\\mathbf{y}=R\\!\\left(\\frac{\\pi}{2}\\right)\\mathbf{x}\n=\n\\begin{pmatrix}\n0 & -1\\\\\n1 & 0\n\\end{pmatrix}\n\\begin{pmatrix}\n3\\\\\n1\n\\end{pmatrix}\n=\n\\begin{pmatrix}\n-1\\\\\n3\n\\end{pmatrix}.\n\\]\n\nしたがって，求める回転後のベクトルは\n\\[\n\\boxed{\\begin{pmatrix}-1\\\\3\\end{pmatrix}}\n\\]"
q2 = "ステップ1：原点まわりに角度 $\\theta$ だけ回転する回転行列は\n\\[\nR(\\theta)=\n\\begin{pmatrix}\n\\cos\\theta & -\\sin\\theta\\\\\n\\sin\\theta & \\cos\\theta\n\\end{pmatrix}\n\\]\nです。\n\nステップ2：$\\theta=90^\\circ=\\frac{\\pi}{2}$ のとき，$\\cos\\frac{\\pi}{2}=0,\\ \\sin\\frac{\\pi}{2}=1$ なので\n\\[\nR\\left(\\frac{\\pi}{2}\\right)=\n\\begin{pmatrix}\n0 & -1\\\\\n1 & 0\n\\end{pmatrix}.\n\\]\n\nステップ3：$\\mathbf{x}=(3,1)$ を回転行列で変換すると\n\\[\nR\\left(\\frac{\\pi}{2}\\right)\\mathbf{x}\n=\n\\begin{pmatrix}\n0 & -1\\\\\n1 & 0\n\\end{pmatrix}\n\\begin{pmatrix}\n3\\\\\n1\n\\end{pmatrix}\n=\n\\begin{pmatrix}\n-1\\\\\n3\n\\end{pmatrix}.\n\\]\n\nゆえに，求める回転後のベクトルは\n\\[\n\\boxed{(-1,\\,3)}\n\\]"

qp1 = parse(q1)
qp2 = parse(q2)
print(qp1)
print(qp2)
print(verify(qp1, qp2))
