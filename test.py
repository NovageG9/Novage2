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


def execute_query(connect, query):
    cursor = connect.cursor()
    try:
        cursor.execute(query)
    except EOFError as e:
        print("Error execute query!")
    connect.commit()
    connect.close()


@app.route('/', methods=['GET', 'POST'])
def index_page():
    if 'logged_in' in session.keys() and session['logged_in']:
        return render_template('index.html')
    else:
        query = f'''select idRegion, nomRegion from Region;'''
        list_region = select_donne(connection(), query)
        print(list_region)
        lieu = [{"ville": "Paris", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
                {"ville": "Lille", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
                {"ville": "Nice", "duree": "3 Jours, 4 Nuits", "Prix": "1650"},
                {"ville": "Bordeau", "duree": "3 Jours, 4 Nuits", "Prix": "1650"}]
        return render_template('index.html', lieu=lieu, region=list_region)


@app.route('/destination')
def destination_page():
    con = connection()
    query = f'''select idLieu, nomVille, nomLieu, dureeConseillee, prix from lieu, ville where lieu.idville = ville.idville;'''
    res = select_donne(con, query)
    print(res)
    path = list()
    for i in res:
        url_img = f'assets/images/lieu/{i[0]}.jpg'
        path.append(url_img)
    return render_template('service.html', params=zip(res, path))


@app.route('/search', methods=['POST'])
def search_page():
    if request.form.get('selectpicker') is not None:
        region = request.form.get('selectpicker')
    print(region)
    con = connection()
    query = f'''select distinct idLieu, nomVille, nomLieu, dureeConseillee, prix from lieu, ville, region where lieu.idville = ville.idville and ville.idRegion={region};'''
    res = select_donne(con, query)
    print(res)
    path = list()
    for i in res:
        url_img = f'assets/images/lieu/{i[0]}.jpg'
        path.append(url_img)
    print(path)
    return render_template('service.html',  params=zip(res, path))


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/info', methods=['GET', 'POST'])
def monInfo_page():
    if request.method == "GET":
        con = connection()
        query = f'''select * from utilisateur where mailUti="{session["username"]}"'''
        info_personne = select_donne(con, query)
        print(info_personne)
        return render_template('infos.html', info=info_personne)
    else:
        if request.form.get('newpwd') is not None:
            password = request.form.get('newpwd')
            print("11111111")
        conn = connection()
        query1 = f'''update utilisateur set mdpUti={password} where mailUti= "{session["username"]}"'''
        print(query1)
        execute_query(conn, query1)
        print("adsfasfsadsfafas111111111")
        return redirect(url_for('logout_page'))


@app.route('/detail/<int:lieu_id>')
def detail_page(lieu_id):
    con = connection()
    query = f'''select nomLieu, descLieu, nomVille, idLieu from lieu, ville where lieu.idville = ville.idville and idLieu = {lieu_id};'''
    res = select_donne(con, query)
    print(res)
    path = f'assets/images/lieu/{lieu_id}.jpg'
    print(path)
    return render_template('detail.html', infos=res, path=path)

#
# @app.route('/add_favo/<int:lieu_id>')
# def add_favo(lieu_id):
#

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
        query = f'''select idUti, mailUti, mdpUti from utilisateur where mailUti="{username}" and mdpUti={password};'''
        print(query)
        user_bon = select_donne(con, query)
        print(user_bon)
        if len(user_bon) > 0:
            print("user_bon")
            session['logged_in'] = True
            session['username'] = username
            session['userid'] = user_bon[0][0]
            return redirect(url_for('index_page'))
        else:
            # 显示错误消息
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)


@app.route('/logout', methods=['GET', 'POST'])
def logout_page():
    session['logged_in'] = False
    session.pop('username', None)
    return redirect(url_for('index_page'))


@app.route('/favos', methods=['GET', 'POST'])
def favos_page():
    if request.method == 'GET':
        con = connection()
        query = f'''select  idLieu, nomLieu, nomVille, nomRegion, dureeConseillee, prix from lieu, ville, region 
        where lieu.idville = ville.idville 
        and ville.idRegion=Region.idRegion 
        and  idLieu in 
        (select idLieu 
        from ajouter 
        where idUti = {session['userid']});'''
        list_like = select_donne(con, query)
        print('like:', list_like)
        return render_template('like.html', li=list_like)


@app.route('/delete/<int:favorite_id>', methods=['POST'])
def delete_favorite(favorite_id):
    print('favorite: ', favorite_id)
    con = connection()
    query = f'''delete from ajouter where idLieu={favorite_id} and idUti={session['userid']};'''
    execute_query(con, query)
    return redirect(url_for('favos_page'))


@app.route('/inscrit', methods=['GET', 'POST'])
def inscrit_page():
    if request.method == 'GET':
        return render_template('inscription.html')
    else:
        if request.form.get('input_nom') is not None:
            username = request.form.get('input_nom')
        if request.form.get('input_email') is not None:
            usermail = request.form.get('input_email')
        if request.form.get('input_password') is not None:
            password = request.form.get('input_password')

        query = f'''SELECT idUti FROM utilisateur ORDER BY idUti DESC LIMIT 1;'''
        id = select_donne(connection(), query)
        new_id = id[0][0] + 1
        query1 = f'''insert into utilisateur(idUti,pseudo,mailUti,mdpUti) values ({new_id},"{username}","{usermail}","{password}")'''
        print(query1)
        execute_query(connection(), query1)
        return redirect(url_for('login_page'))


if __name__ == "__main__":
    app.run()
