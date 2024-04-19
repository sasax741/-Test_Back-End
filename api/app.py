from flask import Flask
import os
from routes.routes_crud import bp as routes_crud

app = Flask(__name__)

# Registra el blueprint en la aplicación
app.register_blueprint(routes_crud)

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT_SCRAPING', 80))
    app.run(host='0.0.0.0', port=PORT)