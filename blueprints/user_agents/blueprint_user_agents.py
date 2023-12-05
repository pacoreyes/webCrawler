from flask import Blueprint, render_template, jsonify, Response
from typing import List, Dict
from models.user_agents import retrieve_user_agents

# Create the user agents blueprint
blueprint_user_agents = Blueprint('user_agents', __name__, url_prefix='/user-agents')


@blueprint_user_agents.route('/')
def display_user_agents():
    """Render the user agents page."""
    return render_template('user-agents/index.html')


blueprint_api_user_agents = Blueprint('user_agents_api', __name__)


@blueprint_api_user_agents.route('/api/user-agents')
def user_agents_endpoint() -> Response:
    """API endpoint to fetch user agent data."""
    user_agents_data: List[Dict] = retrieve_user_agents()
    return jsonify(user_agents_data)
