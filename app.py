from flask import Flask, request

app = Flask(__name__)

@app.route("/query_example")
def query_example():
	language01 = request.args.get("language")
	return "The language is : {}".format(language01)

if __name__ == "__main__":
	app.run(debug = True, port = 3000)

# 目前用 Flask 簡單建立一個頁面，網址為 localhost:3000/query_example
# 要練習的項目為在網址中加入文字如下
# localhost:3000/query_example?key1=value1&key2=value2
# 加入這些文字時，必須使用問號當作開頭
# 這時就能使用 request 達成需求
# language01 = request.args.get("language")
# return "The language is : {}".format(language01)
# 這時再次刷新瀏覽器網頁會顯示，網址為 localhost:3000/query_example
# 網頁會顯示 The language is : None
# 將網址 localhost:3000/query_example 後面加問號 ? 後再加上 language=Python
# localhost:3000/query_example?language=Python
# 頁面刷新後會得到
# The language is : Python