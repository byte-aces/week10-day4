#!/usr/bin/env python3

import random
import time

from flask import Blueprint, g, redirect, render_template, request, session, url_for


module = Blueprint('views', __name__, url_prefix="")


@module.before_request
def before_request():
    g.customer = None
    if 'customer_id' in session:
        # FIXME TO BE CONTINUED...
        g.customer = Customer.query.get(session['customer_id'])


# Front page
@module.route('/', methods=['GET'])
def front():
    return render_template('index.html')


# TODO 404 page
@module.route('/404', methods=['GET'])
def error_404():
    return render_template('404.html')


# FIXME Register page
@module.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        fuzz             = random.uniform(1,9999) / 100000
        username         = request.form['username']
        password         = request.form['password']
        password_confirm = request.form['password_confirm']
        # Check if the username and passwords were submitted
        if username and password and password_confirm:
            # Check if the passwords match
            if password == password_confirm:
                # Note: This is an attempt to mitigate a timing attack, by Eve,
                #       which would hypothetically calculate the Levenshtien
                #       distance between the submitted password and the
                #       submitted username for an existing user.
                time.sleep(fuzz)
                # Check if the username exists (in the database)
                # TODO Re-factor the following into an ORM for PostgreSQL
                import sqlite3
                # --> Open up a connection and cursor objects
                connection = sqlite3.connect('run/datastore/sql.db', check_same_thread=False)
                cursor     = connection.cursor()
                # --> Execute a query
                cursor.execute('SELECT COUNT(*) FROM users WHERE username="{0}";'.format(username))
                tally = int(cursor.fetchall()[0][0])
                if tally == 0:
                    # State: Username doesn't exist
                    # Store submitted username and password in the database
                    # TODO Mitigate a hypothetical SQL injection attack by
                    #      replacing the format invocation with something else.
                    cursor.execute('INSERT INTO users(username, password) VALUES("{0}","{1}");'.format(username, password))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    # FIXME Assign objects to `g` and `session`
                    return redirect(url_for('views.dashboard'))
                else:
                    # State: Username exists
                    # FIXME
                    pass
                # Close the aforementioned connection and cursor objects
                # FIXME
                # close this
                # close that
            else:
                # FIXME
                pass
        else:
            # FIXME
            pass


# FIXME Login page
@module.route('/login', methods=['GET', 'POST'])
def login():
    # # Check if the username and password were submitted
    #     # Check if the username exists
    #         # Check if the submitted password is the stored password for the username
    # return render_template('login.html')

    if request.method == 'GET':
        return render_template('login.html')
    else:
        fuzz             = random.uniform(1,9999) / 100000
        username         = request.form['username']
        password         = request.form['password']
        # Check if the username and password were submitted
        if username and password:
            # Check if the passwords match
            time.sleep(fuzz)
            # Check if the username exists (in the database)
            # TODO Re-factor the following into an ORM for PostgreSQL
            import sqlite3
            # --> Open up a connection and cursor objects
            connection = sqlite3.connect('run/datastore/sql.db', check_same_thread=False)
            cursor     = connection.cursor()
            # --> Execute a query
            cursor.execute('SELECT COUNT(*), MIN(id) FROM users WHERE username="{0}" AND password="{1}";'.format(username, password))
            (tally, customer_id) = cursor.fetchall()[0]
            if tally < 1:
                # bad creds
                pass
            elif tally > 1:
                # currupt database
                pass
            else:
                # good creds
                # FIXME Assign objects to `g` and `session`
                pass
















            if tally == 1:
                time.sleep(fuzz)
                # State: Username doesn't exist
                # Store submitted username and password in the database
                # TODO Mitigate a hypothetical SQL injection attack by
                #      replacing the format invocation with something else.
                cursor.execute('INSERT INTO users(username, password) VALUES("{0}","{1}");'.format(username, password))
                connection.commit()
                cursor.close()
                connection.close()
                return redirect(url_for('views.dashboard'))
            else:
                # State: Username exists
                # FIXME
                pass
            # Close the aforementioned connection and cursor objects
            # FIXME
            # close this
            # close that
        else:
            # FIXME
            pass



###############################################################################
#                                                                             #
# Must be logged in!                                                          #
#                                                                             #
###############################################################################

# FIXME Dashboard page
@module.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    # TODO Write graphical user interface
    return render_template('dashboard.html')


# FIXME Account page
@module.route('/account', methods=['GET', 'POST'])
def account():
    # TODO Write graphical user interface
    return render_template('account.html')


# Note: for local testing
if __name__ == '__main__':
    module.run(debug=True)
