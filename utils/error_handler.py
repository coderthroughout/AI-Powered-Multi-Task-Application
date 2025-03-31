import logging
from flask import jsonify

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def handle_error(error):
    logger.error(f"An error occurred: {str(error)}")
    return jsonify({"error": "An internal server error occurred"}), 500


def setup_error_handling(app):
    app.register_error_handler(Exception, handle_error)
