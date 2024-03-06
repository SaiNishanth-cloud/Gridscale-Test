from flask import Flask, request, jsonify, redirect
from flasgger import Swagger
app = Flask(__name__)
swagger = Swagger(app)

@app.route('/helloworld', methods=['POST'])
def helloworld():
    """
    Hello World API
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
        example:
          name: Nishanth
    responses:
      200:
        description: Hello response
        schema:
          type: object
          properties:
            message:
              type: string
        examples:
          application/json:
            message: Hello Nishanth
    """
    data = request.json
    name = data.get('name', 'World')
    response= {'message':f'Hello {name}'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
