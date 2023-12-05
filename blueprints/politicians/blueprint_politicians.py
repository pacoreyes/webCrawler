from flask import Blueprint, render_template, jsonify, Response
from typing import List, Dict
from models.politicians import retrieve_politicians

# Create the politicians blueprint
blueprint_politicians = Blueprint('politicians', __name__, url_prefix='/politicians')


@blueprint_politicians.route('/')
def display_politicians():
    """Render the politicians page."""
    return render_template('politicians/index.html')


blueprint_api_politicians = Blueprint('politicians_api', __name__)


@blueprint_api_politicians.route('/api/politicians', methods=['GET'])
def politicians_endpoint() -> Response:
    """API endpoint to fetch politician data."""
    politicians_data: List[Dict] = retrieve_politicians()
    return jsonify(politicians_data)
