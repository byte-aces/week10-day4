#!/usr/bin/env python3

import sqlite3


connection = sqlite3.connect('run/datastore/sql.db', check_same_thread=False)
cursor     = connection.cursor()


cursor.execute(
    """CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        username VARCHAR(32) UNIQUE,
        password VARCHAR(64)
    );""")


# TODO Change FLOAT To NUMERIC(24,8)? #table_makers_dilemma
cursor.execute(
    """CREATE TABLE positions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        ticker_symbol VARCHAR(12),
        number_of_units FLOAT,
        volume_weighted_average_price FLOAT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );""")



# TODO Change FLOAT to something more accurate #table_makers_dilemma
cursor.execute(
    """CREATE TABLE transactions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        unix_time FLOAT,
        ticker_symbol VARCHAR(12),
        trade_volume FLOAT,
        transaction_fee FLOAT,
        last_price FLOAT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );""")


cursor.execute(
    """CREATE TABLE wallets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        wallet_address VARCHAR(36),
        FOREIGN KEY (user_id) REFERENCES users(id)
    );""")


connection.commit()
cursor.close()
connection.close()
