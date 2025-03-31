from flask import Blueprint, request, jsonify
from services.writing_service import WritingService
from utils.auth import token_required
from utils.rate_limit import limiter

writing_routes = Blueprint('writing_routes', __name__)
writing_service = WritingService()


@writing_routes.route('/generate-text', methods=['POST'])
@token_required
@limiter.limit("10 per minute")
def generate_text():
    data = request.json
    prompt = data.get('prompt')
    max_tokens = data.get('max_tokens', 500)
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    generated_text = writing_service.generate_text(prompt, max_tokens)
    if generated_text:
        return jsonify({"generated_text": generated_text})
    else:
        return jsonify({"error": "Failed to generate text"}), 500