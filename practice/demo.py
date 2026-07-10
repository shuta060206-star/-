# はじめてのPython: 変数と計算とループ
L = 0.3        # 壁の厚さ [m]
n = 10         # 分割数

dx = L / n     # 分割幅 [m]
print("壁の厚さ:", L, "m")
print("分割幅 dx =", dx, "m =", dx * 1000, "mm")

# ループの練習: 各点の位置を表示
for i in range(n + 1):
    x = i * dx
    print(f"点{i}: x = {x*1000:.0f} mm")
