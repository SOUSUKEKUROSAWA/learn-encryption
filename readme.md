# Learning Encryption By Python
- https://amzn.asia/d/6lmkgDx
## create venv
- ターミナルを開く
- `python -m venv venv`
- `touch .gitignore`
- `vim .gitignore`
- i
- `venv/`
- esc
- :wq
- Ctrl + Shift + p
- `select interpreter`
  - venvとつく方のインタープリタを選択
- `Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process`
  - ポリシーを一時的に変更し，スクリプトの実行を許可
- `. venv/Scripts/activate`
- `deactivate`
  - 仮想環境の非アクティブ化
# unittest
- `python -m unittest discover`