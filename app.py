from flask import Flask,render_template,redirect,url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "inisecreatkey2020"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/redirect-about')
def ayo_redirect_about():
    return redirect(url_for('about'))
if __name__ == "__main__":
    app.run(debug=True,port=5001)
