from flask import Flask
from flask_cors import CORS
from routes.chat_routes import chat_routes
from routes.query_routes import query_routes
from routes.image_routes import image_routes
from routes.video_routes import video_routes
from routes.writing_routes import writing_routes
from routes.document_routes import document_routes
from utils.error_handler import setup_error_handling
from utils.rate_limit import limiter

app = Flask(__name__)
CORS(app)
limiter.init_app(app)

app.register_blueprint(chat_routes)
app.register_blueprint(query_routes)
app.register_blueprint(image_routes)
app.register_blueprint(video_routes)
app.register_blueprint(writing_routes)
app.register_blueprint(document_routes)

setup_error_handling(app)

if __name__ == '__main__':
    app.run(debug=True)