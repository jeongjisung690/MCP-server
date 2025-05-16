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
# モデルを起動（別ターミナル）
ollama run mistral

# Python環境セットアップ
pip install -r requirements.txt

# サーバ起動
uvicorn main:app --reload
