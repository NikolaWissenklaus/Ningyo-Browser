#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Mai 23 14:11:03 2016

@author: T. Wissenklaus (Francisco Lucas da Silva)

"""

from flask import Flask,request
from flask_cors import CORS, cross_origin
from flask import jsonify
import json
import base64

#===============================================================

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#===============================================================

@app.route("/", methods=["GET"])
@cross_origin()
def home():
    #----------------------------------------
    #Importa o Json
    f = open("index.json", "r")
    data = json.loads(f.read())
    f.close()
    #----------------------------------------
    return jsonify(data)

@app.route("/sobre", methods=["GET"])
@cross_origin()
def sobre():
    #----------------------------------------
    #Importa o Json
    f = open("sobre.json", "r")
    data = json.loads(f.read())
    f.close()
    #----------------------------------------
    return jsonify(data)

@app.route("/abacate", methods=["GET"])
@cross_origin()
def abacate():
    #----------------------------------------
    #Importa o Json
    f = open("abacate.json", "r")
    data = json.loads(f.read())
    f.close()
    #----------------------------------------
    return jsonify(data)

@app.route("/seila", methods=["GET"])
@cross_origin()
def seila():
    #----------------------------------------
    #Importa o Json
    f = open("seila.json", "r")
    data = json.loads(f.read())
    f.close()
    #----------------------------------------
    return jsonify(data)
#===============================================================

@app.route("/imagem", methods=["GET"])
@cross_origin()
def img():
    parametro = request.args.get('img')

    f = open(parametro, 'rb')
    txt_do_arquivo = base64.b64encode(f.read()).decode()
    f.close()

    data = {"arq": txt_do_arquivo}

    return jsonify(data)
#===============================================================

app.run(host="0.0.0.0", debug=True)