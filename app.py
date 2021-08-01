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
	<p>Please input Language <input type="text" name="language99"></p>
	<p>Please input Framework <input type="text" name="framework02"></p>
	<p><input type="submit"></p>
	</form>"""

if __name__ == "__main__":
	app.run(debug = True, port = 3000)

# 現在來測試 .get() 和直接用 [] 的差異
# 首先把 language02 改為 language99
# 會發現，由於 表格輸入的資料 = language99 但是 request.form 想要 get 的資料是 language02
# 所以 request.form.get("language02") 一直無法取得資料
# 點下提交後永遠都會顯示 The language is None 無論是否有無在第一個表格放入資料
