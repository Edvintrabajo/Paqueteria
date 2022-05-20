import os
import bottle
from bottle import route, run, template, request, get, post, redirect, static_file, error, response
from config.config import DATABASE
from models.clientes import *

cliente = Cliente(DATABASE)

@get('/')
def index_cliente():
    rows=cliente.select_cliente()
    return template('main_clientes', rows=cliente.select_cliente())

@get('/delete_cliente/<no:int>')
def delete_cliente(no):
    cur_data = cliente.get_dni(no)  
    return template('delete_task', old=cur_data, no=no)


if __name__ == '__main__':
    if not os.path.exists(DATABASE) or os.path.getsize(DATABASE) == 0:
        cliente.select_cliente()
        
    run(host='localhost', port=8080, debug=True, reloader=True)