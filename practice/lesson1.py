# ---- レッスン1: 変数と計算 ----

# 「変数」= 値に名前をつけた箱。「=」は「代入(右の値を左の名前に入れる)」
kabe_atsusa = 300      # 壁の厚さ [mm]
ondo_hajime = 0        # 初期温度 [℃]
ondo_hashi = 1         # 両端の温度 [℃]

# print() で画面に表示できる
print(kabe_atsusa)
print("壁の厚さは", kabe_atsusa, "mm です")

# 変数どうしで計算できる
kabe_m = kabe_atsusa / 1000       # mm → m に変換(割り算は /)
print("メートルだと", kabe_m, "m")

# 計算の基本記号
a = 7
b = 2
print("足し算:", a + b)    # 9
print("引き算:", a - b)    # 5
print("掛け算:", a * b)    # 14
print("割り算:", a / b)    # 3.5
print("2乗:",   a ** 2)    # 49  (** がべき乗)
