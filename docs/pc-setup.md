# PCにPython + VS Code をセットアップする 🛠️

本格的な開発環境を自分のPCに作る手順です。所要時間は30分〜1時間。
Colabで学習を進めながら、空いた時間にゆっくりやればOKです。
詰まったら、エラーメッセージや画面の状況をClaudeに送ってください。

---

## Windows の場合

### 1. Python をインストール

1. https://www.python.org/downloads/ を開き、黄色い「Download Python 3.x.x」ボタンでインストーラをダウンロード
2. インストーラを起動したら、**最初の画面で必ず「Add python.exe to PATH」にチェック** ✅(これを忘れると後で面倒!)
3. 「Install Now」をクリック

確認: スタートメニューから「PowerShell」を開いて次を打つ。バージョンが表示されれば成功。

```
python --version
```

### 2. VS Code をインストール

1. https://code.visualstudio.com/ から「Download for Windows」
2. インストーラの選択肢はぜんぶデフォルトでOK

### 3. VS Code の拡張機能を入れる

VS Code を起動し、左端の四角いアイコン(拡張機能)から以下を検索してインストール:

- **Python**(Microsoft製)— Pythonを動かすための必須拡張
- **Japanese Language Pack**(Microsoft製)— メニューの日本語化(お好みで)
- **Jupyter**(Microsoft製)— Colabと同じノートブック形式をVS Code内で使える

### 4. ライブラリをインストール

PowerShell で:

```
pip install numpy matplotlib
```

### 5. 動作確認

1. デスクトップなどに `renshuu` フォルダを作り、VS Code で「ファイル」→「フォルダーを開く」
2. 新しいファイル `test.py` を作って以下を書く:

```python
print("環境構築せいこう!")
```

3. 右上の ▶(実行)ボタンをクリック。下のターミナルに表示されたら完了 🎉

---

## Mac の場合

### 1. Python をインストール

Macには古いPythonが入っていることがありますが、最新版を入れます。

1. https://www.python.org/downloads/ から macOS 用インストーラをダウンロードして実行(選択肢はデフォルトでOK)

確認: 「ターミナル」アプリ(Launchpad → その他 → ターミナル)で:

```
python3 --version
```

### 2. VS Code をインストール

1. https://code.visualstudio.com/ から「Download for Mac」
2. ダウンロードした zip を展開し、Visual Studio Code.app を「アプリケーション」フォルダにドラッグ

### 3. 拡張機能(Windowsと同じ)

- **Python** / **Japanese Language Pack** / **Jupyter**

### 4. ライブラリをインストール

ターミナルで:

```
pip3 install numpy matplotlib
```

### 5. 動作確認(Windowsの手順5と同じ)

※ Macでは `python` ではなく `python3`、`pip` ではなく `pip3` と打つ点だけ注意。

---

## よくあるつまずき

| 症状 | 原因と対処 |
|------|-----------|
| `python は認識されません` (Windows) | PATHチェックを忘れた。Pythonをアンインストール→チェックを入れて再インストールが早い |
| `pip install` が失敗する | `python -m pip install numpy matplotlib` を試す |
| ▶ ボタンで実行できない | VS Code左下のPythonバージョン表示をクリックし、インストールしたPythonを選択する |
| グラフが表示されない | スクリプト末尾に `plt.show()` が必要(レッスンで説明します) |
