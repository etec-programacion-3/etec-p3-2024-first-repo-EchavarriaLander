from flask import Flask

app=Flask(__name__)

@app.route("/hola")
def hola():
    return "hola mundo"

@app.route("/chau")
def goodbye():
    return "chau"

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f"Hola {nombre}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)

app.run()