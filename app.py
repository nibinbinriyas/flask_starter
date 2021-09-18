from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration")
def registration():
    return render_template("register.html")

@app.route('/courses')
def course():
    return render_template("course.html")

@app.route('/courses/course1')
def course1():
    return render_template('course1.html')

@app.route('/courses/course2')
def course2():
    return render_template('course2.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')