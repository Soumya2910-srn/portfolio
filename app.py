from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
     return render_template("home.html",title="Home")

@app.route("/about")
def about():
     return render_template("about.html",title="About")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
