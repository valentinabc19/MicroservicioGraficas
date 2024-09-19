from flask import Blueprint, jsonify, request
from src.models.cursosModel import obtener_notas_estudiante
from src.services.graficoService import generar_grafico_promedio_estudiante

estudiante_bp = Blueprint('estudiante_bp', __name__)

@estudiante_bp.route('/estudiante/<string:correo>/grafico-promedio', methods=['GET'])
def obtener_grafico_promedio(correo):
    notas = obtener_notas_estudiante(correo)
    if notas:
        grafico_path = generar_grafico_promedio_estudiante(notas)
        return jsonify({"grafico": grafico_path}), 200
    else:
        return jsonify({"error": "No se encontraron datos"}), 404
