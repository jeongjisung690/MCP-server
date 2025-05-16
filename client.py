import requests

def main():
    print("=== MCP CLI Client ===")
    print("質問を入力してください（例：〆切が近い課題を教えて）")
    print("終了するには 'exit' または 'quit' と入力")

    while True:
        user_input = input(">> ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("終了します。")
            break

        try:
            # サーバに問い合わせ（GETではなくPOSTに変更してもOK）
            response = requests.get("http://localhost:8000/ask")
            response.raise_for_status()
            reply = response.json()["response"]
            print("応答：", reply)
        except Exception as e:
            print("エラーが発生しました:", str(e))

if __name__ == "__main__":
    main()
