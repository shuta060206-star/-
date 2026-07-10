"""一次元非定常熱伝導方程式の数値解(陽解法・有限差分法)

課題: 厚さ300mmのコンクリート壁。初期温度0℃。t>0で両端が常に1℃。
3分・30分・2時間・4時間・8時間・12時間後の壁内温度分布をグラフに描く。

実行方法: python heat_conduction.py  (heat_conduction.png が生成される)
"""

import numpy as np
import matplotlib.pyplot as plt

# ---- 計算条件(定数) ----
WALL_THICKNESS = 0.3      # 壁厚 L [m]
CONDUCTIVITY = 1.6        # 熱伝導率 λ [W/(m·K)]
DENSITY = 2200            # 密度 ρ [kg/m³]
SPECIFIC_HEAT = 880       # 比熱 c [J/(kg·K)]
EDGE_TEMP = 1.0           # 境界温度 [℃]
N_DIVISIONS = 30          # 空間分割数
DT = 20                   # 時間刻み [s]
STABILITY_LIMIT = 0.5     # 陽解法の安定条件: r <= 0.5

# グラフに残す時刻 [s] とラベル
RECORD_TIMES = {
    3 * 60: "3 min",
    30 * 60: "30 min",
    2 * 3600: "2 h",
    4 * 3600: "4 h",
    8 * 3600: "8 h",
    12 * 3600: "12 h",
}


def thermal_diffusivity(lam: float, rho: float, c: float) -> float:
    """熱拡散率 a = λ/(ρc) [m²/s]"""
    return lam / (rho * c)


def simulate() -> tuple:
    """12時間後までの温度分布を計算し、(x座標, {ラベル: 分布}) を返す"""
    a = thermal_diffusivity(CONDUCTIVITY, DENSITY, SPECIFIC_HEAT)
    dx = WALL_THICKNESS / N_DIVISIONS
    r = a * DT / dx ** 2
    if r > STABILITY_LIMIT:
        raise ValueError(f"不安定な条件です: r = {r:.3f} > {STABILITY_LIMIT}")

    x = np.linspace(0, WALL_THICKNESS, N_DIVISIONS + 1)
    T = np.zeros(N_DIVISIONS + 1)     # 初期条件: 全点0℃
    T[0] = T[-1] = EDGE_TEMP          # 境界条件: 両端1℃

    snapshots = {}
    total_steps = int(max(RECORD_TIMES) / DT)
    for step in range(1, total_steps + 1):
        T_new = T.copy()
        T_new[1:-1] = T[1:-1] + r * (T[:-2] - 2 * T[1:-1] + T[2:])
        T = T_new
        t_now = step * DT
        if t_now in RECORD_TIMES:
            snapshots[RECORD_TIMES[t_now]] = T.copy()
    return x, snapshots


def plot_result(x, snapshots, filename: str = "heat_conduction.png"):
    """時刻ごとの温度分布を1枚のグラフに描いて保存する"""
    for label, T in snapshots.items():
        plt.plot(x * 1000, T, marker="o", markersize=3, label=label)
    plt.xlabel("x [mm]")
    plt.ylabel("T [C]")
    plt.title("1D transient heat conduction in a 300 mm concrete wall")
    plt.legend()
    plt.grid(True)
    plt.ylim(0, 1.05)
    plt.savefig(filename, dpi=150)
    plt.show()


def main():
    x, snapshots = simulate()
    plot_result(x, snapshots)
    print("計算完了: heat_conduction.png を保存しました")


if __name__ == "__main__":
    main()
