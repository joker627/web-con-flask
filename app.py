from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Registrando: {username} - {password}")
        return 'Registro enviado'
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(f"Iniciando sesión: {username} - {password}")
        return 'Inicio de sesión enviado'
    return render_template('login.html')


# rutas de navegacion
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/lenguajes")
def lenguajes():
    return render_template("lenguajes.html")

@app.route("/contacto", methods=['GET', 'POST']) 
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        asunto = request.form.get('asunto', 'Sin Asunto')
        mensaje = request.form['mensaje']

        print(f"Mensaje recibido de: {nombre}")
        print(f"Email: {email}")
        print(f"Asunto: {asunto}")
        print(f"Mensaje:\n{mensaje}\n---")

        return "¡Mensaje recibido con éxito! Gracias por contactarnos."
    else:
        return render_template("contacto.html")

@app.route("/politica")
def politica():
    return render_template("politica.html")


# Manejador de errores 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)



