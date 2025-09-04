from flask import Flask, render_template, jsonify, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'banco'

mysql = MySQL(app)

# ---------------------- TEMPLATES

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')

@app.route('/post_user')
def postUserPage():
    return render_template('post.html')

# ---------------------------------- GETs

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

# ------------------------- POST

@app.route('/usuarios', methods=['POST'])
def postUser():
    if request.method == 'POST':
        data = request.get_json()

        nome = data.get('nome')
        cpf = data.get('cpf')
        email = data.get('email')
        senha = data.get('senha')

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO usuario (nome, cpf, email, senha) VALUES (%s, %s, %s, %s)', (nome, cpf, email, senha))
        mysql.connection.commit()

        usuario_id = cur.lastrowid

        cur.execute('SELECT * FROM usuario WHERE id = %s', (usuario_id,))
        new_usuario = cur.fetchone()
        cur.close()

        return jsonify(new_usuario), 201
    else:
        return jsonify({"error": "Method not allowed"}), 405

if __name__ == '__main__':
    app.run(debug=True)