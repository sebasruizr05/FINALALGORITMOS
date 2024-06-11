from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return '¡Hola mundo! Esta es la página de inicio de mi aplicación.'

@app.route('/contact', methods=['POST'])
def contact():
    try:
        data = request.json
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")
        
        # Lógica de procesamiento de datos
        
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
