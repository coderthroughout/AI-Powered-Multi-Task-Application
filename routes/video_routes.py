from flask import Blueprint, request, jsonify
from services.video_generation_service import VideoGenerationService
from utils.auth import token_required
from utils.rate_limit import limiter

video_routes = Blueprint('video_routes', __name__)
video_service = VideoGenerationService()


@video_routes.route('/generate-video', methods=['POST'])
@token_required
@limiter.limit("2 per minute")
def generate_video():
    data = request.json
    template_id = data.get('template_id')
    modifications = data.get('modifications')
    if not template_id or not modifications:
        return jsonify({"error": "Template ID and modifications are required"}), 400

    video_url = video_service.generate_video(template_id, modifications)
    if video_url:
        return jsonify({"video_url": video_url})
    else:
        return jsonify({"error": "Failed to generate video"}), 500