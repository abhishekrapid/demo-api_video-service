from extensions import (
    app,
    os
)

from app.controller.service_controller import api
import logging

logging.basicConfig(level=logging.DEBUG)

app.logger.setLevel(logging.INFO)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# register the api
app.register_blueprint(api)

if __name__ == '__main__':
    
    app.run('localhost', 8080, debug=True)
