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

@app.route("/form_example", methods=["POST", "GET"]) # localhost:3000/form_example
def form_example():
	if request.method == "POST":
		language03 = request.form.get("language02")
		framework03 = request.form["framework02"]
		return "<p>The language is {}, and the framework is {}.</P>".format(language03, framework03)

	return """<form method="POST"> 
	<p>Please input Language <input type="text" name="language02"></p>
	<p>Please input Framework <input type="text" name="framework02"></p>
	<p><input type="submit"></p>
	</form>"""

if __name__ == "__main__":
	app.run(debug = True, port = 3000)

# 現在要讓表格的輸入和 return 後的頁面做互動
# 順便看看有 .get() 和直接用 [] 的差異
# 為區別每個 language 和 framework 所以便在後面添加 01, 02, 03
# 完成後的表格若不填寫點提交後會顯示以下
# The language is , and the framework is .
# 填寫 Python 和 Flask 後提交會顯示如下
# The language is Python, and the framework is Flask.
