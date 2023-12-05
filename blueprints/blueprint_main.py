from flask import Blueprint, render_template, jsonify, Response
from models.crawler import execute_crawler

blueprint_homepage = Blueprint('homepage', __name__, url_prefix='/')

@blueprint_homepage.route("/")
def home_page() -> str:
  """Render the home page."""
  return render_template('index.html')


blueprint_start_crawler = Blueprint('start-crawler', __name__, url_prefix='/')

@blueprint_start_crawler.route("/start-crawler")
def initiate_crawler() -> Response:
  """Start the web crawler and notify when finished."""
  execute_crawler()
  return jsonify({"status": "finished"})

blueprint_about = Blueprint('about', __name__, url_prefix='/')

@blueprint_about.route('/about')
def about() -> str:
  """Render the about page."""
  return render_template('about.html')