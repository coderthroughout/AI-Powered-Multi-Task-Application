from flask import Blueprint, request, jsonify
from services.image_generation_service import ImageGenerationService
from utils.auth import token_required
from utils.rate_limit import limiter

image_routes = Blueprint('image_routes', __name__)
image_service = ImageGenerationService()


@image_routes.route('/generate-image', methods=['POST'])
@token_required
@limiter.limit("5 per minute")
def generate_image():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    image_url = image_service.generate_image(prompt)
    if image_url:
        return jsonify({"image_url": image_url})
    else:
        return jsonify({"error": "Failed to generate image"}), 500