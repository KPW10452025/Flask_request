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

@app.route("/form_example")
def form_example():
	return """<form method="POST"> 
	<p>Please input Language <input type="text" name="language"></p>
	<p>Please input Framework <input type="text" name="framework"></p>
	<p><input type="submit"></p>
	</form>"""

if __name__ == "__main__":
	app.run(debug = True, port = 3000)

# 運用 form 製作表格
# 在瀏覽輸入網址 localhost:3000/form_example 便能看到兩行填寫表格和一個提交資料的按鈕
# 但目前只要點選提交後，頁面都會轉換到 Method Not Allowed
