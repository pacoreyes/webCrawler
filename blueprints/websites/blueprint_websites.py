from flask import Response
from typing import List, Dict
from flask import Blueprint, render_template, jsonify
from models.websites import retrieve_websites

# Blueprint instance for website
blueprint_websites = Blueprint('websites', __name__, url_prefix='/websites')


@blueprint_websites.route('/')
def display_websites():
    """Render the websites page."""
    return render_template('websites/index.html')


# Blueprint instance to fetch websites list
blueprint_api_websites = Blueprint('website_api', __name__)


@blueprint_api_websites.route('/api/websites')
def websites_endpoint() -> Response:
    """API endpoint to fetch website data."""
    websites_data: List[Dict] = retrieve_websites()
    return jsonify(websites_data)
