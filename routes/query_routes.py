from flask import Blueprint, request, jsonify
from services.query_service import QueryService

query_routes = Blueprint('query_routes', __name__)
query_service = QueryService()


@query_routes.route('/query', methods=['POST'])
def handle_query():
    data = request.json
    query = data.get('query')
    result = query_service.research(query)
    return jsonify(result)
