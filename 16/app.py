from flask import Flask, render_template_string
app = Flask(__name__)
todos = ["Finish SE Lab", "Learn Docker", "Push to GitHub"]
HTML = '<html><body><h2>My To-Do List</h2><ul>{% for i in items %}<li>{{i}}</li>{% endfor %}</ul></body></html>'
@app.route("/")
def index(): return render_template_string(HTML, items=todos)
if __name__ == "__main__": app.run(host="127.0.0.1", port=5000)
