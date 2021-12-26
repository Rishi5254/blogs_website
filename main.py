from flask import Flask , render_template
import requests

app = Flask(__name__)

response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
data = response.json()



@app.route("/")
def homepage():
    return render_template("index.html", data=data)


@app.route("/about")
def about_page():
    return render_template("about.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def post_page(num):
    return render_template("post.html", data=data[num-1])


if __name__ == "__main__":
    app.run(debug=True)

