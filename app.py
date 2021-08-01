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

@app.route("/form_example", methods=["POST", "GET"])
def form_example():
	if request.method == "POST":
		return "<p>Submitted Form</P>"

	return """<form method="POST"> 
	<p>Please input Language <input type="text" name="language"></p>
	<p>Please input Framework <input type="text" name="framework"></p>
	<p><input type="submit"></p>
	</form>"""

if __name__ == "__main__":
	app.run(debug = True, port = 3000)

# 目前只要點選提交後，頁面都會轉換到 Method Not Allowed
# 在 route 中添加 methods=["POST", "GET"]
# 並用 if 判斷 request.method 是否為 POST 是的話頁面顯示 Submitted Form
# 重新開啟 localhost:3000/form_example 後，現在按下提交會就會出現已設定好的 Submitted Form
