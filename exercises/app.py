from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/<int:student_id>/')
def display_student(student_id):
	student = query_by_id(student_id)
	name = student.name
	year = student.year
	finished = student.finished_lab
	return render_template(
		"student.html",
		student_id = student_id,
		name = name,
		year = year,
		finished = finished
		)

app.run(debug=True)
