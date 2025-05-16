# MCP-server
I made a simple MCP server that can response about the due date of course from Moodle.

structure
- config.json: APIキー・URLなどの設定保存
- llm_ollama.py: Ollamaと連携して応答生成
- mcpserver.py
- moodle_api.py: Moodleから課題取得
- main.py: FastAPIアプリ本体
- client.py
- requirments.txt: 必要なPythonライブラリ


if you wanna try it. do following steps...
before starting the following steps, you need intstall ollama mistral, and relevant python lib.
## Python環境セットアップ
pip install -r requirements.txt
## サーバ起動
uvicorn main:app --reload
## クライアント立ち上げ
python3 client.py

# 実行方法
1．3つターミナル立ち上げ
2．各ターミナルで，以下のコマンド実行
  - ollama serve
  - uvicorn main:app --reload
  - python3 client.py
3. クライアント側で質問受付中になるので，質問してみる．例）課題の〆切が近い科目教えて．

