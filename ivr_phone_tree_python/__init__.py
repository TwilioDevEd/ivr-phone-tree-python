from flask import Flask
from ivr_phone_tree_python.config import config_env_files


def create_app(config_name='development'):
    new_app = Flask(__name__)
    new_app.config.from_object(config_env_files[config_name])

    return new_app


app = create_app()

import ivr_phone_tree_python.views
