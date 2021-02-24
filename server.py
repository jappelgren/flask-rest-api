from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import flask
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect("dbname=python_rest")
cur = conn.cursor()


information_store = ['hello']
@app.route('/information', methods=['GET', 'POST'])
def information():
    
    if request.method == 'GET':
        cur.execute("""SELECT * FROM "information";""")
        conn.commit()
        return jsonify(cur.fetchall())
        
    elif request.method == 'POST':
        cur.execute("""
            INSERT INTO information("information") 
            VALUES (%s)
            """, 
            (request.form.get('information'),))
        conn.commit()
        return  flask.Response(status=201)


@app.route('/information/<the_id>', methods=['DELETE'])
def information_delete(the_id):
    cur.execute("""DELETE FROM "information" WHERE "id" = %s;""", (the_id,))
    conn.commit()
    return flask.Response(status=200)

@app.route('/information/<the_id>', methods=['PUT'])
def information_put(the_id):
    cur.execute("""
    UPDATE information  
    SET "information" = %s
    WHERE id = %s;
    """, (request.form.get('information'), the_id),)
    conn.commit()
    return flask.Response(status=200)

if __name__ == "__main__":
    app.run(debug=True)
