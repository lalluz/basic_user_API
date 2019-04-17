from database_setup import Base, User, Address

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from flask import Flask
from flask import flash
from flask import jsonify
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

import re


app = Flask(__name__)

engine = create_engine('postgresql+psycopg2://codechallenge:secret_password@localhost:5432/codechallenge')  # nopep8

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/users/getusers/', methods=['GET'])
def user_list():
    """List all users."""
    users = session.query(User).all()
    serialized_users = jsonify(Users=[u.serialize for u in users])

    return make_response(serialized_users, 200)


@app.route('/users/createUsers/', methods=['POST'])
def user_create():
    """Create a user."""
    ra = request.args
    name = None if 'name' not in ra else ra['name']
    email = None if 'email' not in ra else ra['email']
    birthdate = None if 'birthdate' not in ra else ra['birthdate']
    address_id = None if 'address_id' not in ra else ra['address_id']

    if not (name and email and birthdate and address_id):
        return make_response(jsonify({"message": "invalid input"}), 405)

    if not is_email_valid(email):
        return make_response(jsonify({"message": "invalid email input"}), 405)

    if not is_birthdate_valid(birthdate):
        return make_response(jsonify({"message": "invalid date input"}), 405)

    user = User(name=name,
                email=email.lower(),
                birthdate=birthdate,
                address_id=address_id)
    session.add(user)
    session.commit()

    serialized_user = jsonify(UserCreated=user.serialize)

    return make_response(serialized_user, 201)


@app.route('/users/getusersById/<user_id>/', methods=['GET'])
# @app.route('/getusersById/<int:user_id>/', methods=['GET'])
def user_detail(user_id):
    """Get a user."""
    try:
        user_id = int(user_id)
    except ValueError:
        return make_response(jsonify({"message": "invalid user id"}), 400)
    try:
        user = session.query(User).filter_by(id=user_id).one()
    except NoResultFound:
        return make_response(jsonify({"message": "user not found"}), 404)

    serialized_user = jsonify(User=user.serialize)

    return make_response(serialized_user, 200)


@app.route('/users/updateUsersById/<user_id>/', methods=['PUT'])
def user_update(user_id):
    """Update a user."""
    try:
        user_id = int(user_id)
    except ValueError:
        return make_response(jsonify({"message": "invalid user id"}), 400)
    try:
        user = session.query(User).filter_by(id=user_id).one()
    except NoResultFound:
        return make_response(jsonify({"message": "user not found"}), 404)

    ra = request.args
    name = user.name if 'name' not in ra else ra['name']
    email = user.email if 'email' not in ra else ra['email']
    birthdate = user.birthdate if 'birthdate' not in ra else ra['birthdate']
    address_id = user.address_id if 'address_id' not in ra else ra['address_id']  # nopep8

    updated_user = User(name=name,
                        email=email.lower(),
                        birthdate=birthdate,
                        address_id=address_id)
    session.add(updated_user)
    session.commit()

    serialized_user = jsonify(UserUpdated=updated_user.serialize)

    return make_response(serialized_user, 200)


@app.route('/users/deleteUsersById/<user_id>/', methods=['DELETE'])
def user_delete(user_id):
    """Delete a user."""
    try:
        user_id = int(user_id)
    except ValueError:
        return make_response(jsonify({"message": "invalid user id"}), 400)
    try:
        user = session.query(User).filter_by(id=user_id).one()
    except NoResultFound:
        return make_response(jsonify({"message": "user not found"}), 404)

    session.delete(user)
    session.commit()

    return make_response(jsonify({"message": "user deleted"}), 200)


def is_email_valid(email):
    '''Email format check'''
    # https://www.scottbrady91.com/Email-Verification/Python-Email-Verification-Script
    if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):  # nopep8
        return True

    return False


def is_birthdate_valid(birthdate):
    '''Simplify date check, should check leap years also.'''
    if len(birthdate) == 10:
        try:
            day = int(birthdate[0:2])
            month = int(birthdate[3:5])
            year = int(birthdate[6:10])
        except ValueError:
            return False

        if not (birthdate[2] == '-' and birthdate[5] == '-'):
            return False

        if (day in range(1, 31) and month in range(1, 13) and year in range(1900, 2019)):  # nopep8
            if (month == 4 or month == 6 or month == 9 or month == 11) and day < 31:  # nopep8
                return True
            if month == 2 and day < 30:
                return True
        return False

    return False


if __name__ == '__main__':
    app.secret_key = "secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
