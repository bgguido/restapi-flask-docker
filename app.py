from flask import Flask, jsonify, request
from flasgger import Swagger

app = Flask(__name__)

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Heladería",
        "description": "API para gestionar opciones y gustos de una heladería ficticia",
        "version": "1.0"
    }
}

swagger = Swagger(app, template=swagger_template)

opciones = [
    {'id': 1, 'cantidad': 'kilo', 'precio': '$20000'},
    {'id': 2, 'cantidad': '1/2kilo', 'precio': '$12000'},
    {'id': 3, 'cantidad': '1/4kilo', 'precio': '$7000'},
    {'id': 4, 'cantidad': 'cucurucho', 'precio': '$5000'}
]

gustos = [
    {'id': 1, 'sabor': 'chocolate'},
    {'id': 2, 'sabor': 'vainilla'},
    {'id': 3, 'sabor': 'frutilla'},
    {'id': 4, 'sabor': 'dulce de leche'}
]

"""
@api {get} /opciones Obtener Opciones
@apiName GetOpciones
@apiGroup Opciones
"""
@app.route('/opciones', methods=['GET'])
def get_opciones():
    """
    Obtiene todas las opciones disponibles en la heladeria con sus precios.
    ---
    responses:
      200:
        description: Lista de opciones con precios.
    """
    return jsonify(opciones)

"""

@api {delete} /opciones/<int:opciones_id> Eliminar Opciones
@apiName DeleteOpciones
@apiGroup Opciones
"""
@app.route('/opciones/<int:opciones_id>', methods=['DELETE'])
def delete_opciones(opciones_id):
    """
    Elimina una opción de la heladeria por ID y luego las vuelve a ordenar.
    ---
    parameters:
      - name: opciones_id
        in: path
        type: integer
        required: true
        description: ID de la opción a eliminar.
    responses:
      200:
        description: Opción eliminada correctamente.
      404:
        description: Opción no encontrada.
    """
    global opciones

    for cantidad in opciones:
        if cantidad['id'] == opciones_id:
            opciones.remove(cantidad)
            break

    for index, cantidad in enumerate(opciones, start=1):
        cantidad['id'] = index
    return jsonify(opciones)

"""
@api {put} /opciones/<int:cantidad_id> Actualizar Opciones
@apiName UpdateOpciones
@apiGroup Opciones
"""
@app.route('/opciones/<int:cantidad_id>', methods=['PUT'])
def update_cantidad(cantidad_id):
    """
    Actualiza el precio de una opción de la heladería por ID.
    ---
    parameters:
      - name: cantidad_id
        in: path
        type: integer
        required: true
        description: ID de la opción a actualizar.
      - in: body
        name: body
        schema:
          type: object
          required:
            - precio
          properties:
            precio:
              type: string
              description: El nuevo precio de la opción.
    responses:
      200:
        description: Opción actualizada correctamente.
      404:
        description: Opción no encontrada.
    """
    for cantidad in cantidades:
        if cantidad['id'] == cantidad_id:
            data = request.get_json()
            cantidad['precio'] = data['precio']
            return jsonify(cantidad), 200

"""
@api {post} /opciones Agregar Opciones
@apiName AddOpciones
@apiGroup Opciones
"""
@app.route('/opciones', methods=['POST'])
def add_cantidad():
    """
    Agrega una nueva opción a la heladería.
    ---
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - cantidad
          properties:
            cantidad:
              type: string
              description: La cantidad de la nueva opción.
    responses:
      201:
        description: Opción agregada correctamente.
      400:
        description: Falta el campo cantidad.
    """
    nueva_cantidad = request.get_json()
    if 'cantidad' in nueva_cantidad:
        max_id = max([cantidad['id'] for cantidad in opciones], default=0) + 1
        nueva_cantidad['id'] = max_id
        opciones.append(nueva_cantidad)
        return jsonify(nueva_cantidad), 201
    else:
        return jsonify({'error': 'Falta el campo sabor'}), 400

"""
@api {get} /gustos Obtener Gustos
@apiName GetGustos
@apiGroup Gustos
"""
@app.route('/gustos', methods=['GET'])
def get_gustos():
    """
    Obtiene todos los gustos disponibles en la heladería.
    ---
    responses:
      200:
        description: Lista de gustos.
    """
    return jsonify(gustos)

"""
@api {post} /gustos Agregar Gustos
@apiName AddGustos
@apiGroup Gustos
"""
@app.route('/gustos', methods=['POST'])
def add_gusto():
    """
    Agrega un nuevo gusto a la heladería.
    ---
    parameters:
      - in: body
        name: body
        schema:
          type: object
          required:
            - sabor
          properties:
            sabor:
              type: string
              description: El sabor del nuevo gusto.
    responses:
      201:
        description: Gusto agregado correctamente.
      400:
        description: Falta el campo sabor.
    """
    nuevo_gusto = request.get_json()
    if 'sabor' in nuevo_gusto:
        max_id = max([gusto['id'] for gusto in gustos], default=0) + 1
        nuevo_gusto['id'] = max_id
        gustos.append(nuevo_gusto)


"""
@api {delete} /gustos/<int:gusto_id> Eliminar Gustos
@apiName DeleteGustos
@apiGroup Gustos
"""
@app.route('/gustos/<int:gusto_id>', methods=['DELETE'])
def delete_gusto(gusto_id):
    """
    Elimina un gusto de la heladería por ID y luego los vuelve a ordenar.
    ---
    parameters:
      - name: gusto_id
        in: path
        type: integer
        required: true
        description: ID del gusto a eliminar.
    responses:
      200:
        description: Gusto eliminado correctamente.
      404:
        description: Gusto no encontrado.
    """
    global gustos

    for gusto in gustos:
        if gusto['id'] == gusto_id:
            gustos.remove(gusto)
            break

    for index, gusto in enumerate(gustos, start=1):
        gusto['id'] = index

if __name__ == '__main__':
    app.run(debug=True)
