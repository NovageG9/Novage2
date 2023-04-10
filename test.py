import os
from flask import Flask, render_template, request, session, url_for, redirect
import sqlite3

app = Flask(__name__)
app.secret_key = 'asdgagerger2dfg224t2'


def connection():
    if not os.path.exists('db/novage_db.sqlite3'):
        print(f"Le fichier {'db/novage_db.sqlite3'} n'existe pas")
        connection = None
    else:
        try:
            connection = sqlite3.connect('db/novage_db.sqlite3')
            print("Connection to SQLite réussi")
        except OSError as e:
            print(f"The error {e} occured")
    return connection


def select_donne(connect, query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
    except EOFError as e:
        print("Error execute query!")
    result = cursor.fetchall()
    connect.close()
    return result


@app.route('/', methods=['GET', 'POST'])
def index_page():
    if 'logged_in' in session.keys():
        if session['logged_in']:
            lieu = [{"ville": "Paris", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
                    {"ville": "Lille", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
                    {"ville": "Nice", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
                    {"ville": "Bordeau", "duree": "3 Jours, 4 Nuits", "Prix": "1650"}, ]
            return render_template('service.html', lieu=lieu, username=session['username'])
    else:
        return render_template('index.html')


@app.route('/destination')
def destination_page():
    # con = connection()
    # if 'logged_in' in session.keys():
    #     lieu = [{"ville": "Paris", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Lille", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Nice", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Bordeau", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Paris", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Lille", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Nice", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Bordeau", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Paris", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Lille", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Nice", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
    #             {"ville": "Bordeau", "duree": "3 Jours, 4 Nuits", "Prix": "1650"}]
    # else:
    # query = '''select '''

    return render_template('service.html', lieu=lieu)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/detail')
def detail_page():
    detail = [{"lieu": "Ile de france", "ville": "Paris, Fr",
               "descrip": "Une région historique et administrative française. ",
               "history": "Ancienne « terre des Francs » où bon nombre de châteaux ont été construits pour les rois et les seigneurs,"
                          "Paris et sa région allie un patrimoine culturel, historique et gastronomique exceptionnel. C'est Paris avec ses quais, ses vieux quartiers, "
                          "sa beauté célébrée dans le monde entier, ce sont Versailles et son château, les bords de Marne et ses guinguettes, Chantilly et ses courses, "
                          "la vallée de Chevreuse avec ses forêts et ses abbayes, Provins et sa cité médiévale classée au patrimoine mondial de l'Unesco, la Roche-Guyon....."}]
    return render_template('detail.html', infos=detail)


@app.route('/politique')
def politique_page():
    return render_template('politique.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'GET':
        print("asdgasdgsagfsdgdfsgfdsgdfssddfshfdh")
        return render_template('login.html')
    else:
        if request.form.get('email') is not None:
            username = request.form['email']
        if request.form.get('pwd') is not None:
            password = request.form['pwd']

        print(username, password)
        con = connection()
        query = f'''select mailUti, mdpUti from utilisateur where mailUti="{username}" and mdpUti={password};'''
        print(query)
        user_bon = select_donne(con, query)
        print(user_bon)
        if user_bon is not None:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('index_page'))
        else:
            # 显示错误消息
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)


@app.route('/inscrit')
def inscrit_page():
    return render_template('inscription.html')


if __name__ == "__main__":
    app.run()
