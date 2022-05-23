import os
import sys
sys.path.append('models') # add the models directory to the path

import bottle
from bottle import route, run, template, request, get, post, redirect, static_file, error, response
from models.clientes import Cliente

cliente = Cliente()

@get('/cliente')
def index_cliente():
    rows= cliente.select()
    return template('main_clientes', rows=cliente.select())

@post('/cliente')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'DNIcliente': request.POST.dni.strip(), 
            'Nombre': request.POST.Nombre.strip(),
            'Apellidos': request.POST.Apellido.strip(),
            'DireccionCliente': request.POST.Direccion.strip()
        }
        cliente.insert(data)

        # se muestra el resultado de la operación
        return redirect('/cliente')


@get('/edit_cliente/<no:varchar(9)>')
def edit_item_form(no):
    fields = ['Nombre', 'Apellidos', 'DireccionCliente']
    where = {'DNIcliente': no}
    cur_data = cliente.get(fields, where)  # get the current data for the item we are editing
    return template('edit_task', old=cur_data, no=no)

@post('/edit_cliente/<no:varchar(9)>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'Nombre': request.POST.Nombre.strip(),
            'Apellidos': request.POST.Apellido.strip(),
            'DireccionCliente': request.POST.Direccion.strip()
        }
        where = {'DNIcliente': no}
        
        cliente.update(data, where)
        
    return redirect('/cliente')





if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)