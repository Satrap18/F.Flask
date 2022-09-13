from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Flask.db'
db = SQLAlchemy(app)


class Book(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	body = db.Column(db.Text, unique=True, nullable=False)
	date = db.Column(db.DateTime,default=datetime.now)


	def __repr__(self):
		return f'({self.id} - {self.body} - {self.date})'

@app.route('/')
def home():
	books = Book.query.all()
	return render_template('home.html', books=books)

@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/<int:Book_id>')
def detail(Book_id):
	book = Book.query.get(Book_id)
	return render_template('detail.html',book=book)

@app.route('/delete/<int:Book_id>')
def delete(Book_id):
	book = Book.query.get(Book_id)
	db.session.delete(book)
	db.session.commit()
	return redirect(url_for('home'))

if __name__ == '__main__':
	app.run(debug=True)