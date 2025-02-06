
''' Primero ejecuta python app.py en terminal
    El puerto de flask 127.0.0.1:5000 se pone en el navegador '''

from flask import Flask, render_template, request
 
app = Flask(__name__)
 
@app.route('/')
def index():
    # Página principal con un formulario para pedir un dato al usuario
    return '''
<!doctype html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Formulario</title>
</head>
<body>
<h1>Introduce un dato</h1>
<form action="/submit" method="post">
<label for="dato">Dato:</label>
<input type="text" id="dato" name="dato" required>
<button type="submit">Enviar</button>
</form>
</body>
</html>
    '''
 
@app.route('/submit', methods=['POST'])
def submit():
    # Recoge el dato enviado por el usuario
    dato = request.form.get('dato')
    return f'''<h1>Dato recibido</h1>
<p>El dato que enviaste es: <strong>{dato}</strong></p>
<a href="/">Volver</a>'''
 
if __name__ == '__main__':
    app.run(debug=True) 