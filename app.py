from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        n1 = float(request.form['nota1'])
        n2 = float(request.form['nota2'])
        n3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (n1 + n2 + n3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template('ejercicio1.html', promedio=round(promedio, 1), estado=estado)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]
        nombre_largo = max(nombres, key=len)
        cantidad = len(nombre_largo)

        mensaje = "El nombre con mayor cantidad de caracteres es:"
        return render_template('ejercicio2.html', mensaje=mensaje, nombre_largo=nombre_largo, cantidad=cantidad)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)