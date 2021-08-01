from flask import Flask, request

app = Flask(__name__)

@app.route("/query_example")
def query_example():
	language01 = request.args.get("language")
	framework01 = request.args["framework"]
	website01 = request.args.get("website")

	return """<p>The language is : {}</p>
	          <p>The framework is : {}<p>
	          <p>The website is : {}<p>""".format(language01, framework01, website01)

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

# 比較 request.args.get() 和 request.args[] 差異
# 這次更新的編碼有 language01, framework01, website01
# 在瀏覽器輸入網址如下
# http://localhost:3000/query_example?language=Python&framework=Flask&website=http://localhost:3000/query_example
# 頁面刷新後會得到
# The language is : Python
# The framework is : Flask
# The website is : http://localhost:3000/query_example
# 試著移除網址中的 &website=http://localhost:3000/query_example 後網址如下
# http://localhost:3000/query_example?language=Python&framework=Flask
# 頁面刷新後會得到
# The language is : Python
# The framework is : Flask
# The website is : None
# 從中得知，因為網址中沒有 website
# 函式中的 request.args.get("website") 便無法生成 website01
# return 出來的結果顯示 None
# 現在在試著移除網址中的 &framework=Flask 後網址如下
# http://localhost:3000/query_example?language=Python
# 頁面刷新後會得到 BadRequestKeyError
# 能看到 KeyError: 'framework'
# 小結，request.args.get() 和 request.args[] 的差異
# 由 request.args.get() 能選擇性的獲得數據，即使沒獲得數據系統也不會崩潰
# 而 request.args[] 就是較強制性必須要獲得數據，沒有獲得數據就會立馬報錯
