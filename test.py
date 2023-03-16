from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3

app = Flask(__name__)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/destination')
def destination_page():
    return render_template('service.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/politique')
def politique_page():
    return render_template('politique.html')


if __name__ == "__main__":
    app.run()
