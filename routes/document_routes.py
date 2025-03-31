from flask import Blueprint, request, jsonify
from services.document_analysis_service import DocumentAnalysisService
from utils.auth import token_required
from utils.rate_limit import limiter

document_routes = Blueprint('document_routes', __name__)
document_service = DocumentAnalysisService()


@document_routes.route('/analyze-document', methods=['POST'])
@token_required
@limiter.limit("5 per minute")
def analyze_document():
    data = request.json
    document_content = data.get('document_content')
    query = data.get('query')
    if not document_content or not query:
        return jsonify({"error": "Document content and query are required"}), 400

    analysis = document_service.analyze_document(document_content, query)
    if analysis:
        return jsonify({"analysis": analysis})
    else:
        return jsonify({"error": "Failed to analyze document"}), 500