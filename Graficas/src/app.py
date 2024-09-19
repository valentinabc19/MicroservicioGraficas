from flask import Flask
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.controllers.estudiantesController import estudiante_bp

app = Flask(__name__)

# Registrar blueprints
app.register_blueprint(estudiante_bp)

if __name__ == '__main__':
    app.run(debug=True)