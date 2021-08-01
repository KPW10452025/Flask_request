from flask import Flask, request

app = Flask(__name__)

@app.route("/query_example")
def query_example():
	request
	return "Todo ..."

if __name__ == "__main__":
	app.run(debug = True, port = 3000)

# 目前用 Flask 簡單建立一個頁面，網址為 localhost:3000/query_example
# 要練習的項目為在網址中加入文字如下
# localhost:3000/query_example?key1=value1&key2=value2
# 加入這些文字時，必須使用問號當作開頭
