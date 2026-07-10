# はじめてのPython: 変数と計算とループ
atsusa = 0.3        # 壁の厚さ [m]
bunkatsu = 10       # 何分割するか

dx = atsusa / bunkatsu
print("壁の厚さ:", atsusa, "m")
print("分割幅 dx =", dx, "m =", dx * 1000, "mm")

# ループの練習: 各点の位置を表示
for i in range(bunkatsu + 1):
    x = i * dx
    print(f"点{i}: x = {x*1000:.0f} mm")
