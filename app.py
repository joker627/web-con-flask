from flask import Flask, render_template

app = Flask(__name__)

# rutas de navegacion
@app.route("/")
def home():
    return render_template("index.html")

# Manejador de errores 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)