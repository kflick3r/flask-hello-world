import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Kassidy Flick in 3308'

@app.route('/dbtest')
def testing():
    conn = psycopg2.connect("postgresql://bballdb_d19c_user:ebReQb5RR3oxhiVHYbAo4Dl20rN0qkZj@dpg-d7akms6slomc73dva49g-a/bballdb_d19c")

    conn.close()
    return "Database Connection Successful"