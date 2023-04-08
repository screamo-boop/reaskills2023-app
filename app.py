from flask import Flask, request, jsonify
import flask
import socket
import psycopg2
from contextlib import closing
from redis import Redis

name='app'
dbuser='postgres'
dbpassword='P@ssw0rd'
dbhost='postgres'
redis_host = 'redis'

app = Flask(__name__)
hostname = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()

pg_health = False
redis_health = False

@app.route("/")
def run():
    try:
      conn = psycopg2.connect(dbname=name, user=dbuser, password=dbpassword, host=dbhost)
      conn.close()
      pg_health = True
    except:
      pg_health = False
    try:
        r = Redis(redis_host, socket_connect_timeout=1)
        r.ping()
        redis_health = True
    except:
        redis_health = False
    return flask.render_template('app.html', ip=ip, hostname=hostname, redis_health=redis_health, pg_health=pg_health)

@app.route("/films", methods=['GET', 'POST'])
def show_films():
        if request.method == 'POST':
            if request.form['show_films'] == 'Show Films':
                conn = psycopg2.connect(dbname=name, user=dbuser, password=dbpassword, host=dbhost)
                cursor = conn.cursor()
                cursor.execute("SELECT title FROM films;")
                rows = cursor.fetchall()
                mylist = []
                for row in rows:
                    mylist.append(row[0])
                cursor.close()
                conn.close()
                return flask.render_template('films.html', content=mylist)
        else:
            return flask.render_template('app.html', ip=ip, hostname=hostname)
