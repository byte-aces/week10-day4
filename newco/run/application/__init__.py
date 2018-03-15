#!/usr/bin/env python3

import os

from flask import Flask, render_template, request, url_for

from application.extend import authorize
from application.models import module as models
from application.views  import module as views


omnibus = Flask(__name__)

omnibus.register_blueprint(models)
omnibus.register_blueprint(views)


def keymaker(omnibus, filename='secret_key'):
    pathname = os.path.join(omnibus.instance_path, filename)
    try:
        omnibus.config['SECRET_KEY'] = open(pathname, "rb").read()
    except IOError:
        parent_directory = os.path.dirname(pathname)
        if not os.path.isdir(parent_directory):
            os.system('mkdir -p {0}'.format(parent_directory))
        os.system('head -c 24 /dev/urandom > {0}'.format(pathname))

keymaker(omnibus)
