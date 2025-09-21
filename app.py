from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista inicial de tareas
tareas = ["Aprender Python", "Crear un entregable", "Practicar Flask"]

@app.route("/")
def index():
    return render_template("index.html", tareas=tareas)

# Agregar tarea
@app.route("/agregar", methods=["POST"])
def agregar():
    nueva_tarea = request.form.get("tarea")
    if nueva_tarea:
        tareas.append(nueva_tarea)
    return redirect("/")

# Eliminar tarea
@app.route("/eliminar/<int:indice>")
def eliminar(indice):
    if 0 <= indice < len(tareas):
        tareas.pop(indice)
    return redirect("/")

# Editar tarea
@app.route("/editar/<int:indice>", methods=["POST"])
def editar(indice):
    nueva_tarea = request.form.get("tarea")
    if nueva_tarea and 0 <= indice < len(tareas):
        tareas[indice] = nueva_tarea
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
