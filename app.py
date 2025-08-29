from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'banco'

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuario")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/livros', methods=['GET'])
def get_livros():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM livro")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/emprestimos', methods=['GET'])
def get_emprestimos():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM emprestimo")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)