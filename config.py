# -----------------------------------------------------------
# Configuration file for the Flask application.
#
# (C) 2021-2023 Juan-Francisco Reyes, Cottbus, Germany
# Brandenburg University of Technology, Germany.
# Released under MIT License
# email pacoreyes.zwei@gmail.com
# -----------------------------------------------------------
class DevelopmentConfig:
  DEBUG = True
  TESTING = False
  # Other development-specific configurations...


class ProductionConfig:
  DEBUG = False
  TESTING = False
  # Other production-specific configurations...


def get_config():
  # Implement your logic to select the appropriate config class
  # based on the current environment (for example, by checking an environment variable)
  return DevelopmentConfig  # or return ProductionConfig
