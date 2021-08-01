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
	<p>Please input Framework <input type="text" name="framework99"></p>
	<p><input type="submit"></p>
	</form>"""

if __name__ == "__main__":
	app.run(debug = True, port = 3000)

# 把 framework02 改為 framework99
# 會發現，由於 表格輸入的資料 = framework99 但是 request.form 想要的資料是 framework02
# 所以 request.form["framework02"] 一直無法取得資料
# 而且因為是使用 [] 格式，無論是否填入資料，提交後必定讓網頁報錯
# werkzeug.exceptions.BadRequestKeyError
# KeyError: 'framework02'
