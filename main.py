#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 18:42:11 2021

@author: y56
"""

import flask
from flask import escape
import functions_framework

import firebase_admin
from firebase_admin import db
from firebase_admin import auth
from firebase_admin import credentials

from flask_cors import cross_origin

@cross_origin()
def main(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    request_json = request.get_json(silent=True)
    request_args = request.args

    id_token = 'QQ'
    if request_json and 'id_token' in request_json:
        id_token = request_json['id_token']
    elif request_args and 'id_token' in request_args:
        id_token = request_args['id_token']
    else:
        raise ValueError('No input ID token!!!')

    print(id_token)

    firebase_admin.initialize_app()

#    default_app = firebase_admin.initialize_app()


    uid = 'QQ'

    decoded_token = auth.verify_id_token(id_token)
    uid = decoded_token['uid']
    email = decoded_token['email']
    print('bad')

    return 'Hello {}!'.format(escape(uid)) + escape(email), 200
