#!/usr/bin/env python3

from functools import wraps

from flask import g, redirect, request, url_for


def authorize(function):
    @wraps(function)
    # The More You Know: `*args` is an abbreviation of positional arguments and
    #                    `**kwargs is an abbreviation of keyword arguments
    def authorizing(*args, **kwargs):
        # The More You Know: `g` exists within the scope of the request
        if g.customer is None:
            # TODO Remove error designation
            message = 'No authority (Error 0)'
            return redirect(url_for('application.login', next=request.path))
        return function(*args, **kwargs)
    return authorizing
