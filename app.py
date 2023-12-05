from flask import Flask, render_template
from typing import Tuple
import os

from config import get_config
from blueprints.politicians.blueprint_politicians import blueprint_politicians, blueprint_api_politicians
from blueprints.websites.blueprint_websites import blueprint_websites, blueprint_api_websites
from blueprints.user_agents.blueprint_user_agents import blueprint_user_agents, blueprint_api_user_agents
from blueprints.blueprint_main import blueprint_homepage, blueprint_start_crawler, blueprint_about




# Initialize Flask app
app = Flask(__name__,
            template_folder="templates",
            static_folder="static")

# Choose the configuration based on the current environment
app.config.from_object(get_config())

# Registering blueprints for politicians page
app.register_blueprint(blueprint_politicians)

# Registering blueprints for website html page
app.register_blueprint(blueprint_websites)

# Registering blueprints for user-agents html page
app.register_blueprint(blueprint_user_agents)

# Registering blueprint for website api calls
app.register_blueprint(blueprint_api_websites)

# Registering blueprint for user-agents api calls
app.register_blueprint(blueprint_api_user_agents)

# Registering blueprint for politicians api calls
app.register_blueprint(blueprint_api_politicians)

# Registering blueprints for homepage html page
app.register_blueprint(blueprint_homepage)

# Registering blueprints for start_crawler function call page
app.register_blueprint(blueprint_start_crawler)

# Registering blueprints for about html page
app.register_blueprint(blueprint_about)

@app.errorhandler(404)
def handle_page_not_found(error: Exception) -> Tuple[str, int]:
  """Handle requests for non-existent routes."""
  print(error)
  return render_template("404.html"), 404


if __name__ == "__main__":
  # Get the port number from the environment variable (default is 5001)
  application_port = int(os.environ.get('PORT', 5001))
  app.run(host='0.0.0.0', port=application_port)

# To run the app in development mode, use the following commands:
# export FLASK_DEBUG=1
# export flask_env=development
# flask run --host=0.0.0.0 --port=5001
