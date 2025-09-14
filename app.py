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

@app.route('/update_passwd')
def updateUserPasswd():
    return render_template('update.html')

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
    

# ---------------------------- UPDATE

@app.route('/usuarios', methods=['PUT'])
def updateUser():
    data = request.get_json()

    email = data.get('email')
    old_passwd = data.get('old_passwd')
    new_passwd = data.get('new_passwd')

    if not email:
        return jsonify({"error": "Email is required to identify the user"}), 400

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE usuario 
        SET senha = %s
        WHERE email = %s AND senha = %s
    """, (new_passwd, email, old_passwd))

    mysql.connection.commit()

    # Return updated user
    cur.execute("SELECT * FROM usuario WHERE email = %s", (email,))
    updated_user = cur.fetchone()
    cur.close()

    if updated_user:
        return jsonify(updated_user), 200
    else:
        return jsonify({"error": "User not found"}), 404


# ---------------------------------------- DELETE

@app.route("/delete_user", methods=[''])
def deleteUser():
    data = request.get_json()

    cpf = data.get('cpf')
    email = data.get('email')
    senha = data.get('senha')
    
    cur = mysql.connection.cursor()
    cur.execute("""
        DELETE FROM usuario
        WHERE cpf = %s AND email = %s AND senha = %s
    """, (cpf, email, passwd))

    mysql.connection.commit()

if __name__ == '__main__':
    app.run(debug=True)