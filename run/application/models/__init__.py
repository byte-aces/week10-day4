#!/usr/bin/env python3

from flask import Blueprint, request


module = Blueprint('models', __name__, url_prefix="/models")




# For local testing
if __name__ == '__main__':
    module.run(debug=True)