from flask import Flask, render_template, request, redirect, flash # pyright: ignore[reportMissingImports]
from flask_sqlalchemy import SQLAlchemy # pyright: ignore[reportMissingImports]
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
# Database setup: SQLite file named 'database.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# DATABASE MODEL: Contact Messages
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

# DATABASE MODEL: Products
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(100), nullable=False)

# ROUTES
@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    content = request.form.get('message')

    if name and email and content:
        new_message = Message(name=name, email=email, content=content)
        db.session.add(new_message)
        db.session.commit()
        return "Message Sent Successfully! We will contact you at " + email
    return "Please fill out all fields."

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # Creates the database tables
    app.run(debug=True)