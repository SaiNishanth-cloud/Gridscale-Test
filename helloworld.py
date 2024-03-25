from datetime import datetime
from flask import Flask, request, jsonify, redirect
from flasgger import Swagger
import logging
app = Flask(__name__) # Creates  a new Flask web server.
swagger = Swagger(app) 

logging.basicConfig(filename='/var/log/containers/app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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

    # Log the API call
    user_id = request.headers.get('User-ID', 'Unknown')
    api_endpoint = '/helloworld'
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"User {user_id} called {api_endpoint} at {timestamp}")

    response= {'message':f'Hello {name}'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
