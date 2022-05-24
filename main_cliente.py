import sys
sys.path.append('models') # add the models directory to the path

from bottle import run, template, request, get, post, redirect, static_file, error
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

        if data.get('DNIcliente') == "" or data.get('Nombre') == "" or data.get('Apellidos') == "" or data.get('DireccionCliente') == "":
            return redirect("/error")

        cliente.insert(data)

        # se muestra el resultado de la operación
        return redirect('/cliente')

@get('/edit_cliente/<no>')
def edit_item_form(no):
    fields = ['Nombre', 'Apellidos', 'DireccionCliente']
    where = {'DNIcliente': no}
    cur_data = cliente.get(fields, where)  # get the current data for the item we are editing
    return template('edit_clientes', old=cur_data, no=no)

@post('/edit_cliente/<no>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'Nombre': request.POST.Nombre.strip(),
            'Apellidos': request.POST.Apellido.strip(),
            'DireccionCliente': request.POST.Direccion.strip()
        }
        if data.get('Nombre') == "":
            del data['Nombre']

        if data.get('Apellidos') == "":
            del data['Apellidos']

        if data.get('DireccionCliente') == "":
            del data['DireccionCliente']

        where = {'DNIcliente': no}
        
        cliente.update(data, where)
        
    return redirect('/cliente')

@get('/delete_cliente/<no>')
def delete_item_form(no):
    fields = ['DNIcliente']
    where = {'DNIcliente': no}
    cur_data = cliente.get(fields, where)  # get the current data for the item we are editing
    return template('delete_clientes', old=cur_data, no=no)

@post('/delete_cliente/<no>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'DNIcliente': no}
        cliente.delete(where)

    return redirect('/cliente')

@error(404)
def error404(error):
    return static_file('404.html', root='static')

if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)