# 非定常熱伝導 — Python学習&課題リポジトリ

Pythonをゼロから学ぶためのリポジトリです。目標は2つ:

1. **課題**: 一次元非定常熱伝導方程式を自分でプログラミングして解く
2. **その先**: プログラミングの中核構文を一通り身につけ、実務で書かれるコードを読める・書けるようになる

## 📚 フォルダ案内

| 場所 | 中身 |
|------|------|
| `docs/colab-no-hajimekata.md` | **まずこれ!** Google Colabの始め方 |
| `docs/pc-setup.md` | PCにPython + VS Codeを入れる手順(Windows/Mac) |
| `lessons/` | レッスンノートブック(Colabで開いて自分で実行する教材) |
| `practice/` | 練習用の小さなスクリプト置き場 |
| `kadai/` | 課題本体(熱伝導方程式)をここに作っていく |

## 🗺️ 学習ロードマップ

**全12レッスン公開済み。** 各レッスンはColabで開いて自分で実行しながら進める形式です(開き方は `docs/colab-no-hajimekata.md`)。終わった答案は `mywork/` に保存 → Claudeが添削。

### 第1部: 中核構文を身につけて課題を解く

- [x] 環境の準備(Colab / PC)
- [x] レッスン1: 変数・print・計算 → `lessons/lesson01_hajimete.ipynb`
- [ ] レッスン2: リストとforループ → `lessons/lesson02_list_loop.ipynb`
- [ ] レッスン3: if文と関数 → `lessons/lesson03_if_function.ipynb`
- [ ] レッスン4: numpy(配列計算) → `lessons/lesson04_numpy.ipynb`
- [ ] レッスン5: matplotlib(グラフ描画) → `lessons/lesson05_matplotlib.ipynb`
- [ ] レッスン6: 熱伝導方程式の差分法 → `lessons/lesson06_heat_equation.ipynb`
- [ ] **課題完成**(お手本: `kadai/heat_conduction.py`、結果: `kadai/heat_conduction.png`)

### 第2部: 実務のコードが読める・書けるようになる

- [ ] レッスン7: 辞書・タプル・文字列 → `lessons/lesson07_dict_tuple_string.ipynb`
- [ ] レッスン8: エラーと例外処理 → `lessons/lesson08_errors.ipynb`
- [ ] レッスン9: ファイル読み書きとモジュール → `lessons/lesson09_files_modules.ipynb`
- [ ] レッスン10: クラスとオブジェクト指向 → `lessons/lesson10_class_oop.ipynb`
- [ ] レッスン11: 実務の作法(PEP 8・命名・docstring・型ヒント) → `lessons/lesson11_clean_code.ipynb`
- [ ] レッスン12: Git/GitHubの基本 → `lessons/lesson12_git_github.ipynb`
- [ ] 卒業課題: 実際のオープンソースコードを読んで構造を説明する(レッスン12末尾参照)

## 🎯 課題の内容

> 厚さ300mmのコンクリート壁。初期温度は全体0℃。時刻 t>0 で両端が常に1℃になったとき、壁内部の温度分布の時間変動を計算せよ。
> 3分後・30分後・2時間後・4時間後・8時間後・12時間後の温度分布のグラフを描くこと。
