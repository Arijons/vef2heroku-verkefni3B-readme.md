from sys import argv

import bottle
from bottle import*
bottle.debug(True)
# -*- coding: utf-8 -*-

from bottle import Bottle, template, route, run


@route('/')
def index():
    return template('news.tpl')

@route("/b")
def heim():
    return template('news.tpl')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./")


@route("/frett/0")
def frett0(frettnumer='Stranger'):
    return template("frett0.tpl",root="./")

@route("/frett/1")
def frett1(frettanumer='Stranger'):
    return template("frett1.tpl",root="./")

@route("/frett/2")
def frett1(frettanumer='Stranger'):
    return template("frett2.tpl",root="./")







@error(404)
def custom404(error):
    return "slá inn rétta route"

bottle.run()

