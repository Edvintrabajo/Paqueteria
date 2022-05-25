import sys
sys.path.append('models') # add the models directory to the path

from bottle import run, template, request, get, post, redirect, static_file, error
from models.oficinista_pedido import Oficinista_Pedido

oficinista_pedido = Oficinista_Pedido()

@get('/oficinista_pedido')
def index_oficinista_pedido():
    rows= oficinista_pedido.select()
    return template('main_oficinista_pedido', rows=oficinista_pedido.select())

@post('/oficinista_pedido')
def new_task_save():
    if request.POST.save:  # the user clicked the `save` button
        data = {
            'IDPedido': request.POST.IDPedido.strip(),
            'ID_Oficinista': request.POST.IDOficinista.strip()
        }

        if data.get('ID_Oficinista') == "" or data.get('IDPedido') == "":
            return redirect("/error")

        oficinista_pedido.insert(data)

        # se muestra el resultado de la operación
        return redirect('/oficinista_pedido')

@get('/edit_oficinista_pedido/<no:int>')
def edit_item_form(no):
    fields = ['ID_Oficinista']
    where = {'IDPedido': no}
    cur_data = oficinista_pedido.get(fields, where)  # get the current data for the item we are editing
    return template('edit_oficinista_pedido', old=cur_data, no=no)

@post('/edit_oficinista_pedido/<no:int>')
def edit_item(no):
    
    if request.POST.save:
        data = {
            'ID_Oficinista': request.POST.IDOficinista.strip()
        }

        if data.get('ID_Oficinista') == "":
            del data['ID_Oficinista']


        where = {'IDPedido': no}
        
        oficinista_pedido.update(data, where)
        
    return redirect('/oficinista_pedido')

@get('/delete_oficinista_pedido/<no:int>')
def delete_item_form(no):
    fields = ['IDPedido']
    where = {'IDPedido': no}
    cur_data = oficinista_pedido.get(fields, where)  # get the current data for the item we are editing
    return template('delete_oficinista_pedido', old=cur_data, no=no)

@post('/delete_oficinista_pedido/<no:int>')
def delete_item(no):
    
    if request.POST.delete:
        where = {'IDPedido': no}
        oficinista_pedido.delete(where)

    return redirect('/oficinista_pedido')

@error(404)
def error404(error):
    return static_file('404.html', root='static')

if __name__ == '__main__':

    run(host='localhost', port=8080, debug=True, reloader=True)